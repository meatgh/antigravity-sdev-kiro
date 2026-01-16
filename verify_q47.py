
import sys

def verify_q47():
    # Absolute Path to ensure robustness
    file_path = "/Users/syedrahman/Desktop/Career-and-Growth/Antigravity-IDE-Real-Git-Both/antigravity-sdev-kiro/content/java/06-oop-fundamentals.md"
    
    with open(file_path, "r") as f:
        content = f.read()
        
    start_marker = "#### Q47: The Builder Pattern"
    end_marker = "#### Q48:"
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    if start_idx == -1:
        print(f"❌ Q47 Start Marker '{start_marker}' not found")
        sys.exit(1)
        
    q47 = content[start_idx:] if end_idx == -1 else content[start_idx:end_idx]
    lines = len(q47.splitlines())
    
    print(f"Q47 Lines: {lines}")
    
    if lines < 2000:
        print("❌ Q47 too short")
        sys.exit(1)
        
    print("✅ Q47 Verification Passed!")

if __name__ == "__main__":
    verify_q47()
