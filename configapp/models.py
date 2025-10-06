from django.db import models


class Base(models.Model):
    created_ed = models.DateTimeField(auto_now_add=True)
    updated_ed = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.__class__.__name__} ({self.created_ed.strftime('%Y-%m-%d %H:%M')})"


class Language(Base):
    title = models.CharField(max_length=50, unique=True)


class PageModels(Base):
    icon = models.ImageField(upload_to="home/icons/", blank=True, null=True)
    title = models.CharField(max_length=255)
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)
    sub = models.IntegerField(null=True, blank=True, default=None)
    url = models.SlugField(max_length=255, unique=True)
    position = models.IntegerField(default=None)
    dic = models.TextField(null=True, blank=True, default=None)

    class Meta:
        unique_together = ('url', 'lang')

    def __str__(self):
        return self.title


class Content(Base):
    page = models.ForeignKey(PageModels, on_delete=models.CASCADE, related_name="contents")
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class ContentText(Base):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name="texts")
    title = models.TextField()
    position = models.IntegerField()
    sub = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} (pos: {self.position})"


class ContentFile(Base):
    title = models.CharField(max_length=255)
    file = models.FileField(default=None, upload_to='files/%Y/%m/%d')
    position = models.IntegerField()
    sub = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ContentImage(Base):
    title = models.CharField(max_length=255)
    file = models.ImageField(default=None, upload_to='photo/%Y/%m/%d')
    position = models.IntegerField()
    sub = models.BooleanField(default=False)


class ContentVideo(Base):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to="videos/")
    position = models.IntegerField()
    sub = models.BooleanField(default=False)

    def __str__(self):
        return self.title
