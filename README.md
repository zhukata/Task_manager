<h1>Task Manager</h1>

<p>
A simple and flexible task management web application
</p>

[Task_manager](https://python-project-52-zkw5.onrender.com/) – это сайт, который позволяет создавать и отслеживать задачи.

### Hexlet tests and linter status:
[![Actions Status](https://github.com/zhukata/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/zhukata/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/6cb41e3884808ddcdb19/maintainability)](https://codeclimate.com/github/zhukata/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/6cb41e3884808ddcdb19/test_coverage)](https://codeclimate.com/github/zhukata/python-project-52/test_coverage)
<div>
    <p>
        <a href="#about">About</a> •
        <a href="#installation">Installation</a> •
        <a href="#usage">Usage</a> •
        <a href="#demo">Demo</a> •
        <a href="#additionally">Additionally</a> 
    </p>
</div>

## About

A task management web application built with Python and [Django](https://www.djangoproject.com/) framework. It allows you to set tasks, assign performers and change their statuses. Registration and authentication are required to work with the system.

To provide users with a convenient, adaptive, modern interface, the project uses the [Bootstrap](https://getbootstrap.com/) framework.

The frontend is rendered on the backend. This means that the page is built by the DjangoTemplates backend, which returns prepared HTML. And this HTML is rendered by the server.

[PostgreSQL](https://www.postgresql.org/) is used as the object-relational database system.

#### --> [Demo](https://python-project-52-zkw5.onrender.com/) <--

### Features

* [x] Set tasks;
* [x] Assign performers;
* [x] Change task statuses;
* [x] Set multiple tasks labels;
* [x] Filter the tasks displayed;
* [x] User authentication and registration;

### Built With

* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Bootstrap 4](https://getbootstrap.com/)
* [PostgreSQL](https://www.postgresql.org/)
* [Poetry](https://python-poetry.org/)
* [Gunicorn](https://gunicorn.org/)
* [Docker](https://www.docker.com/)
* [Render](https://render.com/)
* [Rollbar](https://rollbar.com/)
* [Flake8](https://flake8.pycqa.org/en/latest/)

### Details

For **_user_** authentication, the standard Django tools are used. In this project, users will be authorized for all actions, that is, everything is available to everyone.

Each task in the task manager usually has a **_status_**. With its help you can understand what is happening to the task, whether it is done or not. Tasks can be, for example, in the following statuses: _new, in progress, in testing, completed_.

**_Tasks_** are the main entity in any task manager. A task consists of a name and a description. Each task can have a person to whom it is assigned. It is assumed that this person performs the task. Also, each task has mandatory fields - author (set automatically when creating the task) and status.

**_Labels_** are a flexible alternative to categories. They allow you to group the tasks by different characteristics, such as bugs, features, and so on. Labels are related to the task of relating many to many.

When the tasks become numerous, it becomes difficult to navigate through them. For this purpose, a **_filtering mechanism_** has been implemented, which has the ability to filter tasks by status, performer, label presence, and has the ability to display tasks whose author is the current user.

---

## Installation

### _Easy Mode:_

Why not just let [Docker Compose](https://docs.docker.com/compose/) do all the work, right? Of course, for the magic to happen, [Docker](https://docs.docker.com/desktop/) must be installed and running. 

Clone the project:
```bash
>> git clone https://github.com/ivnvxd/python-project-52.git && cd python-project-52
```

Create `.env` file in the root folder and add following variables:
```dotenv
DATABASE_URL=postgresql://postgres:password@db:5432/postgres
SECRET_KEY={your secret key} # Django will refuse to start if SECRET_KEY is not set
LANGUAGE=en-us # By default the app will use ru-ru locale
```

And run:
```shell
>> docker-compose up
```

Voila! The server is running at http://0.0.0.0:8000 and you can skip directly to [Available Actions](#available-actions-) section.

### _Manual Install:_

There is always an option for those who like to do everything by themselves.

### Prerequisites

#### Python

Before installing the package make sure you have Python version 3.10 or higher installed:

```bash
>> python --version
Python 3.10+
```

#### Poetry

The project uses the Poetry dependency manager. To install Poetry use its [official instruction](https://python-poetry.org/docs/#installation).

#### PostgreSQL / SQLite

There are two main options for using a database management system for this project: **PostgreSQL** and **SQLite**.

PostgreSQL is used as the main database management system. You have to install it first. It can be downloaded from [official website](https://www.postgresql.org/download/) or installed using Homebrew:
```shell
>> brew install postgresql
```

_Alternatively you can skip this step and use **SQLite** database locally._

### Application

To use the application, you need to clone the repository to your computer. This is done using the `git clone` command. Clone the project:

```bash
>> git clone https://github.com/ivnvxd/python-project-52.git && cd python-project-52
```

After that install all necessary dependencies:

```bash
>> make install
```

Create `.env` file in the root folder and add following variables:
```dotenv
DATABASE_URL=postgresql://{provider}://{user}:{password}@{host}:{port}/{db}
SECRET_KEY={your secret key} # Django will refuse to start if SECRET_KEY is not set
LANGUAGE=en-us # By default the app will use ru-ru locale
```
_If you choose to use **SQLite** DBMS, do not add `DATABASE_URL` variable._

To create the necessary tables in the database, start the migration process:
```bash
>> make migrate
```

---

## Usage

Start the Gunicorn Web-server by running:

```shell
>> make start
```

By default, the server will be available at http://0.0.0.0:8000.

It is also possible to start it local in development mode using:

```shell
>> make dev
```

The dev server will be at http://127.0.0.1:8000.

### Available Actions:

- **_Registration_** — First, you need to register in the application using the registration form provided;
- **_Authentication_** — To view the list of tasks and create new ones, you need to log in using the information from the registration form;
- **_Users_** — You can see the list of all registered users on the corresponding page. It is available without authorization. You can change or delete information only about yourself. If a user is the author or performer of a task, it cannot be deleted;
- **_Statuses_** — You can view, add, update, and delete task statuses if you are logged in. Statuses corresponding to any tasks cannot be deleted;
- **_Tasks_** — You can view, add, and update tasks if you are logged in. Only the task creator can delete tasks. You can also filter tasks on the corresponding page with specified statuses, performers, and labels;
- **_Labels_** — You can view, add, update, and delete task labels if you are logged in. Labels matching any tasks cannot be deleted.

---

## Demo

The demo version is available on Render platform:
[https://python-project-52-zkw5.onrender.com/](https://python-project-52-zkw5.onrender.com/)

---

## Additionally

### Dependencies

* python = "^3.10"
* Django = "^5.0.8"
* python-dotenv = "^1.0.1"
* django-bootstrap5 = "^24.2"
* dj-database-url = "^2.2.0"
* psycopg2-binary = "^2.9.9"
* gunicorn = "^22.0.0"
* django-filter = "^24.3"
* rollbar = "^0.16.3"
* django-rest-framework = "^0.1.0"
* djangorestframework-simplejwt = "^5.3.1"

### Dev Dependencies

* flake8 = "^7.1.1"
* coverage = "^7.6.1"

### Makefile Commands

<dl>
    <dt><code>make install</code></dt>
    <dd>Install all dependencies of the package.</dd>
    <dt><code>make migrate</code></dt>
    <dd>Generate and apply database migrations.</dd>
    <dt><code>make dev</code></dt>
    <dd>Run Django development server at http://127.0.0.1:8000/</dd>
    <dt><code>make start</code></dt>
    <dd>Start the Gunicorn web server at http://127.0.0.1:8000/ if no port is specified in the environment variables.</dd>
    <dt><code>make lint</code></dt>
    <dd>Check code with flake8 linter.</dd>
    <dt><code>make test</code></dt>
    <dd>Run tests.</dd>
    <dt><code>make check</code></dt>
    <dd>Validate structure of <code>pyproject.toml</code> file, check code with tests and linter.</dd>
</dl>