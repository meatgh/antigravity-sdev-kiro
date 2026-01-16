html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Singleton Pattern - Distributed Cluster</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js"></script>
    <style>
        body { font-family: 'Segoe UI', sans-serif; background: #1a1a2e; color: #fff; margin: 0; display: flex; flex-direction: column; align-items: center; }
        .container { width: 90%; max-width: 800px; background: #16213e; padding: 20px; border-radius: 12px; margin-top: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); }
        h2 { border-bottom: 2px solid #e94560; padding-bottom: 10px; color: #e94560; }
        .controls { background: #0f3460; padding: 15px; border-radius: 8px; margin-bottom: 20px; display: flex; gap: 10px; justify-content: center; }
        button { padding: 10px 20px; background: #e94560; border: none; color: white; border-radius: 4px; cursor: pointer; font-weight: bold; }
        button:hover { background: #c12945; }
        #viz { height: 400px; background: #0f3460; border-radius: 8px; position: relative; overflow: hidden; }
        .log-panel { height: 100px; background: #000; margin-top: 15px; padding: 10px; font-family: monospace; color: #0f0; overflow-y: auto; border-radius: 4px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>👑 Singleton: The Highlander Principle</h2>
        <p>"There can be only one." - This visualization shows multiple threads attempting to access the Instance.</p>
        
        <div class="controls">
            <button onclick="accessInstance(1)">1 Thread Request</button>
            <button onclick="accessInstance(5)">5 Concurrent Requests</button>
            <button onclick="resetSystem()">Reset System</button>
        </div>

        <div id="viz"></div>
        <div class="log-panel" id="log"></div>
    </div>

    <script>
        const svg = d3.select("#viz").append("svg").attr("width", "100%").attr("height", "100%");
        const width = document.getElementById('viz').clientWidth;
        const height = 400;
        
        let instance = null;
        let threads = [];
        
        // Draw the "Heap" area
        svg.append("circle").attr("cx", width/2).attr("cy", height/2).attr("r", 60).attr("fill", "#1a1a2e").attr("stroke", "#e94560").attr("stroke-width", 2).attr("stroke-dasharray", "5,5");
        svg.append("text").attr("x", width/2).attr("y", height/2 + 80).attr("text-anchor", "middle").attr("fill", "#666").text("Heap Space (Singleton Slot)");

        function log(msg) {
            const el = document.getElementById('log');
            el.innerHTML = `> ${msg}<br>` + el.innerHTML;
        }

        function createInstanceVisual() {
            if (instance) return;
            instance = svg.append("g");
            instance.append("circle")
                .attr("cx", width/2).attr("cy", height/2).attr("r", 0)
                .attr("fill", "#e94560")
                .transition().duration(800).ease(d3.easeElastic)
                .attr("r", 40);
            
            instance.append("text")
                .attr("x", width/2).attr("y", height/2 + 5)
                .attr("text-anchor", "middle")
                .attr("fill", "white")
                .attr("font-weight", "bold")
                .text("INSTANCE");
                
            log("✨ NEW INSTANCE CREATED! (Heavy Operation)");
        }

        function accessInstance(count) {
            for(let i=0; i<count; i++) {
                const threadId = Math.floor(Math.random() * 1000);
                const startX = Math.random() * width;
                const startY = Math.random() < 0.5 ? -20 : height + 20;
                
                const thread = svg.append("circle")
                    .attr("cx", startX)
                    .attr("cy", startY)
                    .attr("r", 8)
                    .attr("fill", "#4cc9f0");
                
                thread.transition().duration(1000).attr("cx", width/2).attr("cy", height/2)
                    .on("end", function() {
                        d3.select(this).remove();
                        if (!instance) {
                            createInstanceVisual();
                        } else {
                            log(`Thread ${threadId} used EXISTING instance.`);
                            // Flash effect
                            instance.select("circle").attr("fill", "#fff").transition().duration(200).attr("fill", "#e94560");
                        }
                    });
            }
        }

        function resetSystem() {
            if (instance) instance.remove();
            instance = null;
            svg.selectAll("circle").filter(function() { return d3.select(this).attr("fill") === "#4cc9f0"; }).remove();
            document.getElementById('log').innerHTML = "";
            log("System Reset. Instance destroyed.");
        }
    </script>
</body>
</html>
'''

with open('singleton_viz.html', 'w') as f:
    f.write(html_content)

print('Generated singleton_viz.html')