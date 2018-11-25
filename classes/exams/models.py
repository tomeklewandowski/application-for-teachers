from django.db import models
from teams.models import CourseType


class Exam(models.Model):
    course_type = models.ForeignKey(
        CourseType,
        verbose_name="Typ kursu",
        on_delete=models.SET_NULL,
        null=True
    )
    name = models.CharField(
        verbose_name="Nazwa",
        max_length=100
    )
    module_num = models.PositiveIntegerField(
        verbose_name="Nr modułu"
    )

    def __str__(self):
        return '{0}: {1}'.format(self.name, self.module_num)

    class Meta:
        verbose_name = "Egzamin"
        verbose_name_plural = "Egzaminy"

class Exercise(models.Model):
    num = models.PositiveIntegerField(
        verbose_name="Nr zadania"
    )
    points = models.PositiveIntegerField(
        verbose_name="Punkty"
    )
    description = models.TextField(
        verbose_name="Treść zadania"
    )
    exam = models.ForeignKey(
        Exam,
        verbose_name="Egzamin",
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        short_desc = ''
        if len(self.description) < 20:
            short_desc = self.description
        else:
            short_desc = self.description[0:20] + '...'
        return '{0}:{1} - {2}'.format(self.exam.name, self.num, short_desc)

    class Meta:
        verbose_name = "Zadanie"
        verbose_name_plural = "Zadania"

class ExerciseStudent(models.Model):
    student = models.ForeignKey(
        'teams.Student',
        verbose_name="Student",
        on_delete=models.CASCADE
    )
    exercise = models.ForeignKey(
        Exercise,
        verbose_name="Zadanie",
        on_delete=models.CASCADE
    )
    points = models.PositiveIntegerField(
        verbose_name="Zdobyte punkty"
    )

    def __str__(self):
        return '{0}:{1}:{2}'.format(
            self.student.github_nick,
            self.exercise.exam.module_num,
            self.exercise.num
        )

    class Meta:
        verbose_name = "Zadanie zrobione przez studenta"
        verbose_name_plural = "Zadania zrobione przez studentów"


