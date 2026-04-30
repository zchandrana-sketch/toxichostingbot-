# 🤖 Toxic Hosting Bot

A Telegram bot for hosting and managing Python (.py) files.

## ✨ Features

- 📤 Upload Python files (.py)
- 📁 Store and manage files
- 📋 List all uploaded files
- 🔒 Secure file handling
- 🚀 Fast and reliable
- 24/7 Availability

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Bot Framework:** python-telegram-bot
- **Hosting:** Render
- **Storage:** In-Memory (can be upgraded to database)

## 📦 Installation

### Local Setup

1. Clone the repository:
```bash
git clone https://github.com/zchandrana-sketch/toxichostingbot-.git
cd toxichostingbot-
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file:
```bash
cp .env.example .env
```

5. Add your bot token to `.env`:
```
TELEGRAM_BOT_TOKEN=your_bot_token_here
```

6. Run the bot:
```bash
python bot.py
```

## 🚀 Deployment on Render

### Step 1: Prepare GitHub Repository
- Make sure your repository is public
- Push all files to GitHub

### Step 2: Create Render Account
1. Go to [render.com](https://render.com)
2. Sign up with GitHub account

### Step 3: Deploy the Bot
1. Click **"New +"** → **"Web Service"**
2. Select your `toxichostingbot-` repository
3. Configure settings:
   - **Name:** `toxichostingbot`
   - **Region:** Choose nearest to you
   - **Branch:** `main`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python bot.py`

### Step 4: Add Environment Variables
1. In Render dashboard, go to **Environment**
2. Add variable:
   ```
   TELEGRAM_BOT_TOKEN = your_bot_token_here
   ```
3. Click **"Deploy"**

### Step 5: Monitor Deployment
- Go to **Logs** tab to see deployment status
- Wait for "Bot started successfully!" message
- Your bot is now live! 🎉

## 📱 Bot Commands

| Command | Description |
|---------|-------------|
| `/start` | Welcome message and instructions |
| `/upload` | Upload instructions for .py files |
| `/list` | View all your uploaded files |
| `/help` | Get help and usage instructions |
| `/about` | About the bot and developer info |

## 💻 How to Use

1. **Find the bot:** Search `@toxichostingbot` on Telegram
2. **Start:** Click `/start`
3. **Upload:** Send a .py file to the bot
4. **View:** Use `/list` to see all your files

## 📝 Getting Bot Token

1. Open Telegram
2. Search for `@BotFather`
3. Send `/newbot`
4. Follow instructions
5. Copy the token and add to `.env`

## 🔒 Security

- Never commit `.env` file
- Keep your bot token secret
- `.gitignore` prevents sensitive data from being pushed
- Use environment variables for sensitive data

## 📊 File Limitations

- **File Type:** .py (Python files only)
- **Size:** Up to 50MB per file
- **Storage:** In-memory (per session)

## 🐛 Troubleshooting

### Bot not responding?
1. Check if bot token is correct
2. Verify TELEGRAM_BOT_TOKEN in environment variables
3. Check logs on Render dashboard
4. Make sure bot is running

### Files not uploading?
1. Check if file is .py format
2. File size should be less than 50MB
3. Check Render logs for errors

## 🚀 Future Enhancements

- [ ] Database integration (MongoDB/PostgreSQL)
- [ ] File download feature
- [ ] File expiration time
- [ ] Multiple file formats support
- [ ] User authentication
- [ ] File sharing between users
- [ ] Admin dashboard

## 👨‍💻 Developer

**@zchandrana_sketch**

## 📄 License

MIT License - Feel free to use and modify

## 📞 Support

For issues or questions:
1. Check README.md
2. Review bot logs
3. Contact developer

---

**Made with ❤️ by Toxic Hosting Team**
