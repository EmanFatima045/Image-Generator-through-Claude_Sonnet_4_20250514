# 🎯 AI Image Tool Recommender (Claude Sonnet 4 + OpenRouter)

A smart AI system that analyzes your text prompt and recommends the **best AI image generation tool** (Midjourney, DALL·E, Canva, etc.).

---

## 🚀 Features

- 🧠 Uses Claude Sonnet 4 via OpenRouter API
- 🎯 Analyzes image prompts deeply
- 🏆 Recommends best AI tool
- 📊 Gives score for all 6 tools
- 💡 Explains reasoning for each tool
- ⚡ Simple CLI-based application

---

## 🧠 Supported AI Tools

The system analyzes and compares 6 AI image tools:

- 🎨 Midjourney → Artistic & cinematic images
- 🖼️ DALL·E 3 → Realistic & accurate prompts
- ⚡ Stable Diffusion → Custom & flexible generation
- 🎯 Canva AI → Social media & design templates
- 🔥 Adobe Firefly → Professional & commercial-safe
- ⚙️ Leonardo AI → Game assets & characters

---

## 🔐 How It Works

1. User enters a prompt
2. Prompt is sent to **Claude Sonnet 4 (via OpenRouter)**
3. AI analyzes:
   - Style (realistic, artistic, cartoon)
   - Purpose (design, game, social media)
   - Complexity
4. Each tool gets a score (0–100)
5. Best tool is selected and displayed

---

## 🔑 OpenRouter Setup

This project uses **OpenRouter API**.

### Step 1: Get API Key
- Go to: https://openrouter.ai
- Sign up (free)
- Get API key from dashboard

### Step 2: Add Key in Code

```python
API_KEY = "your_openrouter_api_key_here"
