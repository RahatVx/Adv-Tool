from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from bot.core.utils import helpers, video_effects

async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = await update.message.effective_attachment.get_file()
    file_path = await helpers.download_file(file)
    
    keyboard = [
        [InlineKeyboardButton("🖼 Convert Format", callback_data="convert_image"),
         InlineKeyboardButton("📐 Resize Image", callback_data="resize_image")],
        [InlineKeyboardButton("🎨 Enhance Quality", callback_data="enhance_image"),
         InlineKeyboardButton("🌀 Remove Background", callback_data="remove_bg")]
    ]
    
    await update.message.reply_text(
        "🖼 Choose image action:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
