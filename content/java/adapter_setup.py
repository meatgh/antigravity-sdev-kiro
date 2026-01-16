
import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Adapter Pattern - Universal Plug</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js"></script>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #1a1a2e;
            color: #e0e0e0;
            margin: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .container {
            width: 90%;
            max-width: 1000px;
            background: #16213e;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
            margin-top: 20px;
        }
        h2 { border-bottom: 2px solid #0f3460; padding-bottom: 10px; color: #e94560; }
        .controls {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
            background: #0f3460;
            padding: 15px;
            border-radius: 8px;
            align-items: center;
        }
        button {
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s;
        }
        .plug-btn { background-color: #e94560; color: white; }
        .plug-btn.disabled { background-color: #555; cursor: not-allowed; }
        .adapt-btn { background-color: #4CAF50; color: white; }
        .reset-btn { background-color: #533483; color: white; }
        
        .viz-area {
            height: 400px;
            background: #0f3460;
            border-radius: 8px;
            position: relative;
            overflow: hidden;
        }
        .code-panel {
            margin-top: 20px;
            background: #000;
            padding: 15px;
            border-radius: 8px;
            font-family: 'Consolas', monospace;
            color: #00ff00;
            height: 150px;
            overflow-y: auto;
            border: 1px solid #333;
        }
        .status-badge {
            padding: 5px 10px;
            border-radius: 4px;
            font-weight: bold;
        }
        .status-disconnected { background: #ff4444; color: white; }
        .status-connected { background: #00C851; color: white; }
    </style>
</head>
<body>
    <div class="container">
        <h2>🔌 Adapter Pattern: The Universal Interceptor</h2>
        <p>Problem: The Legacy <b>Square Plug</b> does not fit the Modern <b>Round Outlet</b>.</p>
        
        <div class="controls">
            <button class="plug-btn" onclick="tryConnectRaw()">Try Force Connect</button>
            <button class="adapt-btn" onclick="attachAdapter()">Attach Adapter</button>
            <button class="reset-btn" onclick="reset()">Reset</button>
            <span id="status" class="status-badge status-disconnected">Disconnected</span>
        </div>

        <div class="viz-area" id="viz"></div>

        <div class="code-panel" id="log">
            > System Ready. Waiting for input...
        </div>
    </div>

    <script>
        const viz = d3.select("#viz");
        const width = viz.node().getBoundingClientRect().width;
        const height = 400;
        const svg = viz.append("svg").attr("width", "100%").attr("height", "100%");
        
        // Configuration
        const centerY = height / 2;
        const wallX = width - 150;
        const plugStartX = 100;
        
        let hasAdapter = false;
        let isConnected = false;

        // Draw Wall Outlet (Round Hole)
        const wall = svg.append("g").attr("transform", `translate(${wallX}, ${centerY})`);
        wall.append("rect")
            .attr("x", -20).attr("y", -60)
            .attr("width", 40).attr("height", 120)
            .attr("fill", "#555").attr("stroke", "#888");
        wall.append("circle") // The Hole
            .attr("cx", 0).attr("cy", 0)
            .attr("r", 25)
            .attr("fill", "#1a1a2e")
            .attr("stroke", "#fff")
            .attr("stroke-width", 2);
        wall.append("text").text("Target (Round)").attr("y", 80).attr("text-anchor", "middle").attr("fill", "#aaa");

        // Plug Group (The Client)
        const plugGroup = svg.append("g").attr("transform", `translate(${plugStartX}, ${centerY})`);
        
        // The Legacy Plug (Square)
        const plugBody = plugGroup.append("rect")
            .attr("x", -60).attr("y", -25)
            .attr("width", 80).attr("height", 50)
            .attr("fill", "#e94560")
            .attr("rx", 5);
        
        const plugProng = plugGroup.append("rect") // Square Prong
            .attr("x", 20).attr("y", -15)
            .attr("width", 30).attr("height", 30)
            .attr("fill", "#c53046");
            
        plugGroup.append("text").text("Legacy (Square)").attr("y", -40).attr("text-anchor", "middle").attr("fill", "#e94560");

        // Adapter Group (Initially Hidden)
        const adapterGroup = plugGroup.append("g")
            .attr("opacity", 0)
            .attr("transform", "translate(50, 0)"); // Positioned at tip of plug
            
        // Adapter Body
        adapterGroup.append("rect")
            .attr("x", 0).attr("y", -20)
            .attr("width", 60).attr("height", 40)
            .attr("fill", "#4CAF50")
            .attr("rx", 4);
            
        // Adapter Interface (Round Prong)
        adapterGroup.append("circle")
            .attr("cx", 60).attr("cy", 0)
            .attr("r", 15)
            .attr("fill", "#4CAF50");

        adapterGroup.append("text").text("Adapter").attr("y", -30).attr("x", 30).attr("text-anchor", "middle").attr("fill", "#4CAF50");

        function log(msg, type='info') {
            const el = document.getElementById('log');
            const color = type === 'error' ? '#ff4444' : (type === 'success' ? '#00C851' : '#00ff00');
            el.innerHTML += `<div style="color:${color}">> ${msg}</div>`;
            el.scrollTop = el.scrollHeight;
        }

        function reset() {
            hasAdapter = false;
            isConnected = false;
            plugGroup.transition().duration(500).attr("transform", `translate(${plugStartX}, ${centerY})`);
            adapterGroup.transition().duration(500).attr("opacity", 0);
            updateStatus("Disconnected", "status-disconnected");
            log("State reset.");
        }

        function updateStatus(text, cls) {
            const el = document.getElementById('status');
            el.textContent = text;
            el.className = `status-badge ${cls}`;
        }

        function tryConnectRaw() {
            if (isConnected) return;
            if (hasAdapter) {
                log("Adapter attached. Use 'Connect' instead.", "info");
                return;
            }

            log("Attempting to insert SQUARE plug into ROUND hole...", "info");
            
            // Animate move to wall
            plugGroup.transition()
                .duration(1000)
                .attr("transform", `translate(${wallX - 60}, ${centerY})`) // Stop short
                .on("end", () => {
                     log("❌ ERROR: TYPE MISMATCH. SquarePeg != RoundHole", "error");
                     // Shake animation
                     plugGroup.transition()
                        .duration(100)
                        .attr("transform", `translate(${wallX - 70}, ${centerY})`)
                        .transition()
                        .duration(100)
                        .attr("transform", `translate(${wallX - 60}, ${centerY})`)
                        .transition()
                        .delay(500)
                        .duration(500)
                        .attr("transform", `translate(${plugStartX}, ${centerY})`); // Retreat
                });
        }

        function attachAdapter() {
            if (hasAdapter) return;
            hasAdapter = true;
            log("🛠️ Wrapping Legacy Plug with Adapter...", "info");
            
            adapterGroup.transition()
                .duration(800)
                .attr("opacity", 1)
                .on("end", () => {
                    log("✅ Adapter Applied. Interface is now ROUND.", "success");
                    connectWithAdapter();
                });
        }

        function connectWithAdapter() {
            log("Connecting Adapted Plug...", "info");
            
            // Move entire group (Plug + Adapter) into wall
            // Wall is at wallX. Adapter tip is at +60 offset from group center.
            // We want adapter tip (60) to touch wall (0).
            const targetX = wallX - 110; 

            plugGroup.transition()
                .delay(500)
                .duration(1500)
                .attr("transform", `translate(${targetX}, ${centerY})`)
                .on("end", () => {
                    isConnected = true;
                    updateStatus("Connected (Adapted)", "status-connected");
                    log("⚡ POWER ON. 220V Flowing safely.", "success");
                    
                    // Visualize flow
                    svg.append("circle")
                        .attr("cx", wallX)
                        .attr("cy", centerY)
                        .attr("r", 5)
                        .attr("fill", "#ffff00")
                        .transition()
                        .duration(1000)
                        .attr("cx", plugStartX)
                        .remove();
                });
        }

    </script>
</body>
</html>
"""

with open("adapter_setup.py", "w") as f:
    f.write(html_content)

print("✅ Created adapter_setup.py. Run 'python3 adapter_setup.py' to generate adapter_viz.html")
