import argparse
import re
import sys

def count_lines_between_markers(file_path, start_marker, end_marker):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    start_index = -1
    end_index = -1

    # Find Start
    for i, line in enumerate(lines):
        if start_marker in line:
            start_index = i
            break
            
    if start_index == -1:
        print(f"❌ ERROR: Start marker '{start_marker}' not found.")
        return 0

    # Find End (after start)
    for i in range(start_index + 1, len(lines)):
        if end_marker in lines[i]:
            end_index = i
            break
            
    # If end marker not found (e.g., last question), goes to end of file
    if end_index == -1:
        end_index = len(lines)

    # Calculate Lines
    content_lines = lines[start_index:end_index]
    line_count = len(content_lines)
    
    # Calculate Code vs Text (heuristic)
    code_lines = len([l for l in content_lines if re.match(r'^\s*[^#<\s]', l)]) # Very rough approximation

    print(f"-" * 40)
    print(f"🧐 QUALITY ENFORCEMENT REPORT")
    print(f"TARGET: {start_marker} -> {end_marker}")
    print(f"-" * 40)
    print(f"📊 TOTAL LINES  : {line_count}")
    print(f"🎯 REQUIREMENT  : 2000+")
    print(f"-" * 40)

    if line_count >= 2000:
        print(f"✅ STATUS: PASSED (Senior SDE Standard Met)")
        print(f"🚀 You may proceed to the next task.")
        return True
    else:
        diff = 2000 - line_count
        print(f"❌ STATUS: FAILED")
        print(f"⚠️  MISSING {diff} LINES.")
        print(f"🛑 ACTION: DO NOT MARK COMPLETE. EXPAND CONTENT.")
        print(f"   SUGGESTION: Add 1 full Enterprise Project (~500 lines).")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    parser.add_argument("--start", required=True)
    parser.add_argument("--end", required=True)
    args = parser.parse_args()

    success = count_lines_between_markers(args.file, args.start, args.end)
    if not success:
        sys.exit(1) # Fail the build
