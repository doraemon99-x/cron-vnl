import subprocess
import time
from datetime import datetime, timedelta
import pytz

def run_job():
    try:
        # Menjalankan file job.py
        result = subprocess.run(['python', 'jobvn.py'], capture_output=True, text=True)
        
        # Menampilkan output dari eksekusi file job.py
        print("Output:\n", result.stdout)
        print("Error (jika ada):\n", result.stderr)
        
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def job():
    print("Menjalankan job pada waktu yang dijadwalkan")
    run_job()

def schedule_job_on_specific_date():
    # Tentukan zona waktu WIB
    wib = pytz.timezone('Asia/Jakarta')
    
    # Tanggal target
    target_date = datetime(2024, 6, 23, tzinfo=wib)

    # Daftar waktu target dalam satu hari
    target_times = [
        "09:51",
        "13:51",
        "16:51",
        "17:51",
        "21:21"
    ]

    while True:
        # Dapatkan waktu saat ini di zona waktu WIB
        now = datetime.now(wib)

        # Periksa apakah hari ini adalah tanggal target
        if now.date() == target_date.date():
            next_run = None
            sleep_duration = None

            # Cari waktu target berikutnya
            for target_time_str in target_times:
                target_time = datetime.strptime(target_time_str, "%H:%M").time()
                target_datetime = datetime.combine(now.date(), target_time, wib)
                
                # Jika waktu target telah lewat untuk hari ini, set untuk hari berikutnya
                if now > target_datetime:
                    continue

                if next_run is None or target_datetime < next_run:
                    next_run = target_datetime

            if next_run:
                sleep_duration = (next_run - now).total_seconds()
                print(f"Menunggu hingga {next_run.strftime('%Y-%m-%d %H:%M:%S')} WIB untuk menjalankan job.")
                time.sleep(sleep_duration)
                
                # Jalankan job pada waktu yang telah ditentukan
                job()
            else:
                # Semua waktu target telah lewat untuk hari ini
                print("Semua waktu target telah lewat untuk hari ini.")
                break
        else:
            # Jika bukan tanggal target, tunggu sampai tanggal target
            time_until_target = (target_date - now).total_seconds()
            print(f"Menunggu hingga {target_date.strftime('%Y-%m-%d')} WIB untuk menjalankan job.")
            time.sleep(time_until_target)

if __name__ == "__main__":
    schedule_job_on_specific_date()
