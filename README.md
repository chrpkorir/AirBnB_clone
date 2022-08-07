# **AirBnB project**

![hairbnb logo](./hbnb.png)

# Phase 0X00. console
The console will be the command interpretor for this project
## **basic useage**
```bash
gina@ubuntu:~$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  create  help  quit

Undocumented commands:
======================
all  destroy  show  update

(hbnb) help quit
Quit command to exit the program
(hbnb) quit
gina@ubuntu:~$
```
#### **COMMANDS IMPLEMENTED**
> use `help` to list all the commandsist 


| command | Description |
| --- | --- |
| **help** | lists all the available commands or the command format if a command is passed in argument [Usage]: `help` or `help` `<command>` |
| **all** | Shows all objects, or all instances of a class [Usage]: `all` `<className>` |
| **create** | Creates a class of any type [Usage]: `create` `<className>` |
| **destroy** |Destroys an individual instance of a class [Usage]: `destroy` `<className> <objectId>` |
| **show** | Shows an individual instance of a class[Usage]: `show` `<className> <objectId>` |
| **update** | Updates an object woth new information [Usage]: `update` `<className> <id> <attName> <attValue>` |
| **EOF** | Exits the program without formatting |
| **quit** | Exits the program |
|
<br>

#### **OBJECTS IMPLEMENTED**
This repository contains the following files:

| Folder | File | Description |
| :--- | :--- | :--- |
| tests |  | Contains test files for AirBnb Clone |
|  | console.py | Command line Interpreter for managing AirBnB objects |
| models | base_model.py | Defines all common attributes/methods for other classes |
| models | amenity.py | Creates class `amenity` |
| models | city.py | Creates class `city` |
| models | place.py | Creates class `place` |
| models | review.py | Creates class `review` |
| models | state.py | Creates class `state` |
| models | user.py | Creates class `user` |
| models/engine/ | file_storage.py | Serializes instances to a JSON file and deserializes JSON file to instances |

this is the end of phase one , sql hopefull next
