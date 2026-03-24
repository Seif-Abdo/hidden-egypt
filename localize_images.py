import os, glob, codecs, re
import urllib.request
import hashlib

print("Starting global image localization process...")

IMAGE_DIR = "images"
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)
    print(f"Created directory: {IMAGE_DIR}")

def download_image(url, filename):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            with open(filename, 'wb') as f:
                f.write(response.read())
        return True
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return False

# Regex to find all Unsplash URLs
url_pattern = re.compile(r'https://images\.unsplash\.com/[^\s\'"\)]+')

# 1. Collect all unique URLs from HTML and CSS files
target_files = glob.glob("*.html") + glob.glob("css/*.css")
url_map = {} # Maps original URL to local path
url_count = 0

for file in target_files:
    with codecs.open(file, 'r', 'utf-8') as f:
        content = f.read()
    
    matches = url_pattern.findall(content)
    for url in set(matches):
        if url not in url_map:
            # Generate a consistent filename
            url_count += 1
            # We can extract the photo ID or just use a generic name
            # e.g. photo-1552309398-fd0f5d4e35be
            match = re.search(r'photo-([a-zA-Z0-9\-]+)', url)
            if match:
                base_name = f"bg_{match.group(1)}.jpg"
            else:
                base_name = f"image_{url_count}.jpg"
            
            local_path = os.path.join(IMAGE_DIR, base_name)
            # Use forward slashes for CSS/HTML linking
            web_path = f"images/{base_name}"
            
            url_map[url] = {
                'local_path': local_path,
                'web_path': web_path,
                'downloaded': False
            }

print(f"Discovered {len(url_map)} unique external images. Starting download...")

# 2. Download Images
for url, data in url_map.items():
    if not os.path.exists(data['local_path']):
        success = download_image(url, data['local_path'])
        data['downloaded'] = success
        if success:
            print(f"Downloaded: {data['web_path']}")
    else:
        print(f"Already exists: {data['web_path']}")
        data['downloaded'] = True

# 3. Replace URLs in all files
modified_files_count = 0
for file in target_files:
    with codecs.open(file, 'r', 'utf-8') as f:
        content = f.read()
    
    new_content = content
    for old_url, data in url_map.items():
        if data['downloaded']:
            # Replace exactly
            # Need to handle potential nested quotes in url() inside CSS, but replace is safe
            new_content = new_content.replace(old_url, data['web_path'])
    
    if new_content != content:
        with codecs.open(file, 'w', 'utf-8') as f:
            f.write(new_content)
        modified_files_count += 1
        print(f"Patched: {file}")

print(f"Successfully localized all images across {modified_files_count} files!")
