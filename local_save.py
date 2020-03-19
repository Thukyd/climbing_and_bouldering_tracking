import json


################ TEST
import datetime

test_user_a = {
    "id" : "123456789",
    "surname" : "Mustermann",
    "forename" : "Max"
}
test_user_b = {
    "id" : "987654321",
    "surname" : "Doe",
    "forename" : "Jane"
}
## entry information
test_record_a = {
    "timetamp" : datetime.datetime.now().timestamp(),
    "grade" : "5+",
    "completion_type" : "on-sight",
    "scale" : 0
}

test_record_b = {
    "timetamp" : datetime.datetime.now().timestamp(),
    "grade" : "5+",
    "completion_type" : "on-sight",
    "scale" : 0
}
#########################

class Entries():
    def __init__(self):
        self.path = "./local/user_data.json"
        # set up intial file
        self.check_for_file()

    def check_for_file(self):
        try:
            with open(self.path) as file:
                pass
        except:
            with open(self.path, "w") as newFile:
                json.dump([], newFile)
                print("New File created")

    def add_user(self, data):
        # user 
        user = data[0]
        # single entry
        user["records"] = []
        user["records"].append(data[1])

        with open(self.path, "r+") as file:
            json_file = json.load(file)
            json_file.append(user)
            file.seek(0)
            json.dump(json_file, file)

    def search_user(self, user_id, data):
        return [element for element in data if element['id'] == user_id]
    
    def add_entry(self, data):

        user = data[0]
        #record = data[1]

        with open(self.path, "r+") as file:
            json_file = json.load(file)
            
 

            # search for user
            element = self.search_user(user["id"], json_file)

            print(element)
   
           
            # element = 1
            # # add new user
            # if element == []:
            #     user_id = user["id"]
            #     user["records"] = []
            #     #json_file.append(user)
            #     print(f"\nadd new user for {user_id}x")
            #add new record entry
            # else: 
            #     user_id = user["id"]
            #     print(f"\nadd new entry for {user_id}")
            #     element[0]["records"].append(record)



            # json_file.append(user)
            file.seek(0)
            #json.dump(json_file, file)


    # TODO
     # create a new json => done
     # create a new user => do
     # create a new entry for user 



Entries().add_entry([test_user_a, test_record_a])
Entries().add_entry([test_user_b, test_record_a])
# Entries().add_entry([test_user_a, test_record_b])
# Entries().add_entry([test_user_b, test_record_b])
# Entries().add_entry([test_user_b, test_record_a])