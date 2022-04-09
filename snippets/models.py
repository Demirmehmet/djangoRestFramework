from django.db import models

LANGUAGE_CHOICES = (
    ("1", "python"),
    ("2", "C++"),
    ("3", "C#"),
    ("4", "java"),
    ("5", "swift"),
)

STYLE_CHOICES = (
    ("1", "friendly"),
    ("2", "unfriendly"),
)


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(default='python', max_length=100, choices=LANGUAGE_CHOICES)
    style = models.CharField(default='friendly', max_length=100, choices=STYLE_CHOICES)

    class Meta:
        ordering = ['created']
