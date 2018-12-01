from django.views import View
from exams.models import Exam, Exercise, ExerciseStudent
from teams.models import CourseType
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import render

class CreateExam(View):
    template_name = 'exams.html'

    def get(self, request):
        exams = Exam.objects.all()
        types = CourseType.objects.all()
        return render(request, self.template_name, {
            'exams': exams,
            'types': types
            })

    def post(self, request):
        name = request.POST.get('name')
        course_type = request.POST.get('course_type')
        module_num = request.POST.get('module_num')
        if name:
            Exam.objects.create(name=name, course_type=course_type, module_num=module_num)
        return self.get(request)

def delete_exam(request, exam_id):
    exam = Exam.objects.get(id=int(exam_id))
    exam.delete()
    return redirect(reverse('list-exams'))


class CreateExercise(View):
    template_name = 'exercise.html'

    def get(self, request):
        exercises = Exercise.objects.all()
        exams = Exam.objects.all()
        return render(request, self.template_name, {
            'exercises': exercises,
            'exams': exams
            })

    def post(self, request):
        exercise_num = request.POST.get('exercise_num')
        exercise_pkt = request.POST.get('exercise_pkt')
        description = request.POST.get('description')
        exam_id = request.POST.get('exam')
        if exercise_num and exercise_pkt and description and exam_id:
            exam = Exam.objects.get(id=int(exam_id))
            Exercise.objects.create(num=exercise_num, points=exercise_pkt, description=description, exam=exam)
        return self.get(request)

def delete_exercise(request, exercise_id):
    exercise = Exercise.objects.get(id=int(exercise_id))
    exercise.delete()
    return redirect(reverse('list-exercise'))


class CreateExerciseStudent(View):
    template_name = 'exercisestudent.html'

    def get(self, request):
        students = Student.objects.all()
        exercises = Exercise.objects.all()
        return render(request,self.template_name, {
            'students': students,
            'exercises': exercises
        })

    def post(self, request):
        exercise_num = request.POST.get('exercise_num')
        exercise_pkt = request.POST.get('exercise_pkt')
        students_points = request.POST.get('student_points')
        if exercise_num and exercise_pkt and students_points:
            ExerciseStudent.objects.create(num=exercise_num, points=exercise_pkt, students_points=students_points)
        return self.get(request)

def delete_exercise_student(request, exercise_student_id):
    exercise_student = ExerciseStudent.objects.get(id=int(exercise_student_id))
    exercise_student.delete()
    return redirect(reverse('list-exercisestudent'))

