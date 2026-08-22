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

def verify_translation(translated_txt_path):
    """
    Verifies the translated txt file for syntax errors, mismatched brackets,
    backslashes, spacing errors, and missing translations.
    """
    line_pattern = re.compile(r"^LINE_(\d{5}): (.*?) ->\s*(.*)$")
    errors = []
    warnings = []
    
    with open(translated_txt_path, mode='r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line_str = line.strip()
            if not line_str or line_str.startswith('#'):
                continue
            
            # Check if it's a command line
            if line_str.startswith('[') and line_str.endswith(']'):
                # Verify commands are not corrupted
                if not re.match(r"^\[(NewLine\(\);|ReadKey\(\);|ClearText\(\);|Op_\d{2}\(\);|Wait\(\d+\);|SetTextColor\(\w+\);|[\w\s\(\);,]+)\]$", line_str):
                    warnings.append(f"Line {line_num}: Potential corrupted command '{line_str}'")
                continue
                
            match = line_pattern.match(line_str)
            if not match:
                errors.append(f"Line {line_num}: Line does not match the expected format (missing '->' or prefix)")
                continue
                
            idx = match.group(1)
            eng_text = match.group(2).strip()
            thai_text = match.group(3).strip()
            
            # 1. Check for empty translation
            if not thai_text and eng_text:
                warnings.append(f"Line {line_num} (LINE_{idx}): Translation is empty. Verify if this is an intended squash.")
                
            # 2. Check for mismatched angle brackets in name tags
            left_angle = thai_text.count('<')
            right_angle = thai_text.count('>')
            if left_angle != right_angle:
                errors.append(f"Line {line_num} (LINE_{idx}): Mismatched name brackets '<' ({left_angle}) vs '>' ({right_angle}) in '{thai_text}'")
                
            # 3. Check for odd double quotes
            quote_count = thai_text.count('"')
            if quote_count % 2 != 0:
                # We skip checking if it matches the original quote count (e.g. split quotes)
                eng_quote_count = eng_text.count('"')
                if quote_count % 2 != eng_quote_count % 2:
                    errors.append(f"Line {line_num} (LINE_{idx}): Odd number of double quotes ({quote_count}) in '{thai_text}'")
                
            # 4. Check for invalid backslashes (escaping quotes)
            if '\\' in thai_text:
                errors.append(f"Line {line_num} (LINE_{idx}): Backslash '\\' found in '{thai_text}'. Do not use backslashes to escape quotes.")
                
            # 5. Check for spaces inside name tags e.g. < นิค >
            if re.search(r"<\s+[^>]+|[^<]+\s+>", thai_text):
                warnings.append(f"Line {line_num} (LINE_{idx}): Spaces found inside name tags in '{thai_text}' (e.g. '< นิค >')")

    print("\n================ VERIFICATION RESULTS ================")
    print(f"Total Errors: {len(errors)}")
    print(f"Total Warnings: {len(warnings)}")
    
    if errors:
        print("\n❌ ERRORS FOUND (Must be fixed):")
        for err in errors:
            print(f"  - {err}")
            
    if warnings:
        print("\n⚠️ WARNINGS FOUND (Verify if intended):")
        for warn in warnings:
            print(f"  - {warn}")
            
    if not errors and not warnings:
        print("\n✅ Verification passed! No issues found.")
    print("======================================================\n")
    
    return len(errors) == 0

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

    # Verify command
    parser_verify = subparsers.add_parser('verify', help='Verify translated txt file for common formatting/syntax errors')
    parser_verify.add_argument('--translated', '-t', required=True, help='Path to the translated TXT file')

    args = parser.parse_args()

    if args.command == 'extract':
        extract_dialogue(args.input, args.output)
    elif args.command == 'merge':
        merge_translation(args.original, args.translated, args.output)
    elif args.command == 'verify':
        verify_translation(args.translated)
