import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram.error import TelegramError
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get bot token from environment
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

if not BOT_TOKEN:
    logger.error("TELEGRAM_BOT_TOKEN not found in environment variables!")
    exit(1)

# Dictionary to store user files
user_files = {}

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /start is issued."""
    user = update.effective_user
    welcome_message = f"""
🎉 Welcome to **Toxic Hosting Bot** {user.mention_html()}!

📁 I can host your .py (Python) files!

**Available Commands:**
/start - Show this welcome message
/upload - Upload a .py file
/list - See all your uploaded files
/help - Get help
/about - About this bot

**How to use:**
1. Send me a .py file
2. I'll host it for you
3. Use /list to see all files

Let's get started! 🚀
    """
    await update.message.reply_html(welcome_message)

# Upload command
async def upload(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle upload command."""
    upload_message = """
📤 **Upload a Python File**

Just send me a .py file and I'll host it for you!

Example:
- Send any .py file
- I'll store it
- Use /list to see all files

✅ Ready to upload? Send the file now!
    """
    await update.message.reply_text(upload_message)

# List command
async def list_files(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """List all uploaded files for the user."""
    user_id = update.effective_user.id
    
    if user_id not in user_files or not user_files[user_id]:
        await update.message.reply_text(
            "📭 You haven't uploaded any files yet!\n\nUse /upload to start uploading."
        )
        return
    
    files_list = user_files[user_id]
    message = "📁 **Your Uploaded Files:**\n\n"
    
    for i, file_info in enumerate(files_list, 1):
        message += f"{i}. 📄 {file_info['filename']}\n"
    
    await update.message.reply_text(message)

# Help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when /help is issued."""
    help_text = """
🆘 **Help & Instructions**

**Commands:**
/start - Welcome message
/upload - Upload instructions
/list - View your files
/help - This help message
/about - About the bot

**How to upload:**
1. Click the attachment/paperclip icon
2. Select a .py file from your device
3. Send it
4. Bot will host it!

**Supported File Types:**
✅ .py (Python files)

**File Storage:**
All files are stored safely and can be accessed via /list

**Questions?**
Contact @zchandrana_sketch
    """
    await update.message.reply_text(help_text)

# About command
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send about information."""
    about_text = """
ℹ️ **About Toxic Hosting Bot**

🤖 **Bot Name:** Toxic Hosting Bot
📌 **Purpose:** Host and manage Python files
👨‍💻 **Developer:** @zchandrana_sketch
🌐 **Hosting:** Render
💾 **Database:** In-Memory Storage

**Features:**
✅ Upload .py files
✅ List uploaded files
✅ File management
✅ 24/7 availability

**Version:** 1.0.0

**Built with:** python-telegram-bot
    """
    await update.message.reply_text(about_text)

# Handle file uploads
async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle document/file uploads."""
    user_id = update.effective_user.id
    document = update.message.document
    
    # Check if file is .py
    if not document.file_name.endswith('.py'):
        await update.message.reply_text(
            "❌ Only .py (Python) files are supported!\n\nPlease send a Python file."
        )
        return
    
    # Store file info
    if user_id not in user_files:
        user_files[user_id] = []
    
    file_info = {
        'filename': document.file_name,
        'file_id': document.file_id,
        'file_size': document.file_size,
        'mime_type': document.mime_type
    }
    
    user_files[user_id].append(file_info)
    
    await update.message.reply_text(
        f"✅ File uploaded successfully!\n\n"
        f"📄 **Filename:** {document.file_name}\n"
        f"📊 **Size:** {document.file_size / 1024:.2f} KB\n\n"
        f"Use /list to see all your files."
    )
    logger.info(f"User {user_id} uploaded file: {document.file_name}")

# Handle text messages
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle text messages."""
    text = update.message.text
    
    if text.startswith('/'):
        return  # Command will be handled by command handler
    
    await update.message.reply_text(
        "👋 Hello! I'm Toxic Hosting Bot.\n\n"
        "Use /help for available commands or /upload to start uploading files!"
    )

# Error handler
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log the error and send a telegram message to notify the developer."""
    logger.error(f"Exception while handling an update:", exc_info=context.error)
    
    if isinstance(update, Update) and update.effective_message:
        await update.effective_message.reply_text(
            "❌ An error occurred. Please try again later."
        )

def main() -> None:
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("upload", upload))
    application.add_handler(CommandHandler("list", list_files))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about))

    # Register message handlers
    application.add_handler(MessageHandler(filters.Document.ALL, handle_document))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    # Add error handler
    application.add_error_handler(error_handler)

    # Start the Bot
    logger.info("Bot started successfully!")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
