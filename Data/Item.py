from array import array
from connexion import conn
from main import app
from pydantic import BaseModel

class Item(BaseModel):
    nameClass = "Item"
    id: int
    name: str
    age: int
    address: str
    mail: str

    items = []

    @staticmethod
    def generate_id():
        # Generation des ids
        id: Item.items.len() + 1
        return id

    def getAll(self):

        self.items.clear()
        command = conn.create_conn()
        command.execute("SELECT * FROM {self.nameClass}")
        rows = command.fetchall()
        for item in rows:
            self.items.append(item)
        conn.close_conn(command)

    @app.get("/Item/{id}")
    def read_Item(num : int, self):
        self.getAll()
        command = conn.create_conn()
        for itemCurrent in self.items:
            if  itemCurrent.id == num:
                return  {"Item :": itemCurrent}
            else:
                print ("not exist")
            break
        conn.close_conn(command)

    @app.post("/Item/create")
    def create_Item(self):
        self.getAll()

        newName = input("Nom :")
        newAge = input("Age :")
        newAddress = input("Address :")
        newMail = input("Mail :")

        command = conn.create_conn()
        command.execute("INSERT INTO {nameClass} VALUES {newName}, {newAge}, {newAddress}, {newMail}")
        conn.close_conn(command)

        return print("item created")

    @app.post("/Item/{id}/modify")
    def modify_Item(num : int, self):
        self.getAll()

        for itemCurrent in Item.items:
            if itemCurrent.id == num:
                print("Item trouvé")
                modif = 1
                while modif != 0:
                    modif = input("Quelle valeur voulez-vous modifiez ? 0 pour finir")
                    if modif == 0:
                        break
                    else:
                        command = conn.create_conn()
                        match modif:
                            case "name":
                                newName = input("Changer {Item.name} :")
                                command.execute("UPDATE {self.nameClass} SET name = {newName} WHERE id = {num}")
                                print("Name changed")
                            case "age":
                                newAge = input("Changer {Item.age} :")
                                command.execute("UPDATE {self.nameClass} SET age = {newAge} WHERE id = {num}")
                                print("Age change")
                            case "address":
                                newAddress = input("Changer {Item.address} :")
                                command.execute("UPDATE {self.nameClass} SET address = {newAddress} WHERE id = {num}")
                                print("Adresse change")
                            case "mail":
                                newMail = input("Changer {Item.mail} :")
                                command.execute("UPDATE {self.nameClass} SET mail = {newMail} WHERE id = {num}")
                                print("mail change")
                        conn.close_conn(command)
                return {"item modified"}
            else:
                print("not exists")
            break

    @app.post("/Item/{id}/delete")
    def suppr_Item(num : int, self):
        self.getAll()

        command = conn.create_conn()
        for itemCurrent in Item.items:
            if itemCurrent.id == num:
                delete = input("Supprimer {itemCurrent.name} ? Y/N")
                if delete == "Y":
                    command.execute("DELETE FROM {self.nameClass}")
                else:
                    break
            else:
                print ("not exist")
            break
        conn.close_conn(command)
        return {"item deleted"}
