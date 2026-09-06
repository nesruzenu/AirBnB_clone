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
