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

test_user_c = {
    "id" : "44444444",
    "surname" : "New",
    "forename" : "User"
}




############### TEST Console Input LOCAL  ##############
import main

status_of_mongo = main.Operations().get_use_mongo_status()
print(f"Is the MongoDb active right now? => {status_of_mongo}")

# 1 console input local
# 2 script input local
# 3 console input mongo
# 4 script input mongo



############### TEST LOCAL RECORD ##############

############### TEST Console Input ##############

#import main



# main.CreateEntry().ask_console()
############### TEST Console Input ##############

############### TEST Mongo ##############

# import main

# main.Mongo()

# print(main.CreateEntry().add_entry(0, 0))



############### TEST Mongo ##############