import re

def verify_q86():
    file_path = "content/java/06-oop-fundamentals.md"
    
    with open(file_path, "r") as f:
        content = f.read()
    
    # 1. Extract Q86 Content
    start_marker = "#### Q86: How do ClassLoaders work"
    end_marker = "#### Q87: What is Type Erasure"
    
    start_idx = content.find(start_marker)
    if start_idx == -1:
        print("❌ Q86 Header NOT Found!")
        exit(1)
        
    end_idx = content.find(end_marker)
    
    if end_idx == -1:
         q86_content = content[start_idx:]
    else:
         q86_content = content[start_idx:end_idx]
    
    line_count = len(q86_content.split('\n'))
    
    print(f"🔍 Verifying Q86 Content...")
    print(f"📊 Q86 Line Count: {line_count}")
    
    # 2. Check for Requirements
    required_sections = {
        "Project 1: Hot-Swap": r"Project 1.*Hot-Swap",
        "Project 2: Isolation": r"Project 2.*Plugin Isolation",
        "Project 3: Encryption": r"Project 3.*Encryption",
        "Deep Dive: Delegation": r"Delegation Model",
        "Deep Dive: Bytecode": r"javap",
        "Visualization": r"Interactive ClassLoader",
    }
    
    missing = []
    for name, regex in required_sections.items():
        if re.search(regex, q86_content, re.IGNORECASE):
            print(f"✅ Found {name}")
        else:
            print(f"❌ Missing {name}")
            missing.append(name)
            
    # 3. Verdict
    if line_count < 2000:
        print(f"❌ Line Count FAILED. {line_count} < 2000")
        missing.append("Line Count")
        
    if missing:
        print("\n⚠️ Q86 VERIFICATION FAILED.")
    else:
        print("\n🎉 Q86 VERIFICATION PASSED! Elite Senior SDE Standard Met.")

if __name__ == "__main__":
    verify_q86()
