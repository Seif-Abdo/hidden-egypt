import os, subprocess

URL_MAP = {
    'siwa_1.jpg': 'https://images.unsplash.com/photo-1771236581590-9cf1463a7d59?q=80&w=1080',
    'siwa_2.jpg': 'https://images.unsplash.com/photo-1598337227515-5645318fb450?q=80&w=1080',
    'canyon_1.jpg': 'https://images.unsplash.com/photo-1561829728-da35df23beab?q=80&w=1080',
    'canyon_2.jpg': 'https://images.unsplash.com/photo-1547013406-e6a8f98bde65?q=80&w=1080',
    'white_desert_1.jpg': 'https://images.unsplash.com/photo-1643236312558-2725e111238b?q=80&w=1080',
    'white_desert_2.jpg': 'https://images.unsplash.com/photo-1542365516-e358b4f95d92?q=80&w=1080',
    'tunis_1.jpg': 'https://images.unsplash.com/photo-1695625195824-4893aaa04b85?q=80&w=1080',
    'tunis_2.jpg': 'https://images.unsplash.com/photo-1533052136932-6aeb851722cb?q=80&w=1080',
    'dendera_1.jpg': 'https://images.unsplash.com/photo-1723997326348-d4953661a61a?q=80&w=1080',
    'dendera_2.jpg': 'https://images.unsplash.com/photo-1562679302-6c6f03173bf5?q=80&w=1080',
    'galum_1.jpg': 'https://images.unsplash.com/photo-1668964413055-0e088e75432f?q=80&w=1080',
    'galum_2.jpg': 'https://images.unsplash.com/photo-1543320147-3dc61298c9dc?q=80&w=1080'
}

IMAGE_DIR = 'images'
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

print(f"Starting Phase 8 asset download via CURL to {IMAGE_DIR}...")

for name, url in URL_MAP.items():
    path = os.path.join(IMAGE_DIR, name)
    print(f"Downloading {name}...")
    
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
            print(f"WARNING: {name} is only {size} bytes. Failed.")
        else:
            print(f"Successfully finished {name} ({size} bytes)")
    except subprocess.CalledProcessError as e:
        print(f"Failed to download {name}: {e}")

print("Phase 8 Asset Download complete.")
