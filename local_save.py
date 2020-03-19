import json


################ TEST
import datetime

test_user = {
    "id" : "123456789",
    "surname" : "Mustermann",
    "forename" : "Max"
}
## entry information
test_record = {
    "timetamp" : datetime.datetime.now().timestamp(),
    "grade" : "5+",
    "completion_type" : "on-sight",
    "scale" : 0
}
#########################

class Entries():
    def __init__(self):
        self.path = "./local/user_data.json"

    def add(self, data):
        # user 
        user = data[0]
        # single entry
        user["records"] = []
        user["records"].append(data[1])
        # add as array
        entry = [user]

        with open(self.path, "a+") as outfile:
            json.dump(entry, outfile)

        print("entry successfully added")

    # TODO
     # create a new json
     # crearte a new user 
     # create a new entry for user


Entries().add([test_user, test_record])
Entries().add([test_user, test_record])