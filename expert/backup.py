import shutil
import os
import datetime
import schedule
import time

def create_backup(source_path, destination_path):
    date_name = datetime.date.today()
    backup_name = os.path.join(destination_path, f"backup_{date_name}")
    try:
        if not os.path.exists(source_path):
            print(f"Error: Source path '{source_path}' does not exist")
            return
        
        os.makedirs(destination_path, exist_ok=True)
        shutil.make_archive(backup_name, 'gztar', source_path)
        print(f"Backup completed: {backup_name}.tar.gz")
    except Exception as e:
        print(f"Backup failed: {e}")

source_path = input("Enter source path: ").strip()
destination_path = input("Enter destination path: ").strip()

create_backup(source_path, destination_path)

# Schedule daily backups
schedule.every().day.at("10:30").do(create_backup, source_path, destination_path)
print("Daily backup scheduled at 10:30 AM")


try:
    while True:
        schedule.run_pending()
        time.sleep(60)
except KeyboardInterrupt:
    print("\nScheduler stopped")