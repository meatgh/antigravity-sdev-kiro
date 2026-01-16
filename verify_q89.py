import re

def verify_q89():
    file_path = "content/java/06-oop-fundamentals.md"
    
    with open(file_path, "r") as f:
        content = f.read()
    
    # 1. Extract Q89 Content
    start_marker = "#### Q89: What are Algebraic Data Types"
    end_marker = "#### Q90: What is a Monad"
    
    start_idx = content.find(start_marker)
    if start_idx == -1:
        print("❌ Q89 Header NOT Found!")
        exit(1)
        
    end_idx = content.find(end_marker)
    
    if end_idx == -1:
         q89_content = content[start_idx:]
    else:
         q89_content = content[start_idx:end_idx]
    
    line_count = len(q89_content.split('\n'))
    
    print(f"🔍 Verifying Q89 Content...")
    print(f"📊 Q89 Line Count: {line_count}")
    
    # 2. Check for Requirements
    required_sections = {
        "Project 1: Expression Evaluator": r"Project 1.*Expression Evaluator",
        "Project 2: Result Pattern": r"Project 2.*Result",
        "Project 3: FSM": r"Project 3.*Finite State Machine",
        "Deep Dive: Sum Types": r"Sum Types",
        "Deep Dive: Exhaustiveness": r"Exhaustiveness",
        "Visualization": r"Interactive Sealed",
    }
    
    missing = []
    for name, regex in required_sections.items():
        if re.search(regex, q89_content, re.IGNORECASE):
            print(f"✅ Found {name}")
        else:
            print(f"❌ Missing {name}")
            missing.append(name)
            
    # 3. Verdict
    if line_count < 2000:
        print(f"❌ Line Count FAILED. {line_count} < 2000")
        missing.append("Line Count")
        
    if missing:
        print("\n⚠️ Q89 VERIFICATION FAILED.")
    else:
        print("\n🎉 Q89 VERIFICATION PASSED! Elite Senior SDE Standard Met.")

if __name__ == "__main__":
    verify_q89()
