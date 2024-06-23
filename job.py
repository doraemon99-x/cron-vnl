import time

import requests

# List of URLs
urls = [
    "https://str.skom.id/vid/vidh/tv.php?id=204",
    "https://str.skom.id/vid/vidh/tv.php?id=205",
    "https://str.skom.id/vid/vidh/tv.php?id=206",
    "https://str.skom.id/vid/vidh/tv.php?id=734",
    "https://str.skom.id/vid/vidh/tv.php?id=733",
    "https://str.skom.id/vid/vidh/tv.php?id=782",
    "https://str.skom.id/vid/vidh/tv.php?id=6852",
    "https://str.skom.id/vid/vidh/tv.php?id=7052",
    "https://str.skom.id/vid/vidmpd/tv.php?id=875",
    "https://str.skom.id/vid/vidmpd/tv.php?id=206",
    "https://str.skom.id/vid/vidmpd/tv.php?id=6685",
    "https://str.skom.id/vid/vidmpd/tv.php?id=6685",
    "https://str.skom.id/vid/vidmpd/tv.php?id=6686",
    "https://str.skom.id/vid/vidmpd/tv.php?id=6786",
    "https://str.skom.id/vid/vidmpd/tv.php?id=6299",
    "https://str.skom.id/vid/vidmpd/tv.php?id=6317",
]

# Visit each URL
for url in urls:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Visited {url} - Status code: {response.status_code} - Berhasil")
        else:
            print(f"Visited {url} - Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error visiting {url} - Error: {e}")
    
    time.sleep(30)  # Delay 30 detik
