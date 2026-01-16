import re

def verify_q88():
    file_path = "content/java/06-oop-fundamentals.md"
    
    with open(file_path, "r") as f:
        content = f.read()
    
    # 1. Extract Q88 Content
    start_marker = "#### Q88: How do you implement a robust Plugin"
    end_marker = "#### Q89: What are Algebraic Data Types"
    
    start_idx = content.find(start_marker)
    if start_idx == -1:
        print("❌ Q88 Header NOT Found!")
        exit(1)
        
    end_idx = content.find(end_marker)
    
    if end_idx == -1:
         q88_content = content[start_idx:]
    else:
         q88_content = content[start_idx:end_idx]
    
    line_count = len(q88_content.split('\n'))
    
    print(f"🔍 Verifying Q88 Content...")
    print(f"📊 Q88 Line Count: {line_count}")
    
    # 2. Check for Requirements
    required_sections = {
        "Project 1: Payment Gateway": r"Project 1.*Payment Gateway",
        "Project 2: Log Appender": r"Project 2.*Log Appender",
        "Project 3: Microkernel": r"Project 3.*Microkernel",
        "Deep Dive: AutoService": r"AutoService",
        "Deep Dive: SPI Config": r"META-INF/services",
        "Visualization": r"Interactive SPI",
    }
    
    missing = []
    for name, regex in required_sections.items():
        if re.search(regex, q88_content, re.IGNORECASE):
            print(f"✅ Found {name}")
        else:
            print(f"❌ Missing {name}")
            missing.append(name)
            
    # 3. Verdict
    if line_count < 2000:
        print(f"❌ Line Count FAILED. {line_count} < 2000")
        missing.append("Line Count")
        
    if missing:
        print("\n⚠️ Q88 VERIFICATION FAILED.")
    else:
        print("\n🎉 Q88 VERIFICATION PASSED! Elite Senior SDE Standard Met.")

if __name__ == "__main__":
    verify_q88()
