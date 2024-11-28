#from App.Core1 import BookAction
from Core import BookAction

manager = BookAction()

manager.add("Да", "Тодасё", 1866)
manager.add("1984", "Тод Говард", 1949)

# manager.remove("0")

print("Информация о книге '1984':", manager.getInfo("1984"))
# print("Список всех книг:", manager.allBooks())

# manager.remove(1)
# print("Список всех книг после удаления:", manager.allBooks())
