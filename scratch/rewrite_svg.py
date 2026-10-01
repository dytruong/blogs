import re

with open("content/posts/how-to-deploy-20-microservices-to-ecs/architecture-pipeline.svg", "r") as f:
    svg = f.read()

# Replace SOPS block with Variables & Secrets
sops_original = """    <!-- SOPS Secrets Repo Box -->
    <rect x="15" y="220" width="240" height="160" rx="8" fill="#f8fafc" stroke="#fbcfe8"/>
    <text x="25" y="244" class="code-text" font-weight="700" fill="#9d174d">🔒 secrets-repo (SOPS)</text>
    <text x="35" y="266" class="code-text" font-size="11px" fill="#64748b">• Encrypted with AWS KMS</text>
    <text x="35" y="284" class="code-text" font-size="11px" fill="#64748b">• Values: ciphertext 🔑</text>
    <text x="35" y="302" class="code-text" font-size="11px" fill="#64748b">• Keys: readable in Git diffs</text>
    
    <rect x="25" y="315" width="220" height="50" rx="6" fill="#fdf2f8" stroke="#f472b6"/>
    <text x="33" y="333" class="code-text" font-size="10px" font-weight="700" fill="#be185d">Decrypted in CI into memory:</text>
    <text x="33" y="352" class="code-text" font-size="10px" fill="#475569">sops -d env.enc.yaml > .env</text>"""

sops_new = """    <!-- Configs & Secrets Repo Box -->
    <rect x="15" y="220" width="240" height="160" rx="8" fill="#f8fafc" stroke="#fbcfe8"/>
    <text x="25" y="244" class="code-text" font-weight="700" fill="#9d174d">📄 deployment/&lt;env&gt;/</text>
    <text x="35" y="266" class="code-text" font-size="11px" fill="#64748b">• variables.json: config</text>
    <text x="35" y="284" class="code-text" font-size="11px" fill="#64748b">• secrets.json: keys only</text>
    <text x="35" y="302" class="code-text" font-size="11px" fill="#64748b">  (Values fetched from SOPS)</text>
    
    <rect x="25" y="315" width="220" height="50" rx="6" fill="#fdf2f8" stroke="#f472b6"/>
    <text x="33" y="333" class="code-text" font-size="10px" font-weight="700" fill="#be185d">Parsed into YAML in CI:</text>
    <text x="33" y="352" class="code-text" font-size="10px" fill="#475569">Source of truth for Task Def</text>"""

svg = svg.replace(sops_original, sops_new)

# Replace Environment Promotion with Dev focus
env_original = """    <!-- UAT -->
    <rect x="15" y="152" width="170" height="95" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>
    <text x="25" y="175" class="box-title" font-size="13px" fill="#b45309">UAT Environment</text>
    <text x="25" y="195" class="code-text" font-size="11px" fill="#64748b">• For QA &amp; client test</text>
    <text x="25" y="213" class="code-text" font-size="11px" fill="#64748b">• Real integration data</text>
    <text x="25" y="233" class="code-text" font-size="11px" fill="#d97706">• Tagged release-candidate</text>

    <!-- Staging & Prod (Identical Twins) -->
    <rect x="15" y="258" width="170" height="225" rx="8" fill="#f0fdf4" stroke="#86efac"/>
    <text x="25" y="282" class="box-title" font-size="13px" fill="#15803d">Staging &amp; Prod</text>
    <text x="25" y="302" class="pill-text" fill="#15803d">★ IDENTICAL TWINS</text>
    
    <text x="25" y="328" class="code-text" font-size="11px" fill="#334155">• Staging = Full dry run</text>
    <text x="25" y="348" class="code-text" font-size="11px" fill="#334155">• Prod = Real users</text>
    <text x="25" y="375" class="code-text" font-size="11px" fill="#64748b">Identical infrastructure:</text>
    <text x="25" y="393" class="code-text" font-size="11px" fill="#64748b">same ECS configs,</text>
    <text x="25" y="411" class="code-text" font-size="11px" fill="#64748b">same CPU/memory,</text>
    <text x="25" y="429" class="code-text" font-size="11px" fill="#64748b">same networking.</text>

    <rect x="25" y="445" width="150" height="28" rx="4" fill="#dcfce7" stroke="#22c55e"/>
    <text x="35" y="464" class="pill-text" fill="#166534">Zero Surprise In Prod!</text>"""

env_new = """    <!-- Self Service -->
    <rect x="15" y="152" width="170" height="150" rx="8" fill="#f0fdf4" stroke="#86efac"/>
    <text x="25" y="175" class="box-title" font-size="13px" fill="#15803d">UAT / Staging / Prod</text>
    <text x="25" y="195" class="code-text" font-size="11px" fill="#64748b">• Complex deployments</text>
    <text x="25" y="213" class="code-text" font-size="11px" fill="#64748b">• Fully self-service!</text>
    <text x="25" y="233" class="code-text" font-size="11px" fill="#64748b">• Dev teams deploy without</text>
    <text x="25" y="251" class="code-text" font-size="11px" fill="#64748b">  waiting for DevOps</text>
    
    <rect x="25" y="265" width="150" height="28" rx="4" fill="#dcfce7" stroke="#22c55e"/>
    <text x="35" y="284" class="pill-text" fill="#166534">DevOps only on standby</text>"""

svg = svg.replace(env_original, env_new)

with open("content/posts/how-to-deploy-20-microservices-to-ecs/architecture-pipeline.svg", "w") as f:
    f.write(svg)
