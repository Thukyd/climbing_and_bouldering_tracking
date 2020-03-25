# Climbing and Bouldering Tracking
Keep track of your boulder routes.

## Features 0.1
- 3 different scale types ("Fontainebleau-bloc", "Fontainebleau-trav", "Vermin-Scale")
- 4 dfifferent completion types ("Flash", "On-Sight", "Rotpunkt", "try" an unsuccessful attempt)
- choice between storage in local json or cloud mongodb


## Tasks (version 0.1):
- [x] grade & completion type mappings
- [x] local storage
- [x] connection to mongo
- [x] option a: input via script with mongodb 
- [x] option b: input via script with local storage
- [ ] set new standard scale type & convert scale types => **currently on hold**
- [x] full test via script
- [x] => update documentation in Github

## Tasks (version 0.2):
- [ ] simple GUI via Svelt

# Next steps for version 0.3?
- [ ] add operations: update / delete records; update / delete user information; set new user?
- [ ] online/offline sync?
- [ ] web(pwa) integration? chatbot/voicebot integration?


# How to configure version 0.1?


## Choose Storage - MongoDB or Local Folder
The location can be changed within config/options.json.
```
{
    ...
    "mongo_db_activated" : false
}
```

## Setup of MongoDB
In order to fill out the mongo/configurations.json with your MongoDB credentials. Further help can be found at: https://www.mongodb.com/


```
{
    "connection": "mongodb+srv://<your_user>:<your_password>@<your_cluster>.gcp.mongodb.net/test?retryWrites=true&w=majority",
    "db_name": "<your_db_name>",
    "collection" : "<your_collection_name>"
}
```

## Set Standard Scale Type
The scale type is defined in the config/options.json Standard is "Fontainebleau-bloc".
```python
{
    "standard_scale" : "0"
}
```
It references to the array in config/mappings.json.
```python
# ...
  "scale_type": {
        "name": [
            "fb-bloc",
            "fb-trav",
            "v-scale"
        ],
 # ...
```

## Change Current User
The current user can be configured in config/user_identity.json
```
{"_id": "987654321", "surname": "Doe", "forename": "Jane"}
```

## Test scripts
Uncomment parts of "test_scripts.py" and let it run. 
