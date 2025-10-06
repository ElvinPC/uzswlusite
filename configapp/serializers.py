from rest_framework import serializers

from configapp.models import *


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"


class PageChildSerializer(serializers.ModelSerializer):

    class Meta:
        model = PageModels
        fields = ['id', 'title', 'url', 'position', 'sub']


class PageSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = PageModels
        fields = ['id', 'title', 'lang', 'sub', 'url', 'position', 'dic', 'children']

    def get_children(self, obj):
        children = PageModels.objects.filter(sub=obj.id)
        return PageChildSerializer(children, many=True).data


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = "__all__"


class ContentTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentText
        fields = "__all__"


class ContentFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentFile
        fields = "__all__"


class ContentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentImage
        fields = "__all__"


class ContentVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentVideo
        fields = "__all__"
