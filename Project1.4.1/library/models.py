from django.db import models
from student.models import Students


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    birth_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.second_name}"


class Comment(models.Model):
    text = models.TextField()
    student = models.ForeignKey(Students, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Book(models.Model):
    title = models.CharField(max_length=200)
    comments = models.ManyToManyField(Comment)
    price = models.FloatField()
    description = models.TextField()
    count = models.IntegerField(default=1)
    create_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.price}"


class BookingBook(models.Model):
    student = models.ManyToManyField(Students)
    comments = models.ManyToManyField(Comment)
    book = models.ManyToManyField(Book)
    take_date = models.DateTimeField(auto_now_add=True)
    returned_date = models.DateTimeField(default=False)

    def __str__(self):
        return f"{self.student} {self.book}"


