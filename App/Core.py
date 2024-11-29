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
                json.dump({"Books": {}},file, ensure_ascii=False)
        with open(DB_path, "r+", encoding="utf-8") as file:
            try:
                json.load(file)
            except:
                print("[JSONDecodeError] in methood __init__: Файл базы данных не соответствует структуре Json. Удалите файл или исправьте вручную.")
    
    def add(self, title:str, author:str, year:int|str, count = 1) -> None:
        """Добавление книги в базу данных/ добавление к существующей книге параметра count. \n
        :param title: Название книги
        :param author: Автор книги
        :param year: Год написания книги"""

        try:
            # Проверка типов переменных
            if(not isinstance(author, str) and not isinstance(title, str)):
                raise Exception("[TypeError] Author и title должен быть string!")
            if(count <= 0):
                raise Exception("[RealityError] Ошибка. Число книг должно быть вещественным целым.")
        # ____________________________________________________________
            statusHave = "На хранении"
            with open(DB_path, "r+", encoding="utf-8") as file:
                data = json.load(file)
                subObj = data["Books"]
                for obj in subObj.keys():
                    if subObj[obj]["title"] == title:
                        subObj[obj]["count"] += count
                        subObj[obj]["status"] = statusHave
                        
                        data["Books"] = subObj

                        file.seek(0)
                        json.dump(data, file, indent=4, ensure_ascii=False)
                        return(None)

                next_id = 0

                while True:
                    if str(next_id) not in data["Books"].keys():
                        break
                    next_id += 1
                
                data["Books"].update({str(next_id): 
                                      {"title": title,
                                        "author": author,
                                        "year": str(year), 
                                        "count": int(count),
                                        "status": statusHave}})

                file.seek(0)
                json.dump(data, file, indent=4, ensure_ascii=False)
                return(None)
        # ---------------------------------------------------
        except Exception as err:
            print("Panic! In methood add:",err)
        finally:
            file.close()
    
    def search(self, identificator:str, det:str) -> list[tuple[dict, str]]|None:
        """
        Функция поиска по любому идентификатору книги. Возвращает ```list[tuple[dict, str]]```, где ```dict``` это объект книга, а ```str``` это ```id``` этой книги в базе данных. \n
        :param identificator: Введите название книги, либо ```id```, либо автора, либо год написания.
        :param det: На выбор предоставляется поиск по title, id, author, year
        """
        # :param pointerOut: Позволяет получить все номера битов объектов подходящих по заданным условиям
        try:
            if det not in ["title", "id", "author", "year"]:
                raise Exception("[DetError] Вы указали неверный идентификатор данных! Используйте: title, id, author или year")
            
            with open(self.file_path, mode="r",encoding="utf-8") as file:
                out = []
                identificator = str(identificator).lower()
                data = json.load(file)
                subObj = data["Books"]
                match det:
                    case "title":
                        for obj in subObj.keys():
                            if subObj[obj]["title"].lower() == identificator:
                                out.append([subObj[obj], obj])
                    case "id":
                        for obj in subObj.keys():
                            if obj == identificator:
                                return [subObj[obj], obj]
                    case "author":
                        for obj in subObj.keys():
                            if subObj[obj]["author"].lower() == identificator:
                                out.append([subObj[obj], obj])
                    case "year":
                        for obj in subObj.keys():
                            if str(subObj[obj]["year"]) == str(identificator):
                                out.append([subObj[obj], obj])
                if len(out) == 0:
                        raise Exception("[DataNotExist] Такого идентификатора не существует в базе данных!")
                return(out)
        except Exception as err:
            print("Panic! In methood search:",err)
        finally:
            file.close()
        
    
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
        :param count: Необязательный параметр. По умолчанию этот параметр равен ```1```. Параметр отвечает за количество взятых книг из базы данных
        :param ForseStatus: Необязательный параметр. По умолчанию этот параметр равен ```0```. Параметр насильно присваевает значение ```status``` в таблице. Если значение ```1```, метод игнорирует количество книг и насильно присваевает значение ```Нет в наличии```. Если значение ```2```, метод игнорирует автоматику и присваевает ```Есть в наличии```.
        """
        try:
            with open(self.file_path, mode="r+",encoding="utf-8") as file:
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
                            file.seek(0)
                            data["Books"][obj] = subObj
                            json.dump(data, file, indent=4, ensure_ascii=False)
                            return subObj
                        else:
                            raise Exception(f"[CountError] Количество этих книг: {data["Books"][obj]["count"]}. Невозможно взять книгу!")
        except Exception as err:
            print("Panic! In methood take:",err)
        finally:
            file.close()


    def remove(self, item:str)-> None:
        """Функция полностью удаляет запись из базы данных
        :param item: В этот параметр передаётся """

        Exception = "Такого id не существует!"
        try:
            with open(self.file_path, mode="r",encoding="utf-8") as file:
                data = json.load(file)
            del data["Books"][item]
                
            with open(self.file_path, mode="w",encoding="utf-8") as file:
                file.seek(0)
                json.dump(data, file, indent=4, ensure_ascii=False)
            
        except Exception as err:
            print("Panic! In methood remove:",err)

    def allPositions(self)-> list[dict]:
        out = []
        with open(self.file_path, mode="r+",encoding="utf-8") as file:
            data = json.load(file)
            for item in data["Books"].keys():
                out.append(data["Books"][item])
            return(out)
        # return(data["Books"])
