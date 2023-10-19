from rest_framework import serializers
from .models import (ProjectModel, SubmissionModel)


class ProjectSerializer(serializers.ModelSerializer):
	submission_count = serializers.SerializerMethodField()
	class Meta:
		model = ProjectModel
		fields = '__all__'

	def get_submission_count(self, obj):
		return SubmissionModel.objects.filter(project=obj).count()

class SubmissionSerializer(serializers.ModelSerializer):
	project = ProjectSerializer(read_only=True)
	project_id = serializers.IntegerField(write_only=True)
	class Meta:
		model = SubmissionModel
		fields = '__all__'
