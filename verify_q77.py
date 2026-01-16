import re

def verify_q77():
    file_path = "content/java/06-oop-fundamentals.md"
    
    checks = {
         # Projects (Checking for titles or distinctive code)
         "Project 1: UI Event Handling": r"Project 1.*UI Event|class DragEvent extends BaseEvent",
         "Project 2: Universal Document Converter": r"Project 2.*Document Converter",
         "Project 3: Cross-Border Payment": r"Project 3.*Payment Processor",
         "Project 4: Physics & Combat": r"Project 4.*Physics",
         "Project 5: Compiler Type Checker": r"Project 5.*Compiler",
         
         # Deep Dives
         "Deep Dive: The Expression Problem": r"Deep Dive.*Expression Problem",
         "Deep Dive: Object Algebras": r"Object Algebras",
         
         # Multi-Language
         "Language: Python": r"Python.*singledispatch",
         "Language: C++": r"C\+\+.*dynamic_cast",
         "Language: Go": r"Go.*Type Switches",
         "Language: C#": r"C#.*dynamic.*keyword",
         
         # LPs & Best Practices
         "Amazon LP: Invent and Simplify": r"Invent and Simplify",
         "Best Practices": r"When to Avoid Double Dispatch",
         "Cheat Sheet": r"Cheat Sheet",
    }

    print("🔍 Verifying Q77 Content...")
    print(f"📄 File: {file_path}")
    
    q77_lines = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            capturing = False
            for line in lines:
                if "#### Q77:" in line:
                    capturing = True
                if capturing:
                    if "#### Q78" in line:
                        break
                    q77_lines.append(line)
    except FileNotFoundError:
        print("❌ File not found.")
        return

    content = "".join(q77_lines)
    line_count = len(q77_lines)
    print(f"📊 Q77 Line Count: {line_count}")

    if line_count == 0:
        print("❌ Q77 Section Not Found (Lines are empty)!")
        return

    all_passed = True
    for name, pattern in checks.items():
        if re.search(pattern, content, re.IGNORECASE | re.DOTALL):
            print(f"✅ Found {name}")
        else:
            print(f"❌ Missing {name}")
            all_passed = False
            
    if line_count > 2000:
        print("✅ Line Count Status: Excellent (>2000)")
    elif line_count > 1500:
        print("⚠️ Line Count Status: Good (>1500) but below target 2000. Acceptable if content is dense.")
    else:
        print("❌ Line Count Status: Low (<1500)")
        
    if all_passed and line_count > 1500:
        print("\n🎉 Q77 VERIFICATION PASSED! Senior SDE Standard Met.")
        print(f"FINAL METRICS: {line_count} Lines, 5 Enterprise Projects, 4 Languages, Deep Analysis.")
    else:
        print("\n⚠️ Q77 VERIFICATION FAILED. See missing items above.")

if __name__ == "__main__":
    verify_q77()
