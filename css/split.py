import os

style_path = r"c:\beta pagnico\surinox\css\style.css"
with open(style_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

def get_lines(ranges):
    out = []
    for start, end in ranges:
        out.extend(lines[start-1:end])
    return "".join(out)

global_css = get_lines([(1, 215), (411, 589), (844, 854)])
home_css = get_lines([(216, 410), (640, 657), (855, 941), (1093, 1114)])
productos_css = get_lines([(658, 804), (942, 1092)])
empresa_css = get_lines([(590, 639)])
faq_css = get_lines([(805, 843)])

# Manual appending to avoid issues with new lines
global_css += "\n\n/* Responsive Design */\n@media (max-width: 992px) {\n    .nav-menu { gap: 1rem; }\n}\n\n@media (max-width: 768px) {\n    .mobile-toggle {\n        display: block;\n    }\n    \n    .nav-menu {\n        position: absolute;\n        top: 100%;\n        left: 0;\n        width: 100%;\n        background-color: var(--white);\n        flex-direction: column;\n        padding: 2rem 0;\n        box-shadow: 0 10px 10px rgba(0,0,0,0.05);\n        clip-path: polygon(0 0, 100% 0, 100% 0, 0 0); /* Hidden */\n        transition: clip-path 0.4s ease-in-out;\n        gap: 0;\n    }\n    \n    .nav-menu.active {\n        clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%); /* Visible */\n    }\n    \n    .nav-link {\n        display: block;\n        padding: 1rem 5%;\n        width: 100%;\n        text-align: center;\n        border-bottom: 1px solid #f0f0f0;\n    }\n    \n    .header .btn-outline {\n        display: none; /* Hide on mobile to simplify header */\n    }\n}\n\n@media (max-width: 480px) {\n    .section-title { font-size: 2rem; }\n    .section-padding { padding: 4rem 0; }\n}\n"

home_css += "\n\n/* Responsive Design for Home */\n@media (max-width: 992px) {\n    .hero-content .title { font-size: 3rem; }\n}\n\n@media (max-width: 768px) {\n    .hero-content .title { font-size: 2.5rem; }\n    \n    .split-layout {\n        flex-direction: column;\n        gap: 2rem;\n        text-align: center;\n    }\n    \n    .split-text {\n        text-align: center !important;\n    }\n    \n    .split-text .section-desc {\n        text-align: center !important;\n    }\n\n    .split-text .separator {\n        margin: 0 auto 1.5rem auto !important;\n    }\n    \n    .split-text .check-list {\n        text-align: left;\n        display: inline-block;\n    }\n    \n    .hero-buttons {\n        flex-wrap: wrap;\n    }\n    \n    .hero-diagonal {\n        clip-path: polygon(0 0, 100% 0, 100% calc(100% - 5vw), 0 100%);\n        padding-bottom: 10vw;\n    }\n    \n    .diagonal-up {\n        clip-path: polygon(0 5vw, 100% 0, 100% 100%, 0 100%);\n        padding-top: calc(4rem + 5vw);\n        margin-top: -5vw;\n    }\n}\n\n@media (max-width: 480px) {\n    .hero-content .title { font-size: 2rem; }\n    .hero-content .description { font-size: 1rem; }\n    .grid-productos { grid-template-columns: 1fr; }\n}\n"

productos_css += "\n\n/* Responsive Design for Productos */\n@media (max-width: 480px) {\n    .apple-card h3 {\n        font-size: 2rem;\n    }\n    \n    .apple-card p.intro {\n        font-size: 1rem;\n    }\n    \n    .apple-specs-grid {\n        flex-direction: column;\n        gap: 2rem;\n    }\n}\n"

base_dir = r"c:\beta pagnico\surinox\css"
with open(os.path.join(base_dir, "global.css"), "w", encoding="utf-8") as f: f.write(global_css)
with open(os.path.join(base_dir, "home.css"), "w", encoding="utf-8") as f: f.write(home_css)
with open(os.path.join(base_dir, "productos.css"), "w", encoding="utf-8") as f: f.write(productos_css)
with open(os.path.join(base_dir, "empresa.css"), "w", encoding="utf-8") as f: f.write(empresa_css)
with open(os.path.join(base_dir, "faq.css"), "w", encoding="utf-8") as f: f.write(faq_css)

print("Split completed successfully.")
