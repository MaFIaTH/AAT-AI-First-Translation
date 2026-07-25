import re

input_path = "/home/beaver_bloyde/.gemini/antigravity-cli/brain/ebabe40d-2bde-4b8b-b33d-e06f1433328f/scratch/chunk_6.txt"
with open(input_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines, 1):
    if line.strip().startswith("LINE_"):
        print(f"{i}: {line.strip()}")
