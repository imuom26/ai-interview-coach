FILLER_WORDS = [
    "um",
    "uh",
    "like",
    "actually",
    "basically",
    "you know"
]


def count_filler_words(text):
    text = text.lower()

    counts = {}

    total = 0

    for word in FILLER_WORDS:
        count = text.count(word)

        counts[word] = count

        total += count

    return counts, total