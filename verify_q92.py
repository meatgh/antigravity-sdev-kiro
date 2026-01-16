
import re
import sys

def verify_q92():
    file_path = "content/java/06-oop-fundamentals.md"
    
    with open(file_path, "r") as f:
        content = f.read()
        
    start_marker = "#### Q92: Type-Safe Builder (Phantom Types)"
    end_marker = "#### Q93: Higher-Kinded Types"
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    if start_idx == -1:
        print("❌ Q92 Start Marker not found")
        sys.exit(1)
        
    q92_content = content[start_idx:] if end_idx == -1 else content[start_idx:end_idx]
    
    lines = q92_content.splitlines()
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
    
    missing = [s for s in required if s not in q92_content]
    if missing:
        print(f"❌ Missing Template Sections: {missing}")
        sys.exit(1)
        
    if "class SqlBuilder" not in q92_content:
        print("❌ Missing Project 1 (SqlBuilder)")
        sys.exit(1)
        
    print("✅ Q92 Verification Passed!")

if __name__ == "__main__":
    verify_q92()
