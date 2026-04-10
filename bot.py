import os
import logging
import requests
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    CallbackQueryHandler, ContextTypes, filters
)
from data import SCHEMES, YOJANAS, JOBS, EXAMS, search_all, get_item_by_id

load_dotenv()
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN  = os.getenv("BOT_TOKEN")
GROQ_KEY   = os.getenv("GROQ_API_KEY")
GROQ_URL   = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "llama3-8b-8192"

def ask_groq(system, user):
    if not GROQ_KEY:
        return "GROQ_API_KEY not set."
    try:
        r = requests.post(GROQ_URL,
            headers={"Authorization": f"Bearer {GROQ_KEY}", "Content-Type": "application/json"},
            json={"model": GROQ_MODEL, "messages": [{"role":"system","content":system},{"role":"user","content":user}], "max_tokens":600, "temperature":0.3},
            timeout=30)
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"AI unavailable: {e}"

def ai_explain(item, item_type):
    return ask_groq(
        "You are a helpful Indian government assistant. Explain in simple Hinglish. Use emojis. Max 300 words.",
        f"Explain {item_type}: {item['name']}\nDescription: {item['description']}\nEligibility: {item.get('eligibility','')}\nBenefit: {item.get('benefit','')}\nHow to Apply: {item.get('how_to_apply','')}"
    )

def main_menu_kb():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🏛️ Schemes", callback_data="cat_schemes"), InlineKeyboardButton("🟠 Yojanas", callback_data="cat_yojanas")],
        [InlineKeyboardButton("💼 Sarkari Jobs", callback_data="cat_jobs"), InlineKeyboardButton("📝 Exams", callback_data="cat_exams")],
        [InlineKeyboardButton("🔍 Search", callback_data="cat_search"), InlineKeyboardButton("🤖 AI Se Pucho", callback_data="cat_ai")],
    ])

def list_kb(items, prefix):
    em = {"s":"🏛️","y":"🟠","j":"💼","e":"📝"}.get(prefix,"📌")
    buttons = [[InlineKeyboardButton(f"{em} {i['name']}", callback_data=f"detail_{i['id']}")] for i in items]
    buttons.append([InlineKeyboardButton("🔙 Main Menu", callback_data="main_menu")])
    return InlineKeyboardMarkup(buttons)

def detail_kb(item_id):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🤖 AI Se Samjhao", callback_data=f"ai_{item_id}")],
        [InlineKeyboardButton("🔙 Main Menu", callback_data="main_menu")],
    ])

def format_detail(item):
    docs = "\n".join(f"  - {d}" for d in item.get("documents", []))
    return (f"*{item['name']}*\n_{item.get('hindi_name','')}_\n\n"
            f"What is it:\n{item['description']}\n\n"
            f"Eligibility:\n{item.get('eligibility','N/A')}\n\n"
            f"Benefit:\n{item.get('benefit','N/A')}\n\n"
            f"Documents:\n{docs}\n\n"
            f"How to Apply:\n{item.get('how_to_apply','N/A')}\n\n"
            f"Website:\n{item.get('website','N/A')}")

async def start(update, ctx):
    name = update.effective_user.first_name or "Dost"
    await update.message.reply_text(
        f"Namaste {name}! I am India Government Schemes Bot\n\nI can help with:\nSchemes, Yojanas, Sarkari Jobs, Exams\n\nType anything or press a button!",
        reply_markup=main_menu_kb())

async def help_cmd(update, ctx):
    await update.message.reply_text("/start /schemes /jobs /exams /yojanas\nOr type: kisan, health, railway, loan, army, neet")

async def schemes_cmd(update, ctx):
    await update.message.reply_text("Schemes - choose one:", reply_markup=list_kb(SCHEMES, "s"))

async def jobs_cmd(update, ctx):
    await update.message.reply_text("Sarkari Jobs - choose one:", reply_markup=list_kb(JOBS, "j"))

async def exams_cmd(update, ctx):
    await update.message.reply_text("Exams - choose one:", reply_markup=list_kb(EXAMS, "e"))

async def yojanas_cmd(update, ctx):
    await update.message.reply_text("Yojanas - choose one:", reply_markup=list_kb(YOJANAS, "y"))

async def handle_text(update, ctx):
    query = update.message.text.strip()
    q = query.lower()
    if q in ["scheme","schemes","yojana"]: await schemes_cmd(update, ctx); return
    if q in ["job","jobs","naukri"]: await jobs_cmd(update, ctx); return
    if q in ["exam","exams"]: await exams_cmd(update, ctx); return
    if q in ["yojanas"]: await yojanas_cmd(update, ctx); return
    results = search_all(query)
    total = sum(len(v) for v in results.values())
    if total == 0:
        await update.message.reply_text("Searching with AI...")
        reply = ask_groq("Expert on Indian government schemes. Answer in simple Hinglish. Use emojis.", query)
        await update.message.reply_text(f"AI Answer:\n\n{reply}", reply_markup=main_menu_kb())
        return
    msg = f"Results for '{query}' ({total} found):\n\n"
    buttons = []
    for item in (results["schemes"]+results["yojanas"])[:3]:
        em = "🏛️" if item in results["schemes"] else "🟠"
        msg += f"{em} {item['name']}\n"
        buttons.append([InlineKeyboardButton(f"{em} {item['name']}", callback_data=f"detail_{item['id']}")])
    for item in results["jobs"][:2]:
        msg += f"💼 {item['name']}\n"
        buttons.append([InlineKeyboardButton(f"💼 {item['name']}", callback_data=f"detail_{item['id']}")])
    for item in results["exams"][:2]:
        msg += f"📝 {item['name']}\n"
        buttons.append([InlineKeyboardButton(f"📝 {item['name']}", callback_data=f"detail_{item['id']}")])
    buttons.append([InlineKeyboardButton("🔙 Main Menu", callback_data="main_menu")])
    await update.message.reply_text(msg, reply_markup=InlineKeyboardMarkup(buttons))

async def button_handler(update, ctx):
    query = update.callback_query
    data = query.data
    await query.answer()
    if data == "main_menu":
        await query.edit_message_text("Main Menu - Kya jaanna chahte hain?", reply_markup=main_menu_kb())
    elif data == "cat_schemes":
        await query.edit_message_text("Government Schemes:", reply_markup=list_kb(SCHEMES, "s"))
    elif data == "cat_yojanas":
        await query.edit_message_text("Sarkari Yojanas:", reply_markup=list_kb(YOJANAS, "y"))
    elif data == "cat_jobs":
        await query.edit_message_text("Sarkari Jobs:", reply_markup=list_kb(JOBS, "j"))
    elif data == "cat_exams":
        await query.edit_message_text("Government Exams:", reply_markup=list_kb(EXAMS, "e"))
    elif data == "cat_search":
        await query.edit_message_text("Type any keyword: kisan, health, railway, loan, army, neet...")
    elif data == "cat_ai":
        await query.edit_message_text("AI Se Pucho - Type your question!")
    elif data.startswith("detail_"):
        item = get_item_by_id(data.replace("detail_", ""))
        if item:
            await query.edit_message_text(format_detail(item), parse_mode="Markdown", reply_markup=detail_kb(item['id']), disable_web_page_preview=True)
    elif data.startswith("ai_"):
        item = get_item_by_id(data.replace("ai_", ""))
        if item:
            await query.edit_message_text("AI samjha raha hai... please wait")
            explanation = ai_explain(item, "scheme/job/exam")
            await query.edit_message_text(f"AI Explanation:\n\n{explanation}",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("Full Details", callback_data=f"detail_{item['id']}")],
                    [InlineKeyboardButton("Main Menu", callback_data="main_menu")]
                ]))

def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN not set!")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("schemes", schemes_cmd))
    app.add_handler(CommandHandler("jobs", jobs_cmd))
    app.add_handler(CommandHandler("exams", exams_cmd))
    app.add_handler(CommandHandler("yojanas", yojanas_cmd))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    logger.info("Bot is running!")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
