import re
import sys
import argparse

def parse_line(line):
    """
    Parses a single line from the script. Returns (type, content)
    Types: 'command', 'dialogue', 'empty', 'other'
    """
    line_str = line.strip()
    if not line_str:
        return 'empty', ''
    
    if line_str.startswith('#"'):
        # Extract dialogue text inside the #"..." format
        content = line_str[2:]
        if content.endswith('"'):
            content = content[:-1]
        return 'dialogue', content
    elif line_str.startswith('[') and line_str.endswith(']'):
        return 'command', line_str
    else:
        return 'other', line_str

def extract_dialogue(txt_path, output_txt_path):
    """
    Extracts dialogue lines from the text script and formats them into a compact text file.
    """
    with open(txt_path, mode='r', encoding='utf-8') as f:
        lines = f.readlines()

    current_speaker = "Clear Speaker"
    current_color = "White"
    extracted_lines = []

    for idx, line in enumerate(lines):
        row_type, content = parse_line(line)
        
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
            # Save the exact 0-indexed line number (idx) so we can map it back during merge
            context_str = f"#{current_speaker} ({current_color})"
            extracted_lines.append({
                'type': 'dialogue',
                'index': idx,
                'context': context_str,
                'text': content
            })

    # Write to target txt file
    with open(output_txt_path, mode='w', encoding='utf-8') as f:
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

    print(f"Successfully extracted {len(extracted_lines)} items to {output_txt_path}")

def merge_translation(original_txt_path, translated_txt_path, output_txt_path):
    """
    Reads the translated txt file and merges it back into the original script layout.
    """
    # Read the translated txt lines
    translations = {}
    line_pattern = re.compile(r"^LINE_(\d{5}): (.*?) ->\s*(.*)$")

    with open(translated_txt_path, mode='r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line_str = line.strip()
            if not line_str or line_str.startswith('#'):
                continue
            
            match = line_pattern.match(line_str)
            if match:
                idx = int(match.group(1))
                thai_translation = match.group(3).strip()
                
                # If there's no translation supplied, we fall back to empty
                if not thai_translation:
                    thai_translation = ""
                
                translations[idx] = thai_translation

    # Read original script
    with open(original_txt_path, mode='r', encoding='utf-8') as f:
        original_lines = f.readlines()

    # Reconstruct script lines
    output_lines = []
    for idx, line in enumerate(original_lines):
        if idx in translations:
            thai_text = translations[idx]
            # Preserve leading spaces of the original line structure (if any)
            leading_whitespace = line[:len(line) - len(line.lstrip())]
            newline = "\n" if line.endswith("\n") else ""
            
            merged_line = f'{leading_whitespace}#"{thai_text}"{newline}'
            output_lines.append(merged_line)
        else:
            output_lines.append(line)

    # Write output script
    with open(output_txt_path, mode='w', encoding='utf-8') as f:
        f.writelines(output_lines)

    print(f"Successfully merged translations into {output_txt_path}")

def verify_translation(translated_txt_path):
    """
    Verifies the translated txt file for syntax errors, mismatched brackets,
    backslashes, spacing errors, and missing translations.
    """
    line_pattern = re.compile(r"^LINE_(\d{5}):\s*(.*?)\s*->\s*(.*)$")
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
    parser_extract.add_argument('--input', '-i', required=True, help='Path to the original script text file')
    parser_extract.add_argument('--output', '-o', required=True, help='Path to output compact TXT file')

    # Merge command
    parser_merge = subparsers.add_parser('merge', help='Merge translated text back to the script')
    parser_merge.add_argument('--original', '-g', required=True, help='Path to the original script text file')
    parser_merge.add_argument('--translated', '-t', required=True, help='Path to the translated TXT file')
    parser_merge.add_argument('--output', '-o', required=True, help='Path to output translated script file')

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
