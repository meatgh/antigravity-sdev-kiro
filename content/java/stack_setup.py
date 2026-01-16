import os

html_content = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        body { font-family: 'Inter', sans-serif; background: #1a1a1a; color: #fff; text-align: center; }
        .bar { fill: #2196F3; rx: 4; }
        .empty-slot { fill: #333; stroke: #555; stroke-dasharray: 2; rx: 4; }
        text { fill: #ccc; font-size: 12px; }
    </style>
</head>
<body>
    <h2>📚 Visualizing Amortized Stack Resizing</h2>
    <p>Watch the array capacity <b>double</b> when full.</p>
    <div id="viz"></div>
    <script>
        const width = 800, height = 300;
        const svg = d3.select("#viz").append("svg").attr("width", width).attr("height", height);
        
        let data = [];
        let capacity = 2; // Start small
        const barWidth = 30;

        function update() {
            // Background slots (Capacity)
            const slots = svg.selectAll(".empty-slot").data(d3.range(capacity));
            slots.enter().append("rect").attr("class", "empty-slot")
                .merge(slots)
                .transition().duration(500)
                .attr("x", (d, i) => 50 + i * (barWidth + 5))
                .attr("y", 100)
                .attr("width", barWidth).attr("height", 100);
            slots.exit().remove();

            // Filled data
            const bars = svg.selectAll(".bar").data(data);
            bars.enter().append("rect").attr("class", "bar")
                .attr("y", 200).attr("height", 0) // Animate up
                .merge(bars)
                .transition().duration(500)
                .attr("x", (d, i) => 50 + i * (barWidth + 5))
                .attr("y", 100).attr("width", barWidth).attr("height", 100);
            bars.exit().remove();
        }

        // Simulation Loop
        let i = 0;
        setInterval(() => {
            if (i < 15) {
                if (data.length === capacity) {
                    capacity *= 2; // Resize!
                }
                data.push(i++);
                update();
            } else {
                data = []; capacity = 2; i = 0; // Reset
            }
        }, 800);
        update();
    </script>
</body>
</html>
"""

with open("stack_viz.html", "w") as f:
    f.write(html_content)
print("✅ Generated stack_viz.html")
