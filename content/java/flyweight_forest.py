import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flyweight Pattern: The Infinite Forest</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        body { font-family: 'Inter', sans-serif; background-color: #f4f6f8; text-align: center; }
        #viz { background: white; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin: 20px auto; width: 800px; height: 500px; position: relative; overflow: hidden; }
        .stats { display: flex; justify-content: space-around; font-size: 14px; margin-top: 10px; color: #333; }
        .memory-box { padding: 10px; border-radius: 8px; background: #e0e7ff; min-width: 150px; }
        .naive { color: #d32f2f; }
        .flyweight { color: #2e7d32; font-weight: bold; }
        button { margin-top: 20px; padding: 10px 20px; font-size: 16px; background-color: #2196F3; color: white; border: none; border-radius: 5px; cursor: pointer; transition: background 0.3s; }
        button:hover { background-color: #1976D2; }
    </style>
</head>
<body>
    <h2>🚀 Flyweight Pattern: Visualizing Memory Optimization</h2>
    <p>Simulating a Game Engine rendering thousands of trees.</p>
    
    <div id="viz"></div>

    <div class="stats">
        <div class="memory-box">
             <h3>Naive Approach</h3>
             <p>Objects Created: <span id="naive-count">0</span></p>
             <p>RAM Usage: <span id="naive-ram" class="naive">0 KB</span></p>
        </div>
        <div class="memory-box">
             <h3>Flyweight Approach</h3>
             <p>Intrinsic Objects: <span id="intrinsic-count">2</span> (Tree Types)</p>
             <p>RAM Usage: <span id="flyweight-ram" class="flyweight">0 KB</span></p>
        </div>
    </div>

    <button onclick="plantForest()">🌲 Plant 1,000 Trees</button>
    <button onclick="clearForest()" style="background-color: #757575;">🔥 Burn Forest</button>

    <script>
        const width = 800;
        const height = 500;
        const svg = d3.select("#viz").append("svg").attr("width", width).attr("height", height);

        // Flyweights (Intrinsic State) - The "Heavy" stuff
        const treeTypes = {
            "Oak": { color: "#228B22", radius: 5 },  // Green
            "Pine": { color: "#006400", radius: 5 }  // DarkGreen
        };

        let treeCount = 0;
        
        function plantForest() {
            const batchSize = 100;
            const newTrees = [];

            for (let i = 0; i < batchSize; i++) {
                const type = Math.random() > 0.5 ? "Oak" : "Pine";
                const x = Math.random() * width;
                const y = Math.random() * height;
                newTrees.push({ type, x, y });
            }

            // D3 Update Pattern
            svg.selectAll(".tree-" + treeCount) // Unique class for batch
                .data(newTrees)
                .enter()
                .append("circle")
                .attr("cx", d => d.x)
                .attr("cy", -10) // Start above screen
                .attr("r", 0)
                .attr("fill", d => treeTypes[d.type].color)
                .attr("opacity", 0.7)
                .transition().duration(1000)
                .attr("cy", d => d.y) // Fall down
                .attr("r", 5);

            treeCount += batchSize;
            updateStats();

            if (treeCount < 1000) {
                setTimeout(plantForest, 100); // Recursive Loop
            }
        }

        function updateStats() {
            document.getElementById("naive-count").innerText = treeCount;
            
            // Naive: Each tree has Color (4 bytes) + Texture (1MB) + Coords (8 bytes)
            // Let's assume naive cost is 1KB per tree for simplicity of demo
            const naiveCostKB = treeCount * 10; 
            document.getElementById("naive-ram").innerText = naiveCostKB.toLocaleString() + " KB";

            // Flyweight: 
            // 2 Types * 10KB (Heavy texture) = 20KB fixed.
            // + TreeCount * 0.016KB (Coords only)
            const flyweightCostKB = 20 + (treeCount * 0.02);
            document.getElementById("flyweight-ram").innerText = flyweightCostKB.toFixed(2) + " KB";
        }

        function clearForest() {
            svg.selectAll("circle").transition().duration(500).attr("r", 0).remove();
            treeCount = 0;
            updateStats();
        }
    </script>
</body>
</html>
"""

with open("flyweight_forest.html", "w") as f:
    f.write(html_content)
print("✅ Generated flyweight_forest.html")
