import codecs, re

print('Executing precision fix script for user-reported visual bugs...')

# -----------------
# 1. FIX INDEX.HTML (Filters and Tabs)
# -----------------
with codecs.open('index.html', 'r', 'utf-8') as f:
    idx = f.read()

# REVERT TABS to Nature/Culture/Adventure
old_tabs_block = '''<div class="tabs-container">
                    <input type="radio" id="tab-nature" name="category" checked>
                    <input type="radio" id="tab-culture" name="category">
                    <input type="radio" id="tab-adventure" name="category">

                    <div class="tabs-nav">
                        <label for="tab-nature" class="tab-label">Nature</label>
                        <label for="tab-culture" class="tab-label">Culture</label>
                        <label for="tab-adventure" class="tab-label">Adventure</label>
                    </div>

                    <div id="content-nature" class="tab-content">
                        <div class="cards-slider">
                            <a href="siwa.html" class="place-card" style="background-image: url('https://images.unsplash.com/photo-1552309398-fd0f5d4e35be?q=80&w=600&auto=format&fit=crop');">
                                <div class="place-card-content"><h3>Siwa Oasis</h3><p>Western Desert</p></div>
                            </a>
                            <a href="colored-canyon.html" class="place-card" style="background-image: url('https://images.unsplash.com/photo-1547013406-e6a8f98bde65?q=80&w=600&auto=format&fit=crop');">
                                <div class="place-card-content"><h3>Colored Canyon</h3><p>Nuweiba</p></div>
                            </a>
                            <a href="white-desert.html" class="place-card" style="background-image: url('https://images.unsplash.com/photo-1542365516-e358b4f95d92?q=80&w=800');">
                                <div class="place-card-content"><h3>White Desert</h3><p>Farafra</p></div>
                            </a>
                        </div>
                    </div>

                    <div id="content-culture" class="tab-content">
                        <div class="cards-slider">
                            <a href="tunis.html" class="place-card" style="background-image: url('https://images.unsplash.com/photo-1533052136932-6aeb851722cb?q=80&w=600&auto=format&fit=crop');">
                                <div class="place-card-content"><h3>Tunis Village</h3><p>Fayoum</p></div>
                            </a>
                            <a href="dendera.html" class="place-card" style="background-image: url('https://images.unsplash.com/photo-1562679302-6c6f03173bf5?q=80&w=600&auto=format&fit=crop');">
                                <div class="place-card-content"><h3>Dendera Temple</h3><p>Qena</p></div>
                            </a>
                        </div>
                    </div>

                    <div id="content-adventure" class="tab-content">
                        <div class="cards-slider">
                            <a href="colored-canyon.html" class="place-card" style="background-image: url('https://images.unsplash.com/photo-1547013406-e6a8f98bde65?q=80&w=600&auto=format&fit=crop');">
                                <div class="place-card-content"><h3>Colored Canyon</h3><p>Nuweiba</p></div>
                            </a>
                            <a href="white-desert.html" class="place-card" style="background-image: url('https://images.unsplash.com/photo-1542365516-e358b4f95d92?q=80&w=800');">
                                <div class="place-card-content"><h3>White Desert</h3><p>Farafra</p></div>
                            </a>
                        </div>
                    </div>
                </div>'''
idx = re.sub(r'<div class="tabs-container">.*?</div>\s*</div>\s*</section>', old_tabs_block + '\n</section>', idx, flags=re.DOTALL)

# REPLACE BOTTOM FILTERS (Desert, Oasis, Mountains, History -> All Regions, Sinai, Desert, Nile Valley)
idx = idx.replace('<span class="filter-name">Desert</span>', '<span class="filter-name">All Regions</span>')
idx = idx.replace('<span class="filter-name">Oasis</span>', '<span class="filter-name">Sinai</span>')
idx = idx.replace('<span class="filter-name">Mountains</span>', '<span class="filter-name">Desert</span>')
idx = idx.replace('<span class="filter-name">History</span>', '<span class="filter-name">Nile Valley</span>')
idx = idx.replace('<span class="filter-icon">🏜️</span>', '<span class="filter-icon">🌍</span>')

with codecs.open('index.html', 'w', 'utf-8') as f:
    f.write(idx)
print('index.html updated (filters reverted and updated properly).')


# -----------------
# 2. FIX CSS (Logo scale discrepancies, Hamburger menu floating bug)
# -----------------
with codecs.open('css/style.css', 'r', 'utf-8') as f:
    css = f.read()

# REMOVE all previous rules about .img-logo to reset it entirely
css = re.sub(r'\.img-logo\s*\{.*?\}', '', css, flags=re.DOTALL)
css = re.sub(r'\.page-header \.img-logo\s*\{.*?\}', '', css, flags=re.DOTALL)

# APPEND STRICT GLOBAL FIXES
global_fixes = '''

/* --- GLOBAL LOGO CONSISTENCY --- */
.img-logo {
    height: 60px !important;
    max-height: 60px !important;
    width: auto !important;
    object-fit: contain !important;
    display: block !important;
    margin: 0 !important;
    padding: 0 !important;
}

@media (max-width: 768px) {
    .img-logo {
        height: 50px !important;
        max-height: 50px !important;
    }
}

/* --- MOBILE HAMBURGER MENU DROPDOWN FIX --- */
/* Nuke any stray CSS setting the mobile menu to float to the right side */
@media (max-width: 768px) {
    .right-panel > .main-nav, .page-header .main-nav, .main-nav {
        position: static !important;
        width: 100% !important;
        display: flex;
        justify-content: flex-end;
    }
    
    .nav-links.active {
        display: flex !important;
        flex-direction: column !important;
        position: absolute !important;
        top: 100% !important; /* Immediately below the header */
        left: 0 !important;
        right: 0 !important;
        width: 100% !important;
        max-width: 100vw !important;
        box-sizing: border-box !important;
        background-color: var(--color-white) !important;
        padding: 30px 20px !important;
        margin: 0 !important;
        box-shadow: 0 15px 30px rgba(0,0,0,0.15) !important;
        border-radius: 0 0 24px 24px !important;
        text-align: center !important;
        z-index: 100000 !important;
        transform: none !important;
    }
}

/* Ensure the header on subpages stretches full width so the menu doesn't break */
.page-header {
    width: 100% !important;
    box-sizing: border-box !important;
}

/* Revert Tab logic in CSS to Nature/Culture/Adventure */
#tab-nature:checked ~ .tabs-nav label[for="tab-nature"],
#tab-culture:checked ~ .tabs-nav label[for="tab-culture"],
#tab-adventure:checked ~ .tabs-nav label[for="tab-adventure"] {
  color: var(--color-text-dark) !important;
}

#tab-nature:checked ~ .tabs-nav label[for="tab-nature"]:after,
#tab-culture:checked ~ .tabs-nav label[for="tab-culture"]:after,
#tab-adventure:checked ~ .tabs-nav label[for="tab-adventure"]:after {
  width: 100% !important;
}

#tab-nature:checked ~ #content-nature,
#tab-culture:checked ~ #content-culture,
#tab-adventure:checked ~ #content-adventure {
  display: block !important;
}
'''
css += global_fixes

with codecs.open('css/style.css', 'w', 'utf-8') as f:
    f.write(css)

print('style.css updated (logo sizes forced strictly and mobile menu float logic overridden to 100vw).')
