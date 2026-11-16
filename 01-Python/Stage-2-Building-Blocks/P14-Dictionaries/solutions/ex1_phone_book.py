contacts = {}

while True:
    choice = input("(a)dd (l)ookup (d)elete (s)how all (q)uit: ").lower()
    if choice == "a":
        name = input("Name: ")
        contacts[name] = input("Number: ")
    elif choice == "l":
        name = input("Name: ")
        print(contacts.get(name, "Not found"))
    elif choice == "d":
        name = input("Name: ")
        if name in contacts:
            del contacts[name]
            print("Deleted")
        else:
            print("Not found")
    elif choice == "s":
        for name in sorted(contacts):
            print(f"{name:15} {contacts[name]}")
    elif choice == "q":
        break
