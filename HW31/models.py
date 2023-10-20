from django.db import models
from django.db import transaction

class TransactionExample(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    @classmethod
    def perform_transaction(cls, name, amount):
        with transaction.atomic():
            instance = cls.objects.select_for_update().get(name=name)
            instance.balance += amount
            instance.save()
            if instance.balance < 0:
                transaction.set_rollback(True)



class AuthorManager(models.Manager):
    def female_authors(self):
        return self.filter(gender='F')

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

class Author(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    objects = AuthorManager()