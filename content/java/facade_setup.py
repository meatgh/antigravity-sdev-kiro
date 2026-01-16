import os

html_content = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        body { font-family: 'Inter', sans-serif; background: #1a1a1a; color: #fff; text-align: center; }
        .node { stroke: #fff; stroke-width: 2px; }
        .client { fill: #2196F3; }
        .facade { fill: #9C27B0; }
        .service { fill: #FF9800; }
        .link { stroke: #666; stroke-width: 2px; }
        .pulse { fill: #FFEB3B; }
        text { fill: #fff; font-size: 14px; pointer-events: none; }
        button { padding: 10px 20px; font-size: 16px; margin: 10px; cursor: pointer; }
    </style>
</head>
<body>
    <h2>Controls: Facade Pattern (API Gateway)</h2>
    <p>Simulating: <b style="color:#2196F3">Mobile App</b> -> <b style="color:#9C27B0">Gateway</b> -> <b style="color:#FF9800">Microservices</b></p>
    <button onclick="triggerMacro()">📱 Execute 'Order Pizza'</button>
    <div id="viz"></div>
    <script>
        const width = 600, height = 400;
        const svg = d3.select("#viz").append("svg").attr("width", width).attr("height", height);

        const nodes = [
            { id: "Mobile App", x: 100, y: 200, type: "client" },
            { id: "API Gateway (Facade)", x: 300, y: 200, type: "facade" },
            { id: "Auth Service", x: 500, y: 100, type: "service" },
            { id: "Order Service", x: 500, y: 200, type: "service" },
            { id: "Payment Service", x: 500, y: 300, type: "service" }
        ];

        const links = [
             { source: 0, target: 1 },
             { source: 1, target: 2 },
             { source: 1, target: 3 },
             { source: 1, target: 4 }
        ];

        // Draw Links
        svg.selectAll("line")
            .data(links)
            .enter().append("line")
            .attr("x1", d => nodes[d.source].x).attr("y1", d => nodes[d.source].y)
            .attr("x2", d => nodes[d.target].x).attr("y2", d => nodes[d.target].y)
            .attr("stroke", "#666").attr("stroke-width", 2);

        // Draw Nodes
        svg.selectAll("circle")
            .data(nodes)
            .enter().append("circle")
            .attr("cx", d => d.x).attr("cy", d => d.y)
            .attr("r", d => d.type === "facade" ? 40 : 20)
            .attr("class", d => d.type)
            .attr("fill", d => d.type === "client" ? "#2196F3" : d.type === "facade" ? "#9C27B0" : "#FF9800");

        svg.selectAll("text")
            .data(nodes)
            .enter().append("text")
            .attr("x", d => d.x).attr("y", d => d.y + 45)
            .attr("text-anchor", "middle")
            .text(d => d.id);

        window.triggerMacro = function() {
            // Pulse to Gateway
            const p1 = svg.append("circle").attr("class", "pulse").attr("r", 5).attr("cx", 100).attr("cy", 200);
            p1.transition().duration(500).attr("cx", 300).remove().on("end", () => {
                // Fan out
                 [2, 3, 4].forEach(targetIdx => {
                     const p = svg.append("circle").attr("class", "pulse").attr("r", 5).attr("cx", 300).attr("cy", 200);
                     p.transition().duration(500).attr("cx", 500).attr("cy", nodes[targetIdx].y).remove();
                 });
            });
        };
    </script>
</body>
</html>
"""

with open("facade_viz.html", "w") as f:
    f.write(html_content)
print("✅ Generated facade_viz.html")
