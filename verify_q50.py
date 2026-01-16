
import sys

def verify_q50():
    file_path = "/Users/syedrahman/Desktop/Career-and-Growth/Antigravity-IDE-Real-Git-Both/antigravity-sdev-kiro/content/java/06-oop-fundamentals.md"
    
    with open(file_path, "r") as f:
        content = f.read()
        
    start_marker = "#### Q50: The Law of Demeter"
    end_marker = "#### Q51:" # Assumes Standard format
    
    # Backup check if format differs
    if "#### Q51:" not in content:
        # Maybe "#### 51."
        end_marker = "#### 51."
        
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    if start_idx == -1:
        print("❌ Q50 Start Marker not found")
        sys.exit(1)
        
    q50 = content[start_idx:] if end_idx == -1 else content[start_idx:end_idx]
    lines = len(q50.splitlines())
    
    print(f"Q50 Lines: {lines}")
    
    if lines < 2000:
        print("❌ Q50 too short")
        sys.exit(1)
        
    print("✅ Q50 Verification Passed!")

if __name__ == "__main__":
    verify_q50()
