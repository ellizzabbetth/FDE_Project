# In your project root or a scripts/ folder
#cat > scripts/check_providers.py << 'EOF'
import os
from openai import OpenAI

for name, key, url, model in [
    ("xAI",     os.environ.get("XAI_API_KEY"),     "https://api.x.ai/v1", "grok-4.3"),
    ("Gemini",  os.environ.get("GEMINI_API_KEY"),  "https://generativelanguage.googleapis.com/v1beta/openai/", "gemini-2.5-flash"),
    ("NVIDIA",  os.environ.get("NVIDIA_API_KEY"),  "https://integrate.api.nvidia.com/v1", "meta/llama-3.3-70b-instruct"),
]:
    if not key:
        print(f"{name}: no key set")
        continue
    try:
        c = OpenAI(api_key=key, base_url=url)
        r = c.chat.completions.create(model=model, messages=[{"role":"user","content":"hi"}], max_tokens=1)
        print(f"{name}: OK → {r.choices[0].message.content[:30]}")
    except Exception as e:
        print(f"{name}: FAILED → {type(e).__name__}: {e}")
# EOF

# python scripts/check_providers.py   