from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    age = models.IntegerField(null=True,blank=True)
    mom_name = models.CharField(max_length=30, blank=True)
    dad_name = models.CharField(max_length=30, null=True)


    def __str__(self):
        return self.first_name



"""
from django.db import models
# importing validationerror
from django.core.exceptions import ValidationError

# creating a validator function
def validate_geeks_mail(value):
	if "@gmail.com" in value:
		return value
	else:
		raise ValidationError("This field accepts mail id of google only")


# Create your models here.
class GeeksModel(models.Model):
	geeks_mail = models.CharField(
						max_length = 200,
						validators =[validate_geeks_mail]
						)

from django.core.validators import FileExtensionValidator
class Post(models.Model):
	PDF = models.FileField(null=True,
						blank=True,
						validators=[FileExtensionValidator( ['pdf'] ) ])

"""