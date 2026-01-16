
import re
import sys

def verify_q100():
    file_path = "content/java/06-oop-fundamentals.md"
    
    with open(file_path, "r") as f:
        content = f.read()
        
    start_marker = "#### Q100: The Future of Java (Valhalla, Panama, Vector)"
    # No end marker, it's the last one!
    
    start_idx = content.find(start_marker)
    
    if start_idx == -1:
        print("❌ Q100 Start Marker not found")
        sys.exit(1)
        
    q100_content = content[start_idx:]
    
    lines = q100_content.splitlines()
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
    
    missing = [s for s in required if s not in q100_content]
    if missing:
        print(f"❌ Missing Template Sections: {missing}")
        sys.exit(1)
        
    if "class PointCloud" not in q100_content:
        print("❌ Missing Project 1 (PointCloud)")
        sys.exit(1)
        
    print("✅ Q100 Verification Passed!")

if __name__ == "__main__":
    verify_q100()
