import os
import logging
import subprocess

logging.basicConfig(level=logging.INFO)

REQUIREMENTS = "requirements.txt"
SCRIPTS_DIR = "scripts"


def __read(file_name: str) -> list:
    file = os.path.join(os.path.dirname(__file__), file_name)

    with open(file, "r") as f:
        return f.read()

def get_scripts() -> list:
    return os.listdir(os.path.join(os.path.dirname(__file__), SCRIPTS_DIR))

def __get_scripts_req() -> list:
    package_dirs_path = os.path.join(os.path.dirname(__file__), SCRIPTS_DIR)
    package_dirs = [
        os.path.join(package_dirs_path, package_dir, REQUIREMENTS)
        for package_dir in os.listdir(package_dirs_path)
    ]

    return package_dirs

venv_dir = "Scripts" if os.path.exists("venv/Scripts") else "bin"

def get_script_requirements() -> list:
    requirements = []

    for script_req in __get_scripts_req():
        if os.path.exists(script_req):
            requirements.extend(__read(script_req).splitlines())
        else:
            logging.info(f"Script requirement doesn't exist: {script_req}")

    return list(dict.fromkeys(requirements))


def install_packages(requirements: list) -> None:
    try:
        if len(requirements) > 0:
            subprocess.run([f"venv/{venv_dir}/pip", "install", *requirements])
        else:
            print("Requirements already satisfied.")

    except Exception as e:
        print(e)


def list_installed_packages():
    subprocess.run([f"venv/{venv_dir}/pip", "list"])
