
import re
import sys

def verify_q90():
    file_path = "content/java/06-oop-fundamentals.md"
    
    with open(file_path, "r") as f:
        content = f.read()
        
    # Check boundaries
    start_marker = "#### Q90: What is a Monad in Java"
    end_marker = "#### Q91: What are Method Handles"
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    if start_idx == -1:
        print("❌ Q90 Start Marker not found")
        sys.exit(1)
        
    q90_content = content[start_idx:] if end_idx == -1 else content[start_idx:end_idx]
    
    # Line Count
    lines = q90_content.splitlines()
    line_count = len(lines)
    print(f"Line Count: {line_count}")
    
    if line_count < 2000:
        print(f"❌ Q90 Line Count too low: {line_count} < 2000")
        sys.exit(1)
        
    # Check Required Sections (FAANG Template)
    required_sections = [
        "## 📋 Question Statement",
        "## 🚀 Solution Evolution Journey",
        "## 🌐 Cross-Language Excellence",
        "## 🛡️ Bulletproof Implementation",
        "## 🎭 Interview Performance Mastery",
        "## 🚀 Expert-Level Enhancements",
        "## 🔗 Problem Pattern Mastery",
        "## 🏭 Enterprise Implementation Context",
        "## 👥 Leadership and Collaboration Excellence",
        "## 🧪 Testing Excellence Framework"
    ]
    
    missing_sections = [s for s in required_sections if s not in q90_content]
    if missing_sections:
        print(f"❌ Missing FAANG Template Sections: {missing_sections}")
        sys.exit(1)
        
    # Check Projects
    if "class Try<T>" not in q90_content and "interface Try<T>" not in q90_content:
        print("❌ 'Try' Monad implementation missing")
        sys.exit(1)
        
    if "class Promise<T>" not in q90_content:
        print("❌ 'Promise' Monad implementation missing")
        sys.exit(1)
        
    print("✅ Q90 Verification Passed!")

if __name__ == "__main__":
    verify_q90()
