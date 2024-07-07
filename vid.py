import time
from datetime import datetime

import pytz
import schedule


def get_response(url):
    import requests  # Import di dalam fungsi agar bisa dieksekusi dalam schedule
    try:
        response = requests.get(url)
        response.raise_for_status()  # Memeriksa apakah permintaan berhasil
        return response.text
    except requests.exceptions.HTTPError as http_err:
        return f'HTTP error occurred: {http_err}'
    except Exception as err:
        return f'Other error occurred: {err}'

def job(url):
    response = get_response(url)
    print(f'Response from {url}:\n{response}\n')

# Daftar URL dan waktu eksekusi
tasks = [
    {
        "url": "https://tipivid.000webhostapp.com/vidmpd/tv.php?id=17470",
        "time": "07:00",
        "date": "2024-07-10"
    },
        {
        "url": "https://tipivid.000webhostapp.com/vidmpd/tv.php?id=17470",
        "time": "07:03",
        "date": "2024-07-10"
    }
    # Tambahkan tugas lainnya di sini
]

wib = pytz.timezone('Asia/Jakarta')

def check_and_run_jobs():
    current_time = datetime.now(wib).strftime("%H:%M")
    current_date = datetime.now(wib).strftime("%Y-%m-%d")
    for task in tasks:
        if current_time == task['time'] and current_date == task['date']:
            job(task['url'])
            tasks.remove(task)  # Hapus tugas yang sudah dijalankan
            if not tasks:
                return schedule.CancelJob  # Batalkan penjadwalan jika tidak ada tugas lagi

schedule.every(1).minutes.do(check_and_run_jobs)

print("Menunggu hingga waktu yang dijadwalkan untuk mengeksekusi job...")

while True:
    schedule.run_pending()
    time.sleep(1)
