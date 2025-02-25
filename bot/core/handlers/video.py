from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from bot.core.utils import ffmpeg_wrapper, helpers

async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = await update.message.effective_attachment.get_file()
    file_path = await helpers.download_file(file)
    
    keyboard = [
        [InlineKeyboardButton("✂️ Trim Video", callback_data="trim_video"),
         InlineKeyboardButton("🎞️ Convert Format", callback_data="convert_video")],
        [InlineKeyboardButton("🖼️ Add Watermark", callback_data="add_watermark"),
         InlineKeyboardButton("🎬 Create GIF", callback_data="create_gif")]
    ]
    
    await update.message.reply_text(
        "🎥 Choose video action:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
