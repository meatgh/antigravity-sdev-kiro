
import re
import sys

def verify_q98():
    file_path = "content/java/06-oop-fundamentals.md"
    
    with open(file_path, "r") as f:
        content = f.read()
        
    start_marker = "#### Q98: Distributed Caching Patterns"
    end_marker = "#### Q99: Reactive Programming"
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    if start_idx == -1:
        print("❌ Q98 Start Marker not found")
        sys.exit(1)
        
    q98_content = content[start_idx:] if end_idx == -1 else content[start_idx:end_idx]
    
    lines = q98_content.splitlines()
    line_count = len(lines)
    print(f"Line Count: {line_count}")
    
    if line_count < 2000:
        print(f"❌ Line Count too low: {line_count} < 2000")
        sys.exit(1)
        
    required = [
        "## 📋 Question Statement",
        "## 🚀 Solution Evolution Journey",
        "## 🌐 Cross-Language Excellence",
        "## 🛡️ Bulletproof Implementation",
        "## 🧪 Testing Excellence Framework"
    ]
    
    missing = [s for s in required if s not in q98_content]
    if missing:
        print(f"❌ Missing Template Sections: {missing}")
        sys.exit(1)
        
    if "class LRUCache" not in q98_content:
        print("❌ Missing Project 1 (LRUCache)")
        sys.exit(1)
        
    print("✅ Q98 Verification Passed!")

if __name__ == "__main__":
    verify_q98()
