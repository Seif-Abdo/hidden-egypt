import os, subprocess

URL_MAP = {
    'siwa_oasis.jpg': 'https://images.unsplash.com/photo-1598337227515-5645318fb450?q=80&w=1080',
    'colored_canyon.jpg': 'https://images.unsplash.com/photo-1547013406-e6a8f98bde65?q=80&w=1080',
    'white_desert.jpg': 'https://images.unsplash.com/photo-1542365516-e358b4f95d92?q=80&w=1080',
    'tunis_village.jpg': 'https://images.unsplash.com/photo-1533052136932-6aeb851722cb?q=80&w=1080',
    'dendera_temple.jpg': 'https://images.unsplash.com/photo-1562679302-6c6f03173bf5?q=80&w=1080',
    'ras_abu_galum.jpg': 'https://images.unsplash.com/photo-1543320147-3dc61298c9dc?q=80&w=1080',
    'ras_abu_galum_alt.jpg': 'https://images.unsplash.com/photo-1559827260-dc66d52bef19?q=80&w=1080',
    'map_preview.jpg': 'https://images.unsplash.com/photo-1524661135-423995f22d0b?q=80&w=1080',
    'home_hero_bg.jpg': 'https://images.unsplash.com/photo-1539650116574-8efeb43e2750?q=80&w=1600'
}

IMAGE_DIR = 'images'
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

print(f"Starting FINAL asset download via CURL to {IMAGE_DIR}...")

for name, url in URL_MAP.items():
    path = os.path.join(IMAGE_DIR, name)
    print(f"Downloading {name}...")
    cmd = [
        'curl', 
        '-L', 
        '-k', # Insecure if needed, though shouldn't be
        '-A', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        '-o', path,
        url
    ]
    try:
        subprocess.run(cmd, check=True)
        print(f"Successfully finished {name}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to download {name}: {e}")

# Create generic fallback
generic = os.path.join(IMAGE_DIR, 'generic_landscape.jpg')
if os.path.exists(os.path.join(IMAGE_DIR, 'white_desert.jpg')):
    import shutil
    shutil.copyfile(os.path.join(IMAGE_DIR, 'white_desert.jpg'), generic)
    print("Created generic_landscape.jpg")

print("Asset Healing complete.")
