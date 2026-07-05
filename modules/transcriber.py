from faster_whisper import WhisperModel


model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)


def transcribe_audio():

    segments, info = model.transcribe(
        "recordings/interview.wav",
        language="en",
        beam_size=5
    )

    text = ""

    for segment in segments:
        text += segment.text + " "

    return text