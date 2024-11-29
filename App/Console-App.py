#from App.Core1 import BookAction
from Core import BookAction
import time, msvcrt, argparse, threading, os


def animation_func():
   global stop_animation
   animation = "|/-\\"
   idx = 0
   while not stop_animation:
       print(animation[idx % len(animation)], end="\r")
       idx += 1
       time.sleep(0.1)


def run_animation():
   animation_func()

def main_menu():
    global stop_animation

    print('Книжный_СУБД v1 от Reborned~Tigrex')

    while True:
        ask = input("""\nВыберите действие: Добавить в базу данных (P),
Удалить книгу из базы данных по id (D),
Вывести все книги (A),
Забрать книгу по id (Сменить статус и количество) (T),
Найти книгу по id, автору, названию, году (S) \n \С помощью этого метода можно получить всю информацию о книге.
Увидеть анимацию (animation).
Выйти(X):\n""")
        match ask.lower():
            case "p":
                title = ' '.join(str(input("Введите название книги: ")).split())
                author = ' '.join(str(input("Введите автора: ")).split())
                year = str(input("Введите год написания книги: "))
                count = bool(input("Введите число книг (Любое целое вещественное): "))
                try:
                    bA.add(title,author,year, count)
                except Exception as err:
                    print(err)
            case "d":
                Id = str(input("Введите id: "))
                try:
                    bA.remove(item=Id)
                    print("Удалено.")
                except Exception as err:
                    print(err)
            case "a":
                print(bA.allPositions())
            case "t":
                Id = str(input("Введите id: "))
                count = int(input("Введите количество книг, что вы хотите забрать: "))
                status = int(input("Установите статус книги:\n Оставить всё на автоматике (0), \n Нет в наличии (1), \nЕсть в наличии (2)\n"))
                bA.take(Id,count,status)
                
                
            case "s":
                det = "".join(str(input("Введите поле, по которому искать: (author|title|id|year)")).split())
                Id = ' '.join(str(input("Введите подходящий идентификатор: (Название|Автор|Год|id) ")).split())
                try:
                    print(bA.search(Id,det))
                except Exception as err:
                    print(err)
            case "animation":
                animation_thread = threading.Thread(target=animation_func)
                stop_animation = False
                animation_thread.start()
                time.sleep(5)
                stop_animation = True
                animation_thread.join()
                continue
                
            case "x":
                quit()

if __name__ == "__main__":
    bA = BookAction()
    main_menu()
    temp = input("Для получения списка комманд введите help|man.")
    match temp:
        case "help":
            pass
        



# manager = BookAction()

# manager.add("Да", "Тодасё", 1866)
# manager.add("1984", "Тод Говард", 1949, count=1)

# manager.remove("0")
# print(manager.take("1"))
# manager.add("Да", "Тодасё", 1866)

# print("Информация о книге '1984':", manager.search("1984", "title"))
# print("Список всех книг:", manager.allPositions())
