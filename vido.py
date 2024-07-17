import time
from datetime import datetime
import pytz
import schedule
from flask import Flask, jsonify
import threading

app = Flask(__name__)

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
        "url": "https://tipivid.000webhostapp.com/vidmpd/tv.php?id=204",
        "time": "14:50",
        "date": "2024-07-18"
    },
    {
        "url": "https://tipivid.000webhostapp.com/vidmpd/tv.php?id=206",
        "time": "19:05",
        "date": "2024-07-18"
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

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

@app.route('/')
def index():
    return jsonify({"message": "Web service is running. Scheduler is active."})

if __name__ == '__main__':
    # Jalankan scheduler dalam thread terpisah agar Flask tidak terblokir
    scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
    scheduler_thread.start()

    # Jalankan Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)
