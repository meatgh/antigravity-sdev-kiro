import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Template Method: ETL Pipeline</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        body { font-family: 'Inter', sans-serif; background-color: #f4f6f8; text-align: center; }
        .pipeline { display: flex; justify-content: space-around; align-items: center; background: white; padding: 40px; border-radius: 12px; margin: 20px auto; width: 800px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); position: relative; }
        .step { width: 120px; height: 80px; display: flex; align-items: center; justify-content: center; background: #e0e0e0; border-radius: 8px; font-weight: bold; position: relative; z-index: 1; border: 2px solid #ccc; transition: all 0.3s; }
        .step.active { border-color: #2196F3; background: #E3F2FD; transform: scale(1.1); box-shadow: 0 0 10px rgba(33, 150, 243, 0.5); }
        .connector { height: 4px; background: #ddd; flex-grow: 1; margin: 0 10px; }
        .packet { position: absolute; width: 30px; height: 30px; background: #FF9800; border-radius: 50%; opacity: 0; z-index: 2; display: flex; align-items: center; justify-content: center; font-size: 12px; color: white; }
        .log { margin-top: 20px; font-family: monospace; color: #555; height: 80px; overflow-y: auto; background: #fff; border: 1px solid #eee; padding: 10px; width: 600px; margin-left: auto; margin-right: auto; text-align: left; }
        .controls { margin-top: 20px; }
        button { padding: 10px 20px; font-size: 16px; margin: 5px; cursor: pointer; border: none; border-radius: 5px; color: white; background: #4CAF50; transition: background 0.2s; }
        button:disabled { background: #ccc; cursor: not-allowed; }
        
        /* Specific Styles for Concrete Steps */
        .csv-mode .step-extract { border-color: #F44336; color: #D32F2F; } /* CSV Specific */
        .json-mode .step-extract { border-color: #9C27B0; color: #7B1FA2; } /* JSON Specific */
    </style>
</head>
<body>
    <h2>🏭 Template Method: The ETL Pipeline</h2>
    <p>The <b>Skeleton</b> (Extract -> Transform -> Load) is fixed. Subclasses override specific steps.</p>
    
    <div class="controls">
        <label>Select Concrete Implementation:</label>
        <select id="implSelector" onchange="resetPipeline()">
            <option value="csv">CSVDataMiner (Reads .csv, Simple Transform)</option>
            <option value="pdf">PDFDataMiner (Reads .pdf, OCR Transform)</option>
        </select>
        <button id="runBtn" onclick="runPipeline()">▶️ Run Algorithm</button>
    </div>

    <div class="pipeline" id="pipelineBox">
        <div id="step1" class="step step-extract">1. EXTRACT<br><small>(Abstract)</small></div>
        <div class="connector"></div>
        <div id="step2" class="step">2. TRANSFORM<br><small>(Abstract)</small></div>
        <div class="connector"></div>
        <div id="step3" class="step">3. LOAD<br><small>(Fixed/Hook)</small></div>
    </div>
    
    <div id="log" class="log">Ready to process...</div>

    <script>
        const log = document.getElementById("log");
        const pipelineBox = document.getElementById("pipelineBox");
        
        function logMsg(msg) {
            log.innerHTML += `<div>${msg}</div>`;
            log.scrollTop = log.scrollHeight;
        }

        function resetPipeline() {
            log.innerHTML = "Ready to process...";
            const mode = document.getElementById("implSelector").value;
            pipelineBox.className = "pipeline " + mode + "-mode";
            
            // Update labels based on selection
            if(mode === 'csv') {
                document.getElementById('step1').innerHTML = "1. READ CSV<br><small>(Override)</small>";
                document.getElementById('step2').innerHTML = "2. PARSE TEXT<br><small>(Override)</small>";
            } else {
                document.getElementById('step1').innerHTML = "1. OCR SCAN<br><small>(Override)</small>";
                document.getElementById('step2').innerHTML = "2. IMG PROCESSING<br><small>(Override)</small>";
            }
        }

        async function runPipeline() {
            document.getElementById("runBtn").disabled = true;
            resetPipeline();
            logMsg(">>> STARTING TEMPLATE METHOD `mine()` <<<");
            
            // Step 1: Extract
            await executeStep("step1", "Extracting Raw Data...", 1000);
            
            // Step 2: Transform
            await executeStep("step2", "Transforming/Cleaning Data...", 1000);
            
            // Step 3: Load (Common)
            await executeStep("step3", "Loading into Data Warehouse (Common Logic)...", 1000);
            
            logMsg(">>> TEMPLATE METHOD COMPLETE <<<");
            document.getElementById("runBtn").disabled = false;
        }

        function executeStep(id, message, duration) {
            return new Promise(resolve => {
                const el = document.getElementById(id);
                el.classList.add("active");
                logMsg(message);
                
                // Create packet animation
                const packet = document.createElement("div");
                packet.className = "packet";
                packet.innerHTML = "📦";
                const startRect = el.getBoundingClientRect();
                const containerRect = pipelineBox.getBoundingClientRect();
                
                packet.style.left = (startRect.left - containerRect.left + 40) + "px";
                packet.style.top = (startRect.top - containerRect.top + 25) + "px";
                pipelineBox.appendChild(packet);
                
                // Animate packet
                packet.style.opacity = 1;
                /* packet animation would go here but simple CSS scale is enough for step highlight */
                
                setTimeout(() => {
                    el.classList.remove("active");
                    packet.remove();
                    resolve();
                }, duration);
            });
        }
        
        resetPipeline(); // init
    </script>
</body>
</html>
"""

with open("template_etl.html", "w") as f:
    f.write(html_content)
print("✅ Generated template_etl.html")
