
import sys

def verify_q45():
    file_path = "content/java/06-oop-fundamentals.md"
    
    with open(file_path, "r") as f:
        content = f.read()
        
    start_marker = "#### Q45: How do you prevent a class"
    end_marker = "#### Q46:"
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    if start_idx == -1:
        print("❌ Q45 Start Marker not found")
        sys.exit(1)
        
    q45_content = content[start_idx:] if end_idx == -1 else content[start_idx:end_idx]
    line_count = len(q45_content.splitlines())
    
    print(f"Q45 Line Count: {line_count}")
    
    if line_count < 2000:
        print(f"❌ Line Count too low: {line_count} < 2000")
        sys.exit(1)
        
    requirements = [
        "## 📋 Question Statement",
        "## 🧪 Testing Excellence Framework",
        "Project 1: Testing Statics"
    ]
    
    for req in requirements:
        if req not in q45_content:
            print(f"❌ Missing Requirement: {req}")
            sys.exit(1)
            
    print("✅ Q45 Verification Passed!")

if __name__ == "__main__":
    verify_q45()
