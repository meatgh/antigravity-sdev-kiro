
import sys

def verify_q48():
    file_path = "/Users/syedrahman/Desktop/Career-and-Growth/Antigravity-IDE-Real-Git-Both/antigravity-sdev-kiro/content/java/06-oop-fundamentals.md"
    
    with open(file_path, "r") as f:
        content = f.read()
        
    start_marker = "#### Q48: What is the difference"
    end_marker = "#### Q49:"
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    if start_idx == -1:
        print("❌ Q48 Start Marker not found")
        sys.exit(1)
        
    q48 = content[start_idx:] if end_idx == -1 else content[start_idx:end_idx]
    lines = len(q48.splitlines())
    
    print(f"Q48 Lines: {lines}")
    
    if lines < 2000:
        print("❌ Q48 too short")
        sys.exit(1)
        
    print("✅ Q48 Verification Passed!")

if __name__ == "__main__":
    verify_q48()
