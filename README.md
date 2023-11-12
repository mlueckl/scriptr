# Scriptr
## House your scripts in a single location and run them with this easy


Add your scripts in the below format:

    📦scriptr
    ┣ 📂scriptr
    ┃ ┣ 📂scripts
    ┃ ┃ ┣ 📂script-reqs
    ┃ ┃ ┃ ┃ ┃ ┣ 📜requirements.txt
    ┃ ┃ ┃ ┃ ┃ ┗ 📜__main__.py
    ┃ ┃ ┗ 📂script-no-reqs
    ┃ ┃ ┃ ┃ ┃ ┗ 📜__main__.py

#### List commands

    $ python3 scriptr --help

#### Install dependencies

    $ python3 scriptr install

#### Run
A specific script

    $ python3 scriptr run script-reqs

Or list avaialble scripts and run selected

    $ python3 scriptr run