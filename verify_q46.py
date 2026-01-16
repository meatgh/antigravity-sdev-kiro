
import sys

def verify_q46():
    file_path = "content/java/06-oop-fundamentals.md"
    
    with open(file_path, "r") as f:
        content = f.read()
        
    start_marker = "#### Q46: What is Method Chaining"
    end_marker = "#### Q47:"
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    if start_idx == -1:
        print("❌ Q46 Start Marker not found")
        sys.exit(1)
        
    q46 = content[start_idx:] if end_idx == -1 else content[start_idx:end_idx]
    lines = len(q46.splitlines())
    
    print(f"Q46 Lines: {lines}")
    
    if lines < 2000:
        print("❌ Q46 too short")
        sys.exit(1)
        
    if "Project 1: Recursive Generic Builder" not in q46:
        print("❌ Missing Project 1")
        sys.exit(1)
        
    print("✅ Q46 Verification Passed!")

if __name__ == "__main__":
    verify_q46()
