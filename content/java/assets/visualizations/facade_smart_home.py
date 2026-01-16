
import json
import os

# Define the data structure for the Smart Home Facade Visualization
data = {
    "nodes": [
        {"id": "User", "group": "client", "label": "User"},
        {"id": "SmartHomeFacade", "group": "facade", "label": "Smart Home Hub (Facade)"},
        
        # Subsystems
        {"id": "Lighting", "group": "subsystem", "label": "Lighting System"},
        {"id": "HVAC", "group": "subsystem", "label": "Thermostat (HVAC)"},
        {"id": "Security", "group": "subsystem", "label": "Security Hub"},
        {"id": "Entertainment", "group": "subsystem", "label": "Media Center"},
        
        # Leaf nodes (Devices)
        {"id": "LivingRoomLight", "group": "device", "label": "Living Room Light"},
        {"id": "KitchenLight", "group": "device", "label": "Kitchen Light"},
        {"id": "ThermostatUnit", "group": "device", "label": "EcoBee Unit"},
        {"id": "DoorLock", "group": "device", "label": "Front Door Lock"},
        {"id": "Camera", "group": "device", "label": "CCTV Camera"},
        {"id": "TV", "group": "device", "label": "Samsung TV"},
        {"id": "SoundBar", "group": "device", "label": "Bose SoundBar"},
        {"id": "Blinds", "group": "device", "label": "Smart Blinds"}
    ],
    "links": [
        # Client -> Facade
        {"source": "User", "target": "SmartHomeFacade", "value": 1},
        
        # Facade -> Subsystems
        {"source": "SmartHomeFacade", "target": "Lighting", "value": 1},
        {"source": "SmartHomeFacade", "target": "HVAC", "value": 1},
        {"source": "SmartHomeFacade", "target": "Security", "value": 1},
        {"source": "SmartHomeFacade", "target": "Entertainment", "value": 1},
        
        # Subsystems -> Devices
        {"source": "Lighting", "target": "LivingRoomLight", "value": 1},
        {"source": "Lighting", "target": "KitchenLight", "value": 1},
        {"source": "HVAC", "target": "ThermostatUnit", "value": 1},
        {"source": "Security", "target": "DoorLock", "value": 1},
        {"source": "Security", "target": "Camera", "value": 1},
        {"source": "Entertainment", "target": "TV", "value": 1},
        {"source": "Entertainment", "target": "SoundBar", "value": 1},
        {"source": "SmartHomeFacade", "target": "Blinds", "value": 1} # Blinds could be direct or via a system
    ]
}

html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Facade Pattern: Smart Home Orchestrator</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        body {{ 
            font-family: 'Segoe UI', sans-serif; 
            background-color: #f0f2f5; 
            display: flex; 
            flex-direction: column; 
            align-items: center; 
            margin: 0;
            padding: 20px;
        }}
        h2 {{ color: #333; }}
        .controls {{
            margin-bottom: 20px;
            display: flex;
            gap: 15px;
        }}
        button {{
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
            font-size: 14px;
            transition: transform 0.1s, box-shadow 0.1s;
        }}
        button:hover {{ transform: translateY(-2px); box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
        #btn-movie {{ background-color: #3b82f6; color: white; }}
        #btn-sleep {{ background-color: #8b5cf6; color: white; }}
        #btn-leave {{ background-color: #ef4444; color: white; }}
        #btn-reset {{ background-color: #6b7280; color: white; }}
        
        svg {{ 
            background-color: white; 
            border-radius: 12px; 
            box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        }}
        
        .node circle {{ stroke: #fff; stroke-width: 2px; }}
        .link {{ stroke: #e5e7eb; stroke-width: 2px; stroke-opacity: 0.6; }}
        
        .status-panel {{
            margin-top: 20px;
            padding: 15px;
            background: white;
            border-radius: 8px;
            width: 600px;
            min-height: 100px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            font-family: monospace;
            color: #374151;
        }}
    </style>
</head>
<body>
    <h2>Facade Pattern: Smart Home Orchestrator</h2>
    
    <div class="controls">
        <button id="btn-movie" onclick="activateMovieMode()">🎬 Movie Mode</button>
        <button id="btn-sleep" onclick="activateSleepMode()">😴 Sleep Mode</button>
        <button id="btn-leave" onclick="activateAwayMode()">🔒 Leave Home</button>
        <button id="btn-reset" onclick="resetSystem()">🔄 Reset</button>
    </div>

    <div id="chart"></div>
    
    <div class="status-panel" id="status-log">
        <div>> System Ready. Waiting for commands via Facade...</div>
    </div>

    <script>
        const data = {json.dumps(data)};
        const width = 800;
        const height = 500;

        const svg = d3.select("#chart")
            .append("svg")
            .attr("width", width)
            .attr("height", height);

        const simulation = d3.forceSimulation(data.nodes)
            .force("link", d3.forceLink(data.links).id(d => d.id).distance(100))
            .force("charge", d3.forceManyBody().strength(-400))
            .force("center", d3.forceCenter(width / 2, height / 2));

        const link = svg.append("g")
            .selectAll("line")
            .data(data.links)
            .enter().append("line")
            .attr("class", "link");

        const node = svg.append("g")
            .selectAll("g")
            .data(data.nodes)
            .enter().append("g")
            .attr("class", "node")
            .call(d3.drag()
                .on("start", dragstarted)
                .on("drag", dragged)
                .on("end", dragended));

        const colors = {{
            "client": "#10b981",
            "facade": "#3b82f6",
            "subsystem": "#f59e0b",
            "device": "#6b7280"
        }};

        node.append("circle")
            .attr("r", d => d.group === "facade" ? 30 : (d.group === "client" ? 25 : 15))
            .attr("fill", d => colors[d.group]);

        node.append("text")
            .attr("dy", d => d.group === "facade" ? 45 : 30)
            .attr("text-anchor", "middle")
            .text(d => d.label)
            .style("font-size", "12px")
            .style("fill", "#374151")
            .style("font-weight", "600");

        simulation.on("tick", () => {{
            link
                .attr("x1", d => d.source.x)
                .attr("y1", d => d.source.y)
                .attr("x2", d => d.target.x)
                .attr("y2", d => d.target.y);

            node
                .attr("transform", d => `translate(${{d.x}},${{d.y}})`);
        }});

        function log(message) {{
            const output = document.getElementById("status-log");
            output.innerHTML += `<div>> ${{message}}</div>`;
            output.scrollTop = output.scrollHeight;
        }}

        function pulseNode(id, color) {{
            svg.selectAll("circle")
                .filter(d => d.id === id)
                .transition()
                .duration(300)
                .attr("fill", color)
                .attr("r", 35)
                .transition()
                .duration(300)
                .attr("r", d => d.group === "facade" ? 30 : (d.group === "client" ? 25 : 15))
                .attr("fill", d => colors[d.group]);
        }}
        
        function activateLink(sourceId, targetId) {{
             svg.selectAll("line")
                .filter(d => d.source.id === sourceId && d.target.id === targetId)
                .transition()
                .duration(500)
                .style("stroke", "#ef4444")
                .style("stroke-width", "4px")
                .transition()
                .duration(500)
                .style("stroke", "#e5e7eb")
                .style("stroke-width", "2px");
        }}

        function activateDevice(deviceId, action, color="#ef4444") {{
            setTimeout(() => {{
                log(`${{action}}`);
                pulseNode(deviceId, color);
            }}, 500); // Slight delay to simulate propagation
        }}

        // --- FACADE METHODS ---

        function activateMovieMode() {{
            log("<strong>[Client]</strong> Calling Facade.watchMovie()...");
            pulseNode("SmartHomeFacade", "#3b82f6");
            
            // Facade orchestrating subsystems
            setTimeout(() => {{
                log("[Facade] Dimming Lights to 10%...");
                activateLink("SmartHomeFacade", "Lighting");
                activateDevice("LivingRoomLight", "Living Room: Dimmed", "#fdba74");
                activateDevice("KitchenLight", "Kitchen: OFF", "#1f2937");
            }}, 300);

            setTimeout(() => {{
                log("[Facade] Lowering Blinds...");
                activateLink("SmartHomeFacade", "Blinds");
                activateDevice("Blinds", "Blinds: Closed", "#1f2937");
            }}, 600);
            
            setTimeout(() => {{
                log("[Facade] Turning on TV & Sound...");
                activateLink("SmartHomeFacade", "Entertainment");
                activateDevice("TV", "TV: ON (Netflix)", "#3b82f6");
                activateDevice("SoundBar", "Sound: ON (Dolby Atmos)", "#3b82f6");
            }}, 900);
        }}

        function activateSleepMode() {{
             log("<strong>[Client]</strong> Calling Facade.nightMode()...");
             pulseNode("SmartHomeFacade", "#8b5cf6");
             
             setTimeout(() => {{
                log("[Facade] Locking Doors...");
                activateLink("SmartHomeFacade", "Security");
                activateDevice("DoorLock", "Doors: LOCKED", "#ef4444");
             }}, 300);
             
             setTimeout(() => {{
                log("[Facade] Turning OFF all lights...");
                activateLink("SmartHomeFacade", "Lighting");
                activateDevice("LivingRoomLight", "LR Light: OFF", "#1f2937");
                activateDevice("KitchenLight", "Kitchen: OFF", "#1f2937");
             }}, 600);
             
             setTimeout(() => {{
                log("[Facade] Setting Temp to 70°F...");
                activateLink("SmartHomeFacade", "HVAC");
                activateDevice("ThermostatUnit", "HVAC: Sleep Mode (70°F)", "#10b981");
             }}, 900);
        }}
        
        function activateAwayMode() {{
             log("<strong>[Client]</strong> Calling Facade.leaveHome()...");
             pulseNode("SmartHomeFacade", "#ef4444");
             
             setTimeout(() => {{
                log("[Facade] Arming Security System...");
                activateLink("SmartHomeFacade", "Security");
                activateDevice("DoorLock", "Doors: LOCKED", "#ef4444");
                activateDevice("Camera", "Cameras: ACTIVE (Motion Detect)", "#ef4444");
             }}, 300);
             
             setTimeout(() => {{
                log("[Facade] Cutting Power to Non-Essentials...");
                activateLink("SmartHomeFacade", "Entertainment");
                activateDevice("TV", "TV: Hard OFF", "#1f2937");
             }}, 600);
        }}

        function resetSystem() {{
            log("System Reset.");
            svg.selectAll("circle").attr("fill", d => colors[d.group]);
        }}

        function dragstarted(event, d) {{
            if (!event.active) simulation.alphaTarget(0.3).restart();
            d.fx = d.x;
            d.fy = d.y;
        }}

        function dragged(event, d) {{
            d.fx = event.x;
            d.fy = event.y;
        }}

        function dragended(event, d) {{
            if (!event.active) simulation.alphaTarget(0);
            d.fx = null;
            d.fy = null;
        }}
    </script>
</body>
</html>
"""

# Ensure directory exists
output_dir = "assets/visualizations"
os.makedirs(output_dir, exist_ok=True)

# Write HTML file
file_path = os.path.join(output_dir, "facade_smart_home.html")
with open(file_path, "w") as f:
    f.write(html_content)

print(f"Visualization generated at: {file_path}")
