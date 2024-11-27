import json, os, logging

Absolute_path = os.getcwd()[:os.getcwd().rfind("\\")]


DB_path = f"{Absolute_path}\\Data\\books.json"
""":Path в переменной: ***f'{Absolute_path}\\Data\\books.json'***"""

class BookAction:
    """Библиотека работы с базой данных в формате json. \n
    :methood BookAction.add(): Добавление книги в базу данных
    :methood BookAction.getInfo(): Получение информации о конкретной книге
    :methood BookAction.take():
    :methood BookAction.remove():
    :methood:"""
    def __init__(self:object, file_path=DB_path) -> object:
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, mode="w+", encoding="utf-8") as file:
                json.dump({"Books": {}},file)
    
    def add(self, title:str, author:str, year:str) -> None:
        """Добавление книги в базу данных. \n
        :param title: Название книги
        :param author: Автор книги
        :param year: Год написания книги"""
        try:
            # Проверка типов переменных
            if(not isinstance((author, title), str)):
                raise Exception(TypeError, "Author must be string!")
        # ____________________________________________________________
            count = 1
            statusHave = "На хранении"
            with open(DB_path, "r+", encoding="utf-8") as file:
                data = json.load(file)

                for obj in data["Books"].keys():
                    if obj["title"].lower() == title.lower:
                        int(obj["count"]) += 1
                        obj["status"] = statusHave
                        return(0)

                
                next_id = len(data["Books"].keys())
                data["Books"].update({next_id: {"title": title, "author": author, "year": year, "count": int(count), "status": statusHave}})

                file.seek(0)
                json.dump(data, file, indent=4)
            return(0)
        
        # ---------------------------------------------------
        except Exception as err:
            print(err)
            return(-1)
    
    def _parseFile(self, identificator:str):

        
    
    def getInfo(self, title):
        """ """
        try:
            with open(self.file_path, mode="r",encoding="utf-8") as file:
                data = json.load(file)
                for obj in data["Books"].keys():
                    if obj["title"] == title:
                        return obj
                raise Exception(NameError)
        except Exception as er:
            print(er, "Такой книги не существует в базе данных!")
            return None
                    
    def take(self, title):
        """Функция изменения статуса выдачи книги. \n
            Будут затронуты поля status и count"""
        pass

    def remove(self, identifier:str):
        with open(self.file_path, mode="r+",encoding="utf-8") as file:
            data = json.load(file)
        del data["Books"][identifier]
            
        with open(self.file_path, mode="w",encoding="utf-8") as file:
            file.seek(0)
            json.dump(data, file, indent=4)
    
    def allPositions()-> dict:
        pass