from game_data import data

flag = True
present = False

while flag:
    print("To check follower of any celebrity by their name -->\n")
    user = input("Enter name: ")

    for i in data:
        if i["name"] == user:
            present = True
            print(f"{user} --> {i["follower_count"]}")

    if not present:
        print(f"{user} is not present in database")

    exit = input("To check again enter 'Y': ").lower()

    import os
    clear = lambda: os.system('cls')
    clear()
    
    if exit != "y":
        flag = False
