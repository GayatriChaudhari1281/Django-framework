from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

class Post(models.Model):
    Status_Choice=(('draft','Draft'),('published','Published'))#DROPDOWN list
    title=models.CharField(max_length=50)
    '''slugfield=automatically copies the data typed from one textfielfd to other.and
     used in SEO Search engine optimization.when we have to search a particular word  '''
    slug=models.SlugField(max_length=50,unique_for_date='publish')
    author=models.ForeignKey(User,related_name='blog_posts',on_delete=models.CASCADE)
    body=models.TextField()#CharField(max_length=1000)
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)#when post is created
    updated=models.DateTimeField(auto_now=True)#when save method gets called
    status=models.CharField(max_length=10,choices=Status_Choice,default='draft')
    tags=TaggableManager()
    class Meta:
        ordering=('-publish',)#since it is tuple we need to give , when single element is there
#while printing post then it internally calls to_str method so we have to override it.
#If we have to post then first title will print
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post_detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])

class Comments(models.Model):
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)#to show when person has commented
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)#if some comments are not good we can disable it from showing
    class Meta:
        ordering=('-created',)
    def __str__(self):
        return 'commented by  {}on {}'.format(self.name,self.post)
