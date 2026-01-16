import re

def verify_q85():
    file_path = "content/java/06-oop-fundamentals.md"
    
    with open(file_path, "r") as f:
        content = f.read()
    
    # 1. Extract Q85 Content
    start_marker = "#### Q85: How does Garbage Collection"
    end_marker = "#### Q86: How do ClassLoaders work"
    
    start_idx = content.find(start_marker)
    if start_idx == -1:
        print("❌ Q85 Header NOT Found!")
        exit(1)
        
    end_idx = content.find(end_marker)
    
    if end_idx == -1:
         q85_content = content[start_idx:]
    else:
         q85_content = content[start_idx:end_idx]
    
    line_count = len(q85_content.split('\n'))
    
    print(f"🔍 Verifying Q85 Content...")
    print(f"📊 Q85 Line Count: {line_count}")
    
    # 2. Check for Requirements
    required_sections = {
        "Project 1: Allocation Recorder": r"Project 1.*Allocation Recorder",
        "Project 2: Object Pool": r"Project 2.*Object Pool",
        "Project 3: Ref Monitor": r"Project 3.*Reference Queue",
        "Deep Dive: ZGC": r"ZGC",
        "Deep Dive: Generational": r"Generational Hypothesis",
        "Visualization": r"Interactive GC",
    }
    
    missing = []
    for name, regex in required_sections.items():
        if re.search(regex, q85_content, re.IGNORECASE):
            print(f"✅ Found {name}")
        else:
            print(f"❌ Missing {name}")
            missing.append(name)
            
    # 3. Verdict
    if line_count < 2000:
        print(f"❌ Line Count FAILED. {line_count} < 2000")
        missing.append("Line Count")
        
    if missing:
        print("\n⚠️ Q85 VERIFICATION FAILED.")
    else:
        print("\n🎉 Q85 VERIFICATION PASSED! Elite Senior SDE Standard Met.")

if __name__ == "__main__":
    verify_q85()
