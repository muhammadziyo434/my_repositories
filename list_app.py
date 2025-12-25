def load_from_file():
    try:
        with open("data.txt", "r") as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        return []

def save_to_file(lst):
    with open("data.txt", "w") as f:
        for item in lst:
            f.write(item + "\n")

def add_items_unlimited(lst):
    while True:
        item = input("Add item ( -1 : exit): ")
        if item.lower() == '-1':
            break
        lst.append(item)

def remove_item(lst):
    print(lst)
    h = int(input("Number of items you want to delete: "))
    for i in range(h):
        item_index = int(input("Which item do you want to delete (enter the order of item, starting from 1): "))
        if 1 <= item_index <= len(lst):
            deleted_item = lst.pop(item_index - 1)
            print(f"Deleted ✅  {deleted_item}")
        else:
            print("Not found ❌")

mylist = load_from_file()

while True:
    print("""
1. Add item
2. Remove item
3. Show list
4. Save
5. Exit
""")

    choice = int(input("Choose: "))

    match choice:
        case 1:
            add_items_unlimited(mylist)
        case 2:
            remove_item(mylist)
        case 3:
            print(mylist)
        case 4:
            save_to_file(mylist)
            print("Saved 💾")
        case 5:
            save_to_file(mylist)
            print("Bye 👋")
            break
        case _:
            print("Wrong choice")