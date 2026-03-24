import os, glob, codecs, re
import urllib.request

print("Starting semantic image localization and URL sweeping...")

IMAGE_DIR = "images"
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

def pull(url_id, out_name):
    # Base url ignoring all parameters
    url = f"https://images.unsplash.com/photo-{url_id}?q=80&w=1200&auto=format&fit=crop"
    final_path = os.path.join(IMAGE_DIR, out_name)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            with open(final_path, 'wb') as f:
                f.write(resp.read())
        return f"images/{out_name}"
    except Exception as e:
        print(f"Failed to download {out_name}: {e}")
        return None

# Semantic Map (Unsplash ID -> Relatable Name)
ASSETS = {
    '1552309398-fd0f5d4e35be': 'siwa_oasis.jpg',
    '1547013406-e6a8f98bde65': 'colored_canyon.jpg',
    '1542365516-e358b4f95d92': 'white_desert.jpg',
    '1533052136932-6aeb851722cb': 'tunis_village.jpg',
    '1562679302-6c6f03173bf5': 'dendera_temple.jpg',
    '1543320147-3dc61298c9dc': 'ras_abu_galum.jpg',
    '1559827260-dc66d52bef19': 'ras_abu_galum_alt.jpg',
    '1524661135-423995f22d0b': 'map_preview.jpg',
    '1539650116574-8efeb43e2750': 'home_hero_bg.jpg'
}

# 1. Download explicit semantic assets
for u_id, semantic_name in ASSETS.items():
    pull(u_id, semantic_name)

# Download a generic fallback placeholder for any 404s/galleries
generic_path = pull('1542365516-e358b4f95d92', 'generic_landscape.jpg') # White Desert

# 2. Global Regex Wipe
# This will find any URL inside url('https://images.unsplash.com/...') or src="..."
files_to_check = glob.glob("*.html") + glob.glob("css/*.css")

for file in files_to_check:
    with codecs.open(file, 'r', 'utf-8') as f:
        html = f.read()

    # We will search for all unsplash occurrences
    # "https://images.unsplash.com/photo-1547013406-e6a8f98bde65?q=80&w=1600"
    
    # Fast exact mapping replacement
    for u_id, semantic_name in ASSETS.items():
        # Replace occurrences of the ID and its parameters
        # Example: https://images.unsplash.com/photo-[ID][anything until single quote, double quote, or parenthesis]
        pattern = r'https://images\.unsplash\.com/photo-' + u_id + r'[^\"\'\)]*'
        html = re.sub(pattern, f"images/{semantic_name}", html)

    # For any remaining Unsplash links (like broken gallery ones), force them to the generic landscape
    html = re.sub(r'https://images\.unsplash\.com/photo-[a-zA-Z0-9\-]+[^\"\'\)]*', 'images/generic_landscape.jpg', html)
    
    # Also fix anything that was previously downloaded as `images/bg_12345.jpg` by my old script
    for u_id, semantic_name in ASSETS.items():
        html = re.sub(f'images/bg_{u_id}\.jpg', f"images/{semantic_name}", html)
    
    # Any other leftover `images/bg_...` generic fallback to the safe landscape
    html = re.sub(r'images/bg_[a-zA-Z0-9\-]+\.jpg', 'images/generic_landscape.jpg', html)
    
    with codecs.open(file, 'w', 'utf-8') as f:
        f.write(html)

print("Semantic asset migration complete!")
