import subprocess
import time

def run_job():
    try:
        # Menjalankan file job.py
        result = subprocess.run(['python', 'job.py'], capture_output=True, text=True)
        
        # Menampilkan output dari eksekusi file job.py
        print("Output:\n", result.stdout)
        print("Error (jika ada):\n", result.stderr)
        
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    while True:
        run_job()
        # Menunggu selama 3 jam (3 * 60 * 60 detik)
        time.sleep(3 * 60 * 60)
