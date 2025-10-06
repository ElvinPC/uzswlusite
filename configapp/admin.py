from django.contrib import admin
from configapp.models import *
admin.site.register([Language,PageModels,Content,ContentText,ContentFile,ContentImage,ContentVideo])
