
html_content = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        body { font-family: 'Inter', sans-serif; background: #1a1a1a; color: #fff; text-align: center; }
        .controls { margin-top: 20px; display: flex; justify-content: center; gap: 20px; }
        button { padding: 8px 16px; margin: 4px; cursor: pointer; border: 1px solid #555; background: #444; color: white; border-radius: 4px; }
        button:hover { background: #555; }
        #canvas { margin-top: 30px; min-height: 400px; display: flex; justify-content: center; }
        .node circle { stroke: #fff; stroke-width: 2px; }
        .node text { font: 12px sans-serif; fill: white; pointer-events: none; text-shadow: 1px 1px 2px #000; }
        .link { fill: none; stroke: #555; stroke-width: 1.5px; }
        #log { font-family: monospace; color: #4CAF50; margin-top: 20px; min-height: 20px; }
    </style>
</head>
<body>
    <h2>Composite Pattern: File System Tree</h2>
    <p>Uniformly treat Files (Leaf) and Directories (Composite).</p>

    <div class="controls">
        <button onclick="addFile()">📄 Add File</button>
        <button onclick="addFolder()">jm Folder</button>
        <button onclick="calcSize()">📏 Calculate Size (Recursive)</button>
    </div>
    
    <div id="log">Root Size: 0 KB</div>
    <div id="canvas"></div>

    <script>
        const width = 600, height = 400;
        
        // Initial Data
        let root = {
            name: "root",
            type: "folder",
            size: 0,
            children: [
                { name: "bin", type: "folder", size: 0, children: [] },
                { name: "home", type: "folder", size: 0, children: [
                    { name: "user", type: "folder", size: 0, children: [
                        { name: "resume.pdf", type: "file", size: 500 },
                        { name: "photo.jpg", type: "file", size: 2000 }
                    ]}
                ]},
                { name: "etc", type: "folder", size: 0, children: [] }
            ]
        };

        const svg = d3.select("#canvas").append("svg").attr("width", width).attr("height", height);
        const g = svg.append("g").attr("transform", "translate(40,0)");
        
        let i = 0;
        const duration = 750;
        let rootNode;
        
        // Tree Layout
        const tree = d3.tree().size([height, width - 160]);
        
        update(root);

        function update(source) {
            rootNode = d3.hierarchy(root, d => d.children);
            rootNode.x0 = height / 2;
            rootNode.y0 = 0;

            const treeData = tree(rootNode);
            const nodes = treeData.descendants();
            const links = treeData.links();

            // Normalize for fixed depth
            nodes.forEach(d => { d.y = d.depth * 100; });

            // Update Nodes
            const node = g.selectAll('g.node').data(nodes, d => d.id || (d.id = ++i));

            const nodeEnter = node.enter().append('g')
                .attr('class', 'node')
                .attr("transform", d => `translate(${source.y0},${source.x0})`)
                .on('click', click);

            nodeEnter.append('circle')
                .attr('r', 10)
                .style("fill", d => d.data.type === 'folder' ? "#E91E63" : "#2196F3");

            nodeEnter.append('text')
                .attr("dy", ".35em")
                .attr("x", d => d.children || d._children ? -13 : 13)
                .attr("text-anchor", d => d.children || d._children ? "end" : "start")
                .text(d => d.data.name + (d.data.type === 'file' ? ` (${d.data.size}KB)` : ""));

            const nodeUpdate = node.merge(nodeEnter).transition().duration(duration)
                .attr("transform", d => `translate(${d.y},${d.x})`);

            nodeUpdate.select('circle')
                .attr('r', 10)
                .style("fill", d => d.data.type === 'folder' ? "#E91E63" : "#2196F3")
                .attr('cursor', 'pointer');

            const nodeExit = node.exit().transition().duration(duration)
                .attr("transform", d => `translate(${source.y},${source.x})`)
                .remove();

            // Update Links
            const link = g.selectAll('path.link').data(links, d => d.target.id);

            const linkEnter = link.enter().insert('path', "g")
                .attr("class", "link")
                .attr('d', d => {
                    const o = {x: source.x0, y: source.y0};
                    return diagonal(o, o);
                });

            const linkUpdate = link.merge(linkEnter).transition().duration(duration)
                .attr('d', d => diagonal(d.source, d.target));

            link.exit().transition().duration(duration)
                .attr('d', d => {
                    const o = {x: source.x, y: source.y};
                    return diagonal(o, o);
                })
                .remove();
        }

        function diagonal(s, d) {
            return `M ${s.y} ${s.x}
                    C ${(s.y + d.y) / 2} ${s.x},
                      ${(s.y + d.y) / 2} ${d.x},
                      ${d.y} ${d.x}`;
        }

        function click(event, d) {
            if (d.children) {
                d._children = d.children;
                d.children = null;
            } else {
                d.children = d._children;
                d._children = null;
            }
            update(d);
        }
        
        function flatten(node) {
            let count = 0;
            if (node.type === 'file') return node.size;
            if (node.children) {
                node.children.forEach(c => count += flatten(c));
            }
            return count;
        }

        function calcSize() {
             // Visual Recursion Highlight could go here
             const total = flatten(root);
             document.getElementById("log").textContent = `Total Recursive Size: ${total} KB`;
             
             // Pulse root
             g.select("circle").transition().attr("r", 20).transition().attr("r", 10);
        }

        function addFile() {
             if(!root.children) root.children = [];
             root.children.push({ name: "new_file.txt", type: "file", size: 100 });
             update(root);
        }
        
        function addFolder() {
             if(!root.children) root.children = [];
             root.children.push({ name: "new_folder", type: "folder", size: 0, children: [] });
             update(root);
        }

    </script>
</body>
</html>
"""

with open("composite_filesystem.html", "w") as f:
    f.write(html_content)
print("✅ Generated composite_filesystem.html")
