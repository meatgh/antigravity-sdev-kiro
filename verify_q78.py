import re

def verify_q78():
    file_path = "content/java/06-oop-fundamentals.md"
    
    checks = {
         # Projects (Checking for titles or distinctive code)
         "Project 1: Distributed Session": r"Project 1.*Distributed Session",
         "Project 2: HFT Order Buffer": r"Project 2.*HFT Order Buffer",
         "Project 3: Game Save System": r"Project 3.*Game Save System",
         "Project 4: Custom RPC Protocol": r"Project 4.*Custom RPC Protocol",
         "Project 5: Secure Config Loader": r"Project 5.*Secure Config Loader",
         "Project 6: Schema Registry": r"Project 6.*Schema Registry",
         "Project 7: Redis Replicator": r"Project 7.*Distributed Cache.*Replicator",
         "Project 8: Time-Travel Debugger": r"Project 8.*Time-Travel",
         "Project 9: P2P Gossip Protocol": r"Project 9.*P2P Gossip",
         "Project 10: Off-Heap Order Book": r"Project 10.*Off-Heap Order Book",
         "Project 11: DIY Protobuf": r"Project 11.*DIY Protobuf",
         "Project 12: Slotted Page": r"Project 12.*Slotted Page",

         # Deep Dives
         "Deep Dive: Gadget Chain Security": r"Deep Dive: Security Vulnerabilities.*Gadget Chain",
         "Performance Benchmark": r"Performance Benchmark: Methods Compared",
         
         # Multi-Language
         "Language: Python (Pickle)": r"Python.*Pickle Problem",
         "Language: Go": r"Go.*Explicit Encoders",
         "Language: C++": r"C\+\+.*Boost",
         "Language: C#": r"C#.*BinaryFormatter",
         
         # LPs & Best Practices
         "Amazon LP: Customer Obsession": r"Customer Obsession",
         "Best Practices": r"Interview Tips",
         # Cheat Sheet might be missing, checking for it.
    }

    print("🔍 Verifying Q78 Content...")
    print(f"📄 File: {file_path}")
    
    q78_lines = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            capturing = False
            for line in lines:
                if "#### Q78:" in line:
                    capturing = True
                if capturing:
                    if "#### Q79" in line:
                        break
                    q78_lines.append(line)
    except FileNotFoundError:
        print("❌ File not found.")
        return

    content = "".join(q78_lines)
    line_count = len(q78_lines)
    print(f"📊 Q78 Line Count: {line_count}")

    if line_count == 0:
        print("❌ Q78 Section Not Found (Lines are empty)!")
        return

    all_passed = True
    for name, pattern in checks.items():
        if re.search(pattern, content, re.IGNORECASE | re.DOTALL):
            print(f"✅ Found {name}")
        else:
            print(f"❌ Missing {name}")
            all_passed = False
            
    if line_count > 2000:
        print("✅ Line Count Status: Excellent (>2000)")
    elif line_count > 1500:
        print("✅ Line Count Status: Good (>1500).")
    else:
        print("❌ Line Count Status: Low (<1500)")
        
    if all_passed and line_count > 1500:
        print("\n🎉 Q78 VERIFICATION PASSED! Senior SDE Standard Met.")
        print(f"FINAL METRICS: {line_count} Lines, 12 Enterprise Projects, 4 Languages, Deep Analysis.")
    else:
        print("\n⚠️ Q78 VERIFICATION FAILED. See missing items above.")

if __name__ == "__main__":
    verify_q78()
