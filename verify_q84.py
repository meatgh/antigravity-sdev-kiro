import re

def verify_q84():
    file_path = "content/java/06-oop-fundamentals.md"
    
    with open(file_path, "r") as f:
        content = f.read()
    
    # 1. Extract Q84 Content
    start_marker = "#### Q84: How does the Java Memory Model"
    end_marker = "#### Q85: How does Garbage Collection"
    
    start_idx = content.find(start_marker)
    if start_idx == -1:
        print("❌ Q84 Header NOT Found!")
        exit(1)
        
    end_idx = content.find(end_marker)
    
    if end_idx == -1:
         q84_content = content[start_idx:]
    else:
         q84_content = content[start_idx:end_idx]
    
    line_count = len(q84_content.split('\n'))
    
    print(f"🔍 Verifying Q84 Content...")
    print(f"📊 Q84 Line Count: {line_count}")
    
    # 2. Check for Requirements
    required_sections = {
        "Project 1: Ring Buffer": r"Project 1.*Ring Buffer",
        "Project 2: Safe Cache": r"Project 2.*Safe Publication",
        "Project 3: False Sharing": r"Project 3.*False Sharing",
        "Deep Dive: Happens-Before": r"Happens-Before",
        "Deep Dive: Memory Barriers": r"Memory Barrier",
        "Visualization": r"Interactive JMM",
    }
    
    missing = []
    for name, regex in required_sections.items():
        if re.search(regex, q84_content, re.IGNORECASE):
            print(f"✅ Found {name}")
        else:
            print(f"❌ Missing {name}")
            missing.append(name)
            
    # 3. Verdict
    if line_count < 2000:
        print(f"❌ Line Count FAILED. {line_count} < 2000")
        missing.append("Line Count")
        
    if missing:
        print("\n⚠️ Q84 VERIFICATION FAILED.")
    else:
        print("\n🎉 Q84 VERIFICATION PASSED! Elite Senior SDE Standard Met.")

if __name__ == "__main__":
    verify_q84()
