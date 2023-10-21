from rest_framework.viewsets import ModelViewSet
from greatproject.utils import (Helper, get_query)
from .models import (ProjectModel, SubmissionModel)
from .serializers import (ProjectSerializer, SubmissionSerializer)
import pytz
from datetime import datetime
from rest_framework.response import Response
from rest_framework import status


class ProjectCreateUpdateView(ModelViewSet):
	queryset = ProjectModel.objects.all()
	serializer_class = ProjectSerializer
	http_method_names = ['post', 'patch', 'delete']


class SubmissionView(ModelViewSet):
	queryset = SubmissionModel.objects.all()
	serializer_class = SubmissionSerializer
	http_method_names = ['post']

	def get_queryset(self):

		if self.request.method.lower() != 'get':
			return self.queryset

		filter_params = self.request.query_params.dict()

		try:
			results = self.queryset.filter(**filter_params)

		except Exception as e:
			raise Exception(e)

		return results
	
	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=False)

		# check that the project is active and not passed deadline
		project = ProjectModel.objects.get(pk=serializer.validated_data['project_id'])
		if not project.isactive:
			return Response({'message': 'Project is not active'}, status=status.HTTP_400_BAD_REQUEST)
		
		utc_now = datetime.now(pytz.utc)
		project_deadline_aware = project.deadline.replace(tzinfo=pytz.utc)
		# check that the deadline is not passed
		if project_deadline_aware < utc_now:
			return Response({'message': 'Project deadline is passed'}, status=status.HTTP_400_BAD_REQUEST)

		# check that the email is not already used for this project
		if SubmissionModel.objects.filter(project_id=serializer.validated_data['project_id'], email=serializer.validated_data['email']).exists():
			return Response({'message': 'Email already submitted for this project'}, status=status.HTTP_400_BAD_REQUEST)

		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class GetProjectView(ModelViewSet):
	queryset = ProjectModel.objects.all()
	serializer_class = ProjectSerializer
	http_method_names = ['get']

	def get_queryset(self):
		if self.request.method.lower() != 'get':
			return self.queryset

		params = self.request.query_params.dict()
		keyword = params.pop('keyword', None)
		params.pop('page', None)
		results = self.queryset.filter(**params)
		if keyword:
			search_fields = ['title']
			query = get_query(keyword, search_fields)
			results = results.filter(query)

		filter_params = self.request.query_params.dict()

		# Remove search key from considerable fields
		if 'keyword' in filter_params:
			del filter_params['keyword']

		try:
			results = self.queryset.filter(**filter_params)

		except Exception as e:
			raise Exception(e)

		return results
