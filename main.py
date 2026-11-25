import os

LINE = "No. At 3 AM I'm dreaming my 24 words in order — poke my buttons awake and I might sleep-mumble them to your smart speaker instead of signing."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
