import requests
from bs4 import BeautifulSoup

print("Привіт,я ваш персональний парсер\nЩо ви бажаєте дізнатись?")

while True:

    print("1. Провірить сайт на існування?\n2. Вивести текст\n3. Проаналізувать текст\n0. Вихід")
    userInput = str(input())


    if userInput == "0":
        break


    elif userInput == "1":

        print("Вставте url")
        userInput1 = str(input())

        try:
            r = requests.get(userInput1)

            if r.ok == True:
                print("Сайт існує")

            else:
                print("Сайта не існує або невірний url")

        except:
            print("невіриний url")


    elif userInput == "2":

        print("Вставте url")
        userInput2 = str(input())

        try:
            r = requests.get(userInput2)

            if r.ok == True:
                page = BeautifulSoup(r.text, 'html.parser')
                print(page)

            else:
                print("Сайта не існує")

        except:
            print("Перевірте url")


    elif userInput == "3":

        print("Вставте url")
        userInput2 = str(input())

        try:
            r = requests.get(userInput2)

            if r.ok == True:
                pass ##########################

            else:
                print("Сайт не існує)")

        except:
            print("Перевірте url")


    else:
        print("Щось не вірно")