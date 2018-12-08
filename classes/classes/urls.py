from django.contrib import admin
from django.urls import path
from teams.views import CreateCourseType, delete_course_type, CreateGroup, delete_group_type, CreateStudents, delete_student
from exams.views import CreateExam, delete_exam, CreateExercise, delete_exercise, CreateExerciseStudent, delete_exercise_student

urlpatterns = [
    path('admin/', admin.site.urls),
    path('types/delete/<int:type_id>', delete_course_type, name='delete-type'),
    path('types/', CreateCourseType.as_view(), name='list-types'),
    path('groups/delete/<int:group_id>', delete_group_type, name='delete-group'),
    path('groups/', CreateGroup.as_view(), name='list-groups'),
    path('students/delete/<int:student_id>', delete_student, name='delete-student'),
    path('students/', CreateStudents.as_view(), name='list-students'),
    path('exams/delete/<int:exam_id>', delete_exam, name='delete-exam'),
    path('exams/', CreateExam.as_view(), name='list-exams'),
    path('exercises/delete/<int:exercise_id>', delete_exercise, name='delete-exercise'),
    path('exercises/', CreateExercise.as_view(), name='list-exercise'),
    path('exercises-students/delete/<int:exercise_student_id>', delete_exercise_student, name='delete-exercise-student'),
    path('exercises-students/', CreateExerciseStudent.as_view(), name='list-exercisestudent'),
]
