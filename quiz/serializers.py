from rest_framework import serializers
from .models import Question, Theme, ImageQuiz


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = '__all__'

class ImageQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageQuiz
        fields = '__all__'
