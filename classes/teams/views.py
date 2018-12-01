from django.shortcuts import render
from django.views import View
from teams.models import CourseType, Group, Student
from django.shortcuts import redirect
from django.urls import reverse
from exams.models import Exercise



class CreateCourseType(View):
    template_name = 'course_types.html'

    def get(self, request):
        types = CourseType.objects.all()
        return render(request, self.template_name, {
            'types': types
        })

    def post(self, request):
        name = request.POST.get('name')
        if name:
            CourseType.objects.create(name=name)
        return self.get(request)

def delete_course_type(request, type_id):
    course_type = CourseType.objects.get(id=type_id)
    course_type.delete()
    return redirect(reverse('list-types'))

class CreateGroup(View):
    template_name = 'groups.html'

    def get(self, request):
        types = CourseType.objects.all()
        groups = Group.objects.all()
        return render(request, self.template_name, {
            'types': types,
            'groups': groups
        })

    def post(self, request):
        signature = request.POST.get('signature')
        course_type_id = request.POST.get('type')
        if signature and course_type_id:
            course_type = CourseType.objects.get(id=int(course_type_id))
            Group.objects.create(signature=signature, course_type=course_type)
        return self.get(request)

def delete_group_type(request, group_id):
    group = Group.objects.get(id=group_id)
    group.delete()
    return redirect(reverse('list-groups'))

class CreateStudents(View):
    template_name = 'students.html'

    def get(self, request):
        students = Student.objects.all()
        groups = Group.objects.all()
        exercises = Exercise.objects.all()
        return render(request, self.template_name, {
            'students': students,
            'groups': groups,
            'exercises': exercises
        })

    def post(self, request):
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        github_nick = request.POST.get('github_nick')
        groups_id = request.POST.get('group')
        if name and surname and email and github_nick and groups_id:
            group = Group.objects.get(id=int(groups_id))
            Student.objects.create(name=name, surname=surname, email=email, github_nick=github_nick, group=group)
        return self.get(request)

def delete_student(request, student_id):
    student = Student.objects.get(id=int(student_id))
    student.delete()
    return redirect(reverse('list-students'))
