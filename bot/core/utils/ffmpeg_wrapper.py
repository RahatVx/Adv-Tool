import ffmpeg
import asyncio

class FFmpegProcessor:
    @staticmethod
    async def compress(input_path, output_path, crf=23, preset='medium'):
        (
            ffmpeg
            .input(input_path)
            .output(output_path, crf=crf, preset=preset)
            .overwrite_output()
            .run_async()
        )
        
    @staticmethod
    async def add_subtitle(input_path, output_path, subtitle_text):
        (
            ffmpeg
            .input(input_path)
            .filter('drawtext', text=subtitle_text, fontsize=24, fontcolor='white')
            .output(output_path)
            .overwrite_output()
            .run_async()
        )
