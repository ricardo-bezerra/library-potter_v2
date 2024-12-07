from django.db import models

class Base (models.Model):
    creat_at = models.DateTimeField(auto_now_add=True)
    actualized_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Books(Base):
    title = models.CharField(max_length=55)
    url = models.URLField(unique=True, max_length=550)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title

class Employees(Base):
    book = models.ForeignKey(Books, related_name='employees', on_delete=models.CASCADE)
    name = models.CharField(max_length=55)
    email = models.EmailField()
    business_unity = models.CharField(max_length=25)
    type_function = models.CharField(max_length=25)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        unique_together = ['email', 'book']

    def __str__(self):
        return f'{self.name} register the book {self.book}'
