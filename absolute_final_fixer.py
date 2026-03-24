import os, subprocess

URL_MAP = {
    'siwa_oasis.jpg': 'https://images.unsplash.com/photo-1771236581590-9cf1463a7d59?q=80&w=1080',
    'colored_canyon.jpg': 'https://images.unsplash.com/photo-1561829728-da35df23beab?q=80&w=1080',
    'white_desert.jpg': 'https://images.unsplash.com/photo-1643236312558-2725e111238b?q=80&w=1080',
    'tunis_village.jpg': 'https://images.unsplash.com/photo-1695625195824-4893aaa04b85?q=80&w=1080',
    'dendera_temple.jpg': 'https://images.unsplash.com/photo-1723997326348-d4953661a61a?q=80&w=1080',
    'ras_abu_galum.jpg': 'https://images.unsplash.com/photo-1668964413055-0e088e75432f?q=80&w=1080',
    'ras_abu_galum_alt.jpg': 'https://images.unsplash.com/photo-1559827260-dc66d52bef19?q=80&w=1080',
    'map_preview.jpg': 'https://images.unsplash.com/photo-1524661135-423995f22d0b?q=80&w=1080',
    'home_hero_bg.jpg': 'https://images.unsplash.com/photo-1539650116574-8efeb43e2750?q=80&w=1600'
}

IMAGE_DIR = 'images'
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

print(f"Starting ABSOLUTE FINAL asset download via CURL to {IMAGE_DIR}...")

for name, url in URL_MAP.items():
    path = os.path.join(IMAGE_DIR, name)
    print(f"Downloading {name}...")
    
    # Always overwrite for the final run to be sure
    cmd = [
        'curl', 
        '-L', 
        '-A', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        '-o', path,
        url
    ]
    try:
        subprocess.run(cmd, check=True)
        size = os.path.getsize(path)
        if size < 1000:
            print(f"WARNING: {name} is only {size} bytes. Likely failed (404/Error).")
        else:
            print(f"Successfully finished {name} ({size} bytes)")
    except subprocess.CalledProcessError as e:
        print(f"Failed to download {name}: {e}")

# Create generic fallback
generic = os.path.join(IMAGE_DIR, 'generic_landscape.jpg')
if os.path.exists(os.path.join(IMAGE_DIR, 'white_desert.jpg')):
    import shutil
    shutil.copyfile(os.path.join(IMAGE_DIR, 'white_desert.jpg'), generic)
    print("Created generic_landscape.jpg")

print("Asset Healing complete.")
