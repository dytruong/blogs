import json

with open("content/posts/how-to-deploy-20-microservices-to-ecs/architecture-pipeline.excalidraw", "r") as f:
    data = json.load(f)

# Update texts
texts = {
    "text_box_repos": "1. Standardized Repositories\n\n📁 boilerplate-repo\n\n📁 microservices/\n├── <service-name>-service\n│   └── .gitlab-ci.yml\n│       include: central-ci\n│       variables: SERVICE_NAME\n└── ... (20+ services)",
    "text_box_central_sops": "2. Config & Secrets\n\n📄 deployment/<env>/variables.json\n(Key-value non-sensitive config)\n\n📄 deployment/<env>/secrets.json\n(Keys only, values fetched from SOPS)\n\nPipeline parses both into YAML\nto create the ECS Task Definition.",
    "text_box_ecr": "3. CI Pipeline (Centralized)\n\n📁 central-ci-template\nContains reusable jobs for backend/frontend.\n\n★ Build Once\nPipeline builds the Docker image and pushes\nto the shared AWS ECR registry with a unique\nSHA tag.",
    "text_box_envs": "4. DEV Deployment\n\n• DEV Env:\n  Fast auto-deploy for developers.\n  Task Definition updated and deployed to ECS.\n\n• UAT, Staging, Prod:\n  More complex, but fully self-service.\n  Dev team deploys without DevOps support!"
}

for el in data["elements"]:
    if el["type"] == "text":
        new_text = texts.get(el["id"])
        if new_text:
            el["text"] = new_text
            el["originalText"] = new_text
            el["width"] = 280
    elif el["type"] == "rectangle":
        el["width"] = 310
        # adjust x spacing to avoid overlap since we made boxes wider
        # current widths were 270, x were 40, 380, 740, 1080
        # new widths 310. let's set x: 40, 420, 800, 1180
        if el["id"] == "box_repos":
            el["x"] = 40
        elif el["id"] == "box_central_sops":
            el["x"] = 420
        elif el["id"] == "box_ecr":
            el["x"] = 800
        elif el["id"] == "box_envs":
            el["x"] = 1180
            
    elif el["type"] == "arrow":
        # adjust arrows
        if el["id"] == "arr_1_to_2":
            el["x"] = 350
            el["width"] = 70
        elif el["id"] == "arr_2_to_3":
            el["x"] = 730
            el["width"] = 70
        elif el["id"] == "arr_3_to_4":
            el["x"] = 1110
            el["width"] = 70

with open("content/posts/how-to-deploy-20-microservices-to-ecs/architecture-pipeline.excalidraw", "w") as f:
    json.dump(data, f, indent=2)

print("Excalidraw updated.")
