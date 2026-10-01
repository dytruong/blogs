import re

with open("content/posts/how-to-deploy-20-microservices-to-ecs/index.md", "r") as f:
    content = f.read()

# Replace section 2
sec2_old = r'## Question 2: "Where Do Secrets Live.*?(?=---)'
sec2_new = """## Question 2: "Where Do Configuration and Secrets Live?"

Every service needs configurations (like ports, log levels) and secrets (like DB connection strings, API tokens).

- ❌ **Bad idea**: Committing plaintext `.env` files with passwords into Git. (Security will hunt you down).
- ❌ **Also bad**: Pasting 50 environment variables manually into GitLab CI web settings for 20 repos. (Drift nightmare).

### The Solution: JSON Configs & Mozilla SOPS 🔒

We define two files in each microservice repository under `deployment/<env>/` (for example, `deployment/development/`):

#### 1. `variables.json` (The Public Configs)
This file holds all non-sensitive configuration in a key-value format. It is completely safe to commit and acts as the source of truth for the service's environment.
```json
{
  "PORT": "3000",
  "LOG_LEVEL": "info",
  "AWS_REGION": "us-east-1"
}
```

#### 2. `secrets.json` (The Secret Keys)
This file holds the **keys only** (as an array). The actual sensitive values are nowhere to be found in this repo.
```json
[
  "DATABASE_PASSWORD",
  "STRIPE_API_KEY"
]
```

#### Where do the actual secret values come from?
We store the actual encrypted secret values in a central, dedicated secrets repository using [Mozilla SOPS](https://github.com/getsops/sops). SOPS encrypts the values using AWS KMS, making them safe to store in Git while leaving the keys readable in diffs.

#### How it comes together in the Pipeline:
1. The CI pipeline reads `variables.json` to get the base configuration.
2. The pipeline reads the keys from `secrets.json`.
3. It fetches the corresponding decrypted values for those keys from the central SOPS secrets repository on the fly.
4. It parses both together into a YAML file to create the final **AWS ECS Task Definition**, and deploys it!

These two JSON files act as our single source of truth for what a deployment looks like!

"""
content = re.sub(sec2_old, sec2_new, content, flags=re.DOTALL)

# Replace section 5
sec5_old = r'## Question 5: "What is the Difference Between Dev, UAT, Staging, and Prod\?".*?(?=---)'
sec5_new = """## Question 5: "How Do We Actually Deploy This?" (Focusing on DEV)

For this guide (Part 1), we are going to focus purely on the **DEV Environment**.

### The Dev Environment Experience
In the Dev environment, speed is everything. 
When a developer pushes code to the `develop` branch, the pipeline automatically kicks off:
1. Runs unit tests and linters.
2. Parses `variables.json` and fetches secrets.
3. Builds and pushes the Docker image to ECR.
4. Updates the ECS Task Definition and deploys the container.

Within minutes, the developer's new code is live in the Dev sandbox, ready for internal integration testing.

### What about UAT, Staging, and Prod?
Deploying to higher environments (UAT, Staging, Production) involves a much more complicated process (think database migrations, cross-region deployments, and Blue/Green traffic shifting).

However, **I resolved this complexity by fully automating it**. 
The result? The development team can trigger deployments to UAT, Staging, and even Production completely on their own, fully self-service, without waiting for DevOps support! (Though as DevOps, we are always on standby to support in case something goes wrong).

We'll dive into the intricate details of how that higher-environment promotion works in Part 2!

"""
content = re.sub(sec5_old, sec5_new, content, flags=re.DOTALL)

with open("content/posts/how-to-deploy-20-microservices-to-ecs/index.md", "w") as f:
    f.write(content)
