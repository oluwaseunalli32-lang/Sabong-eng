import os
import time
import logging

logging.basicConfig(level=logging.INFO)
INTERVAL_SECONDS = int(os.getenv("WORKER_INTERVAL", 86400)) # Default: 24 hours

def run_background_tasks():
    logging.info("Background worker executed: Checking pending tasks / generating daily educational content...")
    # Add your background task logic here (e.g., broadcasting daily tips to a database or channel)

if __name__ == "__main__":
    logging.info("Background worker service started.")
    while True:
        try:
            run_background_tasks()
        except Exception as e:
            logging.error(f"Error in background worker: {e}")
        time.sleep(INTERVAL_SECONDS)
      
