# Game O

![GitHub License](https://img.shields.io/github/license/sabadam32/game-o?color=ff5733&labelColor=0e17b8)
![Python Version from PEP 621 TOML][version-url]

This is an interest project to learn programming with the arcade library.  My goal is to build a game toolset that is educational for entry level users.  
Learning Godot, Unity, or even PyGame for a firt attempt can be overwhelming.  I see this helping game jammers or teachers in classroom settings.  Also places like CoderDojo's would be a good spot for this type of thing.


## Installation

Clone the repo and follow the steps to install the arcade library in your environment.

```zsh
# Start in parent directory you want to use for this project then run
git clone git@github.com:sabadam32/game-o.git
cd game-0
```

setup a virtualenv with Python 3.11.8.  I use pyenv to install versions and setup environments.  Use whatever tools you feel comfortable with.

Pyenv
```zsh
# To install python if you do not already have it
pyenv install 3.11.8

# Setup a virtual environment for developing with arcade library (can be used by multiple arcade game projects)
pyenv virtualenv 3.11.8 arcade-games

# Set the python version for this project folder to arcade-games
pyenv local arcade-games
```

## Usage example
```zsh
python game_o.py
```

<!-- Markdown link & img dfn's -->
[version-url]: https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fsabadam32%2Fgame-o%2Fmain%2Fpyproject.toml&style=flat-square&logo=python&logoColor=ffde57&label=Python%20Version&labelColor=4584b6&color=ffde57&link=https%3A%2F%2Fwww.python.org%2Fdownloads%2Frelease%2Fpython-3118%2F
