import re

def verify_q82():
    file_path = "content/java/06-oop-fundamentals.md"
    
    with open(file_path, "r") as f:
        content = f.read()
    
    # 1. Extract Q82 Content
    start_marker = "#### Q82: How does Aspect-Oriented Programming"
    
    start_idx = content.find(start_marker)
    if start_idx == -1:
        print("❌ Q82 Header NOT Found!")
        exit(1)
        
    end_marker = "#### Q83: How does the Reflection API"
    end_idx = content.find(end_marker)
    
    if end_idx == -1:
         q82_content = content[start_idx:]
    else:
         q82_content = content[start_idx:end_idx]
        
    
    # Check if we found anything (robustness)
    if 'q82_content' not in locals():
         print("❌ Logic Error: q82_content not set")
         exit(1)

    line_count = len(q82_content.split('\n'))
    
    print(f"🔍 Verifying Q82 Content...")
    print(f"📊 Q82 Line Count: {line_count}")
    
    # 2. Check for Requirements
    required_sections = {
        "Project 1: Distributed Tracing": r"Project 1.*Tracing",
        "Project 2: Transaction Manager": r"Project 2.*Transaction",
        "Project 3: RBAC Security": r"Project 3.*RBAC",
        "Deep Dive: JDK vs CGLIB": r"JDK.*vs.*CGLIB",
        "Deep Dive: Self-Invocation": r"Self-Invocation",
        "Visualization": r"Interact with AOP Proxy Chain",
        "Benchmarks": r"Performance.*Benchmark",
    }
    
    missing = []
    for name, regex in required_sections.items():
        if re.search(regex, q82_content, re.IGNORECASE):
            print(f"✅ Found {name}")
        else:
            print(f"❌ Missing {name}")
            missing.append(name)
            
    # 3. Verdict
    if line_count < 2000:
        print(f"❌ Line Count FAILED. {line_count} < 2000")
        missing.append("Line Count")
        
    if missing:
        print("\n⚠️ Q82 VERIFICATION FAILED.")
    else:
        print("\n🎉 Q82 VERIFICATION PASSED! Elite Senior SDE Standard Met.")

if __name__ == "__main__":
    verify_q82()
