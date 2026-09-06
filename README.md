<div align="center">

<!-- Animated header banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=220&section=header&text=AirBnB%20Clone&fontSize=60&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Building%20Airbnb%20from%20the%20ground%20up%2C%20one%20layer%20at%20a%20time&descAlignY=58&descSize=18" width="100%"/>

<!-- Typing animation -->
<a href="https://github.com/nesruzenu/AirBnB_clone">
  <img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&pause=1000&color=F7A83E&center=true&vCenter=true&width=600&lines=Command-line+console+%E2%86%92+Storage+engine;REST+API+%E2%86%92+Web+dynamic+front-end;A+full-stack+clone+of+Airbnb" alt="Typing SVG" />
</a>

<br/>

<!-- Badges -->
![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-In%20Development-orange?style=for-the-badge)
![PEP8](https://img.shields.io/badge/Code%20Style-PEP8-blueviolet?style=for-the-badge)

![GitHub last commit](https://img.shields.io/github/last-commit/nesruzenu/AirBnB_clone?style=flat-square&color=informational)
![GitHub repo size](https://img.shields.io/github/repo-size/nesruzenu/AirBnB_clone?style=flat-square&color=success)
![GitHub issues](https://img.shields.io/github/issues/nesruzenu/AirBnB_clone?style=flat-square&color=critical)
![GitHub stars](https://img.shields.io/github/stars/nesruzenu/AirBnB_clone?style=flat-square&color=yellow)

</div>

<br/>

# AirBnB Clone - The Console

## Description

This project is the first step towards building a full web application: the AirBnB clone. This first piece is a command interpreter to manage objects for the AirBnB application:

* Create a new object (e.g. a new `BaseModel`)
* Retrieve an object from a file, a database, etc.
* Do operations on objects (count, compute stats, etc.)
* Update attributes of an object
* Destroy an object

This command interpreter is the foundation for the rest of the project. Objects are serialized to a JSON file (`file.json`) and deserialized back on startup, so data persists between sessions. Later parts of the project will build on top of this console, adding more classes and eventually a database storage engine and a web front end.

The console currently supports the following object type:

* `BaseModel`

## Environment

This project is developed and tested on Ubuntu 20.04 LTS using Python 3.8.3.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/<your-username>/AirBnB_clone.git
   ```
2. Move into the cloned directory:
   ```
   cd AirBnB_clone
   ```
3. Make the console executable:
   ```
   chmod +x console.py
   ```

## How to Start the Console

**Interactive mode:**
```
$ ./console.py
(hbnb)
```

**Non-interactive mode (piping commands):**
```
$ echo "help" | ./console.py
(hbnb)
```

To exit the console, use `quit` or `EOF` (Ctrl+D).

## How to Use the Console

| Command | Usage | Description |
| --- | --- | --- |
| `help` | `help` or `help <command>` | Displays help information about available commands |
| `quit` | `quit` | Exits the console |
| `EOF` | `EOF` (Ctrl+D) | Exits the console |
| `create` | `create <class name>` | Creates a new instance of a class, saves it to `file.json`, and prints its id |
| `show` | `show <class name> <id>` | Prints the string representation of an instance |
| `destroy` | `destroy <class name> <id>` | Deletes an instance based on the class name and id |
| `all` | `all` or `all <class name>` | Prints all string representations of instances, optionally filtered by class |
| `update` | `update <class name> <id> <attribute name> "<attribute value>"` | Updates an instance by adding or modifying an attribute, then saves the change |

### Error messages

The console prints specific errors for missing or invalid input:

* `** class name missing **` — no class name was given
* `** class doesn't exist **` — the class name given isn't recognized
* `** instance id missing **` — no id was given
* `** no instance found **` — no instance exists with that class and id
* `** attribute name missing **` — (update only) no attribute name was given
* `** value missing **` — (update only) no value was given for the attribute

## Examples

### Interactive mode

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2026, 9, 7, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2026, 9, 7, 3, 10, 25, 903300)}
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2026, 9, 7, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2026, 9, 7, 3, 10, 25, 903300)}"]
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "John"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2026, 9, 7, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2026, 9, 7, 3, 11, 3, 49401), 'first_name': 'John'}
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
[]
(hbnb) quit
$
```

### Non-interactive mode

```
$ echo "create BaseModel" | ./console.py
(hbnb) 38f22813-2753-4d42-b37c-57a17f1f3f96
(hbnb)
$ echo "all BaseModel" | ./console.py
(hbnb) ["[BaseModel] (38f22813-2753-4d42-b37c-57a17f1f3f96) {'id': '38f22813-2753-4d42-b37c-57a17f1f3f96', ...}"]
(hbnb)
```

### Error handling examples

```
$ ./console.py
(hbnb) create
** class name missing **
(hbnb) create MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel 121212
** no instance found **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907
** attribute name missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name
** value missing **
(hbnb) quit
$
```

## Running Tests

All classes, functions, and files are covered by unit tests. Run the full suite with:

```bash
python3 -m unittest discover tests
```

It also passes in non-interactive mode:

```bash
echo "python3 -m unittest discover tests" | bash
```

## Authors

See the [AUTHORS](AUTHORS) file for the list of contributors.
