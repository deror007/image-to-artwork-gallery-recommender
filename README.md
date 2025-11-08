# Image → Art Gallery Recommender 🎨

A small Gradio app that recommends artworks from a curated gallery (9 × 8 = 72 paintings) based on a query image. Upload a photo (or use your webcam) and the app finds visually similar paintings using an embedding model + FAISS nearest-neighbour search.

Key points
- Gallery size: 72 artworks
- Entry point: `app.py` (launches the Gradio UI)
- Uses: PyTorch model for embeddings, FAISS for fast similarity search, and a lightweight dataset of artwork images/URLs

## Features
- Upload an image or use the webcam as the query
- Optionally filter recommendations by art style (Abstract, Floral, Pop, Wildlife, Seascape, Cityscape, Mongolian, Landscape, Sculpture)
- Returns a gallery of similar artwork images (configurable number of results)
- Click a result to open the artwork’s page/shop URL in your browser

## Quick start (macOS / Linux)
1. Clone the repository and change the working directory to this project's local directory.

2. Install dependencies

```bash
pip install -r requirements.txt
```

> The project depends on PyTorch, FAISS (CPU build), Pillow, pandas, gradio and other packages listed in `requirements.txt`.

3. Run the app

```bash
python app.py
```

This will start a Gradio UI (by default served on http://localhost:7860). The app will open a browser tab automatically when you click/select an artwork result.

## Files of interest
- `app.py` — main application and Gradio UI (entry point)
- `model.py` — model loading / embedding helpers
- `index.py` — FAISS index creation and maintenance helpers
- `data.py` — artwork metadata dictionaries (image display URLs and shop links)
- `original.index` — prebuilt FAISS index file used by the app
- `requirements.txt` — Python dependencies

## How it works (short)
1. The app loads an embedding model (see `model.py`) and a FAISS index (`original.index`).
2. A query image is preprocessed and passed through the model to obtain an embedding.
3. FAISS performs a nearest-neighbour search against the indexed artwork embeddings.
4. The top-k results are returned and shown in a Gradio `Gallery` component. Selecting an item opens the artwork page from `data.py`.

## Customization / development notes
- To change the gallery images or metadata, update `data.py`.
- If you add or replace artwork images you should rebuild the FAISS index (see functions in `index.py` — `createIndex`, `appendIndex`).
- Artwork count is set in `app.py` (variable `artwork_counts = 72`). Update if you change the dataset.

## Troubleshooting
- If FAISS fails to import, ensure you installed the correct FAISS package for your environment — the `requirements.txt` contains `faiss_cpu==1.7.4` for CPU-only installs.
- If the UI isn't visible, check the terminal output for the Gradio URL (usually http://localhost:7860).

## License & credits
Made by Russell de Roeper in partnership with Oscore.io

If you reuse parts of this code, please credit the author.
