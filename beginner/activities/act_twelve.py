# Youtube Manager using sqlite3

import sqlite3

conn = sqlite3.connect("youtube.db")

cursor = conn.cursor()

cursor.execute(''' 
               CREATE TABLE IF NOT EXISTS videos (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                time TEXT NOT NULL
    )
''')
def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)
def add_video(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)",(name,time))
    conn.commit()
def update_video(video_id,name,time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?",(name,time,video_id))
    conn.commit()
def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?",(video_id,))
    conn.commit()
def main():
    while True:
        print("\n Youtube Manager App with DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter name: ")
            time = input("Enter time: ")
            add_video(name,time)
        elif choice == '3':
            video_id = input("Enter video id: ")
            name = input("Enter name: ")
            time = input("Enter time: ")
            update_video(video_id,name,time)
        elif choice == '4':
            video_id = input("Enter video id: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice entered")
    conn.close()     
if __name__ == "__main__":
    main()

