"""
AI Image Tool Recommender - Using OpenRouter + Claude Sonnet 4
FREE to use via OpenRouter (https://openrouter.ai)
No Anthropic account needed!

Setup:
1. Go to https://openrouter.ai and sign up free
2. Get your API key from https://openrouter.ai/keys
3. Run: pip install openai
4. Run: python ImageGenerator_OpenRouter.py
"""

import openai
import json

# ── OpenRouter client setup ───────────────────────────────────────────────
# OpenRouter is compatible with the OpenAI Python library
# Just change the base_url and paste your OpenRouter key

API_KEY = "ApI_KEY"  # <-- paste your key here

client = openai.OpenAI(
    api_key="API_KEY",
    base_url="https://openrouter.ai/api/v1",
    default_headers={
        "HTTP-Referer": "http://localhost",
        "X-Title": "AI Image Recommender"
    }
) # type: ignore

# ── Tool definitions ──────────────────────────────────────────────────────
TOOLS = {
    "midjourney":        {"name": "Midjourney",        "emoji": "🎨"},
    "dall_e":            {"name": "DALL·E 3",           "emoji": "🖼️"},
    "stable_diffusion":  {"name": "Stable Diffusion",   "emoji": "⚡"},
    "canva":             {"name": "Canva AI",            "emoji": "🎯"},
    "firefly":           {"name": "Adobe Firefly",       "emoji": "🔥"},
    "leonardo":          {"name": "Leonardo.ai",         "emoji": "⚙️"},
}

# ── System prompt ─────────────────────────────────────────────────────────
SYSTEM_PROMPT = """You are an expert AI image generation tool recommender.

You deeply understand these 6 tools:
- Midjourney: cinematic, artistic, painterly, fantasy, concept art, stylized
- DALL·E 3: photorealistic, precise, prompt-accurate, images with text
- Stable Diffusion: full control, custom models, anime, technical, free/local
- Canva AI: social media, branding, logos, marketing, non-designers
- Adobe Firefly: commercial-safe, professional, Adobe workflow, stock quality
- Leonardo.ai: game assets, consistent characters, anime, fast generation

Analyze the user's image prompt deeply. Understand:
- What style is needed (realistic, artistic, cartoon, etc.)
- What purpose (commercial, personal, game, social media, etc.)
- What complexity level (simple design, detailed illustration, etc.)

Respond with ONLY valid JSON — no markdown, no explanation, nothing else.

{
  "winner": "tool_key",
  "prompt_analysis": "2 sentence analysis of what this prompt needs",
  "winner_reason": "why this specific tool wins for this prompt",
  "scores": {
    "midjourney": 85,
    "dall_e": 70,
    "stable_diffusion": 60,
    "canva": 30,
    "firefly": 45,
    "leonardo": 55
  },
  "reasoning": {
    "midjourney": "one sentence reason for this score",
    "dall_e": "one sentence reason for this score",
    "stable_diffusion": "one sentence reason for this score",
    "canva": "one sentence reason for this score",
    "firefly": "one sentence reason for this score",
    "leonardo": "one sentence reason for this score"
  }
}

Tool key must be one of: midjourney, dall_e, stable_diffusion, canva, firefly, leonardo"""


# ── Core function ─────────────────────────────────────────────────────────
def analyze_prompt(user_prompt: str) -> dict:
    """
    Send prompt to Claude Sonnet 4 via OpenRouter.
    Returns structured JSON with scores and reasoning.
    """
    print("\n  🔍 Analyzing with Claude Sonnet 4 via OpenRouter...\n")

    response = client.chat.completions.create(
        model="anthropic/claude-sonnet-4",       # Claude Sonnet 4 on OpenRouter
        max_tokens=1024,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": f'Analyze this image generation prompt: "{user_prompt}"'
            }
        ]
    )

    raw = response.choices[0].message.content.strip()

    # Clean markdown fences if Claude accidentally adds them
    if "```" in raw:
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
        raw = raw.strip()

    return json.loads(raw)


# ── Display results ───────────────────────────────────────────────────────
def display_results(prompt: str, data: dict):
    winner_key   = data["winner"]
    winner_tool  = TOOLS.get(winner_key, {"name": winner_key, "emoji": "🏆"})

    print("\n" + "=" * 65)
    print(f"  PROMPT   : {prompt[:55]}{'...' if len(prompt) > 55 else ''}")
    print("=" * 65)

    print(f"\n  ANALYSIS : {data['prompt_analysis']}\n")

    print(f"  🏆 BEST TOOL → {winner_tool['emoji']} {winner_tool['name']}")
    print(f"     {data['winner_reason']}\n")

    print("  📊 All tools ranked:\n")

    sorted_tools = sorted(data["scores"].items(), key=lambda x: x[1], reverse=True)

    for rank, (key, score) in enumerate(sorted_tools, 1):
        tool     = TOOLS.get(key, {"name": key, "emoji": "•"})
        filled   = int(score / 5)          # score 0-100 → bar 0-20 chars
        empty    = 20 - filled
        bar      = "█" * filled + "░" * empty
        badge    = "  ⭐ WINNER" if key == winner_key else ""
        reason   = data["reasoning"].get(key, "")

        print(f"  {rank}. {bar}  {score:3d}%  {tool['emoji']} {tool['name']}{badge}")
        print(f"        {reason}\n")

    print("=" * 65 + "\n")


# ── Main loop ─────────────────────────────────────────────────────────────
def main():
    print("\n" + "=" * 65)
    print("   🎯 AI IMAGE TOOL RECOMMENDER")
    print("   Model  : Claude Sonnet 4")
    print("   Via    : OpenRouter (openrouter.ai)")
    print("=" * 65)
    print("  Type your image prompt and press Enter.")
    print("  Type 'quit' to exit.\n")

    while True:
        try:
            prompt = input("  Your prompt: ").strip()

            if not prompt:
                print("  ⚠️  Please enter a prompt.\n")
                continue

            if prompt.lower() in ("quit", "exit", "q"):
                print("\n  👋 Goodbye!\n")
                break

            data = analyze_prompt(prompt)
            display_results(prompt, data)

        except KeyboardInterrupt:
            print("\n\n  👋 Goodbye!\n")
            break

        except json.JSONDecodeError:
            print("  ❌ Could not parse response. Try again.\n")

        except Exception as e:
            print(f"  ❌ Error: {e}")
            print("  Check your API key and internet connection.\n")


if __name__ == "__main__":
    main()