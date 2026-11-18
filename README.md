# Tidy — Todo List

A small Django todo list with tags, deadlines, and completion tracking.

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata tasks/fixtures/demo.json  # optional sample data
python manage.py runserver 127.0.0.1:8000
```

Open <http://127.0.0.1:8000/>. The tag manager is at <http://127.0.0.1:8000/tags/>.

## Features

- Tasks store their description, creation time, optional deadline, completion state, and many-to-many tags.
- The home page sorts open tasks before completed tasks, newest first within each group.
- Create, update, delete, complete, and undo tasks.
- Create, update, and delete tags.
- Responsive layout with a shared navigation sidebar.

## Data model

- `Task`: `content`, `created_at`, optional `deadline`, `is_done`, and a many-to-many relationship with `Tag`.
- `Tag`: unique `name`.
