from modules.filler_words import *

text = """
Hi, um, my name is Tasnia and I like machine learning.
Actually, I have worked on AI projects.
Uh, I also enjoy backend development.
"""

counts, total = count_filler_words(text)

print(counts)
print("Total:", total)