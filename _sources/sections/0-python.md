# How to install Python
```{contents}
:local:
```
## Installing Python on macOS using Terminal

To install Python on macOS using the terminal, follow these steps:

1. Open the Terminal application on your macOS.

2. Check if Python is already installed by running the following command: `python --version`

3. With Homebrew installed, use it to install Python by running the following command in the terminal: `brew install python` 

4. Homebrew will download and install Python along with its dependencies. This process may take a few moments.

5. To verify that Python is successfully installed, run the following command: `python --version`
If Python is installed correctly, the terminal will display the Python version number.

Congratulations! Python is now installed on your macOS using the terminal. You can start using Python for your programming needs.

Happy coding!


## Installing pyenv and Virtual Environments on macOS using Terminal

To install `pyenv` and set up virtual environments on macOS using the terminal, follow these steps:

1. Open the Terminal application on your macOS.

2. Install `pyenv` by running the following command in the terminal:
`brew install pyenv` and then, `brew install pyenv-virtualenv`

3. After the installation is complete, add the following lines to your shell profile file (e.g., `~/.bash_profile`, `~/.zshrc`, or `~/.bashrc`) to enable `pyenv`:
`eval "$(pyenv init -)"`

If that doesn't work, you could try:

```bash
❯ export PYENV_ROOT="$HOME/.pyenv"
❯ export PATH="$PYENV_ROOT/bin:$PATH"
❯ eval "$(pyenv init --path)"
❯ eval "$(pyenv init -)"
❯ eval "$(pyenv virtualenv-init -)"
```

4. Close and reopen the terminal or run the command `source ~/.bash_profile` (or your respective shell profile file) for the changes to take effect.

5. Verify that `pyenv` is installed correctly by running the following command: `pyenv --version` 
The terminal should display the `pyenv` version number if the installation was successful.

6. Install a specific Python version using `pyenv`. For example, to install Python 3.8.10, run the following command:
`pyenv install 3.8.10`

7. Once the Python version is installed, set it as the global default by running:
`pyenv global 3.8.10`

8. To create a virtualenv, `pyenv virtualenv 3.8.10 alfa-py-project`
   
9.  Check virtualenvs, `pyenv virtualenvs` 
    
10. Activate your virtualenv, `pyenv activate alfa-py-project`
    
11. Deactivate your virtualenv, `pyenv deactivate`

## Installing Python Libraries via Terminal on macOS

To install Python libraries using the terminal on macOS, follow these steps:

1. Open the Terminal application on your macOS.

2. Activate your desired Python environment, if applicable. For example, if you are using a virtual environment created with `virtualenv`, activate it by running:`pyenv activate your-virtualenv`

3. Install Python libraries using `pip`, the default package installer for Python. To install a library, run the following command:
`pip install <library_name>` 

Replace `<library_name>` with the name of the library you want to install. You can install multiple libraries in a single command by separating their names with spaces.

4. If you need a specific version of a library, you can specify it by appending `==<version_number>` to the library name. For example:
`pip install numpy==1.20.3` 

5. If you want to upgrade an already installed library to the latest version, use the `--upgrade` flag. For example:
`pip install --upgrade <library_name>` 

6. If you have a requirements file (`requirements.txt`) containing a list of libraries and their versions, you can install them all at once by running the following command in the directory containing the file:
`pip install -r requirements.txt` 

7. After running the installation command, `pip` will download and install the specified libraries along with their dependencies. This process may take a few moments.

8. To verify that the library is installed correctly, you can check its version or import it in a Python script or interpreter and ensure there are no import errors.

Congratulations! You have successfully installed Python libraries using the terminal on your macOS. You can now utilize the installed libraries in your Python projects.

Happy coding!
