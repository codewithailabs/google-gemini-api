from google import genai
from PIL import Image
import os
from io import BytesIO
from datetime import datetime

api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key:
    raise RuntimeError("GOOGLE_API_KEY environment variable is not set")

client = genai.Client(api_key=api_key)

model = "gemini-3-pro-image-preview"  # Or "gemini-3-pro-image-preview" for advanced

system_instruction = (
    "Always generate image prompts in a single line. "
    "Maintain consistent character appearance across images (same person, outfit, hairstyle). "
    "Use modern clean vector illustration style with crisp UI elements (not ink-and-wash). "
    "Include modern minimal icons (apps, chart, brain, wrench, agent, calendar, flight) where relevant. "
    "Design for a 9:16 vertical reel cover: clean layout, uncluttered, strong focal point. "
    "No brand logos, no watermarks, no text."
)

with open("prompts.txt", "r", encoding="utf-8") as f:
    prompts_text = f.read().strip()

if not prompts_text:
    raise RuntimeError("prompts.txt is empty")

prompt_blocks = [block.strip() for block in prompts_text.split("\n\n") if block.strip()]

images_dir = "images"
os.makedirs(images_dir, exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]

for prompt_index, block in enumerate(prompt_blocks, start=1):
    prompt = " ".join(line.strip() for line in block.splitlines() if line.strip())
    response = client.models.generate_content(
        model=model,
        contents=[prompt],
        config=genai.types.GenerateContentConfig(system_instruction=system_instruction),
    )

    parts = response.candidates[0].content.parts if response.candidates else []
    for i, part in enumerate(parts):
        if getattr(part, "inline_data", None):
            img_bytes = part.inline_data.data
            img = Image.open(BytesIO(img_bytes))
            filename = f"gemini_image_{prompt_index}_{i+1}_{timestamp}.png"
            output_path = os.path.join(images_dir, filename)
            img.save(output_path)
            print(f"Saved {output_path}")
