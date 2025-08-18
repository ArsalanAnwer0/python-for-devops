
import json
from queue import Empty

def add_book(book,name,author,year):
    book.append({"name":name,"author":author,"year":year})
    try:
        save_to_file(book)
    except Exception as e:
        ("Error")
def view_all_book(book):
    print("\n Books list: ")
    for index,b in enumerate(book,start = 1):
        print(f"- Name: {b["name"]}, Author: {b["author"]}, Year: {b["year"]}")
def save_to_file(book):
    with open("library.txt",'w') as file:
        json.dump(book,file)

def load_from_file(filename = "library.txt"):
    try:
        with open("library.txt",'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        return {}
    except Empty:
        return {}
    
def search_in_book(book,name):
    for x,y in enumerate(book,start=1):
        if y["name"] == name:
            print(f"name: {y["name"]}, author: {y["author"]},year: {y["year"]}")
    
def main():
    book = load_from_file()
    while True:
        print("\n Library Management System\n")
        print("1. Add book")
        print("2. View all books")
        print("3. Search Book")
        print("4. Remove Book")
        print("5. Save to file")
        print("6. Load from file")
        print("7. Exit\n")
        
        try:
            choice = int(input("Choose option: "))
        except Exception as e:
            print(f"Error: {e}")
        
        match choice:
            case 1:
                name = input("Enter name: ")
                try:
                    year = int(input("Enter year: "))
                except ValueError:
                    print("Invalid input")
                    break
                author = input("Enter author: ")
                add_book(book,name,author,year)
            case 2:
                view_all_book(book)
                
            case 3:
                # search by what
                # only by name
                name = input("Enter book name: ")
                search_in_book(name)
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                break
            case _: 
                print("Invalid choice")
            
        
if __name__ == "__main__":
    main()