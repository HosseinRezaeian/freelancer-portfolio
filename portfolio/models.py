from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=60)
    pic = models.ImageField(upload_to='profile/images')
    pic2 = models.ImageField(upload_to='profile/images')
    birthday = models.DateField()
    experience = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=60)
    degree_choise = (
        ('university degree', 'university degree'),
        ('Masters degree', 'Masters degree'),
        ('Doctorate degree', 'Doctorate degree'),
        ('Vocational school', 'Vocational school'),
        ('High School', 'High School'),
    )
    degree = models.CharField(choices=degree_choise, max_length=20)


    def __str__(self):
        return self.name


class About(models.Model):
    title = models.CharField(max_length=50)
    discription = models.TextField()

    def __str__(self):
        return self.title


class EducationAndExpericence(models.Model):
    class Meta:
        db_table = 'education_expericence'

    title = models.CharField(max_length=50)
    place_name = models.CharField(max_length=50)
    year_from = models.DateField()
    year_to = models.DateField()
    category = (
        ('expericence', 'Expericence'),
        ('education', 'Education'),
    )
    categoryes = models.CharField(choices=category, max_length=13)
    discription = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Skills(models.Model):
    title = models.CharField(max_length=50)
    percent = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)], default=1)

    def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField(max_length=30)
    icon_name = models.CharField(max_length=20)
    discription = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class category_gallery(models.Model):
    name = models.CharField(max_length=50)
    filter = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class picture_gallery(models.Model):
    picture = models.ImageField()
    category = models.ForeignKey(category_gallery, on_delete=models.CASCADE)

    def __str__(self):
        return self.category.filter
