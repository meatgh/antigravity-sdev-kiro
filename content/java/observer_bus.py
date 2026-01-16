import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Observer Pattern: Event Bus</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        body { font-family: 'Inter', sans-serif; background-color: #f4f6f8; text-align: center; }
        .system { display: flex; flex-direction: column; align-items: center; justify-content: center; height: 500px; position: relative; }
        .subject { width: 120px; height: 120px; border-radius: 50%; background: #2196F3; color: white; display: flex; align-items: center; justify-content: center; font-weight: bold; box-shadow: 0 0 20px rgba(33, 150, 243, 0.5); z-index: 10; cursor: pointer; transition: transform 0.2s; }
        .subject:active { transform: scale(0.95); }
        .observer { width: 80px; height: 80px; border-radius: 12px; background: #fff; border: 2px solid #ccc; display: flex; align-items: center; justify-content: center; font-size: 12px; position: absolute; transition: all 0.5s; font-weight: bold; color: #555; }
        .observer.notified { background: #4CAF50; color: white; border-color: #4CAF50; transform: scale(1.1); box-shadow: 0 0 15px rgba(76, 175, 80, 0.6); }
        .signal { position: absolute; width: 10px; height: 10px; background: #FFC107; border-radius: 50%; display: none; z-index: 5; }
        
        .controls { margin-top: 20px; }
        button { padding: 8px 16px; margin: 5px; cursor: pointer; border-radius: 4px; border: none; background: #333; color: white; }
        button.add { background: #4CAF50; }
        button.remove { background: #F44336; }
        button.trigger { background: #2196F3; font-weight: bold; font-size: 1.1em; }
    </style>
</head>
<body>
    <h2>📡 Observer Pattern: The Event Bus</h2>
    <p>The <b>Subject</b> (Center) broadcasts updates. <b>Observers</b> (Satellites) react.</p>
    
    <div class="controls">
        <button class="add" onclick="addObserver()">+ Add Observer</button>
        <button class="remove" onclick="removeObserver()">- Remove Observer</button>
        <button class="trigger" onclick="notifyObservers()">📢 TRIGGER EVENT</button>
    </div>

    <div class="system" id="systemBox">
        <div class="subject" onclick="notifyObservers()">SUBJECT<br>(Click Me)</div>
    </div>

    <script>
        const systemBox = document.getElementById("systemBox");
        const observers = [];
        const radius = 180;
        
        function updateLayout() {
            const centerX = systemBox.offsetWidth / 2;
            const centerY = systemBox.offsetHeight / 2;
            const angleStep = (2 * Math.PI) / observers.length;
            
            observers.forEach((obs, index) => {
                const angle = index * angleStep;
                const x = centerX + radius * Math.cos(angle) - 40; // -40 for centering (width/2)
                const y = centerY + radius * Math.sin(angle) - 40;
                
                obs.style.left = x + "px";
                obs.style.top = y + "px";
            });
        }

        function addObserver() {
            if (observers.length >= 8) return;
            const obs = document.createElement("div");
            obs.className = "observer";
            obs.innerText = "Observer " + (observers.length + 1);
            systemBox.appendChild(obs);
            observers.push(obs);
            updateLayout();
        }

        function removeObserver() {
            if (observers.length === 0) return;
            const obs = observers.pop();
            obs.remove();
            updateLayout();
        }

        function notifyObservers() {
            if (observers.length === 0) return;
            
            // Visual Pulse
            const subject = document.querySelector(".subject");
            subject.style.transform = "scale(1.1)";
            setTimeout(() => subject.style.transform = "scale(1)", 200);

            // Send Signals
            const centerX = systemBox.offsetWidth / 2;
            const centerY = systemBox.offsetHeight / 2;

            observers.forEach(obs => {
                const signal = document.createElement("div");
                signal.className = "signal";
                signal.style.display = "block";
                signal.style.left = (centerX - 5) + "px";
                signal.style.top = (centerY - 5) + "px";
                systemBox.appendChild(signal);
                
                // Animate Signal to Observer
                const obsRect = obs.getBoundingClientRect();
                const containerRect = systemBox.getBoundingClientRect();
                const targetX = obsRect.left - containerRect.left + 35;
                const targetY = obsRect.top - containerRect.top + 35;
                
                const anim = signal.animate([
                    { left: (centerX - 5) + "px", top: (centerY - 5) + "px" },
                    { left: targetX + "px", top: targetY + "px" }
                ], { duration: 600, easing: 'ease-out' });
                
                anim.onfinish = () => {
                    signal.remove();
                    obs.classList.add("notified");
                    obs.innerText = "NOTIFIED!";
                    setTimeout(() => {
                        obs.classList.remove("notified");
                        obs.innerText = "Observer " + (observers.indexOf(obs) + 1);
                    }, 1000);
                };
            });
        }
        
        // Init
        addObserver();
        addObserver();
        addObserver();
    </script>
</body>
</html>
"""

with open("observer_bus.html", "w") as f:
    f.write(html_content)
print("✅ Generated observer_bus.html")
