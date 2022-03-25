from django.db.models import DateTimeField
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    created_at = DateTimeField(auto_now_add=True)
    
    updated_at = DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.username
