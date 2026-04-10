import os, logging, requests
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters
from data import SCHEMES, YOJANAS, JOBS, EXAMS, search_all, get_item_by_id

load_dotenv()
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
GROQ_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

def ask_groq(system, user):
    if not GROQ_KEY: return "GROQ_API_KEY not set."
    try:
        r = requests.post(GROQ_URL, headers={"Authorization": f"Bearer {GROQ_KEY}", "Content-Type": "application/json"},
            json={"model": "llama3-8b-8192", "messages": [{"role":"system","content":system},{"role":"user","content":user}], "max_tokens":600, "temperature":0.3}, timeout=30)
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"].strip()
    except Exception as e: return f"AI unavailable: {e}"

def ai_explain(item, t):
    return ask_groq("Helpful Indian government assistant. Simple Hinglish. Emojis. Max 300 words.",
        f"Explain {t}: {item['name']}\nDesc: {item['description']}\nEligibility: {item.get('eligibility','')}\nBenefit: {item.get('benefit','')}\nApply: {item.get('how_to_apply','')}")

def main_menu_kb():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🏛 Schemes", callback_data="cat_schemes"), InlineKeyboardButton("🟠 Yojanas", callback_data="cat_yojanas")],
        [InlineKeyboardButton("💼 Jobs", callback_data="cat_jobs"), InlineKeyboardButton("📝 Exams", callback_data="cat_exams")],
        [InlineKeyboardButton("🔍 Search", callback_data="cat_search"), InlineKeyboardButton("🤖 AI", callback_data="cat_ai")],
    ])

def list_kb(items, p):
    em = {"s":"🏛","y":"🟠","j":"💼","e":"📝"}.get(p,"📌")
    b = [[InlineKeyboardButton(f"{em} {i['name']}", callback_data=f"detail_{i['id']}")] for i in items]
    b.append([InlineKeyboardButton("🔙 Menu", callback_data="main_menu")])
    return InlineKeyboardMarkup(b)

def detail_kb(iid):
    return InlineKeyboardMarkup([[InlineKeyboardButton("🤖 AI Explain", callback_data=f"ai_{iid}")],[InlineKeyboardButton("🔙 Menu", callback_data="main_menu")]])

def fmt(item):
    docs = "\n".join(f"- {d}" for d in item.get("documents",[]))
    return f"{item['name']}\n{item.get('hindi_name','')}\n\nKya hai:\n{item['description']}\n\nEligibility:\n{item.get('eligibility','N/A')}\n\nBenefit:\n{item.get('benefit','N/A')}\n\nDocuments:\n{docs}\n\nApply:\n{item.get('how_to_apply','N/A')}\n\nWebsite:\n{item.get('website','N/A')}"

async def start(u, c):
    name = u.effective_user.first_name or "Dost"
    await u.message.reply_text(f"Namaste {name}! India Government Bot\n\nSchemes, Yojanas, Jobs, Exams - sab kuch yahan!\n\nType karo ya button dabao:", reply_markup=main_menu_kb())

async def help_cmd(u, c): await u.message.reply_text("/start /schemes /jobs /exams /yojanas\nType: kisan, health, railway, loan, army, neet")
async def schemes_cmd(u, c): await u.message.reply_text("Schemes:", reply_markup=list_kb(SCHEMES,"s"))
async def jobs_cmd(u, c): await u.message.reply_text("Jobs:", reply_markup=list_kb(JOBS,"j"))
async def exams_cmd(u, c): await u.message.reply_text("Exams:", reply_markup=list_kb(EXAMS,"e"))
async def yojanas_cmd(u, c): await u.message.reply_text("Yojanas:", reply_markup=list_kb(YOJANAS,"y"))

async def handle_text(u, c):
    q = u.message.text.strip().lower()
    if q in ["scheme","schemes","yojana"]: await schemes_cmd(u,c); return
    if q in ["job","jobs","naukri"]: await jobs_cmd(u,c); return
    if q in ["exam","exams"]: await exams_cmd(u,c); return
    if q in ["yojanas","yojana"]: await yojanas_cmd(u,c); return
    results = search_all(q)
    total = sum(len(v) for v in results.values())
    if total == 0:
        await u.message.reply_text("Searching...")
        reply = ask_groq("Expert Indian government schemes assistant. Hinglish. Emojis.", u.message.text)
        await u.message.reply_text(f"AI:\n\n{reply}", reply_markup=main_menu_kb()); return
    msg = f"Results for '{q}' ({total}):\n\n"
    buttons = []
    for item in (results["schemes"]+results["yojanas"])[:3]:
        em = "🏛" if item in results["schemes"] else "🟠"
        msg += f"{em} {item['name']}\n"
        buttons.append([InlineKeyboardButton(f"{em} {item['name']}", callback_data=f"detail_{item['id']}")])
    for item in results["jobs"][:2]:
        msg += f"💼 {item['name']}\n"
        buttons.append([InlineKeyboardButton(f"💼 {item['name']}", callback_data=f"detail_{item['id']}")])
    for item in results["exams"][:2]:
        msg += f"📝 {item['name']}\n"
        buttons.append([InlineKeyboardButton(f"📝 {item['name']}", callback_data=f"detail_{item['id']}")])
    buttons.append([InlineKeyboardButton("🔙 Menu", callback_data="main_menu")])
    await u.message.reply_text(msg, reply_markup=InlineKeyboardMarkup(buttons))

async def btn(u, c):
    q = u.callback_query; d = q.data
    await q.answer()
    if d == "main_menu": await q.edit_message_text("Main Menu:", reply_markup=main_menu_kb())
    elif d == "cat_schemes": await q.edit_message_text("Schemes:", reply_markup=list_kb(SCHEMES,"s"))
    elif d == "cat_yojanas": await q.edit_message_text("Yojanas:", reply_markup=list_kb(YOJANAS,"y"))
    elif d == "cat_jobs": await q.edit_message_text("Jobs:", reply_markup=list_kb(JOBS,"j"))
    elif d == "cat_exams": await q.edit_message_text("Exams:", reply_markup=list_kb(EXAMS,"e"))
    elif d == "cat_search": await q.edit_message_text("Type any keyword: kisan, health, railway, loan, army...")
    elif d == "cat_ai": await q.edit_message_text("Type your question in Hindi or English!")
    elif d.startswith("detail_"):
        item = get_item_by_id(d.replace("detail_",""))
        if item: await q.edit_message_text(fmt(item), reply_markup=detail_kb(item['id']), disable_web_page_preview=True)
    elif d.startswith("ai_"):
        item = get_item_by_id(d.replace("ai_",""))
        if item:
            await q.edit_message_text("AI samjha raha hai...")
            exp = ai_explain(item, "scheme/job/exam")
            await q.edit_message_text(f"AI:\n\n{exp}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Details", callback_data=f"detail_{item['id']}")],[InlineKeyboardButton("Menu", callback_data="main_menu")]]))

def main():
    if not BOT_TOKEN: raise ValueError("BOT_TOKEN not set!")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("schemes", schemes_cmd))
    app.add_handler(CommandHandler("jobs", jobs_cmd))
    app.add_handler(CommandHandler("exams", exams_cmd))
    app.add_handler(CommandHandler("yojanas", yojanas_cmd))
    app.add_handler(CallbackQueryHandler(btn))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    logger.info("Bot running!")
    app.run_polling(drop_pending_updates=True, allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
