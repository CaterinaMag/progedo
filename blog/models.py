from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):
    """
    This model represent a category of posts
    """
    title = models.CharField(max_length=512, null=False)
    slug = models.SlugField(null=False, unique=True, max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        """
        Returns the string representation of the model, which is used in the
        Django Admin interface
        """
        return "Category: %s" % self.title

    def get_absolute_url(self): #This tells Django how to calculate the URL for an object
        from django.urls import reverse
        return reverse('category', kwargs={'slug': str(self.slug)})

    class Meta:
        verbose_name_plural = "Categories"

class Post(models.Model):
    """
    This model represent a post of the blog
    """
    title = models.CharField(max_length=1024, null=False)
    slug = models.SlugField(null=False, unique=True, max_length=255)
    category = models.ForeignKey('Category')
    content = models.TextField(null=False)
    date = models.DateField()
    author = models.ForeignKey('auth.User')
    is_published = models.BooleanField(null=False, default=False)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('post', kwargs={'slug': str(self.slug)})

    @property  #questo metodo mi permette di far visualizzare solo i primi 125 caratteri del post
    def excerpt(self):
        return self.content[:125] + "..."

    def __str__(self):
        """
        Returns the string representation of the model, which is used in the
        Django Admin interface
        """
        return "Post: %s" % self.title

# fatto da me
class Comment(models.Model):

    title = models.CharField(max_length=1024, null=False)
    content = models.TextField(null=True)
    #slug = models.SlugField(null=False, unique=True, max_length=255)
    date = models.DateField()
    author = models.ForeignKey('auth.User')
    post = models.ForeignKey('Post') # in teoria qui avrei potuto metterci un related_name = comments, in quel caso cambia il comando jinjia in index per richiamarlo; non piu' il comment_set.all ma comments.all

    def __str__(self):

        return "Comment: %s" % self.content

# fine del fatto da me
    @property
    def gravatar_url(self):
        """
        Returns the gravatar URL for this user
        """
        import hashlib
        m = hashlib.md5()
        m.update(self.author.email.encode())
        return "https://www.gravatar.com/avatar/" + m.hexdigest()


