import json

# Define the HTML template
html_start = """<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>UnBoundX | 自由维度 - Logo Concepts</title>
<style>
  :root {
    --accent: oklch(65% 0.25 35);
    --ink: oklch(25% 0.01 260);
    --paper: oklch(98% 0.005 90);
  }
  
  body {
    margin: 0;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    background-color: var(--paper);
    color: var(--ink);
  }
  
  header {
    background-color: var(--ink);
    color: var(--paper);
    padding: 60px 20px 40px;
    text-align: center;
  }
  
  header h1 {
    font-size: 3.5rem;
    margin: 0 0 10px 0;
    font-weight: 800;
    letter-spacing: -2px;
  }
  header h1 span {
    color: var(--accent);
  }
  header p {
    font-size: 1.2rem;
    opacity: 0.8;
    max-width: 600px;
    margin: 0 auto;
    font-weight: 300;
  }

  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
    gap: 30px;
    padding: 60px;
    max-width: 1600px;
    margin: 0 auto;
  }

  .card {
    background: var(--paper);
    border: 1px solid rgba(0,0,0,0.05);
    border-radius: 16px;
    overflow: hidden;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    box-shadow: 0 10px 30px rgba(0,0,0,0.03);
  }
  
  .card:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.08);
  }
  
  .card-dark {
    background: var(--ink);
    border-color: rgba(255,255,255,0.05);
    color: var(--paper);
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
  }
  
  .card-header {
    padding: 20px 24px;
    border-bottom: 1px solid rgba(0,0,0,0.05);
    font-size: 0.9rem;
    font-weight: 600;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .card-dark .card-header {
    border-bottom-color: rgba(255,255,255,0.1);
  }
  
  .concept-tag {
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    padding: 4px 10px;
    border-radius: 20px;
    background: rgba(0,0,0,0.05);
  }
  .card-dark .concept-tag {
    background: rgba(255,255,255,0.1);
  }
  
  .logo-container {
    padding: 60px 40px;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 140px;
  }
  
  svg {
    width: 100%;
    max-width: 260px;
    height: auto;
  }

  .palette {
    display: flex;
    justify-content: center;
    gap: 30px;
    margin-top: 40px;
  }
  .color-swatch {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
  }
  .color-circle {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
  }
  .color-label {
    font-size: 0.8rem;
    font-weight: 600;
  }
  .color-value {
    font-size: 0.7rem;
    opacity: 0.7;
    font-family: monospace;
  }
</style>
</head>
<body>

<header>
  <h1>UnBound<span>X</span></h1>
  <p>自由维度 | Brand Identity Concepts</p>
  
  <div class="palette">
    <div class="color-swatch">
      <div class="color-circle" style="background: var(--accent);"></div>
      <div class="color-label">Lava Orange</div>
      <div class="color-value">oklch(65% 0.25 35)</div>
    </div>
    <div class="color-swatch">
      <div class="color-circle" style="background: var(--ink); border: 2px solid rgba(255,255,255,0.1);"></div>
      <div class="color-label">Ink</div>
      <div class="color-value">oklch(25% 0.01 260)</div>
    </div>
    <div class="color-swatch">
      <div class="color-circle" style="background: var(--paper);"></div>
      <div class="color-label">Paper</div>
      <div class="color-value">oklch(98% 0.005 90)</div>
    </div>
  </div>
</header>

<div class="grid">
"""

html_end = """
</div>
</body>
</html>
"""

def generate_svg(id, concept, theme, is_dark, icon_svg):
    card_class = "card card-dark" if is_dark else "card"
    text_color = "var(--paper)" if is_dark else "var(--ink)"
    subtext_color = "rgba(255,255,255,0.6)" if is_dark else "rgba(0,0,0,0.5)"
    
    return f'''
  <div class="{card_class}">
    <div class="card-header">
      <span>{id:02d}. {concept}</span>
      <span class="concept-tag">{theme}</span>
    </div>
    <div class="logo-container">
      <svg viewBox="0 0 300 80" xmlns="http://www.w3.org/2000/svg">
        <g transform="translate(10, 15)">
          {icon_svg}
        </g>
        <g transform="translate(75, 40)">
          <text x="0" y="0" font-family="-apple-system, sans-serif" font-weight="800" font-size="28" fill="{text_color}" letter-spacing="-0.5">UnBound<tspan fill="var(--accent)">X</tspan></text>
          <text x="2" y="20" font-family="-apple-system, sans-serif" font-weight="500" font-size="12" fill="{subtext_color}" letter-spacing="4.5">自由维度</text>
        </g>
      </svg>
    </div>
  </div>
'''

# We will define 20 different icons.
# They fit inside a 50x50 bounding box at (0,0) -> (50,50)
logos = [
    # 01 - The Cube Break
    {
        "concept": "Dimension Break",
        "theme": "Geometric",
        "dark": True,
        "icon": '<polygon points="25,0 50,15 50,45 25,30" fill="var(--paper)" opacity="0.8"/><polygon points="0,15 25,30 25,60 0,45" fill="var(--paper)" opacity="0.4"/><polygon points="0,15 25,0 50,15 25,30" fill="var(--accent)" transform="translate(0, -5)"/>'
    },
    # 02 - Infinity Flow
    {
        "concept": "Infinity Flow",
        "theme": "Abstract",
        "dark": False,
        "icon": '<path d="M10,25 C10,10 25,10 35,25 C45,40 60,40 60,25 C60,10 45,10 35,25" fill="none" stroke="var(--ink)" stroke-width="6" stroke-linecap="round"/><circle cx="48" cy="18" r="5" fill="var(--accent)"/>'
    },
    # 03 - The X Portal
    {
        "concept": "X Portal",
        "theme": "Modern",
        "dark": True,
        "icon": '<path d="M5,5 L45,45 M45,5 L5,45" stroke="var(--paper)" stroke-width="8" stroke-linecap="square"/><rect x="20" y="20" width="10" height="10" fill="var(--accent)"/>'
    },
    # 04 - Orbit Nodes
    {
        "concept": "Stellar Orbit",
        "theme": "Tech",
        "dark": False,
        "icon": '<ellipse cx="25" cy="25" rx="25" ry="10" fill="none" stroke="var(--ink)" stroke-width="3" transform="rotate(45 25 25)"/><ellipse cx="25" cy="25" rx="25" ry="10" fill="none" stroke="var(--ink)" stroke-width="3" transform="rotate(-45 25 25)"/><circle cx="25" cy="25" r="6" fill="var(--accent)"/>'
    },
    # 05 - Origami Space
    {
        "concept": "Origami Space",
        "theme": "Minimal",
        "dark": True,
        "icon": '<path d="M10,5 L10,35 C10,45 40,45 40,35 L40,5" fill="none" stroke="var(--paper)" stroke-width="6"/><path d="M10,5 L40,35 M40,5 L10,35" stroke="var(--accent)" stroke-width="4" opacity="0.9"/>'
    },
    # 06 - Neon Pulse
    {
        "concept": "Neon Pulse",
        "theme": "Dynamic",
        "dark": False,
        "icon": '<path d="M0,25 L15,25 L25,5 L35,45 L45,25 L60,25" fill="none" stroke="var(--ink)" stroke-width="4" stroke-linejoin="round"/><circle cx="35" cy="45" r="4" fill="var(--accent)"/>'
    },
    # 07 - Grid Spark
    {
        "concept": "Grid Spark",
        "theme": "Digital",
        "dark": True,
        "icon": '<rect x="5" y="5" width="10" height="10" fill="var(--paper)"/><rect x="20" y="5" width="10" height="10" fill="var(--paper)"/><rect x="35" y="5" width="10" height="10" fill="var(--accent)"/><rect x="5" y="20" width="10" height="10" fill="var(--paper)"/><rect x="20" y="20" width="10" height="10" fill="var(--paper)"/><rect x="35" y="20" width="10" height="10" fill="var(--paper)"/><rect x="5" y="35" width="10" height="10" fill="var(--paper)"/><rect x="20" y="35" width="10" height="10" fill="var(--paper)"/><rect x="35" y="35" width="10" height="10" fill="var(--paper)"/>'
    },
    # 08 - Zenith Arrow
    {
        "concept": "Zenith Arrow",
        "theme": "Motion",
        "dark": False,
        "icon": '<path d="M10,40 L25,20 L40,40" fill="none" stroke="var(--ink)" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/><path d="M10,25 L25,5 L40,25" fill="none" stroke="var(--accent)" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'
    },
    # 09 - Quantum Core
    {
        "concept": "Quantum Core",
        "theme": "Science",
        "dark": True,
        "icon": '<circle cx="25" cy="25" r="20" fill="none" stroke="var(--paper)" stroke-width="2" stroke-dasharray="4 4"/><circle cx="25" cy="25" r="12" fill="none" stroke="var(--paper)" stroke-width="4"/><circle cx="25" cy="25" r="6" fill="var(--accent)"/>'
    },
    # 10 - Minimal X
    {
        "concept": "Minimalist X",
        "theme": "Typographic",
        "dark": False,
        "icon": '<path d="M15,10 L35,40" stroke="var(--ink)" stroke-width="8" stroke-linecap="round"/><path d="M35,10 L15,40" stroke="var(--accent)" stroke-width="8" stroke-linecap="round"/>'
    },
    # 11 - Tesseract
    {
        "concept": "Tesseract",
        "theme": "Geometric",
        "dark": True,
        "icon": '<rect x="10" y="10" width="20" height="20" fill="none" stroke="var(--paper)" stroke-width="2"/><rect x="20" y="20" width="20" height="20" fill="none" stroke="var(--accent)" stroke-width="2"/><line x1="10" y1="10" x2="20" y2="20" stroke="var(--paper)" stroke-width="2"/><line x1="30" y1="10" x2="40" y2="20" stroke="var(--paper)" stroke-width="2"/><line x1="10" y1="30" x2="20" y2="40" stroke="var(--paper)" stroke-width="2"/><line x1="30" y1="30" x2="40" y2="40" stroke="var(--paper)" stroke-width="2"/>'
    },
    # 12 - Aurora Wave
    {
        "concept": "Aurora Wave",
        "theme": "Organic",
        "dark": False,
        "icon": '<path d="M0,25 Q15,5 25,25 T50,25" fill="none" stroke="var(--ink)" stroke-width="5" stroke-linecap="round"/><path d="M0,35 Q15,15 25,35 T50,35" fill="none" stroke="var(--accent)" stroke-width="5" stroke-linecap="round"/>'
    },
    # 13 - Pixel Ascend
    {
        "concept": "Pixel Ascend",
        "theme": "Data",
        "dark": True,
        "icon": '<rect x="5" y="30" width="10" height="15" fill="var(--paper)"/><rect x="20" y="15" width="10" height="30" fill="var(--paper)"/><rect x="35" y="0" width="10" height="45" fill="var(--accent)"/>'
    },
    # 14 - Horizon
    {
        "concept": "Horizon X",
        "theme": "Vision",
        "dark": False,
        "icon": '<path d="M5,25 L45,25" stroke="var(--ink)" stroke-width="4" stroke-linecap="round"/><path d="M15,25 A10,10 0 0,1 35,25" fill="none" stroke="var(--accent)" stroke-width="4"/><path d="M20,15 L30,35 M30,15 L20,35" stroke="var(--ink)" stroke-width="3" stroke-linecap="round"/>'
    },
    # 15 - Data Construct
    {
        "concept": "Data Construct",
        "theme": "Structural",
        "dark": True,
        "icon": '<polygon points="25,5 45,40 5,40" fill="none" stroke="var(--paper)" stroke-width="3"/><polygon points="25,15 35,35 15,35" fill="var(--accent)"/>'
    },
    # 16 - Lens Flare
    {
        "concept": "Lens Flare",
        "theme": "Space",
        "dark": False,
        "icon": '<path d="M25,0 Q25,25 50,25 Q25,25 25,50 Q25,25 0,25 Q25,25 25,0 Z" fill="var(--ink)"/><circle cx="25" cy="25" r="6" fill="var(--accent)"/>'
    },
    # 17 - Code Bracket
    {
        "concept": "Code Bracket",
        "theme": "Developer",
        "dark": True,
        "icon": '<path d="M15,10 L5,25 L15,40" fill="none" stroke="var(--paper)" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/><path d="M35,10 L45,25 L35,40" fill="none" stroke="var(--accent)" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
    },
    # 18 - Lava Flow
    {
        "concept": "Lava Flow",
        "theme": "Fluid",
        "dark": False,
        "icon": '<path d="M25,5 C40,5 45,20 35,35 C25,50 10,40 10,25 C10,10 15,5 25,5 Z" fill="var(--accent)" opacity="0.8"/><path d="M25,10 C35,10 35,20 30,30 C20,40 15,30 15,20 C15,10 20,10 25,10 Z" fill="var(--ink)"/>'
    },
    # 19 - Architect
    {
        "concept": "Architect",
        "theme": "Blueprint",
        "dark": True,
        "icon": '<circle cx="25" cy="25" r="20" fill="none" stroke="var(--paper)" stroke-width="1"/><line x1="5" y1="25" x2="45" y2="25" stroke="var(--paper)" stroke-width="1"/><line x1="25" y1="5" x2="25" y2="45" stroke="var(--paper)" stroke-width="1"/><path d="M15,15 L35,35 M35,15 L15,35" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/>'
    },
    # 20 - U Monogram
    {
        "concept": "U Monogram",
        "theme": "Classic",
        "dark": False,
        "icon": '<path d="M10,10 L10,30 C10,40 40,40 40,30 L40,10" fill="none" stroke="var(--ink)" stroke-width="8" stroke-linecap="square"/><rect x="36" y="26" width="12" height="12" fill="var(--accent)" rx="2"/>'
    }
]

with open('/Users/jackiexiao/code/temp/temp/unboundx-logos.html', 'w', encoding='utf-8') as f:
    f.write(html_start)
    for i, logo in enumerate(logos):
        f.write(generate_svg(i+1, logo['concept'], logo['theme'], logo['dark'], logo['icon']))
    f.write(html_end)

print("HTML generated successfully.")
