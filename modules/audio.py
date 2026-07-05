import sounddevice as sd
from scipy.io.wavfile import write


def record_audio(duration=10):

    sample_rate = 16000

    print("\nRecording started...")

    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    print("Recording finished.")

    write(
        "recordings/interview.wav",
        sample_rate,
        audio
    )