
import re
import sys

def verify_q93():
    file_path = "content/java/06-oop-fundamentals.md"
    
    with open(file_path, "r") as f:
        content = f.read()
        
    start_marker = "#### Q93: Higher-Kinded Types"
    end_marker = "#### Q94: Virtual Threads (Loom)"
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    if start_idx == -1:
        print("❌ Q93 Start Marker not found")
        sys.exit(1)
        
    q93_content = content[start_idx:] if end_idx == -1 else content[start_idx:end_idx]
    
    lines = q93_content.splitlines()
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
    
    missing = [s for s in required if s not in q93_content]
    if missing:
        print(f"❌ Missing Template Sections: {missing}")
        sys.exit(1)
        
    if "interface Kind<F, T>" not in q93_content:
        print("❌ Missing Project 1 (Kind interface)")
        sys.exit(1)
        
    print("✅ Q93 Verification Passed!")

if __name__ == "__main__":
    verify_q93()
