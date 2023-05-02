# Todo List Project

Django project for managing todos


## Installation

Python3 must be already installed

```shell
git clone https://github.com/U-Ra-All/todo_list.git
cd todo_list
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver # starts Django Server
```

Create a file called .env in the same folder as the settings file. 
Make sure to have the following development-specific values in there.
You can find the example in [.env_sample](.env_sample)

```shell
SECRET_KEY = "Your_Super_Secret_Key"
```

You can use the following superuser at http://127.0.0.1:8000/admin/ 
(or create another user by yourself):

```shell
Login: admin.user
Password: 7QancRe2
```

## Features

* Managing todos with tags, deadline and other features
