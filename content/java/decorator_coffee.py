
html_content = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        body { font-family: 'Inter', sans-serif; background: #1a1a1a; color: #fff; text-align: center; }
        .cup { fill: #fff; stroke: #888; stroke-width: 2; }
        .layer { stroke: #fff; stroke-width: 1; opacity: 0.9; rx: 5; ry: 5; transition: height 0.5s, y 0.5s; }
        .controls { margin-top: 20px; }
        button { padding: 10px 20px; font-size: 16px; margin: 5px; cursor: pointer; background: #444; color: white; border: none; border-radius: 4px; }
        button:hover { background: #555; }
        .price-tag { font-size: 24px; font-weight: bold; fill: #4CAF50; }
        .code-preview { font-family: monospace; color: #BBB; margin-top: 10px; font-size: 14px; }
    </style>
</head>
<body>
    <h2>Decorator Pattern: Coffee Builder</h2>
    <p>Dynamically stacking behavior (and cost) at runtime.</p>
    
    <div id="canvas"></div>
    <div class="code-preview" id="code">new Coffee()</div>
    
    <div class="controls">
        <button onclick="addLayer('milk')">+ Milk ($0.5)</button>
        <button onclick="addLayer('mocha')">+ Mocha ($0.8)</button>
        <button onclick="addLayer('whip')">+ Whip ($0.5)</button>
        <button onclick="reset()">Reset</button>
    </div>

    <script>
        const width = 400, height = 400;
        const svg = d3.select("#canvas").append("svg").attr("width", width).attr("height", height);
        
        let stack = [];
        let baseCost = 2.0;

        // Draw Base Cup
        svg.append("path")
            .attr("d", "M 120 300 L 140 100 L 260 100 L 280 300 Z") // Trapezoid cup
            .attr("class", "cup")
            .attr("fill", "none");

        // Price Text
        const priceText = svg.append("text")
            .attr("x", 200).attr("y", 350)
            .attr("text-anchor", "middle")
            .attr("class", "price-tag")
            .text("Cost: $2.00");

        function updateDisplay() {
            let currentY = 290;
            let currentCost = baseCost;
            let codeStr = "new Coffee()";
            
            // Clear existing layers
            svg.selectAll(".layer").remove();

            // Re-draw stack from bottom up
            // Base coffee liquid
            svg.append("rect")
                .attr("x", 130).attr("y", 250).attr("width", 140).attr("height", 40)
                .attr("class", "layer")
                .attr("fill", "#6F4E37"); // Coffee Color

            currentY = 250;
            
            stack.forEach(item => {
                let color = "#FFF";
                let cost = 0;
                let name = "";
                
                if (item === 'milk') { color = "#FFFDD0"; cost = 0.5; name = "Milk"; } // Cream
                if (item === 'mocha') { color = "#3E2723"; cost = 0.8; name = "Mocha"; } // Dark Choc
                if (item === 'whip') { color = "#EEE"; cost = 0.5; name = "Whip"; } // White
                
                currentCost += cost;
                codeStr = `new ${name}(${codeStr})`;
                
                // Draw Layer
                svg.append("rect")
                    .attr("x", 130)
                    .attr("y", currentY - 30)
                    .attr("width", 140)
                    .attr("height", 30)
                    .attr("class", "layer")
                    .attr("fill", color)
                    .style("opacity", 0)
                    .transition().duration(500).style("opacity", 1);
                
                currentY -= 30; // Move up
            });

            priceText.text(`Cost: $${currentCost.toFixed(2)}`);
            d3.select("#code").text(codeStr);
        }

        function addLayer(type) {
            if (stack.length >= 5) { alert("Cup is full!"); return; }
            stack.push(type);
            updateDisplay();
        }

        function reset() {
            stack = [];
            updateDisplay();
        }

        updateDisplay();
    </script>
</body>
</html>
"""

with open("decorator_coffee.html", "w") as f:
    f.write(html_content)
print("✅ Generated decorator_coffee.html")
