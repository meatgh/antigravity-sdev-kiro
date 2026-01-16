
original_file = "content/java/06-oop-fundamentals.md"
new_content_file = "/Users/syedrahman/.gemini/antigravity/brain/a1779793-2266-42ba-9eb7-8c1442cfa40d/q78_expansion.md"

with open(original_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

with open(new_content_file, "r", encoding="utf-8") as f:
    new_lines = f.readlines()

# Indices (1-based to 0-based)
start_index = 84460 # Line 84461
end_index = 84731   # Line 84732

print(f"Original Line Count: {len(lines)}")
print(f"Replacing lines {start_index+1} to {end_index}")
print(f"Old content start: {lines[start_index][:20]}...")
print(f"Old content end: {lines[end_index-1][:20]}...")
print(f"Next section start: {lines[end_index][:20]}...")

final_lines = lines[:start_index] + new_lines + ["\n\n"] + lines[end_index:]

with open(original_file, "w", encoding="utf-8") as f:
    f.writelines(final_lines)

print(f"New Line Count: {len(final_lines)}")
print("Injection Complete.")
