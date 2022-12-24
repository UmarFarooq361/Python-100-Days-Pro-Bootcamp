# try , except , else , finally , raise

friends = ["umar", "ali", "masha"]

def find_friend(index):
    try:
      friend = friends[index]

    except IndexError:
        print("fruit pei")

    else:
        # global friend
        print("run successfully . ")
        print(friend + " is your friend")






find_friend(2)