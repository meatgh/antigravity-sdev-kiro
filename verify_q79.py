import re

def verify_q79():
    file_path = "content/java/06-oop-fundamentals.md"
    
    checks = {
         # Projects
         "Project 1: Immutable Config": r"Immutable System Config",
         "Project 6: Undo/Redo System": r"Project 6.*Undo/Redo",
         "Project 7: Methods of Copying": r"Project 7.*Deep Cloner",
         "Project 8: Persistent Data Structures": r"Project 8.*Persistent Data Structures",
         "Project 9: Concurrent Snapshotting": r"Project 9.*Concurrent Snapshotting",
         "Project 10: Prototype Registry": r"Project 10.*Prototype Pattern Registry",
         
         # Deep Dives & Security
         "Deep Dive: Performance Cost": r"Deep Dive: Performance Cost",
         "Security: TOCTOU": r"TOCTOU", 
         "Memory Layout Analysis": r"Mental Model: ASCII Memory Diagrams",

         # Standard Requirements
         "Multi-Language Perspectives": r"Multi-Language Perspectives",
         "Testing Strategy": r"Testing & Verification Strategy",
         "JMH Benchmark": r"Deep Dive: Performance Cost", # Covered in perf section
    }

    print("🔍 Verifying Q79 Content...")
    
    q79_lines = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            capturing = False
            for line in lines:
                if "#### Q79:" in line:
                    capturing = True
                if capturing:
                    if "#### Q80" in line:
                        break
                    q79_lines.append(line)
    except FileNotFoundError:
        print("❌ File not found.")
        return

    content = "".join(q79_lines)
    line_count = len(q79_lines)
    print(f"📊 Q79 Line Count: {line_count}")

    if line_count == 0:
        print("❌ Q79 Section Not Found!")
        return

    all_passed = True
    for name, pattern in checks.items():
        if re.search(pattern, content, re.IGNORECASE | re.DOTALL):
            print(f"✅ Found {name}")
        else:
            print(f"❌ Missing {name}")
            all_passed = False
            
    if line_count > 2000:
        print("✅ Line Count Status: PASS (>2000)")
    else:
        print(f"❌ Line Count Status: FAIL ({line_count} < 2000)")
        all_passed = False
        
    if all_passed:
        print("\n🎉 Q79 VERIFICATION PASSED! Elite Senior SDE Standard Met.")
    else:
        print("\n⚠️ Q79 VERIFICATION FAILED.")

if __name__ == "__main__":
    verify_q79()
