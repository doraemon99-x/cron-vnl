import time

import requests

# List of URLs
urls = [
    "https://str.skom.id/vid/vidmpd/tv.php?id=17470",
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
