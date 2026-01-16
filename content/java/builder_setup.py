import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Builder Pattern - Robot Assembly Line</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js"></script>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f8f9fa;
            color: #333;
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
            max-width: 900px;
            width: 100%;
            text-align: center;
        }
        h2 { color: #2c3e50; margin-bottom: 10px; }
        p.desc { color: #7f8c8d; margin-bottom: 30px; font-size: 0.95em; }
        
        .controls {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-bottom: 30px;
            flex-wrap: wrap;
        }
        
        button {
            padding: 10px 20px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.2s;
            background-color: #e0e0e0;
            color: #555;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        button:hover { transform: translateY(-2px); }
        button:active { transform: translateY(0); }
        
        button.part-btn.active {
            background-color: #3498db;
            color: white;
            box-shadow: 0 2px 8px rgba(52, 152, 219, 0.3);
        }
        
        button.build-btn {
            background-color: #27ae60;
            color: white;
            margin-left: 20px;
        }
        
        button.reset-btn {
            background-color: #e74c3c;
            color: white;
        }

        .visualization-area {
            position: relative;
            height: 400px;
            border: 2px dashed #bdc3c7;
            border-radius: 8px;
            background: #fafafa;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
        .code-panel {
            margin-top: 20px;
            background: #282c34;
            color: #abb2bf;
            padding: 15px;
            border-radius: 6px;
            text-align: left;
            font-family: 'Consolas', 'Monaco', monospace;
            font-size: 14px;
            height: 120px;
            overflow-y: auto;
            border-left: 5px solid #3498db;
        }

        .robot-part {
            transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            opacity: 0;
            transform: scale(0.5);
        }
        
        .robot-part.visible {
            opacity: 1;
            transform: scale(1);
        }

        .step-indicator {
            position: absolute;
            top: 20px;
            right: 20px;
            background: rgba(255,255,255,0.9);
            padding: 10px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: bold;
            color: #2980b9;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>🛠️ The Builder Pattern: Robot Assembler</h2>
        <p class="desc">Construct a complex object step-by-step. The final object is only created when <code>.build()</code> is called.</p>
        
        <div class="controls">
            <button class="part-btn" onclick="addPart('head')">🤖 Add Head</button>
            <button class="part-btn" onclick="addPart('torso')">👕 Add Torso</button>
            <button class="part-btn" onclick="addPart('arms')">💪 Add Arms</button>
            <button class="part-btn" onclick="addPart('legs')">🦿 Add Legs</button>
            <button class="build-btn" onclick="buildRobot()">🚀 .build()</button>
            <button class="reset-btn" onclick="reset()">❌ Reset</button>
        </div>

        <div class="visualization-area" id="viz">
            <svg width="400" height="350" id="robot-svg"></svg>
            <div class="step-indicator" id="step-indicator">State: Empty Builder</div>
        </div>

        <div class="code-panel" id="code-display">
            // RobotBuilder initialized...
        </div>
    </div>

    <script>
        // State
        const state = {
            head: false,
            torso: false,
            arms: false,
            legs: false,
            built: false
        };

        const svg = d3.select("#robot-svg");
        const codeDisplay = document.getElementById('code-display');
        const updateCode = (text) => {
            codeDisplay.innerHTML += `<div>${text}</div>`;
            codeDisplay.scrollTop = codeDisplay.scrollHeight;
        };

        // Draw placeholders
        function init() {
            svg.selectAll("*").remove();
            updateCode("// new RobotBuilder()");
            document.getElementById('step-indicator').innerText = "State: In Progress";
        }

        function addPart(part) {
            if (state.built) {
                alert("Robot is already built! Reset to start over.");
                return;
            }
            
            if (state[part]) return; // Already added
            state[part] = true;

            // Highlight button
            document.querySelectorAll(`.part-btn`).forEach(btn => {
                if(btn.innerText.toLowerCase().includes(part)) btn.classList.add('active');
            });

            // Update Code
            updateCode(`.set${part.charAt(0).toUpperCase() + part.slice(1)}(true)`);

            // Visualize Part (Ghostly until built?) No, show immediately in Builder
            drawPart(part, false);
        }

        function drawPart(part, isFinal) {
            const color = isFinal ? "#3498db" : "#95a5a6";
            const stroke = isFinal ? "#2980b9" : "#7f8c8d";
            
            const g = svg.append("g")
                .attr("class", "robot-part")
                .attr("id", "part-" + part);

            if (part === 'head') {
                g.append("rect").attr("x", 150).attr("y", 50).attr("width", 100).attr("height", 80).attr("rx", 10).attr("fill", color).attr("stroke", stroke).attr("stroke-width", 2);
                g.append("circle").attr("cx", 180).attr("cy", 80).attr("r", 10).attr("fill", "white");
                g.append("circle").attr("cx", 220).attr("cy", 80).attr("r", 10).attr("fill", "white");
                g.append("rect").attr("x", 175).attr("y", 110).attr("width", 50).attr("height", 5).attr("fill", "white");
                // Antenna
                g.append("line").attr("x1", 200).attr("y1", 50).attr("x2", 200).attr("y2", 20).attr("stroke", stroke).attr("stroke-width", 2);
                g.append("circle").attr("cx", 200).attr("cy", 20).attr("r", 5).attr("fill", "#e74c3c");
            } else if (part === 'torso') {
                g.append("rect").attr("x", 140).attr("y", 135).attr("width", 120).attr("height", 120).attr("rx", 5).attr("fill", color).attr("stroke", stroke).attr("stroke-width", 2);
                // Chest detail
                g.append("circle").attr("cx", 200).attr("cy", 170).attr("r", 15).attr("fill", "#f1c40f");
            } else if (part === 'arms') {
                // Left
                g.append("rect").attr("x", 90).attr("y", 140).attr("width", 45).attr("height", 100).attr("rx", 5).attr("fill", color).attr("stroke", stroke).attr("stroke-width", 2);
                // Right
                g.append("rect").attr("x", 265).attr("y", 140).attr("width", 45).attr("height", 100).attr("rx", 5).attr("fill", color).attr("stroke", stroke).attr("stroke-width", 2);
            } else if (part === 'legs') {
                // Left
                g.append("rect").attr("x", 150).attr("y", 260).attr("width", 40).attr("height", 80).attr("rx", 5).attr("fill", color).attr("stroke", stroke).attr("stroke-width", 2);
                // Right
                g.append("rect").attr("x", 210).attr("y", 260).attr("width", 40).attr("height", 80).attr("rx", 5).attr("fill", color).attr("stroke", stroke).attr("stroke-width", 2);
            }

            // Animate entry
            g.classed("visible", true);
        }

        function buildRobot() {
            if (state.built) return;
            state.built = true;
            
            updateCode(".build();");
            document.getElementById('step-indicator').innerText = "State: Immutable Robot Created";

            // Transformation Animation: Turn everything Blue (Official)
            svg.selectAll("rect, circle").transition().duration(1000)
                .style("fill", function() {
                    if (this.getAttribute("fill") === "#f1c40f") return "#f1c40f"; // Keep heart gold
                    if (this.getAttribute("fill") === "#e74c3c") return "#e74c3c"; // Keep antenna red
                    if (this.getAttribute("fill") === "white") return "white"; // Keep eyes white
                    return "#3498db"; 
                })
                .style("stroke", "#2980b9");
                
            // Celebration confetti
            createConfetti();
        }

        function createConfetti() {
            for(let i=0; i<30; i++) {
                svg.append("circle")
                    .attr("cx", 200)
                    .attr("cy", 175)
                    .attr("r", 5)
                    .attr("fill", ["#e74c3c", "#f1c40f", "#2ecc71", "#9b59b6"][Math.floor(Math.random()*4)])
                    .transition().duration(1500)
                    .attr("cx", 100 + Math.random()*200)
                    .attr("cy", 50 + Math.random()*300)
                    .style("opacity", 0)
                    .remove();
            }
        }

        function reset() {
            state.head = false;
            state.torso = false;
            state.arms = false;
            state.legs = false;
            state.built = false;
            document.querySelectorAll('.part-btn').forEach(btn => btn.classList.remove('active'));
            document.getElementById('code-display').innerHTML = "";
            init();
        }

        // Init
        init();

    </script>
</body>
</html>"""

with open("builder_viz.html", "w") as f:
    f.write(html_content)

print("Generated builder_viz.html")
