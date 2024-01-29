from django.urls import path
from .views import (ExerciseList, ExerciseDetail, ExerciseListByCategory, ExerciseListByEquipment, ExerciseListByMechanic, ExerciseListByLevel, ExerciseListByForce, ExerciseListBySecondaryMuscles, ExerciseListByPrimaryMuscles, ExerciseListByName)

urlpatterns = [
    path('', ExerciseList.as_view(), name='exercise-list'),
    path('<uuid:pk>/', ExerciseDetail.as_view(), name='exercise-detail'),
    path('by_category/', ExerciseListByCategory.as_view(), name='exercise-list-by-category'),
    path('by_equipment/', ExerciseListByEquipment.as_view(), name='exercise-list-by-equipment'),
    path('by_mechanic/', ExerciseListByMechanic.as_view(), name='exercise-list-by-mechanic'),
    path('by_level/', ExerciseListByLevel.as_view(), name='exercise-list-by-level'),
    path('by_force/', ExerciseListByForce.as_view(), name='exercise-list-by-force'),
    path('by_secondary_muscles/', ExerciseListBySecondaryMuscles.as_view(), name='exercise-list-by-secondary-muscles'),
    path('by_primary_muscles/', ExerciseListByPrimaryMuscles.as_view(), name='exercise-list-by-primary-muscles'),
    path('by_name/', ExerciseListByName.as_view(), name='exercise-list-by-name'),
]
