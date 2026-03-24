import codecs, re

with codecs.open('index.html', 'r', 'utf-8') as f:
    idx = f.read()

# 1. RESTORE RAS ABU GALUM TO THE ADVENTURE TAB
adventure_fixed = '''<div id="content-adventure" class="tab-content">
                        <div class="cards-slider">
                            <a href="ras-abu-galum.html" class="place-card" style="background-image: url('https://images.unsplash.com/photo-1559827260-dc66d52bef19?q=80&w=600&auto=format&fit=crop');">
                                <div class="place-card-content"><h3>Ras Abu Galum</h3><p>South Sinai</p></div>
                            </a>
                            <a href="colored-canyon.html" class="place-card" style="background-image: url('https://images.unsplash.com/photo-1547013406-e6a8f98bde65?q=80&w=600&auto=format&fit=crop');">
                                <div class="place-card-content"><h3>Colored Canyon</h3><p>Nuweiba</p></div>
                            </a>
                            <a href="white-desert.html" class="place-card" style="background-image: url('https://images.unsplash.com/photo-1542365516-e358b4f95d92?q=80&w=800');">
                                <div class="place-card-content"><h3>White Desert</h3><p>Farafra</p></div>
                            </a>
                        </div>
                    </div>'''
idx = re.sub(r'<div id="content-adventure" class="tab-content">.*?</div>\s*</div>', adventure_fixed, idx, flags=re.DOTALL)


# 2. UPGRADE THE FILTER ICONS TO RELATABLE SVGS
globe_svg = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path><path d="M2 12h20"></path></svg>'
mountain_svg = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 3l4 8 5-5 5 15H2L8 3z"></path></svg>'
sun_svg = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>'
waves_svg = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12c5 0 5 4 10 4s5-4 10-4M2 18c5 0 5 4 10 4s5-4 10-4M2 6c5 0 5 4 10 4s5-4 10-4"></path></svg>'

filters_block = f'''                <div class="filters-container">
                    <a href="explore.html" class="filter-btn" style="text-decoration:none;">
                        <div class="filter-icon" style="color: var(--color-secondary);">{globe_svg}</div>
                        <span class="filter-name">All Regions</span>
                    </a>
                    <a href="explore.html#filter-sinai" class="filter-btn" style="text-decoration:none;">
                        <div class="filter-icon" style="color: var(--color-secondary);">{mountain_svg}</div>
                        <span class="filter-name">Sinai</span>
                    </a>
                    <a href="explore.html#filter-desert" class="filter-btn" style="text-decoration:none;">
                        <div class="filter-icon" style="color: var(--color-secondary);">{sun_svg}</div>
                        <span class="filter-name">Desert</span>
                    </a>
                    <a href="explore.html#filter-nile" class="filter-btn" style="text-decoration:none;">
                        <div class="filter-icon" style="color: var(--color-secondary);">{waves_svg}</div>
                        <span class="filter-name">Nile Valley</span>
                    </a>
                </div>'''

idx = re.sub(r'<div class="filters-container">.*?</div>\s*</section>', filters_block + '\\n            </section>', idx, flags=re.DOTALL)

with codecs.open('index.html', 'w', 'utf-8') as f:
    f.write(idx)

print('Success')
