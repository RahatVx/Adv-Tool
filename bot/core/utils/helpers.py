import os
import time
import magic
from config.settings import Config

class Helpers:
    @staticmethod
    async def download_file(file):
        file_name = f"{int(time.time())}_{file.file_name}"
        file_path = os.path.join(Config.TEMP_DIR, file_name)
        await file.download_to_drive(file_path)
        return file_path

    @staticmethod
    def validate_media(file_path):
        mime = magic.Magic(mime=True)
        file_type = mime.from_file(file_path)
        return file_type.split('/')[0] in ['video', 'audio', 'image']

    @staticmethod
    def format_size(size_bytes):
        # Size formatting logic
        pass
