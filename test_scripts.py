import datetime
import main

test_user_a = {
    "_id" : "123456789",
    "surname" : "Mustermann",
    "forename" : "Max"
}

test_user_b = {
    "_id" : "987654321",
    "surname" : "Doe",
    "forename" : "Jane"
}

test_user_c = {
    "_id" : "44444444",
    "surname" : "New",
    "forename" : "User"
}

test_user_d = {
    "_id" : "88888888",
    "surname" : "Wumpermann",
    "forename" : "Alfred"
}


test_record_a = {
    "timetamp" : datetime.datetime.now().timestamp(),
    "grade" : 16,
    "completion_type" : "flash",
    "scale" : 0
}

test_record_b = {
    "timetamp" : datetime.datetime.now().timestamp(),
    "grade" : 12,
    "completion_type" : "on-sight",
    "scale" : 0
}


############### A) Storage Status #############

# print("\n")
# status_of_mongo = main.Operations().get_use_mongo_status()
# print(f"Is the MongoDb active right now? => {status_of_mongo}")
# print("\n")

############### A) Storage Status #############

############### B) Operations Status #############

# print("\n")
# mapping = main.Operations().get_mapping()
# print(f"Check the mapping =>\n {mapping}")
# print("Completion Type")
# print(main.CompletionType().get_mapping())
# print("Scale Type")
# print(main.Grades().get_mapping())
# print("\n")

############### B) Operations Status #############



############### C) Script Local RECORD ##############

# print(main.Operations().get_user())
# main.Operations().set_user(test_user_d)
# print(main.Operations().get_user())
# main.Operations().add_entry_local(test_record_b)
# print("\n")

############### C) Script Local RECORD ##############



############### D) Script MongoDB RECORD ##############WW



# TODO 1 check user_existance / Mongo Search (true/false)
# https://stackoverflow.com/questions/25163658/mongodb-return-true-if-document-exists

# shoudl return true or false
# does_user_exist = main.OptionMongoDb().check_user_existance(test_user_a["_id"])
# print(f"existiert der Nuter bereits? {does_user_exist}")


# TODO 2 add_entry_monogo (Neuen Nutzer anlegen und zu altem Nutzer hinzufügen
# main.Operations().add_entry_mongo(test_record_a)

print(main.Operations().get_user())
# set my user
main.Operations().set_user(test_user_b)
print(main.Operations().get_user())
# add new entry
main.Operations().add_entry_mongo(test_record_a)
print("\n")

############### D) Script MongoDB RECORD ##############