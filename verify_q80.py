import re

def verify_q80():
    file_path = "content/java/06-oop-fundamentals.md"
    
    checks = {
         # Projects
         "Project 1: Monolith Decomposition": r"Project 1.*Monolith Decomposition",
         "Project 2: Plugin Framework": r"Project 2.*Plugin Framework",
         "Project 3: Generic Repository": r"Project 3.*Generic Repository",
         
         # Deep Dives & Theory
         "Deep Dive: Dependency Rule": r"Deep Dive.*Dependency Rule",
         "Liskov Substitution Principle": r"Liskov Substitution Principle",
         "Interface Segregation": r"Interface Segregation Principle",
         
         # Standard Requirements
         "Multi-Language Perspectives": r"Multi-Language Perspectives",
         "Interview Simulation": r"Interview Simulation",
         "Testing Strategy": r"Testing & Verification Strategy",
         "Visualizing Dependencies": r"Interact with Dependency Graph", # Key for D3
    }

    print("🔍 Verifying Q80 Content...")
    
    q80_lines = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            capturing = False
            for line in lines:
                if "#### Q80:" in line:
                    capturing = True
                if capturing:
                    if "#### Q81" in line:
                        break
                    q80_lines.append(line)
    except FileNotFoundError:
        print("❌ File not found.")
        return

    content = "".join(q80_lines)
    line_count = len(q80_lines)
    print(f"📊 Q80 Line Count: {line_count}")

    if line_count == 0:
        print("❌ Q80 Section Not Found!")
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
        print("\n🎉 Q80 VERIFICATION PASSED! Elite Senior SDE Standard Met.")
    else:
        print("\n⚠️ Q80 VERIFICATION FAILED.")

if __name__ == "__main__":
    verify_q80()
