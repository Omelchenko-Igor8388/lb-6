print("Вітаю у вашій бібліотеці економіки\nЩо ви бажаєте\n")

filePath = "text.txt"
one = "1.txt"
two = "2.txt"
three = "3.txt"
four = "4.txt"
five = "5.txt"
six = "6.txt"
seven = "7.txt"
eight = "8.txt"
nine = "9.txt"
ten = "10.txt"

while True:

    print("0. Вийти з бібліотеки\n1. Показати всі книги\n2. Додати книгу\n3. Взять книгу під номером...\n4. Пошук за назвою...\n5. Читати опис книги під номером...\n")

    userInput = str(input())

    if userInput == "0":
        break


    elif userInput == "1":

        file1 = open(filePath, "r", encoding='utf-8')
        file2 = file1.readlines()

        for line in file2:
            print(line)


    elif userInput == "2":

        print("Введіть доповнення")
        newData = (str(input()) + "\n")

        file1 = open(filePath, "a+", encoding='utf-8')
        file1.write(newData)
        file1.close()

        print("Данні додано\n")


    elif userInput == "3":

        print("Який рядок друкувати?")
        row1 = int(input())

        line = open(filePath, encoding='utf-8').readlines()[row1]
        print(line)



    elif userInput == "4":

        print("Введіть фамілію або бал")
        searchInput = str(input())

        file1 = open(filePath, "r", encoding='utf-8')
        file2 = file1.readlines()

        for row in file2:
            if searchInput in row:
                print(row)



    elif userInput == "5":

        print("Введіть номер кники")
        searchInput = str(input())

        if searchInput == "one":
            file1 = open(one, "r", encoding='utf-8')
            file2 = file1.readlines()

            for line in file2:
                print(line)

        elif searchInput == "two":
            file1 = open(two, "r", encoding='utf-8')
            file2 = file1.readlines()

            for line in file2:
                print(line)

        elif searchInput == "three":
            file1 = open(three, "r", encoding='utf-8')
            file2 = file1.readlines()

            for line in file2:
                print(line)

        elif searchInput == "four":
            file1 = open(four, "r", encoding='utf-8')
            file2 = file1.readlines()

            for line in file2:
                print(line)

        elif searchInput == "five":
            file1 = open(five, "r", encoding='utf-8')
            file2 = file1.readlines()

            for line in file2:
                print(line)

        elif searchInput == "six":
            file1 = open(six, "r", encoding='utf-8')
            file2 = file1.readlines()

            for line in file2:
                print(line)

        elif searchInput == "seven":
            file1 = open(seven, "r", encoding='utf-8')
            file2 = file1.readlines()

            for line in file2:
                print(line)

        elif searchInput == "eight":
            file1 = open(eight, "r", encoding='utf-8')
            file2 = file1.readlines()

            for line in file2:
                print(line)

        elif searchInput == "nine":
            file1 = open(nine, "r", encoding='utf-8')
            file2 = file1.readlines()

            for line in file2:
                print(line)

        elif searchInput == "ten":
            file1 = open(ten, "r", encoding='utf-8')
            file2 = file1.readlines()

            for line in file2:
                print(line)


else:
        print("Виберіть щось з списку")



