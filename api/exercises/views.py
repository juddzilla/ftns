from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import status
from .models import Exercise
from .serializers import ExerciseSerializer


class ExerciseList(APIView):
    """
    List all exercises, or create a new exercise.
    """
    def get(self, request, format=None):
        exercises = Exercise.objects.all()
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExerciseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExerciseDetail(APIView):
    """
    Retrieve, update or delete an exercise instance.
    """
    def get_object(self, pk):
        try:
            return Exercise.objects.get(pk=pk)
        except Exercise.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        exercise = self.get_object(pk)
        print(100)
        print(exercise.primary_muscles)
        serializer = ExerciseSerializer(exercise)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        exercise = self.get_object(pk)
        serializer = ExerciseSerializer(exercise, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        exercise = self.get_object(pk)
        exercise.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ExerciseListByCategory(ListAPIView):
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        category = self.request.query_params.get('category')
        return Exercise.objects.filter(category=category) if category else Exercise.objects.none()

class ExerciseListByEquipment(ListAPIView):
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        equipment = self.request.query_params.get('equipment')
        return Exercise.objects.filter(equipment=equipment) if equipment else Exercise.objects.none()

class ExerciseListByMechanic(ListAPIView):
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        mechanic = self.request.query_params.get('mechanic')
        return Exercise.objects.filter(mechanic=mechanic) if mechanic else Exercise.objects.none()

class ExerciseListByLevel(ListAPIView):
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        level = self.request.query_params.get('level')
        return Exercise.objects.filter(level=level) if level else Exercise.objects.none()

class ExerciseListByForce(ListAPIView):
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        force = self.request.query_params.get('force')
        return Exercise.objects.filter(force=force) if force else Exercise.objects.none()

class ExerciseListBySecondaryMuscles(ListAPIView):
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        secondary_muscles = self.request.query_params.get('secondary_muscles')
        return Exercise.objects.filter(secondary_muscles__contains=[secondary_muscles]) if secondary_muscles else Exercise.objects.none()

class ExerciseListByPrimaryMuscles(ListAPIView):
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        primary_muscles = self.request.query_params.get('primary_muscles')
        return Exercise.objects.filter(primary_muscles__contains=[primary_muscles]) if primary_muscles else Exercise.objects.none()

class ExerciseListByName(ListAPIView):
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name')
        return Exercise.objects.filter(name__icontains=name) if name else Exercise.objects.none()
