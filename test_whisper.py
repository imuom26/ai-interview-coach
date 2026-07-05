from faster_whisper import WhisperModel

print("Loading model...")

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

print("Transcribing...")

segments, info = model.transcribe(
    "recordings/interview.wav"
)

text = ""

for segment in segments:
    text += segment.text + " "

print("\nTRANSCRIPTION:")
print(text)
from modules.filler_words import *

counts, total = count_filler_words(text)

print("\nFILLER WORDS:")
print(counts)
print("Total:", total)
from scorer import *

communication_score = (
    calculate_communication_score(total)
)

print(
    f"Communication Score: "
    f"{communication_score}%"
)