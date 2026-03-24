import os, urllib.request

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

IMAGE_DIR = 'images'
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

print(f"Starting final asset download to {IMAGE_DIR}...")

for u_id, name in ASSETS.items():
    url = f"https://images.unsplash.com/photo-{u_id}?q=80&w=1200&auto=format&fit=crop"
    path = os.path.join(IMAGE_DIR, name)
    
    # Try renaming local bg_<id>.jpg first
    old_local = os.path.join(IMAGE_DIR, f"bg_{u_id}.jpg")
    if os.path.exists(old_local):
        print(f"Renaming local {old_local} to {path}")
        if os.path.exists(path): os.remove(path)
        os.rename(old_local, path)
        continue

    if os.path.exists(path):
        print(f"Asset {name} already exists. Skipping download.")
        continue

    print(f"Downloading {name} from Unsplash ID {u_id}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
        with urllib.request.urlopen(req) as response:
            with open(path, 'wb') as f:
                f.write(response.read())
        print(f"Successfully downloaded {name}")
    except Exception as e:
        print(f"Failed to download {name}: {e}")

# Create generic fallback
generic = os.path.join(IMAGE_DIR, 'generic_landscape.jpg')
if not os.path.exists(generic) and os.path.exists(os.path.join(IMAGE_DIR, 'white_desert.jpg')):
    import shutil
    shutil.copyfile(os.path.join(IMAGE_DIR, 'white_desert.jpg'), generic)
    print("Created generic_landscape.jpg")

print("Final asset check complete.")
