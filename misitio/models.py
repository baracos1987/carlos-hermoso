from django.db import models

# Create tabla contactenos profe....
class contactenos (models.Model):
    email = models.EmailField()
    Subject = models.CharField(max_length=196)
    Message = models.TextField()

# los contactos aparezcan con el nombre del correo
    def __str__(self):
        return self.email