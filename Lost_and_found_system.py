lost_items = []

def add_lost_item():
    item = input("Enter item name: ")
    location = input("Enter location found/lost: ")
    lost_items.append({"item": item, "location": location})
    print("Item recorded")

def view_lost_items():
    if not lost_items:
        print("No lost items recorded")
    else:
        for item in lost_items:
            print(item["item"], "- Location:", item["location"])

def main():
    while True:
        print("1. Add Lost Item")
        print("2. View Lost Items")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_lost_item()
        elif choice == "2":
            view_lost_items()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
