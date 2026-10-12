# Slides: *Learn Quantum Computing with QiliSDK*

These slides use [Marp](https://marp.app/), which renders Markdown as a presentation. They introduce
the tutorial, explain the main concepts with small diagrams, show the QiliSDK architecture and
`QTensor` overviews, and point to further material. The worked examples and exercises are in `notebooks/`.

- `qilisdk_tutorial.md`: the deck source (edit this).
- `qilisdk_tutorial.html`: the rendered deck; it loads images from the adjacent `img/` folder. Re-render it after editing the Markdown source.
- `img/`: the SVG diagrams used by the slides and notebooks, the two QiliSDK overview images (`overall.jpg`, `qtensor.jpg`), and the QR codes for this tutorial's repository, the QiliSDK source, and the docs. The notebooks embed PNG copies of the SVGs so they work in Colab and VS Code; after editing one, run `python scripts/embed_diagrams.py` from the repository root to refresh them (it needs Inkscape).

## Present / edit

- **VS Code:** use the **“Marp for VS Code”** extension to preview, present, or export to PDF, PPTX, or HTML.
- **Browser:** open `qilisdk_tutorial.html` (keep the `img/` folder next to it). Arrow keys to navigate;
  press `f` for fullscreen.

## Re-render with the Marp command-line interface

With Node.js and npm installed, run the commands below from the repository root. `npx` runs the Marp tool to convert the source into the requested format.

```bash
cd slides

# HTML (no browser needed)
npx @marp-team/marp-cli@4.5.1 qilisdk_tutorial.md --html -o qilisdk_tutorial.html

# PDF or PPTX (needs a local Chrome/Chromium; --allow-local-files lets it read img/)
npx @marp-team/marp-cli@4.5.1 qilisdk_tutorial.md --pdf  --allow-local-files
npx @marp-team/marp-cli@4.5.1 qilisdk_tutorial.md --pptx --allow-local-files
```

The deck renders equations with KaTeX (`$…$`), defines its purple theme in an inline `<style>` block,
and uses `class:` directives to style title and divider slides. Images use height settings
such as `![h:500](img/…)` to fit the 16:9 slides.
