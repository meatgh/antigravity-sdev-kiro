
import sys

def verify_q49():
    file_path = "/Users/syedrahman/Desktop/Career-and-Growth/Antigravity-IDE-Real-Git-Both/antigravity-sdev-kiro/content/java/06-oop-fundamentals.md"
    
    with open(file_path, "r") as f:
        content = f.read()
        
    start_marker = "#### Q49: Immutability Deep Dive"
    end_marker = "#### Q50:"
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    if start_idx == -1:
        print("❌ Q49 Start Marker not found")
        sys.exit(1)
        
    q49 = content[start_idx:] if end_idx == -1 else content[start_idx:end_idx]
    lines = len(q49.splitlines())
    
    print(f"Q49 Lines: {lines}")
    
    if lines < 2000:
        print("❌ Q49 too short")
        sys.exit(1)
        
    print("✅ Q49 Verification Passed!")

if __name__ == "__main__":
    verify_q49()
