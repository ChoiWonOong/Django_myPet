from django.db import models

# Create your models here.
# 게시글(Post)엔 이름(petname), 내용(contents)이 존재합니다

class Post(models.Model):
    postname = models.CharField(max_length=50)
    petimage = models.ImageField(upload_to='pets', blank = True)
    contents = models.TextField()

    def __str__(self):
        return self.postname

class Meta:
    ordering=['-id']   # id (ASC), -id(DESC)