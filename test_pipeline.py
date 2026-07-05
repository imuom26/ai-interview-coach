from modules.audio import *
from modules.transcriber import *
from modules.filler_words import *
from scorer import *

record_audio(10)

text = transcribe_audio()

print("\nTRANSCRIPTION:")
print(text)

counts, total = count_filler_words(text)

print("\nFILLERS:")
print(counts)

communication_score = (
    calculate_communication_score(total)
)

print(
    f"\nCommunication Score: "
    f"{communication_score}%"
)