from django.db import models


# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=202)
    image = models.ImageField(upload_to='about/')
    body = models.TextField()
    python = models.CharField(max_length=202)
    telegram_bot = models.CharField(max_length=202)
    backend = models.CharField(max_length=202)
    rest = models.CharField(max_length=202)

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=202)

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    title = models.CharField(max_length=202)
    image = models.ImageField(upload_to='portfolio/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=202)
    body = models.TextField()

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Resume_work(models.Model):
    title = models.CharField(max_length=202)
    office = models.CharField(max_length=202)
    address = models.CharField(max_length=202)
    wort_time = models.CharField(max_length=202)

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Resume_education(models.Model):
    title = models.CharField(max_length=202)
    education = models.CharField(max_length=202)
    read_time = models.CharField(max_length=202)

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Happy_client(models.Model):
    fullname = models.CharField(max_length=202)
    image = models.ImageField(upload_to='happy_clients/')
    body = models.TextField()

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    first_name = models.CharField(max_length=202)
    last_name = models.CharField(max_length=202)
    email = models.EmailField()
    message = models.TextField()
    is_published = models.BooleanField(default=False)

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name
