## PowerPointGame

A small Python tool that composes a playable game as a PowerPoint presentation (PPTX) using image/sound assets and a level description. Running `generate.py` builds the presentation and writes `dist/game.pptx`.

This project was inspired by Zanzlanz’s video, [“Making the Most Complicated PowerPoint Game!”](https://www.youtube.com/watch?v=SmYDGnwg4dA)

### Credits
- Image assets - [Zanzlanz](https://www.youtube.com/@zanzlanz)
- Sound assets - [Pixabay](https://pixabay.com/) and [Freesound](https://freesound.org/)

### Quick overview
- Source entry: `generate.py` (calls `util.Crawler` to generate game scenes, and `util.Composer` to generate PowerPoint slides)
- Output: `dist/game.pptx`
- Assets: the `asset/` directory (images, audio) — keep these files in place relative to the project root.

### Prerequisites
- Python 3.10+ (the code uses modern type hints and was developed with newer Python versions)
- PowerPoint is not required to generate the file, but a PowerPoint-compatible viewer is required to play the output.

On Windows (PowerShell) these steps assume you have `python` on PATH.

### Install dependencies (recommended)
1. Create and activate a virtual environment:

```powershell
python -m venv .venv
\.venv\Scripts\Activate.ps1
```

2. Upgrade pip and install dependencies:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Optional: if you use a type checker, you can install `types-lxml` for better typing support:

```powershell
pip install types-lxml
```

### Run
From the project root (where `generate.py` lives):

```powershell
python generate.py
```

The script will allocate slides and compose the presentation. When finished the file will be saved as `dist/game.pptx` and logging will be printed to the console.

### Customization
- Edit the `LEVELS` list in `generate.py` to change or add levels (it uses emoji-based maps).
- Edit `ASSETS` in `generate.py` to point to different image/audio files. The composer asserts that image assets end with `.png`, music with `.mp3`, and sounds with `.wav`.
