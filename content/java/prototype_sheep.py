import os

html_content = """<!DOCTYPE html>
<html>
<head>
    <title>Prototype Pattern: Sheep Cloning</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        body { font-family: 'Inter', sans-serif; background: #f4f6f8; color: #333; text-align: center; }
        .sheep { transition: transform 0.5s; cursor: pointer; }
        .dna-strand { stroke-width: 4; stroke-linecap: round; }
        .controls { margin-top: 20px; }
        button { padding: 10px 20px; font-size: 16px; margin: 5px; cursor: pointer; background: #444; color: white; border: none; border-radius: 4px; }
        button:hover { background: #555; }
        button.action { background: #2196F3; font-weight: bold; }
        .label { font-size: 12px; fill: #666; }
        .title { font-size: 14px; fill: #333; font-weight: bold; }
        .box { fill: white; stroke: #ccc; stroke-width: 2; rx: 8; }
    </style>
</head>
<body>
    <h2>🐑 Prototype Pattern: Shallow vs Deep Copy</h2>
    <p><b>Shallow Copy</b> shares the DNA reference. <b>Deep Copy</b> creates new DNA.</p>
    
    <div id="canvas"></div>
    
    <div class="controls">
        <button class="action" onclick="cloneSheep('shallow')">Clone (Shallow)</button>
        <button class="action" onclick="cloneSheep('deep')">Clone (Deep)</button>
        <button style="background: #D32F2F" onclick="mutateOriginal()">Mutate Original DNA 🧬</button>
        <button onclick="reset()">Reset</button>
    </div>

    <script>
        const width = 800, height = 400;
        const svg = d3.select("#canvas").append("svg").attr("width", width).attr("height", height);
        
        let clones = [];
        let originalDNA = { color: "#4CAF50" }; // Green
        
        // Define Original Sheep
        const originalSheep = {
            id: "Original",
            x: 150, y: 150,
            dna: originalDNA // Reference
        };

        function draw() {
            svg.selectAll("*").remove();
            
            // Draw Arrows and Links would go here
            
            // Draw Original
            drawSheepObj(originalSheep);
            
            // Draw Clones
            clones.forEach((clone, i) => {
                drawSheepObj(clone);
            });
        }

        function drawSheepObj(sheep) {
            const g = svg.append("g").attr("class", "sheep").attr("transform", `translate(${sheep.x}, ${sheep.y})`);
            
            // Box
            g.append("rect").attr("x", -50).attr("y", -40).attr("width", 100).attr("height", 80).attr("class", "box");
            
            // Label
            g.append("text").attr("y", -50).attr("text-anchor", "middle").attr("class", "title").text(sheep.id);
            
            // Sheep Body (Simple Circle)
            g.append("circle").attr("r", 20).attr("fill", "#eee").attr("stroke", "#333");
            
            // DNA
            g.append("line")
                .attr("x1", -30).attr("y1", 25).attr("x2", 30).attr("y2", 25)
                .attr("class", "dna-strand")
                .attr("stroke", sheep.dna.color);
                
            g.append("text").attr("y", 38).attr("text-anchor", "middle").attr("font-size", "10px").text("DNA");
        }
        
        function cloneSheep(type) {
            if (clones.length >= 3) return;
            
            const newX = 300 + (clones.length * 120);
            let newSheep;
            
            if (type === 'shallow') {
                newSheep = {
                    id: "Shallow Copy",
                    x: newX, y: 150,
                    dna: originalSheep.dna // REFERENCE COPY
                };
            } else {
                newSheep = {
                    id: "Deep Copy",
                    x: newX, y: 250,
                    dna: { color: originalSheep.dna.color } // NEW OBJECT
                };
            }
            clones.push(newSheep);
            draw();
        }
        
        function mutateOriginal() {
            // Mutate the Object that Original points to
            originalSheep.dna.color = "#F44336"; // Red
            draw();
            // Shallow copies will auto-update because they point to same obj
            // Deep copies won't
        }
        
        function reset() {
            originalDNA = { color: "#4CAF50" };
            originalSheep.dna = originalDNA;
            clones = [];
            draw();
        }
        
        draw();
    </script>
</body>
</html>
"""

with open("prototype_sheep.html", "w") as f:
    f.write(html_content)
print("✅ Generated prototype_sheep.html")
