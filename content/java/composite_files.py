
html_content = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        body { font-family: 'Inter', sans-serif; background: #1a1a1a; color: #fff; text-align: center; }
        .node circle { stroke: #fff; stroke-width: 2px; }
        .node text { font: 12px sans-serif; fill: #fff; }
        .link { fill: none; stroke: #555; stroke-width: 1.5px; }
        .controls { margin-top: 20px; }
        button { padding: 10px 20px; font-size: 16px; margin: 5px; cursor: pointer; background: #444; color: white; border: none; border-radius: 4px; }
        button:hover { background: #555; }
        .info { margin-top: 20px; font-size: 14px; color: #aaa; }
        .size-tag { fill: #4CAF50; font-size: 10px; }
    </style>
</head>
<body>
    <h2>Composite Pattern: File System Explorer</h2>
    <p>Uniformly treating Folders (Composites) and Files (Leaves).</p>
    
    <div id="canvas"></div>
    <div class="info" id="status">Total Size: calculation pending...</div>
    
    <div class="controls">
        <button onclick="addFile()">+ Add Random File</button>
        <button onclick="calculateSize()">Recursive Size()</button>
        <button onclick="reset()">Reset</button>
    </div>

    <script>
        const width = 600, height = 400;
        const svg = d3.select("#canvas").append("svg").attr("width", width).attr("height", height);
        
        let root = {
            name: "Root",
            type: "folder",
            children: [
                { name: "src", type: "folder", children: [
                    { name: "Main.java", type: "file", size: 50 },
                    { name: "Utils.java", type: "file", size: 30 }
                ]},
                { name: "resources", type: "folder", children: [
                    { name: "config.xml", type: "file", size: 120 }
                ]},
                { name: "README.md", type: "file", size: 10 }
            ]
        };

        let i = 0;
        const tree = d3.tree().size([height, width - 150]);
        let rootNode;

        function update() {
            rootNode = d3.hierarchy(root);
            tree(rootNode);

            // Links
            const links = svg.selectAll(".link").data(rootNode.links());
            links.enter().append("path").attr("class", "link")
                .merge(links)
                .attr("d", d3.linkHorizontal().x(d => d.y).y(d => d.x));
            links.exit().remove();

            // Nodes
            const nodes = svg.selectAll(".node").data(rootNode.descendants());
            const nodeEnter = nodes.enter().append("g")
                .attr("class", "node")
                .attr("transform", d => `translate(${d.y},${d.x})`);

            nodeEnter.append("circle")
                .attr("r", 10)
                .attr("fill", d => d.data.type === 'folder' ? "#2196F3" : "#FFF") // Blue for Folder, White for File
                .on("click", (event, d) => {
                    if(d.data.type === 'folder') {
                        // Demo: Could expand/collapse
                        alert("Folder: " + d.data.name);
                    } else {
                        alert("File: " + d.data.name + " (" + d.data.size + "KB)");
                    }
                });

            nodeEnter.append("text")
                .attr("dy", -15)
                .attr("x", 0)
                .style("text-anchor", "middle")
                .text(d => d.data.name);

            nodeEnter.append("text")
                .attr("class", "size-label")
                .attr("dy", 3)
                .attr("dx", 0)
                .style("text-anchor", "middle")
                .style("font-size", "8px")
                .style("fill", "#000")
                .text(d => d.data.type === 'folder' ? "D" : "F");

            nodes.merge(nodeEnter).transition().duration(500)
                .attr("transform", d => `translate(${d.y},${d.x})`);
            
            nodes.exit().remove();
        }

        function addFile() {
             // Add a file to a random folder
             const findFolders = (node) => {
                 let folders = [];
                 if (node.type === 'folder') {
                     folders.push(node);
                     if (node.children) node.children.forEach(c => folders = folders.concat(findFolders(c)));
                 }
                 return folders;
             };
             
             const folders = findFolders(root);
             const randomFolder = folders[Math.floor(Math.random() * folders.length)];
             
             if (!randomFolder.children) randomFolder.children = [];
             randomFolder.children.push({
                 name: `NewFile${Math.floor(Math.random()*100)}.txt`,
                 type: "file",
                 size: Math.floor(Math.random() * 100)
             });
             update();
             d3.select("#status").text("File added. Click 'Recursive Size' to update total.");
        }

        // The Logic of Composite Pattern: Treat leaf and composite uniformly via .getSize()
        function calculateSize() {
            
            function getSize(node) {
                // Highlight scan
                // Visualization of recursion could happen here
                if (node.type === 'file') return node.size;
                if (node.type === 'folder') {
                    if (!node.children) return 0;
                    return node.children.reduce((sum, child) => sum + getSize(child), 0);
                }
                return 0;
            }

            const total = getSize(root);
            d3.select("#status").html(`Calculated Total Size: <b style='color:#4CAF50'>${total} KB</b> (via uniform recursion)`);
            
            // Visual Flash
            svg.selectAll("circle").transition().duration(200).attr("r", 15).transition().duration(200).attr("r", 10);
        }

        function reset() {
            root = {
                name: "Root",
                type: "folder",
                children: [
                    { name: "src", type: "folder", children: [
                         { name: "Main.java", type: "file", size: 50 }
                    ]}
                ]
            };
            update();
            d3.select("#status").text("");
        }

        update();
    </script>
</body>
</html>
"""

with open("composite_files.html", "w") as f:
    f.write(html_content)
print("✅ Generated composite_files.html")
