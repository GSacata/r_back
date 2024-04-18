from rest_framework import serializers
from .models import TodoTask

class TodoTaskSerializer(serializers.ModelSerializer):
    model = TodoTask
    fields = ['task_title', 'task_completion', 'task_created_at', 'task_updated_at']