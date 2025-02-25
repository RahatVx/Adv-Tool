VIDEO_PRESETS = {
    'compress': {
        'low': {'crf': 28, 'preset': 'fast'},
        'medium': {'crf': 23, 'preset': 'medium'},
        'high': {'crf': 18, 'preset': 'slow'}
    },
    'resolution': {
        '1080p': {'width': 1920, 'height': 1080},
        '720p': {'width': 1280, 'height': 720},
        '480p': {'width': 854, 'height': 480}
    }
}

AUDIO_PRESETS = {
    'bitrate': {
        'low': '64k',
        'medium': '128k', 
        'high': '320k'
    }
}
