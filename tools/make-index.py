#!/usr/bin/env python3
"""Make content/index.md (Quartz's homepage) from the vault's main page.

The vault's home note is "Star Wars RPG (FFG) Wiki.md". Quartz needs an
index.md at the content root, so copy that note's body under a minimal
frontmatter (title only, properties panel hidden). The original note stays,
so wikilinks to it keep working.
"""
import pathlib, sys

content = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "content")
src = content / "Star Wars RPG (FFG) Wiki.md"
text = src.read_text(encoding="utf-8")
if text.startswith("---\n"):
    end = text.index("\n---\n", 4)
    body = text[end + 5 :]
else:
    body = text
(content / "index.md").write_text(
    '---\ntitle: "Star Wars RPG (FFG) Wiki"\nquartz-properties: false\n---\n' + body,
    encoding="utf-8",
)
print(f"wrote {content / 'index.md'} from {src.name}")
