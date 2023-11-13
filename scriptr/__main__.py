#!/usr/bin/env python3

import os
import typer
import logging
import subprocess

from typing import Optional
from typing_extensions import Annotated

from scriptr.script_handler import (
    get_script_requirements,
    install_packages,
    list_installed_packages,
    get_scripts
)

app = typer.Typer()

@app.command(name="list-reqs")
def list_scripts_reqs():
    print(get_script_requirements())


@app.command(name="install-reqs")
def install_script_reqs():
    install_packages(get_script_requirements())


@app.command(name="list-inst")
def list_installed():
    list_installed_packages()

@app.command(name='list-scripts')
def list_scripts():
    print('\n'.join(get_scripts()))

@app.command(name='run')
def run(script: Annotated[Optional[str], typer.Argument()] = None):
    if not script:
        available_scripts = get_scripts()
        print('Select Script:')
        for key, script in enumerate(available_scripts):
            print(f'{key}. {script}')

        selected_script = input()
        os.system('cls')
        script = available_scripts[int(selected_script)]

    venv_dir = "Scripts" if os.path.exists("venv/Scripts") else "bin"
    if script in get_scripts():
        subprocess.run([f'venv/{venv_dir}/python', f'scriptr/scripts/{script}'])
    else:
        logging.warning(f'{script} not available!')

def main():
    app()

if __name__ == "__main__":
    main()
