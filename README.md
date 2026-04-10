# 🇮🇳 India Government Schemes Telegram Bot

A FREE Telegram bot that tells you about:
- 🏛️ Government Schemes (PM Kisan, Ayushman, Mudra...)
- 🟠 Yojanas (Ujjwala, Beti Bachao, Swachh Bharat...)
- 💼 Sarkari Jobs (SSC, Railway, Bank, Army...)
- 📝 Exams (JEE, NEET, UPSC, CTET...)

**AI powered by Groq (free) | Deployed on Railway.app (free)**

---

## 🚀 STEP 1 — Get Your Free Keys (10 minutes)

### A) Telegram Bot Token (FREE)
1. Open Telegram → search **@BotFather**
2. Send `/newbot`
3. Choose a name: e.g. `India Schemes Bot`
4. Choose a username: e.g. `india_schemes_bot`
5. Copy the token it gives you (looks like `7123456789:ABCdef...`)

### B) Groq API Key (FREE)
1. Go to → https://console.groq.com
2. Sign up with Google/email (free)
3. Go to **API Keys** → **Create API Key**
4. Copy the key (looks like `gsk_...`)

---

## 🚀 STEP 2 — Deploy on Railway.app (FREE)

### Option A — Deploy via GitHub (Recommended, easiest)

1. **Create a GitHub account** if you don't have one → github.com

2. **Create a new repository** on GitHub:
   - Click `+` → `New repository`
   - Name it `india-gov-bot`
   - Set to **Public**
   - Click `Create repository`

3. **Upload these files** to the repository:
   - `bot.py`
   - `data.py`
   - `requirements.txt`
   - `Procfile`
   - `railway.json`
   
   (Click `Add file` → `Upload files` on GitHub)

4. **Go to Railway.app** → https://railway.app
   - Sign up with GitHub (free)
   - Click `New Project`
   - Click `Deploy from GitHub repo`
   - Select your `india-gov-bot` repo
   - Click `Deploy Now`

5. **Add Environment Variables** in Railway:
   - Go to your project → `Variables` tab
   - Add these two:
     ```
     BOT_TOKEN = paste_your_telegram_token_here
     GROQ_API_KEY = paste_your_groq_key_here
     ```
   - Click `Save` — Railway auto-restarts the bot

6. **Done!** Go to Telegram and test your bot 🎉

---

### Option B — Run Locally (for testing)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Create .env file
cp .env.example .env
# Edit .env and paste your BOT_TOKEN and GROQ_API_KEY

# 3. Run bot
python bot.py
```

---

## 🎯 How to Use the Bot

Open your bot on Telegram and:

| Type this | Bot shows |
|-----------|-----------|
| `/start` | Main menu with buttons |
| `scheme` or `yojana` | All schemes list |
| `job` or `naukri` | All jobs list |
| `exam` | All exams list |
| `kisan` | PM Kisan scheme details |
| `health` | Ayushman Bharat details |
| `railway` | Railway job details |
| `loan` | Mudra yojana details |
| Any question | AI answers in Hinglish |

---

## 📋 Bot Commands to set in BotFather

Send this to @BotFather → `/setcommands` → select your bot → paste:

```
start - Main menu
schemes - All government schemes
yojanas - All yojanas list
jobs - All sarkari jobs
exams - All government exams
help - Help and instructions
```

---

## ❓ Troubleshooting

| Problem | Fix |
|---------|-----|
| Bot not responding | Check Railway logs → Variables tab |
| `BOT_TOKEN` error | Re-check token from BotFather |
| AI not working | Re-check GROQ_API_KEY from console.groq.com |
| Railway deploy failed | Check all 5 files are uploaded to GitHub |

---

## 💡 Adding More Schemes

Open `data.py` and add to the `SCHEMES` list:

```python
{
    "id": "new_scheme",
    "name": "Scheme Name",
    "hindi_name": "हिंदी नाम",
    "category": "Category",
    "description": "What it is",
    "eligibility": "Who can apply",
    "documents": ["Doc 1", "Doc 2"],
    "how_to_apply": "1. Step one\n2. Step two",
    "website": "https://example.gov.in",
    "benefit": "What benefit",
    "tags": ["keyword1", "keyword2"]
},
```

Push to GitHub → Railway auto-deploys! ✅
