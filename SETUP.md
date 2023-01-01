## SETUP

This documentation is for those who want to setup this workflow locally to do some work on it.


### poetry

This workflow uses a tool called [poetry](https://python-poetry.org) for depencency management. 
To install poetry in your local enviroment follow [these instructions](https://python-poetry.org/docs/#installation).


### dependencies

Once you have poetry installed, the next thing is to fetch all of this project's dependencies using the command [poetry install](https://python-poetry.org/docs/cli/#install). 
This command will use the `pyproject.toml` file to create a virtual env and install all the necesary libraries from pypi.


### release

To import the current state of the workflow into Alfred, you can use the script `./scripts/release.sh`. 
This will package all the required components to run the workflow in Alfred without any external depencencies.

At the end, you'll be automatically prompted to import it into Alfred.

> You can find the generated `.alfredworkflow` files in the `releases/` folder.