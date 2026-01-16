import os

html_content = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        body { font-family: 'Inter', sans-serif; background: #1a1a1a; color: #fff; text-align: center; }
        .node { fill: #333; stroke: #fff; stroke-width: 2px; }
        .node.subject { fill: #FFEB3B; stroke: #FBC02D; stroke-width: 3px; }
        .node.observer { fill: #42A5F5; stroke: #1E88E5; cursor: pointer; }
        .node.unsubscribed { fill: #555; stroke: #777; stroke-dasharray: 4; }
        .link { stroke: #666; stroke-width: 1.5px; opacity: 0.6; }
        .pulse { animation: pulse 1s infinite; }
        @keyframes pulse {
            0% { r: 10; stroke-width: 2px; }
            50% { r: 14; stroke-width: 4px; }
            100% { r: 10; stroke-width: 2px; }
        }
        text { fill: #fff; font-size: 12px; pointer-events: none; }
        button { padding: 10px 20px; font-size: 16px; margin: 10px; cursor: pointer; background: #333; color: white; border: 1px solid #555; }
        button:hover { background: #444; }
    </style>
</head>
<body>
    <h2>Controls: Observer Pattern (News Agency)</h2>
    <p>Event: <span id="event">None</span> | Subscribers: <span id="count">3</span></p>
    <div style="margin-bottom: 20px;">
        <button onclick="trigger('publish')">📰 Publish News</button>
        <button onclick="trigger('add')">➕ Add Subscriber</button>
        <button onclick="trigger('remove')">➖ Lapsed Listener (Leak)</button>
    </div>
    
    <div id="viz"></div>
    <script>
        const width = 800, height = 500;
        const svg = d3.select("#viz").append("svg").attr("width", width).attr("height", height);

        // Data
        let nodes = [
            { id: "Subject", type: "subject", x: width/2, y: height/2 }
        ];
        
        // Initial Observers
        for(let i=1; i<=3; i++) {
            nodes.push({ id: "Obs" + i, type: "observer", x: Math.random() * width, y: Math.random() * height });
        }
        
        let links = nodes.slice(1).map(n => ({ source: nodes[0], target: n }));

        const simulation = d3.forceSimulation(nodes)
            .force("link", d3.forceLink(links).id(d => d.id).distance(150))
            .force("charge", d3.forceManyBody().strength(-300))
            .force("center", d3.forceCenter(width / 2, height / 2));

        // Draw Links
        let linkDetails = svg.append("g").selectAll("line");

        // Draw Nodes
        let nodeDetails = svg.append("g").selectAll("circle");
        let texts = svg.append("g").selectAll("text");

        function update() {
            linkDetails = linkDetails.data(links);
            linkDetails.exit().remove();
            const linkEnter = linkDetails.enter().append("line").attr("class", "link");
            linkDetails = linkEnter.merge(linkDetails);

            nodeDetails = nodeDetails.data(nodes);
            nodeDetails.exit().transition().duration(500).attr("r", 0).remove();
            const nodeEnter = nodeDetails.enter().append("circle")
                .attr("class", d => "node " + d.type)
                .attr("r", d => d.type === "subject" ? 30 : 20)
                .call(d3.drag()
                    .on("start", dragstarted)
                    .on("drag", dragged)
                    .on("end", dragended));
            nodeDetails = nodeEnter.merge(nodeDetails);
            
            texts = texts.data(nodes);
            texts.exit().remove();
            const textEnter = texts.enter().append("text")
                .text(d => d.id)
                .attr("text-anchor", "middle")
                .attr("dy", 40);
            texts = textEnter.merge(texts);

            simulation.nodes(nodes).on("tick", ticked);
            simulation.force("link").links(links);
            simulation.alpha(1).restart();
            
            document.getElementById("count").innerText = nodes.length - 1;
        }

        function ticked() {
            linkDetails
                .attr("x1", d => d.source.x).attr("y1", d => d.source.y)
                .attr("x2", d => d.target.x).attr("y2", d => d.target.y);

            nodeDetails
                .attr("cx", d => d.x).attr("cy", d => d.y);
                
            texts
                .attr("x", d => d.x).attr("y", d => d.y);
        }

        update();

        window.trigger = function(action) {
            if (action === "publish") {
                document.getElementById("event").innerText = "Breaking News! " + Math.floor(Math.random() * 1000);
                
                // Flash Effect
                svg.selectAll(".observer")
                    .transition().duration(200).attr("fill", "#fff")
                    .transition().duration(500).attr("fill", "#42A5F5");
                    
                // Particle Emission
                nodes.slice(1).forEach(obs => {
                    svg.append("circle")
                        .attr("cx", nodes[0].x).attr("cy", nodes[0].y).attr("r", 5).attr("fill", "yellow")
                        .transition().duration(1000)
                        .attr("cx", obs.x).attr("cy", obs.y)
                        .remove();
                });
                
            } else if (action === "add") {
                const id = "Obs" + (nodes.length);
                const newNode = { id: id, type: "observer", x: width/2, y: height/2 };
                nodes.push(newNode);
                links.push({ source: nodes[0], target: newNode });
                update();
            } else if (action === "remove") {
                // Determine memory leak - remove link but KEEP node?
                // Visualizing Lapsed Listener:
                // We remove the link, but the node stays in memory (red color)
                if (links.length > 0) {
                    const victimLinkIndex = Math.floor(Math.random() * links.length);
                    const victimNode = links[victimLinkIndex].target;
                    
                    // Remove Link
                    links.splice(victimLinkIndex, 1);
                    
                    // Mark Node as Leaked (Red)
                    victimNode.type = "unsubscribed"; // Just change visuals manually
                    d3.selectAll(".node").filter(d => d === victimNode)
                        .attr("class", "node unsubscribed")
                        .attr("fill", "#ff5252"); 
                        
                    // Don't call update() fully or it re-renders classes. 
                    simulation.force("link").links(links);
                    simulation.alpha(1).restart();
                    d3.select(".link-group").selectAll("line").data(links).exit().remove(); // Hacky quick update
                    update(); // safer
                }
            }
        };

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

with open("observer_viz.html", "w") as f:
    f.write(html_content)
print("✅ Generated observer_viz.html")
