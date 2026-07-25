import csv
import re
import sys
import argparse

def parse_csv_row(row):
    """
    Parses a CSV row. Returns (type, content)
    Types: 'command', 'dialogue', 'empty'
    """
    if not row or (len(row) == 1 and not row[0].strip()):
        return 'empty', ''
    col1 = row[0].strip()
    if col1.startswith('#"'):
        # Extract the dialogue text inside the #"..." format
        # e.g., #"It's been two months since" -> It's been two months since
        # If it was escaped in CSV as "#""It's been two months since"""
        # Python csv reader will automatically unescape it to #"It's been two months since"
        dialogue_text = col1[2:-1] if col1.endswith('"') else col1[2:]
        return 'dialogue', dialogue_text
    elif col1.startswith('[') and col1.endswith(']'):
        return 'command', col1
    else:
        return 'other', col1

def extract_dialogue(csv_path, txt_path):
    """
    Extracts dialogue lines from the CSV and formats them into a compact text file.
    """
    with open(csv_path, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)

    current_speaker = "Clear Speaker"
    current_color = "White"
    extracted_lines = []

    for idx, row in enumerate(rows):
        row_type, content = parse_csv_row(row)
        
        if row_type == 'command':
            # Track speaker and color
            if content.startswith('[SetTextColor('):
                current_color = content[14:-2] # e.g. Blue, Green, Red, White
            elif content in ['[NewLine();]', '[ReadKey();]'] or content.startswith('[Op_'):
                extracted_lines.append({
                    'type': 'command',
                    'text': content
                })
            elif content not in ['[ClearText();]'] and not content.startswith('[Wait('):
                current_speaker = content[1:-1]
        
        elif row_type == 'dialogue':
            # We save the row index (0-indexed) so we can map it back during merge
            context_str = f"#{current_speaker} ({current_color})"
            extracted_lines.append({
                'type': 'dialogue',
                'index': idx,
                'context': context_str,
                'text': content
            })

    # Write to target txt file
    with open(txt_path, mode='w', encoding='utf-8') as f:
        f.write("# ========================================================\n")
        f.write("# PHOENIX WRIGHT TRANSLATION FILE (COMPACT FORMAT)\n")
        f.write("# Translate ONLY the text after the '->' symbol.\n")
        f.write("# Copy the bracketed command lines (e.g. [NewLine();]) verbatim.\n")
        f.write("# Keep the '<>' names formatting rules.\n")
        f.write("# ========================================================\n\n")
        
        last_context = ""
        for item in extracted_lines:
            if item['type'] == 'command':
                f.write(f"{item['text']}\n")
            elif item['type'] == 'dialogue':
                if item['context'] != last_context:
                    f.write(f"\n{item['context']}\n")
                    last_context = item['context']
                # Output in format: LINE_00004: English text -> 
                f.write(f"LINE_{item['index']:05d}: {item['text']} -> \n")

    print(f"Successfully extracted {len(extracted_lines)} items to {txt_path}")

def merge_translation(original_csv_path, translated_txt_path, output_csv_path):
    """
    Reads the translated txt file and merges it back into the original CSV layout.
    """
    # Read the translated txt lines
    translations = {}
    line_pattern = re.compile(r"^LINE_(\d{5}): (.*?) ->\s*(.*)$")

    with open(translated_txt_path, mode='r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            match = line_pattern.match(line)
            if match:
                idx = int(match.group(1))
                eng_text = match.group(2)
                thai_translation = match.group(3).strip()
                
                # If there's no translation supplied, we fall back to empty or english
                if not thai_translation:
                    thai_translation = ""
                
                translations[idx] = thai_translation
            else:
                # Support lines that might have multiple lines or parsing issues
                pass

    # Read original CSV
    with open(original_csv_path, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)

    # Reconstruct CSV
    output_rows = []
    for idx, row in enumerate(rows):
        row_type, content = parse_csv_row(row)
        
        if idx in translations:
            thai_text = translations[idx]
            # Wrap in #"..." format
            formatted_thai = f'#"{thai_text}"'
            # Update Column 3 (index 2)
            if len(row) >= 3:
                row[2] = formatted_thai
            elif len(row) == 2:
                row.append(formatted_thai)
            elif len(row) == 1:
                row.extend(['', formatted_thai])
            else:
                row = ['', '', formatted_thai]
        else:
            # For non-dialogue lines, Column 3 is the same as Column 1
            if row_type == 'command':
                val = row[0]
            elif row_type == 'empty':
                val = ''
            else:
                val = row[0]
                
            if len(row) >= 3:
                row[2] = val
            elif len(row) == 2:
                row.append(val)
            elif len(row) == 1:
                row.extend(['', val])
            else:
                row = ['', '', val]
                
        output_rows.append(row)

    # Write output CSV
    with open(output_csv_path, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(output_rows)

    print(f"Successfully merged translations into {output_csv_path}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="PWAA Translation Helper to reduce token usage.")
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Extract command
    parser_extract = subparsers.add_parser('extract', help='Extract dialogue lines to a compact txt file')
    parser_extract.add_argument('--input', '-i', required=True, help='Path to the original script CSV')
    parser_extract.add_argument('--output', '-o', required=True, help='Path to output compact TXT file')

    # Merge command
    parser_merge = subparsers.add_parser('merge', help='Merge translated text back to the CSV')
    parser_merge.add_argument('--original', '-g', required=True, help='Path to the original script CSV')
    parser_merge.add_argument('--translated', '-t', required=True, help='Path to the translated TXT file')
    parser_merge.add_argument('--output', '-o', required=True, help='Path to output translated CSV')

    args = parser.parse_args()

    if args.command == 'extract':
        extract_dialogue(args.input, args.output)
    elif args.command == 'merge':
        merge_translation(args.original, args.translated, args.output)
