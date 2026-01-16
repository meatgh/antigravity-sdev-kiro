import json
import os

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Proxy Pattern Visualization</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        body { background-color: #121212; color: #e0e0e0; font-family: 'Segoe UI', sans-serif; display: flex; flex-direction: column; align-items: center; }
        h2 { color: #bb86fc; }
        .node circle { stroke: #fff; stroke-width: 1.5px; }
        .link { stroke: #999; stroke-opacity: 0.6; stroke-width: 2px; }
        .label { font-size: 12px; fill: #ccc; pointer-events: none; }
        .link-label { font-size: 10px; fill: #aaa; }
        #viz { width: 800px; height: 600px; border: 1px solid #333; border-radius: 8px; background: #1e1e1e; }
        .legend { display: flex; gap: 20px; margin-bottom: 15px; }
        .legend-item { display: flex; align-items: center; gap: 5px; }
        .dot { width: 12px; height: 12px; border-radius: 50%; }
    </style>
</head>
<body>
    <h2>🛡️ Proxy Pattern: The Gatekeeper</h2>
    <div class="legend">
        <div class="legend-item"><div class="dot" style="background:#03dac6"></div>Client</div>
        <div class="legend-item"><div class="dot" style="background:#bb86fc"></div>Proxy (Gatekeeper)</div>
        <div class="legend-item"><div class="dot" style="background:#cf6679"></div>Real Subject (Service)</div>
    </div>
    <div id="viz"></div>
    <script>
        const data = __DATA_PLACEHOLDER__;

        const width = 800;
        const height = 600;

        const svg = d3.select("#viz").append("svg")
            .attr("width", width)
            .attr("height", height);

        // Arrow marker
        svg.append("defs").selectAll("marker")
            .data(["end"])
            .enter().append("marker")
            .attr("id", "arrow")
            .attr("viewBox", "0 -5 10 10")
            .attr("refX", 25)
            .attr("refY", 0)
            .attr("markerWidth", 6)
            .attr("markerHeight", 6)
            .attr("orient", "auto")
            .append("path")
            .attr("d", "M0,-5L10,0L0,5")
            .attr("fill", "#999");

        const simulation = d3.forceSimulation(data.nodes)
            .force("link", d3.forceLink(data.links).id(d => d.id).distance(150))
            .force("charge", d3.forceManyBody().strength(-500))
            .force("center", d3.forceCenter(width / 2, height / 2));

        const link = svg.append("g")
            .selectAll(".link")
            .data(data.links)
            .enter().append("line")
            .attr("class", "link")
            .attr("marker-end", "url(#arrow)");

        const linkLabel = svg.append("g")
            .selectAll(".link-label")
            .data(data.links)
            .enter().append("text")
            .attr("class", "link-label")
            .attr("dy", -5)
            .text(d => d.label);

        const node = svg.append("g")
            .selectAll(".node")
            .data(data.nodes)
            .enter().append("g")
            .attr("class", "node")
            .call(d3.drag()
                .on("start", dragstarted)
                .on("drag", dragged)
                .on("end", dragended));

        node.append("circle")
            .attr("r", d => d.radius)
            .attr("fill", d => {
                if(d.group === 1) return "#03dac6"; // Client
                if(d.group === 2) return "#bb86fc"; // Proxy
                return "#cf6679"; // RealSubject
            });

        node.append("text")
            .attr("class", "label")
            .attr("dx", 0)
            .attr("dy", d => d.radius + 15)
            .attr("text-anchor", "middle")
            .text(d => d.id);

        simulation.on("tick", () => {
            link
                .attr("x1", d => d.source.x)
                .attr("y1", d => d.source.y)
                .attr("x2", d => d.target.x)
                .attr("y2", d => d.target.y);

            linkLabel
                .attr("x", d => (d.source.x + d.target.x) / 2)
                .attr("y", d => (d.source.y + d.target.y) / 2);

            node
                .attr("transform", d => `translate(${d.x},${d.y})`);
        });

        function dragstarted(event, d) {
            if (!event.active) simulation.alphaTarget(0.3).restart();
            d.fx = d.x;
            d.fy = d.y;
        }

        function dragged(event, d) {
            d.fx = event.x;
            d.fy = event.y;
        }

        function dragended(event, d) {
            if (!event.active) simulation.alphaTarget(0);
            d.fx = null;
            d.fy = null;
        }
    </script>
</body>
</html>
"""

def generate_proxy_visualization():
    nodes = [
        {"id": "Client", "group": 1, "radius": 20},
        {"id": "Proxy", "group": 2, "radius": 30},
        {"id": "SecurityLayer", "group": 2, "radius": 15},
        {"id": "CacheLayer", "group": 2, "radius": 15},
        {"id": "RealSubject", "group": 3, "radius": 25},
        {"id": "RemoteServer", "group": 3, "radius": 10},
        {"id": "Database", "group": 3, "radius": 10}
    ]

    links = [
        {"source": "Client", "target": "Proxy", "label": "request()"},
        {"source": "Proxy", "target": "SecurityLayer", "label": "1. checkAccess()"},
        {"source": "Proxy", "target": "CacheLayer", "label": "2. checkCache()"},
        {"source": "Proxy", "target": "RealSubject", "label": "3. delegate()"},
        {"source": "RealSubject", "target": "RemoteServer", "label": "network call"},
        {"source": "RealSubject", "target": "Database", "label": "query"}
    ]

    data = {"nodes": nodes, "links": links}
    
    # Inject data into HTML
    final_html = html_template.replace("__DATA_PLACEHOLDER__", json.dumps(data))
    
    with open("proxy_viz.html", "w") as f:
        f.write(final_html)
    
    print("✅ Generated proxy_viz.html")

if __name__ == "__main__":
    generate_proxy_visualization()
