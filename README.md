# Gemini Image Generator 🎨

Batch-generate images with the Google Gemini API. Write your prompts in a text file, run one script, and get every image saved with a timestamped filename.

Built as a demo for the [codewithailabs](https://youtube.com/@codewithailabs) YouTube channel.

## What it does

- Reads prompts from `prompts.txt` (one prompt per paragraph)
- Sends each one to the `gemini-3-pro-image-preview` model
- Saves every image it gets back to the `images/` folder

The script includes a built-in style guide (the `system_instruction` in `image.py`). It asks for clean vector illustrations in a **9:16 vertical reel-cover** layout, with a consistent character and no logos or text. Edit it to change the look.

## What's inside

| File | What it does |
|---|---|
| `image.py` | The generator script |
| `prompts.txt` | Your prompts, one per paragraph |
| `requirements.txt` | Python packages |
| `gemini_image_2.png` | A sample output |

## Prerequisites

- Python 3.10 or newer
- A Gemini API key from [aistudio.google.com/apikey](https://aistudio.google.com/apikey)

## Setup

### 1. Clone and install

```bash
git clone https://github.com/codewithailabs/google-gemini-api.git
cd google-gemini-api
pip install -r requirements.txt
```

### 2. Set your API key

```bash
# macOS / Linux
export GOOGLE_API_KEY="your-key-here"
```

```powershell
# Windows (saved for future terminals; open a new terminal afterwards)
setx GOOGLE_API_KEY "your-key-here"
```

### 3. Write your prompts

Put them in `prompts.txt`. Separate prompts with a blank line. A prompt can span several lines; they're joined into one.

```text
Telugu moral story scene: wise king teaching kids in a palace, cartoon style for children

Futuristic Hyderabad skyline at sunset with flying taxis, vibrant comic style
```

## Run

```bash
python image.py
```

Images are saved to `images/` as:

```
gemini_image_<prompt number>_<image number>_YYYYMMDD_HHMMSS_mmm.png
```

## Troubleshooting

| Problem | Fix |
|---|---|
| `GOOGLE_API_KEY environment variable is not set` | Set the key (step 2). On Windows, open a new terminal after `setx` |
| `prompts.txt is empty` | Add at least one prompt |
| `404 model not found` | The image model name has changed. Update `model` in `image.py` to the current one in the Gemini docs |
| No images saved | The model replied with text only. Make the prompt more clearly ask for an image |

## Credits

Built for **[codewithailabs](https://youtube.com/@codewithailabs)**. Questions? Comment on the video or open a GitHub issue.
