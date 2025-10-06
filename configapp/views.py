from django.db.models import Q
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from configapp.serializers import *
from rest_framework.views import APIView
from configapp.models import *


class LanguageView(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class PageModelsAPIView(APIView):

    @swagger_auto_schema(
        operation_description="Barcha sahifalar ro'yxatini olish",
        responses={200: PageSerializer(many=True)}
    )
    def get(self, request):
        pages = PageModels.objects.filter(Q(sub__isnull=True) | Q(sub=0)).order_by('position')
        serializer = PageSerializer(pages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Yangi sahifa yaratish",
        request_body=PageSerializer,
        responses={201: PageSerializer()}
    )
    def post(self, request):
        serializer = PageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PageDetailAPIView(APIView):

    @swagger_auto_schema(
        operation_description="Til bo‘yicha barcha sahifalarni olish yoki ma’lum slugli sahifani olish",
        manual_parameters=[
            openapi.Parameter('lang_code', openapi.IN_PATH, description="Til kodi (masalan: uz, ru, en)",
                              type=openapi.TYPE_STRING),
            openapi.Parameter('slug', openapi.IN_PATH, description="Sahifa URL yoki slug qiymati",
                              type=openapi.TYPE_STRING),
        ],
        responses={200: PageSerializer()}
    )
    def get(self, request, lang_code, path=None):
        lang_map = {"uz": 1, "ru": 2, "en": 3}
        lang_id = lang_map.get(lang_code.lower())
        if not lang_id:
            return Response({"error": "Til topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        if not path:
            pages = PageModels.objects.filter(lang=lang_id, sub__isnull=True).order_by('position')
            serializer = PageSerializer(pages, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        segments = path.strip('/').split('/')
        parent_url = segments[0]
        parent = PageModels.objects.filter(lang=lang_id, url=parent_url, sub__isnull=True).first()
        if not parent:
            return Response({"error": "Ota sahifa topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        page = parent
        if len(segments) > 1:
            for slug in segments[1:]:
                child = PageModels.objects.filter(lang=lang_id, url=slug, sub=page.id).first()
                if not child:
                    return Response({"error": f"Child sahifa topilmadi: {slug}"}, status=status.HTTP_404_NOT_FOUND)
                page = child

        serializer = PageSerializer(page)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Yangi sahifa yaratish",
        request_body=PageSerializer,
        responses={201: PageSerializer()}
    )
    def post(self, request, lang_code, slug=None):
        lang_map = {"uz": 1, "ru": 2, "en": 3}
        lang_id = lang_map.get(lang_code.lower())
        if not lang_id:
            return Response({"error": "Til topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()
        data['lang'] = lang_id
        serializer = PageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Sahifani yangilash",
        request_body=PageSerializer,
        manual_parameters=[
            openapi.Parameter('slug', openapi.IN_PATH, description="Sahifa URL yoki slug qiymati",
                              type=openapi.TYPE_STRING)
        ],
        responses={200: PageSerializer()}
    )
    def put(self, request, lang_code, slug):
        lang_map = {"uz": 1, "ru": 2, "en": 3}
        lang_id = lang_map.get(lang_code.lower())
        if not lang_id:
            return Response({"error": "Til topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        page = PageModels.objects.filter(lang=lang_id, url__iexact=slug).first()
        if not page:
            return Response({"error": "Sahifa topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PageSerializer(page, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Sahifani o'chirish",
        manual_parameters=[
            openapi.Parameter('slug', openapi.IN_PATH, description="Sahifa URL yoki slug qiymati",
                              type=openapi.TYPE_STRING)
        ],
        responses={204: "Deleted successfully"}
    )
    def delete(self, request, lang_code, slug):
        lang_map = {"uz": 1, "ru": 2, "en": 3}
        lang_id = lang_map.get(lang_code.lower())
        if not lang_id:
            return Response({"error": "Til topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        page = PageModels.objects.filter(lang=lang_id, url__iexact=slug).first()
        if not page:
            return Response({"error": "Sahifa topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        page.delete()
        return Response({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class ContentView(ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class ContentTextView(ModelViewSet):
    queryset = ContentText.objects.all()
    serializer_class = ContentTextSerializer


class ContentFileView(ModelViewSet):
    queryset = ContentFile.objects.all()
    serializer_class = ContentFileSerializer


class ContentImageView(ModelViewSet):
    queryset = ContentImage.objects.all()
    serializer_class = ContentImageSerializer


class ContentVideoView(ModelViewSet):
    queryset = ContentVideo.objects.all()
    serializer_class = ContentVideoSerializer
