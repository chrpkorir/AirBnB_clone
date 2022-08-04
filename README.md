# Airbnb Clone
![logo](./hbnb.png)

# project base model <br>

## Class BaseModel
### Public instance attributes
- id
- created_at
- updated_at
### Public instance methods:
```py
 def save(self): """updates the public instance attribute"""
def to_dict(self): """returns a dictionary containing all key/value of __dict__ of the instance"""
     
```

## **00 AirBnB Clone Console**
console.py to manage our backend
## Usage
The shell should work like this in interactive mode:
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
It can be also used in non-interactive mode:

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================

EOF  help  quit
(hbnb) 
$
```


