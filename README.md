# Google Gemini API Image Generator

Generate images with the Google Gemini API using prompt text files and save results with timestamped filenames.

## Requirements

- Python 3.10+
- A Google Gemini API key
- Packages: `google-genai`, `Pillow`

## Setup

1) Create and activate a virtual environment (optional).
2) Install dependencies:

```powershell
pip install google-genai pillow
```

3) Set your API key (persisted for your user account):

```powershell
setx GOOGLE_API_KEY "your-key-here"
```

Restart your terminal after setting the variable.

## Prompts file format

Create `prompts.txt` in the project root.

- One prompt per paragraph.
- Separate prompts with a blank line.
- Multi-line prompts are allowed; lines are joined into a single prompt.

Example:

```text
Telugu moral story scene: wise king teaching kids in Bengaluru palace, cartoon style for children

Futuristic Hyderabad skyline at sunset with flying taxis, vibrant comic style

Watercolor landscape of tea plantations in Assam, misty morning, serene
```

## Run

```powershell
python image.py
```

Images are written to `images/` with filenames like:

```
gemini_image_<promptIndex>_<imageIndex>_YYYYMMDD_HHMMSS_mmm.png
```

## Notes

- If `prompts.txt` is empty, the script will raise an error.
- If `GOOGLE_API_KEY` is not set, the script will raise an error.
