from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config.settings import Config
from .handlers import (
    video, audio, image, tools
)

class MediaBot:
    def __init__(self):
        self.app = Application.builder().token(Config.BOT_TOKEN).build()
        self._setup_handlers()
        
    def _setup_handlers(self):
        self.app.add_handler(CommandHandler("start", self._start))
        self.app.add_handler(MessageHandler(filters.VIDEO, video.handle_video))
        self.app.add_handler(MessageHandler(filters.AUDIO, audio.handle_audio))
        self.app.add_handler(MessageHandler(filters.PHOTO, image.handle_image))
        
        # Register callback handlers
        tools.setup_tools_handlers(self.app)
        
    async def _start(self, update, context):
        await update.message.reply_text(
            "🎉 Welcome to Ultimate Media Bot!\n"
            "Send any media file or use /tools menu"
        )
        
    def run(self):
        self.app.run_polling()
