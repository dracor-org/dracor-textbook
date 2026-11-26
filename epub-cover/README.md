# EPUB cover

`cover.html` is the source of `docs/_static/figures/epub-cover.png` (1600 × 2560 px).
To render it again with Chrome:

```
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new \
  --hide-scrollbars --force-device-scale-factor=1 --window-size=1600,2560 \
  --screenshot=docs/_static/figures/epub-cover.png "file://$PWD/epub-cover/cover.html"
```
