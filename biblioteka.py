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

        print("Яку книгу бажаєте додати?")
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

        print("Введіть назву книги")
        searchInput = str(input())

        file1 = open(filePath, "r", encoding='utf-8')
        file2 = file1.readlines()

        for row in file2:
            if searchInput in row:
                print(row)



    elif userInput == "5":

        print("Введіть номер кники")
        searchInput = str(input())

        searchInputAnswers = ["one", "two", "tree", "four", "five", "six", "seven", "eight", "nine", "ten"]

        if searchInput in searchInputAnswers:
            file1 = open(searchInput, "r", encoding='utf-8')
            file2 = file1.readlines()

            for line in file2:
                print(line)

        else:
            print("Неіснує такої книжки")


    else:
            print("Виберіть щось з списку")