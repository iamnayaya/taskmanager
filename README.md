# Task Manager

## Setup Instructions

1. **Clone the repository:**
    ```bash
    git clone (https://github.com/iamnayaya/taskmanager)
    cd task_manager
    ```

2. **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. **Apply migrations and create a superuser:**
    ```bash
    python manage.py migrate
    python manage.py createsuperuser
    ```

4. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

5. **Access the application:**
    Open your web browser and go to [http://localhost:8000](http://localhost:8000).

## Features

- **Task Management:**
    - Create, edit, and delete tasks.
    - Assign tasks to users.
    - Filter and sort tasks by various criteria.
    - Drag-and-drop functionality to change task status.
    
- **Dashboard:**
    - View task statistics (total tasks, completed tasks, in-progress tasks, overdue tasks).
    - Recent activities overview.

- **Calendar:**
    - View tasks in a calendar format for better scheduling.

- **Members:**
    - Manage team members.
    - Assign tasks to specific users.

- **User Authentication:**
    - Secure login and logout functionality.
    - Authorization to restrict access to certain views.

## API Endpoints

- **Get all tasks:**
    ```
    GET /api/tasks/
    ```
- **Get tasks by status:**
    ```
    GET /api/tasks/?status=<status>
    ```

## Technologies Used

- **Backend:**
    - Django
    - Django REST framework

- **Frontend:**
    - HTML
    - TailwindCSS
    - jQuery

## Testing

- **Run unit tests:**
    ```bash
    python manage.py test
    ```

## Documentation

- Detailed documentation for API endpoints, models, and views can be found in the `docs/` directory.

