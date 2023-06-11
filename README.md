# Django Todo App

A simple Todo app built with Django framework that allows users to create, manage, and organize their tasks.

## Features

- User registration and authentication: Users can sign up for an account and log in to manage their tasks.
- Task creation: Users can create new tasks by providing a title, description, priority, and completion date.
- Task management: Users can view, edit, and delete their tasks.
- Task filtering: Users can filter tasks based on their completion status (completed/incomplete).
- User-friendly interface: The app provides a clean and intuitive interface for easy task management.


## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/django-todo-app.git
   ```

2. Navigate to the project directory:

   ```shell
   cd django-todo-app
   ```

3. Create a virtual environment (optional but recommended):

   ```shell
   python -m venv env
   ```

4. Activate the virtual environment:

   - For Windows:

     ```shell
     .\env\Scripts\activate
     ```

   - For macOS/Linux:

     ```shell
     source env/bin/activate
     ```

5. Install the project dependencies:

   ```shell
   pip install -r requirements.txt
   ```

6. Apply the database migrations:

   ```shell
   python manage.py migrate
   ```

7. Start the development server:

   ```shell
   python manage.py runserver
   ```

8. Open your web browser and visit [http://localhost:8000](http://localhost:8000) to access the Todo app.

## Usage

1. Sign up for a new account by clicking on the "Sign Up" link on the homepage.
2. Log in with your credentials.
3. Create a new task by clicking on the "Create Task" button and filling out the required fields.
4. View, edit, or delete your tasks by clicking on the respective buttons on the task list page.
5. Use the task filtering options to view completed or incomplete tasks.
6. Log out of your account when you're done.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

```

