import os, glob, codecs, re

print("Running ultimate QA sweep fixes...")

# 1. Update imagery for all HTML files
IMAGE_MAP = {
    '1539650116574-8efeb43e2750': '1542365516-e358b4f95d92',  # White Desert
    '1572252009286-268acec5b8d0': '1552309398-fd0f5d4e35be',  # Siwa
    '1621250325308-540203f6f3cc': '1547013406-e6a8f98bde65',  # Colored Canyon
    '1600375990520-4e314ce17a3a': '1562679302-6c6f03173bf5',  # Dendera
}

for file in glob.glob('*.html'):
    with codecs.open(file, 'r', 'utf-8') as f:
        html = f.read()

    # Apply all image mappings for geographic accuracy
    for old, new in IMAGE_MAP.items():
        html = html.replace(old, new)

    # Move contact us inside nav-links for mobile hamburger support
    if 'class="btn nav-contact"' in html and '<ul class="nav-links"' in html:
        # Extract the node
        nav_match = re.search(r'(<a[^>]*class="[^"]*nav-contact[^"]*"[^>]*>.*?</a>)', html)
        if nav_match:
            anchor = nav_match.group(1)
            # Remove from everywhere outside
            html = html.replace(anchor, '')
            # Add to the end of the ul structure twice (one for desktop outside, one for mobile inside)
            html = html.replace('</ul>', f'    <li class="mobile-only-contact">{anchor}</li>\n                </ul>')
            html = html.replace('</nav>', f'    <div class="desktop-only-contact">{anchor}</div>\n            </nav>')

    # Fix geographic inaccuracy on footer (replace global map with Egypt map or similar)
    # The footer SVG is just a decorative globe. We will just leave the SVG as is, or replace it with a compass 
    html = html.replace('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="footer-icon"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>', 
                        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="footer-icon"><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"></polygon><circle cx="12" cy="12" r="10"></circle></svg>') # Compass icon

    with codecs.open(file, 'w', 'utf-8') as f:
        f.write(html)

print("HTML structure and images fixed.")

# 2. Fix CSS QA Issues
with codecs.open('css/style.css', 'r', 'utf-8') as f:
    css = f.read()

# Delete buggy rogue `fixed !important` lines from previous edit (lines ~641-659)
css = re.sub(r'\.right-panel > \.main-nav, \.page-header \.main-nav, \.main-nav \{\s*position: fixed !important;.*?\}', '', css, flags=re.DOTALL)
css = re.sub(r'\.nav-links\.active \{\s*position: fixed !important;.*?\}', '', css, flags=re.DOTALL)

# Add correct polished visual CSS for everything flagged by QA
css_fixes = '''
/* FINAL QA SWEEP FIXES */

/* Desktop Nav Alignment */
.split-container .right-panel {
    padding-top: 60px; /* Aligns visually with the logo */
}

/* Touch Target Sizing */
.filter-chip, .tab-label {
    cursor: pointer;
    min-width: 44px;
    min-height: 44px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
}

/* Mobile Core Architecture */
.mobile-only-contact { display: none; }
.desktop-only-contact { display: block; }

@media (max-width: 768px) {
    /* Header Transparency Fix */
    .page-header {
        background: rgba(255, 255, 255, 0.98) !important;
        backdrop-filter: blur(12px) !important;
        -webkit-backdrop-filter: blur(12px) !important;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08) !important;
        position: sticky !important;
        top: 0 !important;
        z-index: 9999 !important;
    }

    /* Hero Overlap Fix */
    .hero-content {
        padding-top: 140px; /* Explicit clearance for aggressive oversized logo bounding box */
    }

    /* Mobile Menu UX */
    .mobile-only-contact { display: block; margin-top: 20px; }
    .desktop-only-contact { display: none; }
    
    .nav-links.active {
        display: flex !important;
        flex-direction: column !important;
        position: absolute !important;
        top: 100% !important;
        left: 0 !important;
        right: 0 !important;
        height: auto !important;
        background: var(--color-white) !important;
        padding: 30px 20px !important;
        box-shadow: 0 20px 40px rgba(0,0,0,0.15) !important;
        border-radius: 0 0 24px 24px !important;
        text-align: center !important;
        z-index: 10000 !important;
        animation: slideDown 0.3s ease forwards;
        transform-origin: top center;
    }

    @keyframes slideDown {
        from { opacity: 0; transform: translateY(-10px) scaleY(0.95); }
        to { opacity: 1; transform: translateY(0) scaleY(1); }
    }
}
'''
if '/* FINAL QA SWEEP FIXES */' not in css:
    css += css_fixes

with codecs.open('css/style.css', 'w', 'utf-8') as f:
    f.write(css)

print("Master CSS architecture applied.")
