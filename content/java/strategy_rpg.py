import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Strategy Pattern: The Battle Arena</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        body { font-family: 'Inter', sans-serif; background-color: #f4f6f8; text-align: center; }
        #arena { background: white; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin: 20px auto; width: 600px; height: 300px; position: relative; display: flex; align-items: center; justify-content: space-between; padding: 0 100px; overflow: hidden; }
        .character { font-size: 60px; transition: all 0.3s; z-index: 2; }
        .controls { margin-top: 20px; }
        button { padding: 10px 20px; font-size: 16px; margin: 5px; cursor: pointer; border: none; border-radius: 5px; color: white; transition: background 0.2s; }
        .btn-melee { background-color: #D32F2F; }
        .btn-ranged { background-color: #388E3C; }
        .btn-magic { background-color: #7B1FA2; }
        .projectile { position: absolute; font-size: 30px; }
        .log { margin-top: 20px; font-family: monospace; color: #555; }
    </style>
</head>
<body>
    <h2>♟️ Strategy Pattern: Dynamic Behavior</h2>
    <p>The Context (Hero) delegates the algorithm to the Strategy (Weapon).</p>
    
    <div id="arena">
        <div id="hero" class="character">🦸</div>
        <div id="enemy" class="character">👹</div>
    </div>

    <div class="controls">
        <p>Select Strategy:</p>
        <button class="btn-melee" onclick="setStrategy('melee')">⚔️ SwordStrategy</button>
        <button class="btn-ranged" onclick="setStrategy('ranged')">🏹 BowStrategy</button>
        <button class="btn-magic" onclick="setStrategy('magic')">🔥 MagicStrategy</button>
    </div>
    
    <button onclick="executeStrategy()" style="background-color: #2196F3; font-size: 18px; margin-top: 20px;">▶️ Hero.attack()</button>

    <div id="log" class="log">Strategy: None selected</div>

    <script>
        let currentStrategy = null;
        const hero = document.getElementById("hero");
        const enemy = document.getElementById("enemy");
        const log = document.getElementById("log");

        function setStrategy(type) {
            currentStrategy = type;
            log.innerText = "Strategy set to: " + type.toUpperCase() + "_STRATEGY";
            // Visual feedback of change
            hero.style.transform = "scale(1.1)";
            setTimeout(() => hero.style.transform = "scale(1)", 200);
        }

        function executeStrategy() {
            if (!currentStrategy) {
                log.innerText = "⚠️ No Strategy selected! (NullPointerException or Default)";
                return;
            }

            log.innerText = "Executing: " + currentStrategy.toUpperCase() + "...";

            if (currentStrategy === 'melee') {
                // Melee Animation: Move forward and whack
                hero.style.transform = "translateX(300px)";
                setTimeout(() => {
                    enemy.style.transform = "rotate(20deg)";
                    setTimeout(() => {
                        hero.style.transform = "translateX(0px)";
                        enemy.style.transform = "rotate(0deg)";
                    }, 300);
                }, 200);
            } 
            else if (currentStrategy === 'ranged') {
                // Ranged Animation: Fire projectile
                const arrow = document.createElement("div");
                arrow.innerHTML = "🏹";
                arrow.className = "projectile";
                arrow.style.left = "150px";
                arrow.style.top = "120px";
                document.getElementById("arena").appendChild(arrow);
                
                // Animate
                let pos = 150;
                const interval = setInterval(() => {
                    pos += 15;
                    arrow.style.left = pos + "px";
                    if (pos > 500) {
                        clearInterval(interval);
                        arrow.remove();
                        enemy.style.transform = "scale(0.8)";
                        setTimeout(() => enemy.style.transform = "scale(1)", 200);
                    }
                }, 20);
            }
            else if (currentStrategy === 'magic') {
                // Magic Animation: Big explosion on enemy
                const fire = document.createElement("div");
                fire.innerHTML = "💥";
                fire.className = "projectile";
                fire.style.left = "500px";
                fire.style.top = "100px";
                fire.style.fontSize = "80px";
                document.getElementById("arena").appendChild(fire);
                
                setTimeout(() => {
                    fire.remove();
                    enemy.innerHTML = "💀";
                    setTimeout(() => enemy.innerHTML = "👹", 1000);
                }, 500);
            }
        }
    </script>
</body>
</html>
"""

with open("strategy_rpg.html", "w") as f:
    f.write(html_content)
print("✅ Generated strategy_rpg.html")
