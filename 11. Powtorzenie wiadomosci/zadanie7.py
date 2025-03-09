with open("ciagi.txt", "r") as file:
    ciags = list(file.readlines())
    for line in ciags:
        numbers = list(map(int, line.split()))
        print(numbers)

        n = len(numbers)
        for i in range(n - 2):
            if sum(numbers[i:i + 2]) == 10:
                print(numbers)
                break
