import os
import logging

logging.basicConfig(level=logging.INFO)

REQUIREMENTS = "requirements.txt"
PACKAGE_NAME = "scriptr"
SCRIPTS_DIR = "scripts"


def _read(file_name: str) -> list:
    file = os.path.join(os.path.dirname(__file__), file_name)

    with open(file, "r") as f:
        return f.read()


def _get_scripts_req() -> list:
    package_dirs_path = os.path.join(
        os.path.dirname(__file__), f"{PACKAGE_NAME}", SCRIPTS_DIR
    )
    package_dirs = [
        os.path.join(package_dirs_path, package_dir, REQUIREMENTS)
        for package_dir in os.listdir(package_dirs_path)
    ]

    return package_dirs


def _read_script_requirements() -> list:
    requirements = []

    for script_req in _get_scripts_req():
        if os.path.exists(script_req):
            requirements.extend(_read(script_req).splitlines())

    return list(dict.fromkeys(requirements))


print(_get_scripts_req())
print(_read_script_requirements())
