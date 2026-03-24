"""
Phase 10: Remove all JS, delete map/template files, replace map view with Google Maps iframes.
"""
import os, re

ROOT = r"d:\Hidden Egypt"

# ─── 1. Google Maps embed URLs per destination ─────────────────────────────
GMAPS = {
    "siwa.html": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d111898.32!2d25.4789!3d29.2033!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x14376d7faa9a6e33%3A0x4e5c7e45a487ac13!2sSiwa%20Oasis!5e0!3m2!1sen!2seg!4v1",
    "colored-canyon.html": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d47000!2d34.4!3d29.05!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x14fd2cd40d89f5b7%3A0x8d1aef6e7e3a7b9a!2sColored%20Canyon%2C%20Nuweiba!5e0!3m2!1sen!2seg!4v1",
    "white-desert.html": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d80000!2d27.93!3d27.38!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x14388bccfe8eeae3%3A0x56ef87ae8fcdfbf4!2sWhite%20Desert%20National%20Park!5e0!3m2!1sen!2seg!4v1",
    "tunis.html": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d20000!2d30.689!3d29.434!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x145839b857a91461%3A0x1e5cf12e14b74b9!2sTunis%20Village%2C%20Fayoum!5e0!3m2!1sen!2seg!4v1",
    "dendera.html": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d10000!2d32.6697!3d26.1422!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x1444b23a8c5d3d99%3A0x8c6f0eb3aadb4c4a!2sDendera%20Temple%20Complex!5e0!3m2!1sen!2seg!4v1",
    "ras-abu-galum.html": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d20000!2d34.5297!3d28.5611!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x14fcd9b0f4e67e7d%3A0x9f8e91c10d5b4e02!2sRas%20Abu%20Galum!5e0!3m2!1sen!2seg!4v1",
}

# ─── 2. Process each HTML file ─────────────────────────────────────────────
html_files = [f for f in os.listdir(ROOT) if f.endswith(".html")]

for fname in html_files:
    fpath = os.path.join(ROOT, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # A) Remove <script src="js/main.js"></script>
    content = re.sub(r'\s*<script src="js/main\.js"><\/script>', "", content)

    # B) Replace onclick hamburger toggle with CSS-only label+checkbox approach
    # The onclick uses classList.toggle — replace with a <label for> pattern doesn't need JS
    # Since we already have a checkbox-free version with inline onclick, we can't 100% remove
    # the onclick without restructuring HTML. The simplest pure-CSS approach:
    # Wrap nav-links in a checkbox:target hack. But since the current HTML uses IDs + onclick,
    # the cleanest removal is using a <label> + hidden checkbox.
    # For now, strip the inline JS and rely on the :target CSS pattern already in style.css if present,
    # OR add a <label for> that uses a hidden checkbox.
    # We'll implement the hidden checkbox approach per file.

    # Replace: <div class="menu-toggle" onclick="document.getElementById('sub-nav-links').classList.toggle('active')">
    # With: a <label> that toggles a hidden checkbox
    # First inject the hidden checkbox before the nav (we'll do it in the nav block)

    # Replace menu-toggle onclick with label approach
    content = re.sub(
        r'<div class="menu-toggle" onclick="[^"]*">(\s*<span></span><span></span><span></span>\s*)</div>',
        r'<label class="menu-toggle" for="nav-toggle" aria-label="Toggle navigation">\1</label>',
        content
    )

    # index.html uses a slightly different pattern
    content = re.sub(
        r'<div class="menu-toggle" onclick="[^"]*">(\s*<span[^>]*></span><span[^>]*></span><span[^>]*></span>\s*)</div>',
        r'<label class="menu-toggle" for="nav-toggle" aria-label="Toggle navigation">\1</label>',
        content
    )

    # Inject hidden checkbox input just before <header class="page-header"> or the nav
    if 'for="nav-toggle"' in content and '<input type="checkbox" id="nav-toggle"' not in content:
        content = content.replace(
            '<header',
            '<input type="checkbox" id="nav-toggle" class="nav-toggle-input" aria-hidden="true">\n<header',
            1
        )

    # C) Replace map-miniature block with Google Maps iframe
    if fname in GMAPS:
        embed_url = GMAPS[fname]
        new_map_block = f'''<div class="map-miniature" style="margin-top: 40px;">
                    <h3 style="margin-bottom: 16px; color: var(--color-secondary);">Map View</h3>
                    <div style="border-radius: var(--border-radius); overflow: hidden; border: none; box-shadow: 0 4px 20px rgba(30,58,95,0.1);">
                        <iframe
                            src="{embed_url}"
                            width="100%"
                            height="280"
                            style="border:0; display:block;"
                            allowfullscreen=""
                            loading="lazy"
                            referrerpolicy="no-referrer-when-downgrade"
                            title="Map location">
                        </iframe>
                    </div>
                </div>'''

        # Replace entire map-miniature block
        content = re.sub(
            r'<div class="map-miniature"[^>]*>.*?</div>\s*</aside>',
            new_map_block + '\n            </aside>',
            content,
            flags=re.DOTALL
        )

    # D) Remove nav links to discover-map.html
    content = re.sub(
        r'\s*<li><a href="discover-map\.html"[^>]*>[^<]*</a></li>',
        "",
        content
    )

    if content != original:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated: {fname}")
    else:
        print(f"No changes: {fname}")

# ─── 3. Delete files ─────────────────────────────────────────────────────
to_delete = [
    os.path.join(ROOT, "discover-map.html"),
    os.path.join(ROOT, "place-template.html"),
    os.path.join(ROOT, "js", "main.js"),
]

for path in to_delete:
    if os.path.exists(path):
        os.remove(path)
        print(f"Deleted: {path}")

print("Done.")
