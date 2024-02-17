from django.db import models

# Create your models here.
JOB_TYPE = (
    ('full time job','full time job'),
    ('part time job','part time job'),
)

class job(models.Model):
    title = models.CharField(max_length=100)

    pass
    job_type = models.CharField(max_length=15,choices=JOB_TYPE)
    #location
    description =models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.title