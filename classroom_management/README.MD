# Classroom Management Tool

A web-based application for managing classrooms, courses, and grades. This tool is designed for administrators, teachers, and students, providing role-based dashboards and functionalities.

## Features

- **Admin Dashboard**:
  - Create and manage teacher users.
  - Create and manage classrooms and courses.
  - View summaries of users, classrooms, and courses.

- **Teacher Dashboard**:
  - View assigned classrooms and courses.
  - Manage students and their grades.

- **Student Dashboard**:
  - View enrolled classrooms and courses.
  - Check grades and feedback for each course.

## How Users Use the App

### Admin
1. **Sign In**: Admins log in using their credentials.
2. **Create Users**: Admins can create teacher accounts via the "Create New User" form.
3. **Create Classrooms and Courses**:
   - Use the "Create New Classroom" form to add classrooms.
   - Use the "Create New Course" form to assign courses to teachers and classrooms.
4. **Manage Data**:
   - Edit or delete classrooms and courses from the admin dashboard.

### Teacher
1. **Sign In**: Teachers log in using their credentials.
2. **View Classrooms**: Teachers can view their assigned classrooms and courses.
3. **Manage Grades**:
   - Add or edit grades for students in their courses.
   - Provide feedback for each grade.

### Student
1. **Sign In**: Students log in using their credentials.
2. **View Classrooms and Courses**: Students can see their enrolled classrooms and courses.
3. **Check Grades**: Students can view their grades and feedback for each course.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd classroom-management
    ```

## Install dependencies:
```bash make install-dependencies ````

## Set up the .env file with the following variables:
```bash POSTGRES_DATABASE=dj_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=qwerty
POSTGRES_HOST=database
POSTGRES_PORT=5432
```

## Run the application with docker:
```bash 
make compose.setup
```

## Run the application local:
```bash 
make start
```

## Dependencies
- Django
- uvicorn (ASGI web server)
- sqlmodel
- psycopg2-binary (Postgres driver)
- pytest (Dev dependency)
- django-pytest (Dev dependency)
- whitenoise (>=6.9.0, <7.0.0) (For serving files through ASGI with DEBUG=False)
- License
- This project is licensed under the MIT License.

## caveat
Erro encontrado: Não consigo criar tests com Users visto que utilizo um user asbtract