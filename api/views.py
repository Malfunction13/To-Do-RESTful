from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from .serializers import TaskListSerializer, TaskDetailSerializer
from .models import Task
import datetime

class TasksList(APIView):

    def get(self, request):
        tasks = Task.objects.all().order_by('-id')
        serializer = TaskListSerializer(tasks, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = TaskListSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class TaskDetail(APIView):

    def get_task(self, pk):
        try:
            return Task.objects.get(pk=pk)

        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        task = self.get_task(pk)
        serializer = TaskDetailSerializer(task)

        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_task(pk)
        serializer = TaskDetailSerializer(task, data=request.data)

        if serializer.is_valid():
            if serializer.validated_data['completed'] == True:
                serializer.validated_data['time_completed'] = datetime.datetime.now()
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        else:

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_task(pk)
        task.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)