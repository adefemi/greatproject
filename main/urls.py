from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (SubmissionView, ProjectCreateUpdateView, GetProjectView)


router = DefaultRouter()
router.register('submission-url', SubmissionView, basename='submission-url')
router.register('create-project-url', ProjectCreateUpdateView, basename='create-project-url_list')
router.register('get-project-url', GetProjectView, basename='get-project-url_list')

urlpatterns = [
	path('', include(router.urls)),
]
