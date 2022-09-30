from django import forms
from .models import Student
from .models import Question

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 모델
        fields = ['subject', 'content']  # QuestionForm에서 사용할 Question 모델의 속성
        labels = {
            'subject': '제목',
            'content': '내용',
        }