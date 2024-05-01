from django.db import models

class TeamStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    image = models.ImageField(upload_to="images/")
    twitter = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=212)
    image = models.ImageField(upload_to='author', blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
class Category(TeamStamp):
    title = models.CharField(max_length=40)
    def __str__(self):
        return self.title

class Tag(TeamStamp):
    title = models.CharField(max_length=40)
    def __str__(self):
        return self.title


class About(TeamStamp):
    title = models.CharField(max_length=212)
    image = models.ImageField(upload_to="images/")
    video = models.FileField(upload_to="videos/")
    description = models.TextField()
    description_missin = models.TextField()
    description_vision = models.TextField()
    description_value = models.TextField()

    def __str__(self):
        return self.title


class HappyClients(TeamStamp):
    description = models.TextField()
    image = models.ImageField(upload_to="images/")
    full_name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name

class Comment(TeamStamp):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    website = models.URLField()
    message = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ContactInfo(TeamStamp):
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    website = models.URLField()
