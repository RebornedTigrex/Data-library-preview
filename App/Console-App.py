#from App.Core1 import BookAction
from Core import BookAction
import time, keyboard


manager = BookAction()

class m:
    def dM():
        print("Книга удалена!")
        return ""

    def pressBtn():
        print("\n Для продолжения нажмите любую клавишу:\n")
        while keyboard.read_key() == False:
            pass
        return ""

def auto():
    print("Приготовьтесь, мы добавляем книгу:")
    time.sleep(1)
    print("Автор этой книги будет: Пьер Кюри,")
    time.sleep(0.5)
    print("Название будет: 'Игра радиоактивным стержнем на рояле'")
    time.sleep(0.5)
    print("Год будет: 1685\n")
    
    manager.add("Игра радиоактивным стержнем на рояле","Пьер Кюри",1685)
    time.sleep(1)
    print("Добавим ещё парочку книг для наглядности. \nId ключ будет создан по порядку: Если какой-то элемент будет удалён - его id будет занято новым объектом.")
    
    manager.add("Увеселительные напитки: Бытие бармена", "Тодасё", 1866)
    manager.add("1984", "Тод Говард", 1949, count=2)

    print("Сейчас вы можете взглянуть в Data/books.json.",m.pressBtn())

    print("А сейчас мы удалим книгу Тода Говарда из базы данных.")
    time.sleep(1)
    print(" Вот дела! Я не знаю id этой книги! Придётся найти её с помощью метода search.")
    time.sleep(0.5)
    temp = manager.search("Тод Говард","author")[0][1]
    print(f"Id книги Говарда будет:{temp}. Удалим же её.")
    time.sleep(0.5)
    m.dM()
    print("Теперь вы можете взглянуть снова на наш файл.", m.pressBtn())

    print("Мы можем забрать книгу из нашей библиотеки: Для этого есть метод take")
    
    
    


if __name__ == "__main__":
    print("Здравствуйте! Вы запустили СУБД для управления книгами.")
    while i.lower() not in ["autotest", "selftest", "a", "s"]:
        i = input("Если вы хотите запустить тест: напишите autoTest (a),\n если вы хотите попробовать функционал самостоятельно, то напишите selfTest (s)")

    match i.lower()[:1]:
        case "a":
            auto()
        



# manager = BookAction()

# manager.add("Да", "Тодасё", 1866)
# manager.add("1984", "Тод Говард", 1949, count=1)

# manager.remove("0")
# print(manager.take("1"))
# manager.add("Да", "Тодасё", 1866)

# print("Информация о книге '1984':", manager.search("1984", "title"))
# print("Список всех книг:", manager.allPositions())
