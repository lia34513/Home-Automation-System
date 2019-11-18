# Parity_Home_Automation

This repository contains the code required to setup the data models for a home automation system.
It is built using Django (Python-based API framework as the back-end), SQLite3 (persistent storage), and Python3.

# Local Installation

- Install Python3 and Django
- Setup the SQLite3: `python3 manage.py makemigrations`, `python3 manage.py migrate'
- Run the Server: `python3 manage.py runserver`
- Send request by POSTMAN: `https://www.getpostman.com/`

# Database

- Table: home_automation
    - Fields: 
        - id: Integer, Primary key
        - roomtype: String, Not Null
        - light_status: Integer, Values: `0` is off and `1` is on
        - temperature_degree: Float
        - thermostat_status: String, Values: `off`, `cool`, `heat`, `fan-on`, `auto`
# API End Points

- POST `http://127.0.0.1:8000/admin/initial`
    - Create initial rooms into home_automation(database)
    - Add three rooms with their roomtypes(`bedroom`, `livingroom`, `bathroom`) and unique id
    - Set light_status, temperature_degree, thermostat_status to Null
    - Output: json file
        - Wrong Message or Success Message with list of database
        
    
- POST `http://127.0.0.1:8000/admin/addroom`
    - Create your own room, assign new unique id to the room
    - Provide value for `Roomtype`
    - `Lightstatus`,`Temperature`,`Thermostatstatus` optional to set a value
    - Input: Set `Header` in the POSTMAN
        - key: Roomtype, value: `String`
        - key: Lightstatus, value: `1`, `0` or Null
        - key: Temperature, value: `Float number` or Null
        - key: Thermostatstatus, value:  `off`, `cool`, `heat`, `fan-on`, `auto` or Null
        - Input examples: 
            - `Roomtype=kitchen`
            - `Roomtype=garage, Lightstatus=1, Temperature=20, Thermostatstatus=off`
            - `Roomtype=bedroom, Lightstatus=0`
    - Output: json file
        - Wrong Message or Success Message with list of database
        
- DELETE `http://127.0.0.1:8000/admin/clear`
    - Delete all data in the home_automation table
    - Output: json file
        - Success Message with list of database
        
- GET `http://127.0.0.1:8000/admin/list`
    - Show all data in the home_automation table
    - Output: json file
        - list of database
    
- PUT `http://127.0.0.1:8000/admin/light`
    - Change the light status for the room with id
    - `Id` must exist in the home_automation table
    - `Value` must be `0` or `1`
    - Input: Set `Header` in the POSTMAN
        - key: Id, value: `Integer`
        - key: Value, value: `1` or `0`
        - Input examples: 
            - `Id=1, Value=0`
    - Output: json file
        - Wrong Message or Success Message with list of database

- PUT `http://127.0.0.1:8000/admin/temperature`
    - Change the temperature degree for the room with id
    - `Id` must exist in the home_automation table
    - `Value` must be a number
    - Input: Set `Header` in the POSTMAN
        - key: Id, value: `Integer`
        - key: Value, value: `Float`
        - Input examples: 
            - `Id=1, Value=20`
    - Output: json file
        - Wrong Message or Success Message with list of database

- PUT `http://127.0.0.1:8000/admin/thermostat`
    - Change the thermostat status for the room with id
    - `Id` must exist in the home_automation table
    - `Value` must be `off`, `cool`, `heat`, `fan-on` or `auto`
    - Input: Set `Header` in the POSTMAN
        - key: Id, value: `Integer`
        - key: Value, value: `off`, `cool`, `heat`, `fan-on`, `auto`
        - Input examples: 
            - `Id=1, Value=off`
    - Output: json file
        - Wrong Message or Success Message with list of database
        
   