# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.8+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

You can check poetry is installed by running `poetry --version` from a terminal.

**Please note that after installing poetry you may need to restart VSCode and any terminals you are running before poetry will be recognised.**

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/2.3.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Trello Setup

### Environment Variables

In `.env`, add your Trello api key and token. If you don't have a key or token, follow the instructions [here](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/#managing-your-api-key) to set them up:

```bash
$ TRELLO_API_KEY=<key>
$ TRELLO_API_TOKEN=<token>
```

### Creating Trello Lists

In your trello account, on any board, create three lists: one for "Not Started", one for "In Progress" and one for "Complete" (it doesn't matter what you names your lists).

In the Thunder Client (or any alternative e.g. Postman) make the following GET request: 
```bash
$ https://api.trello.com/1/members/me/boards?key=<api_key>&token=<api_token>
```
This will list all your boards. Find the board on which you created your lists and take a note of the ID.

(example of what an ID can look like: `65d6337573a6275aed0ec68a`)

Now, make another GET request using the ID you just found:
```bash
$ https://api.trello.com/1/boards/<board_id>/lists?=all&key=<api_key>&token=<api_token>
```
This will list all the lists on your board. Find your three lists and take a note of their IDs.

In `.env`, add your board ID and list IDs:

```bash
$ TRELLO_BOARD_ID=<board_id>
$ NOT_STARTED_LIST_ID=<not_started_list_id>
$ IN_PROGRESS_LIST_ID=<in_progress_list_id>
$ COMPLETE_LIST_ID=<complete_list_id>
```

## Running the App

Once the all dependencies have been installed, and the Trello setup has been done, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app 'todo_app/app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 113-666-066
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Running the Tests

Run the command from the terminal:
```bash
$ pytest
```

To run specific tests, run this command instead (all tests can be found the ./tests folder):
```bash
$ pytest <path_to_directory_or_file> 
```

## Adding new Tests

The `./tests` directory mirrors the `./todo_app` directory in structure. When you create a test, place it in the tests directory in a place that matches its location in `./todo_app`. You can create a new directory if the corresponding `./todo_app` directory does not exists in `./tests`.

Test files should be in the following format:

```bash
$ _<anything>_test.py
```

If the directory in `./tests` doesn't already have an empty file called `__init__.py`, create one.

In order for Pytest to correctly resolve imports, it needs to recognise the tests, like the application code, as Python packages. This requires each directory to hold a file (typically empty) named `__init__.py`.

## Ansible Playbook

The `ansible_config` folder contains all the files needed to host the website on the vm:

```bash
Ansible Controller Node IP: 13.42.115.137
Managed Node IP: 18.175.38.223
```

All of the files in `ansible_config` exist on the controller node, but changes will need to be copied over (except for `todoapp.service` which will need to be pushed to git). The reccommended way to do this is to connect the controller node via the VS Code Remote SSH plugin and copy paste the contents.

You can also SSH via the command line - you will prompted for a password (which I will not list here, but let me know if you need it). Then a text editor such as VIM can be used to change the files.

To run the playbook, type the following command:

```bash
ansible-playbook playbook.yml -i inventory.ini
```

You will be prompted for the API key and token that you have stored in your `.env` file.

The board and list IDs are stored in the `.env.j2` file directly (in `/ansible_config`), so if these change, change them here and copy the changes over to the VM.

The website will then run and can be accessed at `http://18.175.38.223:5000/`

To see the application logs, SSH from the control node into the managed node using:

```bash
ssh ec2-user@18.175.38.223
```

Then run the command:

```bash
journalctl -u todoapp
```


