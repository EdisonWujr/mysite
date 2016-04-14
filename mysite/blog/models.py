<<<<<<< HEAD
from __future__ import unicode_literals

from django.db import models

from django.contrib import admin
# Create your models here.
=======
from django.db import models
from django.contrib import admin
>>>>>>> 0fa34c774731f84c03efe9c3f10892984cc88f15

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
<<<<<<< HEAD
    class Meta:
        ordering = ('-timestamp',)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp','body')


admin.site.register(BlogPost,BlogPostAdmin)


=======

admin.site.register(BlogPost)
>>>>>>> 0fa34c774731f84c03efe9c3f10892984cc88f15
