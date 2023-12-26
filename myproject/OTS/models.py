from django.db import models


class Candidate(models.Model):
    username = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(null=False, max_length=20)
    name = models.CharField(null=False, max_length=20)
    test_attempted = models.IntegerField(default=0)
    point = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.username} {self.name}"


class Question(models.Model):
    qid = models.AutoField(primary_key=True, auto_created=True)
    question = models.TextField()
    a = models.CharField(max_length=255)
    b = models.CharField(max_length=255)
    c = models.CharField(max_length=255)
    d = models.CharField(max_length=255)
    answer = models.CharField(max_length=2)


class Result(models.Model):
    resultid = models.BigAutoField(primary_key=True, auto_created=True)
    username = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    time = models.TimeField(auto_now=True)
    attempt = models.IntegerField()
    right = models.IntegerField()
    wrong = models.IntegerField()

class Form(models.Model):
    name = models.CharField(max_length=200)
    email  = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField()



