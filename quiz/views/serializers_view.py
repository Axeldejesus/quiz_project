from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from ..models import Question, Theme, ImageQuiz
from ..serializers import QuestionSerializer, ThemeSerializer,  ImageQuizSerializer

class ReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    
    pass  

class QuestionViewSet(ReadOnlyViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny]

class ThemeViewSet(ReadOnlyViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    permission_classes = [AllowAny]

class ImageQuizViewSet(ReadOnlyViewSet):
    queryset = ImageQuiz.objects.all()
    serializer_class = ImageQuizSerializer
    permission_classes = [AllowAny]

