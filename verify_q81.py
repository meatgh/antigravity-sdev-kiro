import re

def verify_q81():
    file_path = "content/java/06-oop-fundamentals.md"
    
    with open(file_path, "r") as f:
        content = f.read()
    
    # 1. Extract Q81 Content
    # Start: #### Q81: What is Clean Architecture
    # End:   #### Q82:
    
    pattern = r"(#### Q81: What is Clean Architecture.*?)(?=#### Q82:)"
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        print("❌ Q81 Header NOT Found!")
        exit(1)
        
    q81_content = match.group(1)
    line_count = len(q81_content.split('\n'))
    
    print(f"🔍 Verifying Q81 Content...")
    print(f"📊 Q81 Line Count: {line_count}")
    
    # 2. Check for Requirements
    required_sections = {
        "Project 1: Hollow Clean Core": r"Project 1.*Hollow.*Clean Core",
        "Project 2: Screaming Architecture": r"Project 2.*Screaming Architecture",
        "Project 3: Humble Object": r"Project 3.*Humble Object",
        "Deep Dive: Dependency Rule": r"Deep Dive.*Dependency Rule",
        "Visualization": r"Interact with Clean Architecture",
        "Multi-Language: Rust": r"Rust.*Ownership",
        "Testing Strategy": r"Testing.*Strategy",
    }
    
    missing = []
    for name, regex in required_sections.items():
        if re.search(regex, q81_content, re.IGNORECASE):
            print(f"✅ Found {name}")
        else:
            print(f"❌ Missing {name}")
            missing.append(name)
            
    # 3. Verdict
    if line_count < 2000:
        print(f"❌ Line Count FAILED. {line_count} < 2000")
        missing.append("Line Count")
        
    if missing:
        print("\n⚠️ Q81 VERIFICATION FAILED.")
    else:
        print("\n🎉 Q81 VERIFICATION PASSED! Elite Senior SDE Standard Met.")

if __name__ == "__main__":
    verify_q81()
