import os, glob, codecs, re

print('Fixing linter errors and updating Home Page architecture...')

# 1. Fix the </body> syntax error on subpages
for file in glob.glob('*.html'):
    with codecs.open(file, 'r', 'utf-8') as f:
        html = f.read()
    
    # Another possibility: a div wasn't closed before </body>
    div_count = html.count('<div') - html.count('</div')
    if div_count > 0 and 'index.html' not in file:
        print(f'{file} has {div_count} unclosed divs. Auto-closing before </body>')
        html = html.replace('</body>', ('</div>'*div_count) + '\n</body>')

    # Re-save
    with codecs.open(file, 'w', 'utf-8') as f:
        f.write(html)

# 2. Overhaul index.html (Home Page)
with codecs.open('index.html', 'r', 'utf-8') as f:
    idx = f.read()

# Remove old logo container from left-panel
idx = re.sub(r'<div class="logo-container">.*?</div>', '', idx, flags=re.DOTALL)

# Remove old main-nav from right-panel
idx = re.sub(r'<nav class="main-nav">.*?</nav>', '', idx, flags=re.DOTALL)

# Inject unified global header right after <body> or <div class='split-container'>
unified_header = '''
    <!-- Unified Absolute Header -->
    <header class="home-header" style="position: absolute; top: 0; left: 0; right: 0; z-index: 1000; padding: 40px 60px; display: flex; justify-content: space-between; align-items: center;">
        <!-- Logo -->
        <a href="index.html" style="display: block;">
            <img src="logo.png" alt="Hidden Egypt" class="img-logo relative-logo">
        </a>

        <!-- Navigation -->
        <nav class="main-nav" style="margin-bottom: 0;">
            <ul class="nav-links" id="index-nav-links">
                <li><a href="index.html" class="active" style="color:var(--color-secondary);">Home</a></li>
                <li><a href="explore.html">Explore</a></li>
                <li><a href="gallery.html">Gallery</a></li>
                <li><a href="about.html">About Us</a></li>
                <li class="mobile-only-contact"><a href="contact.html" class="btn nav-contact">Contact Us</a></li>
            </ul>
            <div class="menu-toggle" onclick="document.getElementById('index-nav-links').classList.toggle('active')">
                <span></span><span></span><span></span>
            </div>
            <div class="desktop-only-contact">
                <a href="contact.html" class="btn nav-contact" style="padding: 10px 24px; font-size: 0.95rem;">Contact Us</a>
            </div>
        </nav>
    </header>
'''
if 'class="home-header"' not in idx:
    idx = idx.replace('<div class="split-container">', '<div class="split-container">\n' + unified_header)

# 3. Refactor Home Page Filters
new_tabs = '''
                <div class="tabs-container">
                    <input type="radio" id="tab-all" name="category" checked>
                    <input type="radio" id="tab-sinai" name="category">
                    <input type="radio" id="tab-desert" name="category">
                    <input type="radio" id="tab-nile" name="category">

                    <div class="tabs-nav">
                        <label for="tab-all" class="tab-label">All Regions</label>
                        <label for="tab-sinai" class="tab-label">Sinai</label>
                        <label for="tab-desert" class="tab-label">Desert</label>
                        <label for="tab-nile" class="tab-label">Nile Valley</label>
                    </div>

                    <div id="content-all" class="tab-content">
                        <div class="cards-slider">
                            <a href="siwa.html" class="place-card" style="background-image: url('https://images.unsplash.com/photo-1552309398-fd0f5d4e35be?q=80&w=600&auto=format&fit=crop');">
                                <div class="place-card-content"><h3>Siwa Oasis</h3><p>Western Desert</p></div>
                            </a>
                            <a href="tunis.html" class="place-card" style="background-image: url('https://images.unsplash.com/photo-1533052136932-6aeb851722cb?q=80&w=600&auto=format&fit=crop');">
                                <div class="place-card-content"><h3>Tunis Village</h3><p>Fayoum</p></div>
                            </a>
                            <a href="colored-canyon.html" class="place-card" style="background-image: url('https://images.unsplash.com/photo-1547013406-e6a8f98bde65?q=80&w=600&auto=format&fit=crop');">
                                <div class="place-card-content"><h3>Colored Canyon</h3><p>Nuweiba</p></div>
                            </a>
                            <a href="white-desert.html" class="place-card" style="background-image: url('https://images.unsplash.com/photo-1542365516-e358b4f95d92?q=80&w=800');">
                                <div class="place-card-content"><h3>White Desert</h3><p>Farafra</p></div>
                            </a>
                            <a href="dendera.html" class="place-card" style="background-image: url('https://images.unsplash.com/photo-1562679302-6c6f03173bf5?q=80&w=600&auto=format&fit=crop');">
                                <div class="place-card-content"><h3>Dendera Temple</h3><p>Qena</p></div>
                            </a>
                        </div>
                    </div>

                    <div id="content-sinai" class="tab-content">
                        <div class="cards-slider">
                            <a href="colored-canyon.html" class="place-card" style="background-image: url('https://images.unsplash.com/photo-1547013406-e6a8f98bde65?q=80&w=600&auto=format&fit=crop');">
                                <div class="place-card-content"><h3>Colored Canyon</h3><p>Nuweiba</p></div>
                            </a>
                        </div>
                    </div>

                    <div id="content-desert" class="tab-content">
                        <div class="cards-slider">
                            <a href="siwa.html" class="place-card" style="background-image: url('https://images.unsplash.com/photo-1552309398-fd0f5d4e35be?q=80&w=600&auto=format&fit=crop');">
                                <div class="place-card-content"><h3>Siwa Oasis</h3><p>Western Desert</p></div>
                            </a>
                            <a href="white-desert.html" class="place-card" style="background-image: url('https://images.unsplash.com/photo-1542365516-e358b4f95d92?q=80&w=800');">
                                <div class="place-card-content"><h3>White Desert</h3><p>Farafra</p></div>
                            </a>
                        </div>
                    </div>

                    <div id="content-nile" class="tab-content">
                        <div class="cards-slider">
                            <a href="tunis.html" class="place-card" style="background-image: url('https://images.unsplash.com/photo-1533052136932-6aeb851722cb?q=80&w=600&auto=format&fit=crop');">
                                <div class="place-card-content"><h3>Tunis Village</h3><p>Fayoum</p></div>
                            </a>
                            <a href="dendera.html" class="place-card" style="background-image: url('https://images.unsplash.com/photo-1562679302-6c6f03173bf5?q=80&w=600&auto=format&fit=crop');">
                                <div class="place-card-content"><h3>Dendera Temple</h3><p>Qena</p></div>
                            </a>
                        </div>
                    </div>
                </div>
'''
if 'id="tab-all"' not in idx:
    idx = re.sub(r'<div class="tabs-container">.*?</div>\s*</div>\s*</section>', new_tabs + '\n</section>', idx, flags=re.DOTALL)

with codecs.open('index.html', 'w', 'utf-8') as f:
    f.write(idx)

# Clean up CSS hacks since logo is physically cropped!
with codecs.open('css/style.css', 'r', 'utf-8') as f:
    css = f.read()

# Replace .img-logo massive hacks
css = re.sub(r'/\* Pristine Mobile Flow and Logo Aesthetics \*/.*?\.right-panel\!important', '', css, flags=re.DOTALL)
css = re.sub(r'\.img-logo \{.*?\}', '', css, flags=re.DOTALL)
css = re.sub(r'@media \(max-width: 768px\) \{\s*\.img-logo \{.*?\}\s*\}', '', css, flags=re.DOTALL)

clean_logo = '''
/* Clean Native Logo Box */
.img-logo {
  height: 90px;
  max-width: auto;
  object-fit: contain;
  mix-blend-mode: multiply;
  filter: contrast(1.1) brightness(1.1);
  display: block;
}

@media (max-width: 768px) {
  .img-logo { 
      height: 60px; 
  }
}
'''
if '/* Clean Native Logo Box */' not in css:
    css += clean_logo

# Add matching tab display rules for the new tabs
new_tab_logic = '''
#tab-all:checked ~ .tabs-nav label[for="tab-all"],
#tab-sinai:checked ~ .tabs-nav label[for="tab-sinai"],
#tab-desert:checked ~ .tabs-nav label[for="tab-desert"],
#tab-nile:checked ~ .tabs-nav label[for="tab-nile"] {
  color: var(--color-text-dark);
}

#tab-all:checked ~ .tabs-nav label[for="tab-all"]:after,
#tab-sinai:checked ~ .tabs-nav label[for="tab-sinai"]:after,
#tab-desert:checked ~ .tabs-nav label[for="tab-desert"]:after,
#tab-nile:checked ~ .tabs-nav label[for="tab-nile"]:after {
  width: 100%;
}

#tab-all:checked ~ #content-all,
#tab-sinai:checked ~ #content-sinai,
#tab-desert:checked ~ #content-desert,
#tab-nile:checked ~ #content-nile {
  display: block;
}
'''
if '#tab-all:checked' not in css:
    css += new_tab_logic

# Also fix the mobile hamburger margin
css += '''
@media (max-width: 768px) {
    .home-header { padding: 20px 30px !important; }
}
'''

with codecs.open('css/style.css', 'w', 'utf-8') as f:
    f.write(css)

print('Done rewriting Home page architecture and clearing hacks.')
