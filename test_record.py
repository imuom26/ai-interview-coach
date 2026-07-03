import sounddevice as sd
from scipy.io.wavfile import write

duration = 5
sample_rate = 16000

print("Recording starts...")
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

print("Saved to recordings/interview.wav")