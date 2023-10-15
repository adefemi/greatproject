from rest_framework import serializers
from .models import (ProjectModel, SubmissionModel)


class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProjectModel
		fields = '__all__'


class SubmissionSerializer(serializers.ModelSerializer):
	project = ProjectSerializer(read_only=True)
	project_id = serializers.IntegerField(write_only=True)
	class Meta:
		model = SubmissionModel
		fields = '__all__'
