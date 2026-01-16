
html_content = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        body { font-family: 'Inter', sans-serif; background: #1a1a1a; color: #fff; text-align: center; }
        .controls { margin-top: 20px; display: flex; justify-content: center; gap: 20px; }
        .control-group { background: #333; padding: 15px; border-radius: 8px; }
        button { padding: 8px 16px; margin: 4px; cursor: pointer; border: 1px solid #555; background: #444; color: white; border-radius: 4px; }
        button.active { background: #2196F3; border-color: #2196F3; }
        button:hover { background: #555; }
        #canvas { margin-top: 30px; height: 200px; display: flex; align-items: center; justify-content: center; }
        #code-display { font-family: monospace; color: #4CAF50; font-size: 16px; margin-top: 20px; }
    </style>
</head>
<body>
    <h2>Bridge Pattern: Decoupling Abstraction & Implementation</h2>
    <p>We avoid 3x3 = 9 classes (RedCircle, BlueSquare...). We use 3+3 = 6 classes composed dynamically.</p>

    <div class="controls">
        <div class="control-group">
            <h4>1. Select Shape (Abstraction)</h4>
            <button onclick="setShape('Circle')" id="btn-Circle" class="active">Circle</button>
            <button onclick="setShape('Square')" id="btn-Square">Square</button>
            <button onclick="setShape('Triangle')" id="btn-Triangle">Triangle</button>
        </div>
        <div class="control-group">
            <h4>2. Select Color (Implementor)</h4>
            <button onclick="setColor('Red')" id="btn-Red" class="active">Red</button>
            <button onclick="setColor('Green')" id="btn-Green">Green</button>
            <button onclick="setColor('Blue')" id="btn-Blue">Blue</button>
        </div>
    </div>

    <div id="canvas"></div>
    <div id="code-display">Shape shape = new Circle(new RedColor());</div>

    <script>
        let currentShape = 'Circle';
        let currentColor = 'Red';
        
        const colorMap = {
            'Red': '#F44336',
            'Green': '#4CAF50',
            'Blue': '#2196F3'
        };

        const canvas = d3.select("#canvas").append("svg").attr("width", 200).attr("height", 200);

        function render() {
            canvas.selectAll("*").remove();
            
            const colorHex = colorMap[currentColor];
            
            let element;
            if (currentShape === 'Circle') {
                element = canvas.append("circle")
                    .attr("cx", 100).attr("cy", 100).attr("r", 0)
                    .attr("fill", colorHex);
                element.transition().duration(500).attr("r", 60);
            } else if (currentShape === 'Square') {
                element = canvas.append("rect")
                    .attr("x", 40).attr("y", 40).attr("width", 0).attr("height", 0)
                    .attr("fill", colorHex)
                    .attr("transform", "translate(60, 60)"); // animate form center? slightly complex for rect
                
                // Simple transition
                element.attr("x", 100).attr("y", 100).attr("width", 0).attr("height", 0);
                element.transition().duration(500)
                    .attr("x", 40).attr("y", 40).attr("width", 120).attr("height", 120);
            } else if (currentShape === 'Triangle') {
                // Triangle path
                const path = d3.path();
                path.moveTo(100, 40);
                path.lineTo(160, 150);
                path.lineTo(40, 150);
                path.closePath();
                
                element = canvas.append("path")
                    .attr("d", path.toString())
                    .attr("fill", colorHex)
                    .attr("opacity", 0);
                element.transition().duration(500).attr("opacity", 1);
            }

            document.getElementById("code-display").textContent = 
                `Shape shape = new ${currentShape}(new ${currentColor}Color());`;
                
            updateButtons();
        }

        function setShape(s) {
            currentShape = s;
            render();
        }

        function setColor(c) {
            currentColor = c;
            render();
        }
        
        function updateButtons() {
            d3.selectAll("button").classed("active", false);
            d3.select("#btn-" + currentShape).classed("active", true);
            d3.select("#btn-" + currentColor).classed("active", true);
        }

        render();
    </script>
</body>
</html>
"""

with open("bridge_shapes.html", "w") as f:
    f.write(html_content)
print("✅ Generated bridge_shapes.html")
