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

## 📖 Table of Contents

- [About the Project](#-about-the-project)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Command Reference](#-command-reference)
- [Testing](#-testing)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [Authors](#-authors)
- [License](#-license)

<br/>

## 🏡 About the Project

> This project is the beginning of a series of projects aimed at recreating the
> **AirBnB** platform end-to-end — from a simple command-line console, all
> the way to a fully deployed web application with a REST API and a dynamic
> front-end.

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/216122065-2f028bae-25d3-4a01-9c8f-4d31c1fed021.gif" width="500">
</div>

The project is built incrementally, mirroring how real production systems evolve:

| Stage | Component            | Description                                                |
|:-----:|-----------------------|-------------------------------------------------------------|
| 0️⃣    | **Console**            | A command interpreter to manage app objects                 |
| 1️⃣    | **Storage Engine**     | Serializes/deserializes objects to/from a JSON file          |
| 2️⃣    | **Web Static**         | Hand-built HTML/CSS front-end mockups                        |
| 3️⃣    | **MySQL Storage**      | Swaps the storage engine for a relational database           |
| 4️⃣    | **Web Framework**      | Deploys a dynamic, templated front-end                       |
| 5️⃣    | **REST API**           | Exposes all objects over a documented HTTP API                |
| 6️⃣    | **Web Dynamic**        | Connects the front-end live to the API                       |

<br/>

## 🧱 Architecture

```mermaid
flowchart LR
    A[Console] -->|create / update / destroy| B(Models)
    B --> C{Storage Engine}
    C -->|FileStorage| D[(JSON file)]
    C -->|DBStorage| E[(MySQL)]
    F[REST API] --> C
    G[Web Front-End] --> F
    style A fill:#4c8bf5,color:#fff
    style F fill:#f7a83e,color:#fff
    style G fill:#34a853,color:#fff
```

<br/>

## 🛠 Tech Stack

<div align="center">
<img src="https://skillicons.dev/icons?i=python,mysql,html,css,js,git,linux,bash" />
</div>

<br/>

## 📂 Project Structure

<details>
<summary>Click to expand full file tree</summary>

```
AirBnB_clone/
├── console.py                 # Entry point of the command interpreter
├── models/
│   ├── __init__.py
│   ├── base_model.py          # BaseModel: id, created_at, updated_at, save/reload
│   ├── user.py
│   ├── state.py
│   ├── city.py
│   ├── amenity.py
│   ├── place.py
│   ├── review.py
│   └── engine/
│       ├── __init__.py
│       └── file_storage.py    # Serializes instances to a JSON file
├── tests/
│   ├── test_models/
│   └── test_console.py
├── AUTHORS
├── README.md
└── requirements.txt
```

</details>

<br/>

## 🚀 Getting Started

### Prerequisites

![Python](https://img.shields.io/badge/-Python%203.8+-3776AB?style=flat-square&logo=python&logoColor=white)
![OS](https://img.shields.io/badge/-Ubuntu%2020.04-E95420?style=flat-square&logo=ubuntu&logoColor=white)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/nesruzenu/AirBnB_clone.git

# 2. Move into the project directory
cd AirBnB_clone

# 3. (Optional) create a virtual environment
python3 -m venv venv && source venv/bin/activate

# 4. Give the console executable permissions
chmod +x console.py
```

<br/>

## 💻 Usage

### Interactive mode

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) quit
$
```

### Non-interactive mode

```bash
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

<br/>

## 📋 Command Reference

| Command    | Syntax                                   | Description                                    |
|------------|-------------------------------------------|-------------------------------------------------|
| `create`   | `create <Class>`                          | Creates a new instance, saves it, prints its id |
| `show`     | `show <Class> <id>`                       | Prints the string representation of an instance |
| `destroy`  | `destroy <Class> <id>`                     | Deletes an instance based on class name and id  |
| `all`      | `all [Class]`                              | Prints all instances, optionally filtered       |
| `update`   | `update <Class> <id> <attribute> <value>`  | Updates an instance's attribute                 |
| `quit`     | `quit`                                      | Exits the console                               |
| `EOF`      | `Ctrl+D`                                   | Exits the console                               |

**Example:**

```bash
(hbnb) create User
49faff9a-6318-451f-87b6-910505c55907

(hbnb) show User 49faff9a-6318-451f-87b6-910505c55907
[User] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-...', 'created_at': ..., 'updated_at': ...}

(hbnb) destroy User 49faff9a-6318-451f-87b6-910505c55907
(hbnb)
```

<br/>

## 🧪 Testing

```bash
python3 -m unittest discover tests
```

<div align="center">

![Tests](https://img.shields.io/badge/Tests-Unittest-blue?style=flat-square&logo=python)
![Coverage](https://img.shields.io/badge/PEP8-Compliant-brightgreen?style=flat-square)

</div>

<br/>

## 🗺 Roadmap

- [x] Command interpreter (console)
- [x] BaseModel + serialization
- [x] FileStorage engine
- [ ] Web static HTML templates
- [ ] MySQL storage engine
- [ ] Web framework (dynamic templates)
- [ ] REST API
- [ ] Full front-end/back-end integration

<br/>

## 🤝 Contributing

Contributions are welcome! Please fork the repo and open a pull request, or
open an issue to discuss what you'd like to change.

```bash
git checkout -b feature/your-feature-name
git commit -m "Add: short description of change"
git push origin feature/your-feature-name
```

<br/>

## 👤 Authors

<div align="center">

<a href="https://github.com/nesruzenu">
  <img src="https://github.com/nesruzenu.png" width="90" style="border-radius:50%;" />
</a>

**Nesru Zenu**
[![GitHub](https://img.shields.io/badge/GitHub-nesruzenu-181717?style=flat-square&logo=github)](https://github.com/nesruzenu)

</div>

See the [AUTHORS](AUTHORS) file for the full list of contributors.

<br/>

## 📄 License

This project is licensed under the MIT License — see the `LICENSE` file for details.

<br/>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=120&section=footer" width="100%"/>

⭐️ If you found this project interesting, consider giving it a star!
</div>
