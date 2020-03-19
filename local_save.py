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
    
    def add_entry(self, data):
        # user 
        user = data[0]
        
        # check if user exists
        

        # add current record entry
        #user["records"] = []
        #user["records"].append(data[1])

        
        print(user["id"])

        with open(self.path, "r+") as file:
            json_file = json.load(file)
            
            if not any(d.get('id', None) == user["id"] for d in json_file):
                
                print("It does not exist")
            else:
                
                print("Already there, buddy")

            #json_file.append(user)
            #file.seek(0)
            #json.dump(json_file, file)


    # TODO
     # create a new json => done
     # create a new user => do
     # create a new entry for user 



Entries().add_entry([test_user_a, test_record_a])
Entries().add_entry([test_user_b, test_record_a])
Entries().add_entry([test_user_a, test_record_a])
Entries().add_entry([test_user_b, test_record_a])
Entries().add_entry([test_user_b, test_record_a])