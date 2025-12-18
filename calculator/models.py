from django.db import models


class Subject(models.Model):
    GRADE_CHOICES = [
        ('A', 'A'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B', 'B'),
        ('B-', 'B-'),
        ('C+', 'C+'),
        ('C', 'C'),
        ('C-', 'C-'),
        ('D+', 'D+'),
        ('D', 'D'),
        ('F', 'F'),
    ]

    name = models.CharField(max_length=100)
    credits = models.PositiveIntegerField()
    letter_grade = models.CharField(
        max_length=2,
        choices=GRADE_CHOICES
    )

    @property
    def grade_point(self):
        grade_map = {
            'A': 4.0,
            'A-': 3.67,
            'B+': 3.33,
            'B': 3.0,
            'B-': 2.67,
            'C+': 2.33,
            'C': 2.0,
            'C-': 1.67,
            'D+': 1.33,
            'D': 1.0,
            'F': 0.0,
        }
        return grade_map[self.letter_grade]

    def __str__(self):
        return f"{self.name} ({self.letter_grade})"
