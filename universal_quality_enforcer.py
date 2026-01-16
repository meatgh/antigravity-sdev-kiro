import re
import sys
import os

TARGET_FILE = "content/java/06-oop-fundamentals.md"

def analyze_file(filepath):
    if not os.path.exists(filepath):
        print(f"❌ File not found: {filepath}")
        return

    with open(filepath, 'r') as f:
        lines = f.readlines()

    print(f"🔍 Analyzing {filepath} ({len(lines)} lines)...\n")

    current_q = None
    q_start = 0
    stats = {}
    q_ids_to_check = ["41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "67", "68", "69", "70", "71"]
    # Regex for Question Headers
    q_pattern = re.compile(r"^#### (Q\d+):")

    for i, line in enumerate(lines):
        match = q_pattern.match(line)
        if match:
            # End previous question
            if current_q:
                stats[current_q]['end'] = i
                stats[current_q]['lines'] = i - q_start
            
            # Start new question
            current_q = match.group(1)
            q_start = i
            stats[current_q] = {'start': i, 'content': []}
        
        if current_q:
            stats[current_q]['content'].append(line)

    # End last question
    if current_q:
        stats[current_q]['end'] = len(lines)
        stats[current_q]['lines'] = len(lines) - q_start

    # Verify Standards
    passed_all = True
    for q_id, data in stats.items():
        # Identify specific qs to check (or all)
        # We focus on Q65, Q66, Q67
        if q_id not in ['Q66', 'Q67', 'Q68', 'Q69', 'Q70', 'Q71']: 
            continue

        content_str = "".join(data['content'])
        line_count = data['lines']
        
        # Check Enterprise Projects
        # Check Enterprise Projects (Robust Regex)
        project_count = len(re.findall(r"^#+ .*Project", content_str, re.IGNORECASE | re.MULTILINE))
        
        # Check Visualization
        has_viz = "d3.select" in content_str or "visualization" in content_str.lower()
        
        # Check Reference
        has_ref = "REFERENCES" in content_str

        print(f"📊 {q_id} Report:")
        print(f"   - Lines: {line_count} (Target: 2000+)")
        print(f"   - Projects: {project_count} (Target: 3+)")
        print(f"   - Visualization: {'✅' if has_viz else '❌'}")
        print(f"   - References: {'✅' if has_ref else '❌'}")

        if line_count < 2000:
            print(f"   ❌ FAILED LINE COUNT (Needs {2000 - line_count} more)")
            passed_all = False
        else:
            print("   ✅ LINE COUNT PASSED")
        
        print("")

    if passed_all:
        print("\n✅ OVERALL STATUS: ALL CHECKS PASSED")
    else:
        print("\n❌ OVERALL STATUS: SOME CHECKS FAILED")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = TARGET_FILE
    analyze_file(target)
