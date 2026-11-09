# Tidy — Todo List

A clean and responsive Todo List web application built with Django. Tidy helps users organize daily tasks, manage deadlines, track progress, and group related tasks using tags.

## Features

### Task Management
- Create new tasks with descriptions.
- Edit existing tasks.
- Delete tasks.
- Mark tasks as completed or undo completion.
- Set optional deadlines.
- Automatically record task creation date and time.
- Assign multiple tags to a task.

### Tag Management
- Create, edit, and delete tags.
- Organize tasks by categories.
- Assign multiple tags to individual tasks.
- View the number of tasks associated with each tag.

### User Interface
- Clean and modern interface.
- Sidebar navigation available across pages.
- Separate sections for active and completed tasks.
- Responsive layout.
- Task ordering: active tasks first, newest tasks first.

## Technologies

- Python
- Django 5.2+
- SQLite3
- HTML5
- CSS3
- Django Templates
- Django ModelForms

## Project Structure

```text
todo-list/
│
├── tasks/
│   ├── migrations/
│   ├── fixtures/
│   │   └── demo.json
│   ├── static/
│   │   └── tasks/
│   │       └── styles.css
│   ├── templates/
│   │   └── tasks/
│   │       ├── base.html
│   │       ├── task_list.html
│   │       ├── task_form.html
│   │       ├── tag_list.html
│   │       └── tag_form.html
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── todo/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── README.md
```

## Data Models

**Task**

| Field | Description |
|---|---|
| content | Task description |
| created_at | Task creation date and time |
| deadline | Optional task deadline |
| is_done | Task completion status |
| tags | Many-to-many relationship with Tag |

**Tag**

| Field | Description |
|---|---|
| name | Unique tag name |

A task can have multiple tags, and each tag can be assigned to multiple tasks.

## Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/brit2pac/tidy-todo-list
cd todo-list-in-this-practice-project
```

2. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply database migrations:

```bash
python manage.py migrate
```

5. (Optional) Load demo data:

```bash
python manage.py loaddata tasks/fixtures/demo.json
```

6. Start the development server:

```bash
python manage.py runserver
```

7. Open the application:

```text
http://127.0.0.1:8000/
```

## Application Pages

| Page | URL |
|---|---|
| Home / Task List | `/` |
| Add Task | `/tasks/add/` |
| Tag List | `/tags/` |
| Add Tag | `/tags/add/` |

## Screenshots

Screenshots of the application interface will be added here.

- Home page — Task List
- Add / Edit Task
- Tag List
- Add / Edit Tag

## Learning Outcomes

This project was developed as a practical Django project to demonstrate:

- Django models and database relationships.
- ModelForms and form validation.
- Function-based views.
- URL routing and template inheritance.
- CRUD operations.
- Django ORM and query optimization using `prefetch_related`.
- CSRF protection and POST-based actions.
- Static files and custom CSS styling.

---

## Screenshots

