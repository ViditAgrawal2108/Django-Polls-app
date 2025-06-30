from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Question, Choice
from .serializers import QuestionSerializer
from django.shortcuts import get_object_or_404
from django.db.models import F

@api_view(['GET'])
def question_list(request):
    questions = Question.objects.all().order_by('-pub_date')
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    serializer = QuestionSerializer(question)
    return Response(serializer.data)

@api_view(['POST'])
def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    choice_id = request.data.get('choice_id')
    
    if not choice_id:
        return Response({'error': 'choice_id is required.'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        selected_choice = question.choice_set.get(pk=choice_id)
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        selected_choice.refresh_from_db()
        return Response({'message': 'Vote recorded.', 'votes': selected_choice.votes})
    except Choice.DoesNotExist:
        return Response({'error': 'Invalid choice ID.'}, status=status.HTTP_400_BAD_REQUEST)
