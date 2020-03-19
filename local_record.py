import json

class Entries():
    def __init__(self):
        self.path = "./local/user_data.json"

    def search_user(self, user_id, data):
        # returns matching dictionary
        return [element for element in data if element['id'] == user_id]
    
    def add_entry(self, data):

        user = data[0]
        record = data[1]

        with open(self.path, "r+") as file:
            json_file = json.load(file)
            file.seek(0)

            # search for
            element = self.search_user(user["id"], json_file)

            # add new user
            if element == []:
                # add empty list of records
                user["records"] = []
                # add new user with new record
                json_file.append(user)
            # add new record entry 
            else: 
                user_id = user["id"]
                element[0]["records"].append(record)

            file.truncate()
            json.dump(json_file, file)


# TODO: Create a module!!!





################ TEST
# import datetime

# test_user_a = {
#     "id" : "123456789",
#     "surname" : "Mustermann",
#     "forename" : "Max"
# }
# test_user_b = {
#     "id" : "987654321",
#     "surname" : "Doe",
#     "forename" : "Jane"
# }
# ## entry information
# test_record_a = {
#     "timetamp" : datetime.datetime.now().timestamp(),
#     "grade" : "5+",
#     "completion_type" : "on-sight",
#     "scale" : 0
# }

# test_record_b = {
#     "timetamp" : datetime.datetime.now().timestamp(),
#     "grade" : "5+",
#     "completion_type" : "on-sight",
#     "scale" : 0
# }
#
# Entries().add_entry([test_user_a, test_record_a]) #NEW USER
# Entries().add_entry([test_user_b, test_record_a]) #ADD RECORD
# Entries().add_entry([test_user_a, test_record_b])
# Entries().add_entry([test_user_b, test_record_b])
# Entries().add_entry([test_user_b, test_record_a])