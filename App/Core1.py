import json, os, logging

Absolute_path = os.getcwd()[:os.getcwd().rfind("\\")]
DB_path = f"{Absolute_path}\\Data\\books.json"

fieldnames = [{"id":{"title":{}, "author":{}, "year":{}, "status":{}}}]

class BookAction:
    """Библиотека работы с базой данных в формате json. \n
    :mehood BookAction.add(self, title:str, author:str, year:str):"""
    def __init__(self:object, file_path=DB_path) -> object:
        """:param file_path: Путь до базы данных. Стандартный путь является абсолютным и находится от Core: Data/books.json"""
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, mode="w+") as file:
                json.dump({"Books": []},file)
    
    
    def add(self, title:str, author:str, year:str)-> bool:
        """Добавление книги в базу данных. \n
        Если книга не будет добавлена, то эта функция выдаст False и запишет в логи подробности."""
        with open(self.file_path, mode="r+", encoding="UTF-8") as file:
            data = json.load(file)
            status = "В наличии"
            next_id = int(len(data)) # Получаем следующий ID
            #data["Books"] = ({"id": next_id, "title": title, "author": author, "year": year, "status":status})
            data["Books"] = ({next_id:{"title": title, "author": author, "year": year, "status":status}})
            file.seek(0)  # Возвращаемся в начало файла
            json.dump(data, file, indent=4)  # Записываем обновленный список книг

    def _compare():
        pass

    def remove(self, identifier:str):
        """"""
        with open(self.file_path, mode="r+") as file:
            data = json.load(file)
            data["Books"][str(identifier)] = 
            file.seek(0)
            file.truncate()  # Очищаем файл
            json.dump(data, file, indent=4)

    def getInfo(self, title):
        with open(self.file_path, mode="r") as file:
            data = json.load(file)
            for item in data["Books"].keys():
                if data["Books"][item]["title"].lower() == title.lower():
                    return item
        return None

    def allBooks(self) -> list:
        with open(self.file_path, mode="r") as file:
            return json.load(file)



# def check_file():
#     if not (os.path.exists(DB_path)):
#         pass
    

# def append(id, title, author, year, status)-> None:
#     with open(DB_path, mode="w+") as csvfile:
#         reader = csv.reader(csvfile, delimiter=",", quotechar="|")
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         for row in reader:
#             print(row)

#         if fieldnames not in reader:
#             writer.writeheader()
#         else:
#             print("Заголовок найден")

#     with open(DB_path,"a") as csvfile:
#         writer = csv.writer(csvfile, delimiter=",", quotechar="|")
#         writer.writerow([id, title, author, year, status])
#     print("Завершено")

# def read_all():
#     with open(DB_path, "r") as reader:
#         for row in reader:
#             print(row)

