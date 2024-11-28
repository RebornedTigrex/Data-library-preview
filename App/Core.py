import json, os, logging

Absolute_path = os.getcwd().replace("App", "")


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
    # TODO add
    def add(self, title:str, author:str, year:str, count = 1) -> None:
        """Добавление книги в базу данных/ добавление к существующей книге параметра count. \n
        :param title: Название книги
        :param author: Автор книги
        :param year: Год написания книги"""
        # try:
        #     # Проверка типов переменных
        #     if(not isinstance(author, str) and not isinstance(title, str)):
        #         raise Exception(TypeError, "Author и title должен быть string!")
        # ____________________________________________________________
        statusHave = "На хранении"
        with open(DB_path, "r+", encoding="utf-8") as file:
            data = json.load(file)
            subObj = data["Books"]
            for obj in subObj.keys():
                if subObj[obj]["title"].lower() == title.lower():
                    subObj[obj]["count"] += 1
                    subObj[obj]["status"] = statusHave

            
            next_id = len(data["Books"].keys())
            data["Books"].update({next_id: {"title": title, "author": author, "year": year, "count": int(count), "status": statusHave}})

            file.seek(0)
            json.dump(data, file, indent=4)
        
        # ---------------------------------------------------
        # except Exception as err:
        #     print(err)
        #     return(-1)
    
    def search(self, identificator:str, det = "id" """, pointerOut = False""") -> list[dict]|None:
        """:param det: На выбор предоставляется поиск по title, id, author, year \n"""
        # :param pointerOut: Позволяет получить все номера битов объектов подходящих по заданным условиям
        try:
            with open(self.file_path, mode="r",encoding="utf-8") as file:
                out = []
                data = json.load(file)
                match det:
                    case "title":
                        for obj in data["Books"].keys():
                            if data[obj]["title"] == identificator:
                                out.append(data[obj])
                    case "id":
                        for obj in data["Books"].keys():
                            if obj == identificator:
                                return data[obj]
                    case "author":
                        for obj in data["Books"].keys():
                            if data[obj]["author"] == identificator:
                                out.append(data[obj])
                    case "year":
                        for obj in data["Books"].keys():
                            if data[obj]["year"] == identificator:
                                out.append(data[obj])
                if len(out) == 0:
                     raise Exception(NameError)
                return(out)
        except Exception as err:
            print(err, "Такого идентификатора не существует в базе данных!")
            return(None)
        
        #     raise Exception(NameError)
        # except Exception as er:
        #     print(er, "Такого идентификатора не существует в базе данных!")
        #     return None
        
    
    # def getInfo(self, title):
    #     """ """
    #     # try:
    #     with open(self.file_path, mode="r",encoding="utf-8") as file:
    #         data = json.load(file)
    #         for obj in data["Books"].keys():
    #             if data[obj]["title"] == title:
    #                 return data[obj]
    #     #     raise Exception(NameError)
    #     # except Exception as er:
    #     #     print(er, "Такого идентификатора не существует в базе данных!")
    #     #     return None
                    
    def take(self, id:str, count = 1, ForseStatus = 0) -> list[dict]:
        """Функция изменения статуса выдачи книги. Будут затронуты поля status и count.\n
        :param id: Этот параметр принимает id номер книги.
        :param count: Необязательный параметр. По умолчанию этот параметр равен ```1```. Он отвечает за количество взятых книг из базы данных
        :param ForseStatus: Необязательный параметр. По умолчанию этот параметр равен ```0```. Он насильно присваевает значение ```status``` в таблице. Если значение ```1```, метод игнорирует количество книг и насильно присваевает значение ```Нет в наличии```. Если значение ```2```, метод игнорирует автоматику и присваевает ```Есть в наличии```.
        """

        with open(self.file_path, mode="w+",encoding="utf-8") as file:
            data = json.load(file)
            for obj in data["Books"].keys():
                if obj == id:
                    subObj = data["Books"][obj]
                    if subObj["count"] - count >= 0:
                        subObj["count"] -= count
                        if subObj["count"] <= 0 and ForseStatus == 0:
                            subObj["status"] = "Нет в наличии"
                        elif ForseStatus <= 1:
                            subObj["status"] = "Нет в наличии"
                        elif ForseStatus >= 2:
                            subObj["status"] = "На хранении"
                        return subObj
                    else:
                        raise Exception(f"Количество книг {data["Books"][obj]["count"]}. Невозможно взять новую!")

 

    def remove(self, id:str)-> None:
        """Функция полностью удаляет запись из базы данных"""

        with open(self.file_path, mode="r+",encoding="utf-8") as file:
            data = json.load(file)
        del data["Books"][id]
            
        with open(self.file_path, mode="w",encoding="utf-8") as file:
            file.seek(0)
            json.dump(data, file, indent=4)
    

    def allPositions(self)-> list[dict]:
        out = []
        with open(self.file_path, mode="r+",encoding="utf-8") as file:
            data = json.load(file)
            for item in data["Books"]:
                out.append(item)
        return(out)
