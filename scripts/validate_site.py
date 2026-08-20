from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import sys

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_PAGES = [
    "index.html",
    "entender/racio-omega-6-3.html",
    "ciencia/index.html",
    "ciencia/cardiovascular.html",
    "ciencia/inflamacao.html",
    "ciencia/cerebro.html",
    "ciencia/pele.html",
    "ciencia/desempenho.html",
    "ciencia/condicoes.html",
    "testar-e-acompanhar.html",
    "biblioteca.html",
    "metodologia.html",
    "sobre.html",
    "produtos/index.html",
    "en/index.html",
    "404.html",
]

SKIP_SCHEMES = {"http", "https", "mailto", "tel", "data", "javascript"}


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.refs: list[tuple[str, str]] = []
        self.in_title = False
        self.title = ""
        self.h1_count = 0
        self.meta_description = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        if tag == "title":
            self.in_title = True
        if tag == "h1":
            self.h1_count += 1
        if tag == "meta" and (data.get("name") or "").lower() == "description" and data.get("content"):
            self.meta_description = True
        for attr in ("href", "src"):
            value = data.get(attr)
            if value:
                self.refs.append((attr, value))

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title += data.strip()


def resolve_local(page: Path, ref: str) -> Path | None:
    ref = ref.strip()
    if not ref or ref.startswith("#"):
        return None
    parsed = urlsplit(ref)
    if parsed.scheme.lower() in SKIP_SCHEMES or parsed.netloc:
        return None
    path = unquote(parsed.path)
    if not path:
        return None
    if path.startswith("/"):
        target = ROOT / path.lstrip("/")
    else:
        target = page.parent / path
    if target.is_dir():
        target = target / "index.html"
    return target.resolve()


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    for rel in PUBLIC_PAGES:
        page = ROOT / rel
        if not page.exists():
            errors.append(f"MISSING PAGE: {rel}")
            continue

        parser = PageParser()
        parser.feed(page.read_text(encoding="utf-8", errors="replace"))

        if not parser.title.strip():
            errors.append(f"MISSING <title>: {rel}")
        if parser.h1_count != 1:
            warnings.append(f"H1 COUNT {parser.h1_count}: {rel}")
        if rel != "404.html" and not parser.meta_description:
            warnings.append(f"MISSING META DESCRIPTION: {rel}")

        for attr, ref in parser.refs:
            target = resolve_local(page, ref)
            if target is None:
                continue
            try:
                target.relative_to(ROOT)
            except ValueError:
                errors.append(f"OUTSIDE ROOT: {rel} -> {ref}")
                continue
            if not target.exists():
                errors.append(f"BROKEN {attr.upper()}: {rel} -> {ref}")

    print(f"Validated {len(PUBLIC_PAGES)} public pages.")
    if warnings:
        print("\nWarnings:")
        for item in warnings:
            print(f"  - {item}")
    if errors:
        print("\nErrors:")
        for item in errors:
            print(f"  - {item}")
        return 1
    print("\nNo broken local links or missing referenced files found in the public editorial pages.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
