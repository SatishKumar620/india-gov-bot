"""
🇮🇳 India Government Schemes Telegram Bot
==========================================
FREE deployment on Railway.app
AI powered by Groq (free tier)
"""

import os
import logging
import requests
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, MessageHandler,
    CallbackQueryHandler, ContextTypes, filters
)
from data import SCHEMES, YOJANAS, JOBS, EXAMS, search_all, get_item_by_id

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

BOT_TOKEN  = os.getenv("BOT_TOKEN")
GROQ_KEY   = os.getenv("GROQ_API_KEY")
GROQ_URL   = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "llama3-8b-8192"   # free & fast on Groq


# ── Groq AI ──────────────────────────────────────────────────────────────────

def ask_groq(system: str, user: str) -> str:
    if not GROQ_KEY:
        return "⚠️ GROQ_API_KEY not set."
    try:
        r = requests.post(
            GROQ_URL,
            headers={"Authorization": f"Bearer {GROQ_KEY}", "Content-Type": "application/json"},
            json={
                "model": GROQ_MODEL,
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user",   "content": user}
                ],
                "max_tokens": 600,
                "temperature": 0.3,
            },
            timeout=30,
        )
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        logger.error(f"Groq error: {e}")
        return "⚠️ AI unavailable right now. Showing database info."


def ai_explain(item: dict, item_type: str) -> str:
    system = (
        "You are a helpful Indian government assistant. "
        "Explain government schemes/jobs/exams to common Indian citizens. "
        "Use simple Hinglish (mix of Hindi + English). Be friendly and concise. "
        "Use emojis. Max 350 words."
    )
    user = f"""Explain this {item_type} simply:
Name: {item['name']} ({item.get('hindi_name','')})
Description: {item['description']}
Eligibility: {item.get('eligibility','')}
How to Apply: {item.get('how_to_apply','')}
Benefit: {item.get('benefit','')}

Cover: kya hai, kaun apply kar sakta, kaise apply karein, kya documents chahiye."""
    return ask_groq(system, user)


# ── Keyboards ─────────────────────────────────────────────────────────────────

def main_menu_kb():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🏛️ Schemes",     callback_data="cat_schemes"),
         InlineKeyboardButton("🟠 Yojanas",     callback_data="cat_yojanas")],
        [InlineKeyboardButton("💼 Sarkari Jobs", callback_data="cat_jobs"),
         InlineKeyboardButton("📝 Exams",        callback_data="cat_exams")],
        [InlineKeyboardButton("🔍 Search",       callback_data="cat_search"),
         InlineKeyboardButton("🤖 AI Se Pucho",  callback_data="cat_ai")],
    ])


def list_kb(items: list, prefix: str):
    emoji_map = {"s": "🏛️", "y": "🟠", "j": "💼", "e": "📝"}
    em = emoji_map.get(prefix, "📌")
    buttons = [[InlineKeyboardButton(f"{em} {item['name']}", callback_data=f"detail_{item['id']}")]
               for item in items]
    buttons.append([InlineKeyboardButton("🔙 Main Menu", callback_data="main_menu")])
    return InlineKeyboardMarkup(buttons)


def detail_kb(item_id: str):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🤖 AI Explain Karo", callback_data=f"ai_{item_id}")],
        [InlineKeyboardButton("🔙 Main Menu",        callback_data="main_menu")],
    ])


# ── Format helpers ────────────────────────────────────────────────────────────

def format_detail(item: dict) -> str:
    docs = "\n".join(f"  • {d}" for d in item.get("documents", []))
    steps = item.get("how_to_apply", "Website par jaayein")
    return (
        f"*{item['name']}*\n"
        f"_{item.get('hindi_name', '')}_ \n\n"
        f"📋 *Kya hai?*\n{item['description']}\n\n"
        f"✅ *Eligibility:*\n{item.get('eligibility', 'N/A')}\n\n"
        f"💰 *Benefit:*\n{item.get('benefit', 'N/A')}\n\n"
        f"📄 *Documents Needed:*\n{docs}\n\n"
        f"📝 *Kaise Apply Karein:*\n{steps}\n\n"
        f"🌐 *Official Website:*\n{item.get('website', 'N/A')}"
    )


# ── Handlers ──────────────────────────────────────────────────────────────────

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.first_name or "Dost"
    text = (
        f"🙏 *Namaste {name}!*\n\n"
        "Main aapka *India Government Schemes Bot* hoon 🇮🇳\n\n"
        "Main aapko in cheezein bata sakta hoon:\n"
        "🏛️ *Schemes* — PM Kisan, Ayushman, Mudra...\n"
        "🟠 *Yojanas* — Ujjwala, Beti Bachao, Swachh Bharat...\n"
        "💼 *Sarkari Jobs* — SSC, Railway, Bank, Army...\n"
        "📝 *Exams* — JEE, NEET, UPSC, CTET...\n\n"
        "Bas type karo ya button dabao! 👇"
    )
    await update.message.reply_text(text, parse_mode="Markdown", reply_markup=main_menu_kb())


async def help_cmd(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🆘 *Help*\n\n"
        "• /start — Main menu\n"
        "• /schemes — All schemes list\n"
        "• /jobs — All jobs list\n"
        "• /exams — All exams list\n"
        "• /yojanas — All yojanas list\n"
        "• Type anything to search (e.g. 'kisan', 'railway', 'health')\n\n"
        "💡 Koi bhi scheme ka naam type karo, main dhundh dunga!",
        parse_mode="Markdown"
    )


async def schemes_cmd(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏛️ *Government Schemes*\nEk choose karein:",
        parse_mode="Markdown",
        reply_markup=list_kb(SCHEMES, "s")
    )


async def jobs_cmd(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💼 *Sarkari Jobs*\nEk choose karein:",
        parse_mode="Markdown",
        reply_markup=list_kb(JOBS, "j")
    )


async def exams_cmd(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📝 *Government Exams*\nEk choose karein:",
        parse_mode="Markdown",
        reply_markup=list_kb(EXAMS, "e")
    )


async def yojanas_cmd(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🟠 *Sarkari Yojanas*\nEk choose karein:",
        parse_mode="Markdown",
        reply_markup=list_kb(YOJANAS, "y")
    )


async def handle_text(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    query = update.message.text.strip()

    # Check for simple category words first
    q = query.lower()
    if q in ["scheme", "schemes", "yojana", "सरकारी योजना"]:
        await schemes_cmd(update, ctx); return
    if q in ["job", "jobs", "naukri", "sarkari job", "नौकरी"]:
        await jobs_cmd(update, ctx); return
    if q in ["exam", "exams", "परीक्षा"]:
        await exams_cmd(update, ctx); return
    if q in ["yojanas", "yojana"]:
        await yojanas_cmd(update, ctx); return

    # Search across all
    results = search_all(query)
    total = sum(len(v) for v in results.values())

    if total == 0:
        # Use AI to answer freeform
        await update.message.reply_text("🔍 Searching with AI...")
        system = (
            "You are an expert on Indian government schemes, jobs, and exams. "
            "Answer in simple Hinglish. Be helpful and concise. Use emojis."
        )
        ai_reply = ask_groq(system, query)
        await update.message.reply_text(
            f"🤖 *AI Answer:*\n\n{ai_reply}",
            parse_mode="Markdown",
            reply_markup=main_menu_kb()
        )
        return

    # Build result message
    msg = f"🔍 *'{query}' ke liye results ({total} mile):*\n\n"
    buttons = []

    for item in results["schemes"][:3]:
        msg += f"🏛️ {item['name']}\n"
        buttons.append([InlineKeyboardButton(f"🏛️ {item['name']}", callback_data=f"detail_{item['id']}")])

    for item in results["yojanas"][:3]:
        msg += f"🟠 {item['name']}\n"
        buttons.append([InlineKeyboardButton(f"🟠 {item['name']}", callback_data=f"detail_{item['id']}")])

    for item in results["jobs"][:3]:
        msg += f"💼 {item['name']}\n"
        buttons.append([InlineKeyboardButton(f"💼 {item['name']}", callback_data=f"detail_{item['id']}")])

    for item in results["exams"][:3]:
        msg += f"📝 {item['name']}\n"
        buttons.append([InlineKeyboardButton(f"📝 {item['name']}", callback_data=f"detail_{item['id']}")])

    buttons.append([InlineKeyboardButton("🔙 Main Menu", callback_data="main_menu")])
    await update.message.reply_text(msg, parse_mode="Markdown",
                                     reply_markup=InlineKeyboardMarkup(buttons))


async def button_handler(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    query  = update.callback_query
    data   = query.data
    await query.answer()

    # Main menu
    if data == "main_menu":
        await query.edit_message_text(
            "🇮🇳 *Main Menu* — Kya jaanna chahte hain?",
            parse_mode="Markdown", reply_markup=main_menu_kb()
        )

    # Category lists
    elif data == "cat_schemes":
        await query.edit_message_text("🏛️ *Government Schemes*", parse_mode="Markdown",
                                       reply_markup=list_kb(SCHEMES, "s"))
    elif data == "cat_yojanas":
        await query.edit_message_text("🟠 *Sarkari Yojanas*", parse_mode="Markdown",
                                       reply_markup=list_kb(YOJANAS, "y"))
    elif data == "cat_jobs":
        await query.edit_message_text("💼 *Sarkari Jobs*", parse_mode="Markdown",
                                       reply_markup=list_kb(JOBS, "j"))
    elif data == "cat_exams":
        await query.edit_message_text("📝 *Government Exams*", parse_mode="Markdown",
                                       reply_markup=list_kb(EXAMS, "e"))

    elif data == "cat_search":
        await query.edit_message_text(
            "🔍 *Search Karo*\n\nKuch bhi type karo — scheme, job, exam ka naam ya keyword\n"
            "Example: *kisan*, *railway*, *health*, *loan*, *army*",
            parse_mode="Markdown"
        )

    elif data == "cat_ai":
        await query.edit_message_text(
            "🤖 *AI Se Pucho*\n\nKoi bhi sawaal type karo about:\n"
            "• Koi bhi government scheme\n• Sarkari naukri\n• Exam preparation\n• Eligibility check\n\n"
            "Seedha message bhejo! 👇",
            parse_mode="Markdown"
        )

    # Detail view
    elif data.startswith("detail_"):
        item_id = data.replace("detail_", "")
        item = get_item_by_id(item_id)
        if item:
            await query.edit_message_text(
                format_detail(item),
                parse_mode="Markdown",
                reply_markup=detail_kb(item_id),
                disable_web_page_preview=True
            )

    # AI explain
    elif data.startswith("ai_"):
        item_id = data.replace("ai_", "")
        item = get_item_by_id(item_id)
        if item:
            await query.edit_message_text("🤖 AI explain kar raha hai... thoda wait karo ⏳")
            explanation = ai_explain(item, "government scheme/job/exam")
            await query.edit_message_text(
                f"🤖 *AI Explanation:*\n\n{explanation}",
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("📋 Full Details", callback_data=f"detail_{item_id}")],
                    [InlineKeyboardButton("🔙 Main Menu",   callback_data="main_menu")],
                ])
            )


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN not set in .env file!")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start",    start))
    app.add_handler(CommandHandler("help",     help_cmd))
    app.add_handler(CommandHandler("schemes",  schemes_cmd))
    app.add_handler(CommandHandler("jobs",     jobs_cmd))
    app.add_handler(CommandHandler("exams",    exams_cmd))
    app.add_handler(CommandHandler("yojanas",  yojanas_cmd))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    logger.info("🤖 Bot started!")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
