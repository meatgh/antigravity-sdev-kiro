import re

def verify_q87():
    file_path = "content/java/06-oop-fundamentals.md"
    
    with open(file_path, "r") as f:
        content = f.read()
    
    # 1. Extract Q87 Content
    start_marker = "#### Q87: What is Type Erasure"
    end_marker = "#### Q88: How do you implement a robust Plugin"
    
    start_idx = content.find(start_marker)
    if start_idx == -1:
        print("❌ Q87 Header NOT Found!")
        exit(1)
        
    end_idx = content.find(end_marker)
    
    if end_idx == -1:
         q87_content = content[start_idx:]
    else:
         q87_content = content[start_idx:end_idx]
    
    line_count = len(q87_content.split('\n'))
    
    print(f"🔍 Verifying Q87 Content...")
    print(f"📊 Q87 Line Count: {line_count}")
    
    # 2. Check for Requirements
    required_sections = {
        "Project 1: Erasure Prober": r"Project 1.*Erasure Prober",
        "Project 2: Dynamic Proxy": r"Project 2.*Dynamic Proxy",
        "Project 3: Crypto Types": r"Project 3.*Crypto Type",
        "Deep Dive: Bridge Methods": r"Bridge Method",
        "Deep Dive: Heap Pollution": r"Heap Pollution",
        "Visualization": r"Interactive Erasure",
    }
    
    missing = []
    for name, regex in required_sections.items():
        if re.search(regex, q87_content, re.IGNORECASE):
            print(f"✅ Found {name}")
        else:
            print(f"❌ Missing {name}")
            missing.append(name)
            
    # 3. Verdict
    if line_count < 2000:
        print(f"❌ Line Count FAILED. {line_count} < 2000")
        missing.append("Line Count")
        
    if missing:
        print("\n⚠️ Q87 VERIFICATION FAILED.")
    else:
        print("\n🎉 Q87 VERIFICATION PASSED! Elite Senior SDE Standard Met.")

if __name__ == "__main__":
    verify_q87()
