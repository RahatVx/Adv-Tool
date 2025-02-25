from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes

def setup_tools_handlers(app):
    app.add_handler(CommandHandler("tools", show_tools_menu))

async def show_tools_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📦 Batch Process", callback_data="batch_process"),
         InlineKeyboardButton("⚙️ Settings", callback_data="settings")],
        [InlineKeyboardButton("📊 Statistics", callback_data="stats"),
         InlineKeyboardButton("🛠 Admin Tools", callback_data="admin_tools")]
    ]
    
    await update.message.reply_text(
        "🛠️ Advanced Tools Menu:",
        reply_markup=InlineKeyboardMarkup(keyboard)
