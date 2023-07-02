from django.db import models

# Create your models here.





class course(models.Model):
    name = models.CharField(max_length=25)
    tagline = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/')
    def __str__(self):
        return self.name
    
class PDF_var(models.Model):
       document=models.FileField(upload_to='doc/')
       document_title=models.CharField(max_length=10)
       ducument_description=models.TextField(max_length=100)
       module=models.ForeignKey(course,on_delete=models.CASCADE)
       def __str__(self):
            return self.document_title

