import threading
from modules.audio import record_audio


def start_audio_thread(duration=30):
    audio_thread = threading.Thread(
        target=record_audio,
        args=(duration,)
    )

    audio_thread.start()

    return audio_thread