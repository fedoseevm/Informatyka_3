file = open("ciagi.txt", "r")
lists = list(map(str, file.read().split("\n")))
# lists = file.readlines()
print(lists)

# for T in lists:
