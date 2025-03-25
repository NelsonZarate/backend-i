
# Classroom Management Tool

## 📊 Roadmap Visualization (Gantt Chart Style)

| Phase                | Tasks                                      | Duration  | Status          |
|----------------------|--------------------------------------------|-----------|-----------------|
| Planning & Setup     | Project init, Auth system                  | day 1  | 🟡 (In Progress) |
| Core Features        | Courses, Assignments                       | day 2  | ⚪ (Pending)     |
| Advanced Features    | Grades, Attendance                         | day 3  | ⚪ (Pending)     |
| Testing & Documentation                      | day 4 | ⚪ (Pending)     |



## 📌 Day 1: Project Setup & Authentication
**Goal**: Basic Django setup + user roles (Teacher/Student).

### ✅ Tasks:
1. **Project Setup**
    - `django-admin startproject classroom`
    - `python manage.py startapp accounts`
    - Install: `django`, `pillow`, `django-crispy-forms`
  
2. **Custom User Model**
    - Extend `AbstractUser` (add `is_teacher`, `is_student`)
    - Register in `admin.py`

3. **Login/Registration**
    - `django-allauth` (quick auth setup) or manual forms
    - Basic templates (`login.html`, `signup.html`)

4. **Basic Dashboard**
    - Redirect teachers/students to different dashboards

## 📌 Day 2: Course Management
**Goal**: Teachers create courses, students enroll.

### ✅ Tasks:
1. **Course Model**
    ```python
    class Course(models.Model):
        title = models.CharField(max_length=200)
        teacher = models.ForeignKey(User, on_delete=models.CASCADE)
        students = models.ManyToManyField(User, blank=True, related_name='courses')
    ```

2. **Views**
    - Teachers: `CreateCourse`, `CourseListView`
    - Students: `EnrollView`

3. **Templates**
    - `course_list.html` (shows available courses)
    - `course_detail.html` (enroll button for students)

## 📌 Day 3: Assignment System
**Goal**: Teachers post assignments, students submit.

### ✅ Tasks:
1. **Assignment Model**
    ```python
    class Assignment(models.Model):
        title = models.CharField(max_length=200)
        description = models.TextField()
        due_date = models.DateTimeField()
        course = models.ForeignKey(Course, on_delete=models.CASCADE)
    ```

2. **Submission Model**
    ```python
    class Submission(models.Model):
        assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
        student = models.ForeignKey(User, on_delete=models.CASCADE)
        file = models.FileField(upload_to='submissions/')
        submitted_at = models.DateTimeField(auto_now_add=True)
    ```

3. **Views**
    - Teachers: `CreateAssignment`, `ViewSubmissions`
    - Students: `SubmitAssignment`

## 📌 Day 4: Grading & Attendance (Basic)
**Goal**: Teachers grade assignments & mark attendance.

### ✅ Tasks:
1. **Grade Model**
    ```python
    class Grade(models.Model):
        submission = models.OneToOneField(Submission, on_delete=models.CASCADE)
        score = models.FloatField()
        feedback = models.TextField()
    ```

2. **Attendance Model**
    ```python
    class Attendance(models.Model):
        student = models.ForeignKey(User, on_delete=models.CASCADE)
        course = models.ForeignKey(Course, on_delete=models.CASCADE)
        date = models.DateField()
        status = models.BooleanField(default=False)  # Present/Absent
    ```

3. **Views**
    - Teachers: `GradeSubmission`, `MarkAttendance`
    - Students: `ViewGrades`

## 📌 Day 5: Polish & Deploy
**Goal**: Fix bugs, improve UI, deploy.

## 🚀 Final Deliverables (After 5 Days)
### ✅ Teachers can:
- Create courses
- Post assignments
- Grade submissions
- Mark attendance

### ✅ Students can:
- Enroll in courses
- Submit assignments
- View grades