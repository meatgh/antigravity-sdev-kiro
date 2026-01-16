
html_content = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        body { font-family: 'Inter', sans-serif; background: #1a1a1a; color: #fff; text-align: center; }
        .controls { margin-top: 20px; display: flex; justify-content: center; gap: 20px; }
        button { padding: 10px 20px; font-size: 14px; margin: 4px; cursor: pointer; border: 1px solid #555; background: #444; color: white; border-radius: 4px; }
        button:hover { background: #555; }
        button.blocked { border-color: #f44336; color: #f44336; }
        button.allowed { border-color: #4CAF50; color: #4CAF50; }
        #canvas { margin-top: 30px; display: flex; justify-content: center; height: 300px; }
        .node text { font: 12px sans-serif; fill: white; pointer-events: none; text-shadow: 1px 1px 2px #000; }
        #log { font-family: monospace; color: #4CAF50; margin-top: 20px; min-height: 20px; }
        .shield { filter: drop-shadow(0px 0px 5px #2196F3); }
    </style>
</head>
<body>
    <h2>Proxy Pattern: Security Firewall</h2>
    <p>The Proxy intercepts requests BEFORE they reach the Real Subject.</p>

    <div class="controls">
        <button onclick="requestAccess('User', 'ADMIN')" class="allowed">Req: User (ADMIN)</button>
        <button onclick="requestAccess('Hacker', 'GUEST')" class="blocked">Req: Hacker (GUEST)</button>
        <button onclick="requestAccess('Bot', 'NONE')" class="blocked">Req: Bot (NONE)</button>
    </div>
    
    <div id="log">Status: Ready</div>
    <div id="canvas"></div>

    <script>
        const width = 700, height = 300;
        const svg = d3.select("#canvas").append("svg").attr("width", width).attr("height", height);
        
        // Nodes
        const clientX = 100;
        const proxyX = 350;
        const serverX = 600;
        const groundY = 150;

        // Draw Components
        // 1. Client Zone
        svg.append("circle").attr("cx", clientX).attr("cy", groundY).attr("r", 30).attr("fill", "#9E9E9E");
        svg.append("text").attr("x", clientX).attr("y", groundY + 50).attr("text-anchor", "middle").text("Client");

        // 2. Proxy (Shield)
        const shieldGroup = svg.append("g").attr("transform", `translate(${proxyX}, ${groundY})`).attr("class", "shield");
        shieldGroup.append("rect").attr("x", -20).attr("y", -50).attr("width", 40).attr("height", 100).attr("rx", 5).attr("fill", "#2196F3");
        shieldGroup.append("text").attr("x", 0).attr("y", 70).attr("text-anchor", "middle").text("Protection Proxy");
        
        // 3. Real Subject (Server)
        svg.append("rect").attr("x", serverX - 30).attr("y", groundY - 30).attr("width", 60).attr("height", 60).attr("fill", "#4CAF50");
        svg.append("text").attr("x", serverX).attr("y", groundY + 50).attr("text-anchor", "middle").text("RealDB (Sensitive)");

        function requestAccess(user, role) {
            // 1. Packet Animation Client -> Proxy
            const packet = svg.append("circle")
                .attr("cx", clientX).attr("cy", groundY).attr("r", 8).attr("fill", "#FFF");
                
            packet.transition().duration(1000).attr("cx", proxyX - 30)
                .on("end", () => {
                   // Proxy Check Logic
                   document.getElementById("log").textContent = `Proxy: Checking Role for ${user}...`;
                   
                   setTimeout(() => {
                       if(role === 'ADMIN') {
                           // Allow
                           shieldGroup.select("rect").transition().attr("fill", "#4CAF50").transition().attr("fill", "#2196F3");
                           document.getElementById("log").textContent = "Proxy: Access GRANTED. Forwarding...";
                           
                           packet.transition().duration(1000).attr("cx", serverX - 40)
                            .on("end", () => {
                                packet.remove();
                                // Server Pulse
                                svg.append("circle").attr("cx", serverX).attr("cy", groundY).attr("r", 0).attr("fill", "none").attr("stroke", "#4CAF50").attr("stroke-width", 2)
                                    .transition().duration(500).attr("r", 60).remove();
                                document.getElementById("log").textContent = "RealDB: Query Executed.";
                            });
                           
                       } else {
                           // Block
                           shieldGroup.select("rect").transition().attr("fill", "#f44336").transition().attr("fill", "#2196F3");
                           document.getElementById("log").textContent = `Proxy: Access DENIED. Role ${role} insufficient.`;
                           
                           // Bounce back
                           packet.transition().duration(500).attr("cx", clientX).remove();
                       }
                   }, 500);
                });
        }
    </script>
</body>
</html>
"""

with open("proxy_firewall.html", "w") as f:
    f.write(html_content)
print("✅ Generated proxy_firewall.html")
