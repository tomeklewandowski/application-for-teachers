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
