from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200,unique=True)
    password = models.CharField(max_length=200)
class book(models.Model):
    book_id=models.IntegerField(primary_key=True)
    book_name=models.CharField(max_length=200)
    book_author=models.CharField(max_length=200)
    book_type=models.CharField(max_length=200)


