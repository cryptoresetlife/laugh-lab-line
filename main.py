"""One-Liner Laugh Lab: a robot vacuum's excuse after eating a sock."""
import os

LINE = (
    "I didn't eat your sock. Its partner left months ago, "
    "and it asked me to take it somewhere quiet."
)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE.strip())
