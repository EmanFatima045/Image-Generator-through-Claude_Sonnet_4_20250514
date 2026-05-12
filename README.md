<div align="center">

<!-- Animated Header Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=210&section=header&text=AI%20Image%20Tool%20Recommender&fontSize=40&fontColor=fff&animation=twinkling&fontAlignY=33&desc=Claude%20Sonnet%204%20%C3%97%20OpenRouter%20%E2%80%94%20Intelligent%20Prompt%20Analysis&descAlignY=55&descSize=15" width="100%"/>

<br/>

<!-- Badges Row 1 -->
<img src="https://img.shields.io/badge/Claude-Sonnet%204-CC785C?style=for-the-badge&logo=anthropic&logoColor=white"/>
<img src="https://img.shields.io/badge/OpenRouter-API-6C47FF?style=for-the-badge&logo=openai&logoColor=white"/>
<img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge"/>

<br/><br/>

<!-- Badges Row 2 -->
<img src="https://img.shields.io/badge/Tools%20Analyzed-6-F59E0B?style=flat-square"/>
<img src="https://img.shields.io/badge/Score%20Range-0--100-EF4444?style=flat-square"/>
<img src="https://img.shields.io/badge/CLI-Interface-0EA5E9?style=flat-square"/>
<img src="https://img.shields.io/badge/PRs-Welcome-8B5CF6?style=flat-square"/>
<img src="https://img.shields.io/badge/Status-Active-22C55E?style=flat-square"/>

<br/><br/>

> ### 🧠 Stop guessing. Start generating.
> Enter your creative prompt → Claude Sonnet 4 analyzes style, purpose & complexity  
> → Get a scored, explained recommendation for the perfect AI image tool.

<br/>

<!-- Snake animation as visual separator -->
<img src="https://raw.githubusercontent.com/Platane/snk/output/github-contribution-grid-snake-dark.svg" width="80%"/>

<br/>

</div>

---

## 📌 Table of Contents

- [✨ What Makes This Different](#-what-makes-this-different)
- [🔍 How It Works](#-how-it-works)
- [🎨 Supported AI Tools](#-supported-ai-tools)
- [🔐 OpenRouter Setup](#-openrouter-setup)
- [⚡ Quickstart](#-quickstart)
- [📦 Installation](#-installation)
- [💻 Usage & Example Output](#-usage--example-output)
- [🏗️ Project Structure](#-project-structure)
- [🤝 Contributing](#-contributing)

---

## ✨ What Makes This Different

<table>
<tr>
<td width="50%">

### 🤖 Previous Version
```
facebook/bart-large-mnli
────────────────────────
• Zero-shot NLI model
• Pattern matching
• Fixed label scoring
• ~1.6 GB local download
• Fast but surface-level
```

</td>
<td width="50%">

### 🚀 This Version
```
Claude Sonnet 4 via OpenRouter
──────────────────────────────
• Full LLM reasoning
• Deep context understanding
• Scored + explained output
• No local model needed
• Nuanced, justified picks
```

</td>
</tr>
</table>

Claude Sonnet 4 doesn't just match labels — it **reasons** about your prompt like a creative director would: considering artistic style, intended audience, commercial use case, and technical complexity before making its call.

---

## 🔍 How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   📝 User Prompt                                                │
│        │                                                        │
│        ▼                                                        │
│   🌐 OpenRouter API  ──►  🧠 Claude Sonnet 4                   │
│                                                                 │
│   Claude analyzes 4 dimensions:                                 │
│   ┌──────────────┬────────────────────────────────────────┐    │
│   │  🎭 Style    │ Realistic / Artistic / Cartoon / 3D    │    │
│   │  🎯 Purpose  │ Social media / Game / Commercial / Art │    │
│   │  🔧 Control  │ Simple / Detailed / Technical          │    │
│   │  📜 Safety   │ Open / Restricted / Commercial-safe    │    │
│   └──────────────┴────────────────────────────────────────┘    │
│        │                                                        │
│        ▼                                                        │
│   📊 Scores each tool  (0 – 100)                                │
│        │                                                        │
│        ▼                                                        │
│   🏆 Recommendation + Reasoning displayed                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🎨 Supported AI Tools

<div align="center">

| Tool | Strength | Best Use Case | Score Factors |
|------|----------|---------------|---------------|
| 🎨 **Midjourney** | Artistic & cinematic | Fantasy, concept art, moody visuals | Style depth, aesthetic quality |
| 🖼️ **DALL·E 3** | Photorealistic accuracy | Product shots, factual scenes | Realism, prompt fidelity |
| ⚡ **Stable Diffusion** | Flexibility & control | Custom models, experimental work | Technical control, customization |
| 🎯 **Canva AI** | Design templates | Social media, branded graphics | Simplicity, marketing layout |
| 🔥 **Adobe Firefly** | Commercial-safe output | Ads, editorial, professional work | IP safety, professional finish |
| ⚙️ **Leonardo AI** | Game & character art | RPG assets, creatures, UI sprites | Game-readiness, detail level |

</div>

---

## 🔐 OpenRouter Setup

OpenRouter gives you access to Claude Sonnet 4 and 100+ other models through a single unified API.

### Step 1 — Get Your Free API Key

```
1. Visit  →  https://openrouter.ai
2. Sign up (free tier available)
3. Go to  →  Dashboard > API Keys
4. Click  →  "Create Key"
5. Copy your key  →  sk-or-v1-...
```

### Step 2 — Add Key to the Project

Open `main.py` and replace the placeholder:

```python
# main.py
API_KEY = "sk-or-v1-your_key_here"   # 👈 Paste your key here
```

> ⚠️ **Security tip:** Never commit your API key to GitHub.  
> Use a `.env` file and add it to `.gitignore` instead:

```bash
# .env
OPENROUTER_API_KEY=sk-or-v1-your_key_here
```

```python
# main.py (safer approach)
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")
```

---

## ⚡ Quickstart

```bash
# 1. Clone the repo
git clone https://github.com/EmanFatima045/image-Generation-through-Facebook_BART_large_mnli.git
cd image-Generation-through-Facebook_BART_large_mnli

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your OpenRouter API key to main.py (or .env)

# 4. Run it
python main.py
```

---

## 📦 Installation

### Requirements

- Python **3.8+**
- An [OpenRouter](https://openrouter.ai) account (free)
- Internet connection

### Full Setup

```bash
# Clone
git clone https://github.com/EmanFatima045/image-Generation-through-Facebook_BART_large_mnli.git
cd image-Generation-through-Facebook_BART_large_mnli

# (Recommended) Virtual environment
python -m venv venv
source venv/bin/activate         # macOS / Linux
venv\Scripts\activate            # Windows

# Install
pip install -r requirements.txt
```

### `requirements.txt`

```txt
requests>=2.28.0
python-dotenv>=1.0.0
```

> 💡 Unlike the BART version, **no large model downloads** are required. The heavy lifting happens on OpenRouter's servers.

---

## 💻 Usage & Example Output

```bash
python main.py
```

```
╔══════════════════════════════════════════════════════════╗
║     🎯  AI Image Tool Recommender                        ║
║     Powered by Claude Sonnet 4  ×  OpenRouter            ║
╚══════════════════════════════════════════════════════════╝

Enter your image prompt: A glowing neon cyberpunk samurai in a rainy Tokyo alley
```

```
🧠 Sending to Claude Sonnet 4...

📊 Tool Scores:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  🎨 Midjourney          ████████████░░░░  92
  ⚙️  Leonardo AI         █████████░░░░░░░  74
  ⚡ Stable Diffusion    ████████░░░░░░░░  68
  🖼️  DALL·E 3            ██████░░░░░░░░░░  51
  🔥 Adobe Firefly       ████░░░░░░░░░░░░  37
  🎯 Canva AI            ██░░░░░░░░░░░░░░  18
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🏆  BEST TOOL:  Midjourney  (92 / 100)

💡  REASONING:
    This prompt is rich in cinematic atmosphere — neon lighting, rain, urban
    noir, and a strong aesthetic identity. Midjourney excels at translating
    mood-driven, visually layered prompts into stunning images with minimal
    instruction. The cyberpunk + samurai combination is also a genre it
    handles exceptionally well.
```

---

## 🏗️ Project Structure

```
📂 image-Generation-through-Facebook_BART_large_mnli/
│
├── 📄 main.py               # CLI entry point & user interaction
├── 📄 recommender.py        # OpenRouter API call + Claude prompt logic
├── 📄 tools.py              # Tool definitions, descriptions, scoring labels
├── 📄 .env.example          # Template for environment variables
├── 📄 requirements.txt      # Python dependencies
└── 📄 README.md             # You are here
```

---

## 🤝 Contributing

Want to add a new AI tool or improve the Claude prompt? PRs are welcome!

```bash
# 1. Fork this repo
# 2. Create your branch
git checkout -b feature/add-ideogram-ai

# 3. Make your changes and commit
git commit -m "feat: add Ideogram AI to tool list"

# 4. Push and open a Pull Request
git push origin feature/add-ideogram-ai
```

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=100&section=footer" width="100%"/>

**Built with 🧠 by [Eman Fatima](https://github.com/EmanFatima045)**

*If this project saved you time, a ⭐ star goes a long way!*

[![GitHub Stars](https://img.shields.io/github/stars/EmanFatima045/image-Generation-through-Facebook_BART_large_mnli?style=social)](https://github.com/EmanFatima045/image-Generation-through-Facebook_BART_large_mnli)
&nbsp;&nbsp;
[![Follow](https://img.shields.io/github/followers/EmanFatima045?style=social)](https://github.com/EmanFatima045)

</div>
