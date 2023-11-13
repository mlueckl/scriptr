import os
from setuptools import setup, find_packages

README = "README.md"
REQUIREMENTS = "requirements.txt"


def _read(file_name: str) -> list:
    file = os.path.join(os.path.dirname(__file__), file_name)

    with open(file, "r") as f:
        return f.read()


def _read_script_requirements():
    script_path = os.path.join(os.path.dirname(__file__), "scriptr/scripts")
    os.open(script_path)


setup(
    version="0.1.0",
    name="scriptr",
    description="CLI to execute many scripts.",
    author="Michael Lueckl",
    author_email="mlueckl@criteo.com",
    packages=find_packages(),
    long_description=_read(README),
    install_requires=_read(REQUIREMENTS).splitlines(),
    entry_points={
        'console_scripts': [
            'scriptr=scriptr.__main__:main'
        ]
    }
)
