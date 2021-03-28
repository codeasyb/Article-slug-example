from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title
    
#   this works with intger for primary keys
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
    
#     class Meta:
#         unique_together = ('title', 'slug')
    
    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    # this works with slugs 
    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})
