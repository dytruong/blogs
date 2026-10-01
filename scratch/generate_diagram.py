import json

def make_rect(id_name, x, y, width, height, text="", bg_color="#dbeafe", stroke_color="#1e40af", fill_style="solid", text_color="#1e293b", font_size=15):
    rect = {
        "id": id_name,
        "type": "rectangle",
        "x": x,
        "y": y,
        "width": width,
        "height": height,
        "angle": 0,
        "strokeColor": stroke_color,
        "backgroundColor": bg_color,
        "fillStyle": fill_style,
        "strokeWidth": 2,
        "strokeStyle": "solid",
        "roughness": 1,
        "opacity": 100,
        "groupIds": [],
        "roundness": {"type": 3},
        "seed": 1042,
        "version": 1,
        "versionNonce": 1,
        "isDeleted": False,
        "boundElements": []
    }
    elements = [rect]
    if text:
        text_id = f"text_{id_name}"
        text_el = {
            "id": text_id,
            "type": "text",
            "x": x + 14,
            "y": y + (height / 2) - (font_size * len(text.splitlines()) * 0.7),
            "width": width - 28,
            "height": font_size * 1.4 * len(text.splitlines()),
            "angle": 0,
            "strokeColor": text_color,
            "backgroundColor": "transparent",
            "fillStyle": "solid",
            "strokeWidth": 1,
            "strokeStyle": "solid",
            "roughness": 0,
            "opacity": 100,
            "groupIds": [],
            "seed": 2042,
            "version": 1,
            "versionNonce": 1,
            "isDeleted": False,
            "text": text,
            "fontSize": font_size,
            "fontFamily": 3,
            "textAlign": "center",
            "verticalAlign": "middle",
            "baseline": 14,
            "containerId": id_name,
            "originalText": text
        }
        rect["boundElements"].append({"id": text_id, "type": "text"})
        elements.append(text_el)
    return elements

def make_arrow(id_name, start_x, start_y, end_x, end_y, stroke_color="#1e3a5f"):
    return {
        "id": id_name,
        "type": "arrow",
        "x": start_x,
        "y": start_y,
        "width": end_x - start_x,
        "height": end_y - start_y,
        "angle": 0,
        "strokeColor": stroke_color,
        "backgroundColor": "transparent",
        "fillStyle": "solid",
        "strokeWidth": 2,
        "strokeStyle": "solid",
        "roughness": 1,
        "opacity": 100,
        "groupIds": [],
        "seed": 3042,
        "version": 1,
        "versionNonce": 1,
        "isDeleted": False,
        "points": [
            [0, 0],
            [end_x - start_x, end_y - start_y]
        ],
        "startBinding": None,
        "endBinding": None,
        "startArrowhead": None,
        "endArrowhead": "arrow"
    }

elements = []

# Box 1: Boilerplate & Standardized Repos
elements.extend(make_rect("box_repos", 40, 60, 270, 340, 
    "1. Standardized Repositories\n\n"
    "📁 boilerplate-repo\n"
    "(Standard Dockerfile, linter, tests)\n\n"
    "📁 microservices/\n"
    "├── <service-name>-service\n"
    "│   └── .gitlab-ci.yml\n"
    "│       include: central-ci\n"
    "│       variables: SERVICE_NAME\n"
    "└── ... (20+ backend & frontend)", 
    "#eff6ff", "#2563eb", "solid", "#1e3a5f", 14))

elements.append(make_arrow("arr_1_to_2", 310, 230, 380, 230, "#2563eb"))

# Box 2: Central CI & Mozilla SOPS
elements.extend(make_rect("box_central_sops", 380, 60, 290, 340,
    "2. Central Pipeline & Secrets\n\n"
    "📁 central-ci-template\n"
    "├── /templates/backend.yml\n"
    "├── /templates/frontend.yml\n"
    "└── /templates/base-jobs.yml\n\n"
    "🔒 Mozilla SOPS Secrets Repo\n"
    "• Encrypted with AWS KMS\n"
    "• Keys plaintext, values cipher\n"
    "• Decrypted in CI on the fly!",
    "#f5f3ff", "#7c3aed", "solid", "#4c1d95", 14))

elements.append(make_arrow("arr_2_to_3", 670, 230, 740, 230, "#7c3aed"))

# Box 3: Single Shared ECR
elements.extend(make_rect("box_ecr", 740, 60, 270, 340,
    "3. Shared AWS ECR Registry\n\n"
    "★ Build Once, Deploy Everywhere\n"
    "• Single Docker image tag (SHA)\n"
    "• Cross-Account Repository Policy\n"
    "  allows UAT, Staging, & Prod\n"
    "  to pull the exact same digest.\n\n"
    "No rebuild in Prod = No drift!",
    "#fff7ed", "#ea580c", "solid", "#9a3412", 14))

elements.append(make_arrow("arr_3_to_4", 1010, 230, 1080, 230, "#ea580c"))

# Box 4: Environment Promotion Ladder
elements.extend(make_rect("box_envs", 1080, 60, 270, 340,
    "4. Environment Promotion\n\n"
    "• DEV:\n"
    "  Push to develop, fast auto-deploy\n\n"
    "• UAT:\n"
    "  QA & client tests with real data\n\n"
    "• STAGING & PROD (Identical Twins):\n"
    "  Staging = Full dry run\n"
    "  Prod = Real end users\n"
    "  Zero surprise deployment!",
    "#ecfdf5", "#059669", "solid", "#065f46", 14))

data = {
    "type": "excalidraw",
    "version": 2,
    "source": "https://excalidraw.com",
    "elements": elements,
    "appState": {
        "viewBackgroundColor": "#ffffff",
        "gridSize": 20
    },
    "files": {}
}

out_path = "content/posts/how-to-deploy-20-microservices-to-ecs/architecture-pipeline.excalidraw"
with open(out_path, "w") as f:
    json.dump(data, f, indent=2)

print("Regenerated Excalidraw file at", out_path)
