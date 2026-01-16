import re

def verify_q83():
    file_path = "content/java/06-oop-fundamentals.md"
    
    with open(file_path, "r") as f:
        content = f.read()
    
    # 1. Extract Q83 Content
    # Using more robust substring search
    start_marker = "#### Q83: How does the Reflection API"
    # Q84 is the next one
    end_marker = "#### Q84: How does the Java Memory Model"
    
    start_idx = content.find(start_marker)
    if start_idx == -1:
        print("❌ Q83 Header NOT Found!")
        exit(1)
        
    end_idx = content.find(end_marker)
    
    if end_idx == -1:
         q83_content = content[start_idx:]
    else:
         q83_content = content[start_idx:end_idx]
    
    line_count = len(q83_content.split('\n'))
    
    print(f"🔍 Verifying Q83 Content...")
    print(f"📊 Q83 Line Count: {line_count}")
    
    # 2. Check for Requirements
    required_sections = {
        "Project 1: DI Container": r"Project 1.*DI Container",
        "Project 2: Universal ORM": r"Project 2.*ORM",
        "Project 3: Test Runner": r"Project 3.*Test Runner",
        "Deep Dive: Unsafe": r"sun.misc.Unsafe",
        "Deep Dive: Performance": r"Reflection vs Direct",
        "Visualization": r"Interactive Class Explorer",
    }
    
    missing = []
    for name, regex in required_sections.items():
        if re.search(regex, q83_content, re.IGNORECASE):
            print(f"✅ Found {name}")
        else:
            print(f"❌ Missing {name}")
            missing.append(name)
            
    # 3. Verdict
    if line_count < 2000:
        print(f"❌ Line Count FAILED. {line_count} < 2000")
        missing.append("Line Count")
        
    if missing:
        print("\n⚠️ Q83 VERIFICATION FAILED.")
    else:
        print("\n🎉 Q83 VERIFICATION PASSED! Elite Senior SDE Standard Met.")

if __name__ == "__main__":
    verify_q83()
