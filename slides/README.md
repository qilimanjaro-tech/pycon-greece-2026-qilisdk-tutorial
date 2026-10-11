# Slides: *Learn Quantum Computing with QiliSDK*

A [Marp](https://marp.app/) deck (Markdown-based). It's a **thin framing deck**: title, motivation
("why quantum computing", the 2026 reality check, what we'll build), the architecture and `QTensor`
diagrams, two or three concept slides per tutorial part, and pointers to the full tutorial. The actual
teaching happens in the `notebooks/`; these slides orient and recap.

- `qilisdk_tutorial.md`: the deck source (edit this).
- `qilisdk_tutorial.html`: pre-rendered, self-contained-ish (loads `img/` alongside it).
- `img/`: the two diagrams (`overall.jpg`, `qtensor.jpg`) and the QR codes for the QiliSDK source and docs.

## Present / edit

- **Easiest:** VS Code + the **“Marp for VS Code”** extension → live preview, present, and one-click
  export to PDF/PPTX/HTML.
- **Browser:** open `qilisdk_tutorial.html` (keep the `img/` folder next to it). Arrow keys to navigate;
  press `f` for fullscreen.

## Re-render with the Marp CLI

```bash
cd slides

# HTML (no browser needed)
npx @marp-team/marp-cli@latest qilisdk_tutorial.md --html -o qilisdk_tutorial.html

# PDF or PPTX (needs a local Chrome/Chromium; --allow-local-files lets it read img/)
npx @marp-team/marp-cli@latest qilisdk_tutorial.md --pdf  --allow-local-files
npx @marp-team/marp-cli@latest qilisdk_tutorial.md --pptx --allow-local-files
```

> The deck uses KaTeX math (`$…$`), a custom purple theme (inline `<style>`), and `class:` directives
> for the title/divider slides. Diagrams are sized by height (`![h:500](img/…)`) to fit 16:9.
