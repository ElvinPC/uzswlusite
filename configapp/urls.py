from django.urls import path, include
from configapp.views import *
from rest_framework.routers import DefaultRouter, Route

router = DefaultRouter()
router.register(r'Language', LanguageView, basename="/")
router.register(r'Content', ContentView)
router.register(r'ContentText', ContentTextView)
router.register(r'ContentFile', ContentFileView)
router.register(r'ContentImage', ContentImageView)
router.register(r'ContentVideo', ContentVideoView)
urlpatterns = [
    path('', include(router.urls)),
    path('pages/', PageModelsAPIView.as_view()),
    path('pages/<str:lang_code>/', PageDetailAPIView.as_view(), name='pages-list'),
    path('pages/<str:lang_code>/<path:path>/', PageDetailAPIView.as_view(), name='pages-detail'),

]
