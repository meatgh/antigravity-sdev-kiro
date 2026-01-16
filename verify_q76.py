import re

def verify_q76():
    file_path = "content/java/06-oop-fundamentals.md"
    
    checks = {
         "Project 1: SQL Query Builder": r"Project 1.*SQL Query Builder",
         "Project 2: Dynamic Fraud Detection Rule Engine": r"Project 2.*Rule Engine",
         "Project 3: Mathematical Expression Evaluator": r"Project 3.*Mathematical",
         "Project 4: Cron Expression Scheduler": r"Project 4.*Cron",
         "Project 5: Mini-Regex Engine": r"Project 5.*Regex",
         "Project 6: High-Frequency Trading Matcher": r"Project 6.*High-Frequency",
         "Project 7: Smart Home Automation": r"Project 7.*Smart Home",
         "Project 8: Functional Reactive Stream": r"Project 8.*Reactive Stream",
         "Project 9: Musical Notation Sequencer": r"Project 9.*Musical",
         "Project 10: Text Adventure Game": r"Project 10.*Text Adventure",
         "Project 11: L-System Fractal": r"Project 11.*L-System",
         "Project 12: JMH Benchmarking": r"Project 12.*Benchmarking",
         "Cheatsheet": r"Ultimate Interpreter Cheatsheet",
         "Visualization Link": r"interpreter_viz\.html",
         "Deep Dive: ReDoS": r"Deep Dive.*ReDoS",
         "Deep Dive: Stack Overflow": r"Deep Dive.*Stack Overflow",
         "Deep Dive: Cycle Detection": r"Deep Dive.*Cycle Detection",
         "LP: Customer Obsession": r"Customer Obsession",
         "LP: Invent and Simplify": r"Invent and Simplify",
         "LP: Dive Deep": r"Dive Deep",
         "LP: Bias for Action": r"Bias for Action",
         "Language: Python": r"Python Perspective",
         "Language: C++": r"C\+\+ Perspective",
         "Language: Go": r"Go Perspective",
    }

    print("🔍 Verifying Q76 Content...")
    print(f"📄 File: {file_path}")
    
    q76_lines = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            capturing = False
            for line in lines:
                if "#### Q76:" in line:
                    capturing = True
                if capturing:
                    if "#### Q77" in line:
                        break
                    q76_lines.append(line)
    except FileNotFoundError:
        print("❌ File not found.")
        return

    content = "".join(q76_lines)
    line_count = len(q76_lines)
    print(f"📊 Q76 Line Count: {line_count}")

    if line_count == 0:
        print("❌ Q76 Section Not Found (Lines are empty)!")
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
    elif line_count > 1000:
        print("⚠️ Line Count Status: Good (>1000) but below target 2000")
    else:
        print("❌ Line Count Status: Failed (<1000)")
        all_passed = False

    if all_passed and line_count > 2000:
        print("\n🎉 Q76 VERIFICATION PASSED! Senior SDE Standard Met.")
        print(f"FINAL METRICS: {line_count} Lines, 12 Projects, 3 Languages, 4 LPs, 1 Visualization.")
    else:
        print("\n⚠️ Q76 VERIFICATION FAILED. See missing items above.")

if __name__ == "__main__":
    verify_q76()
