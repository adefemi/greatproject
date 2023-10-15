from django.contrib import admin
from .models import (ProjectModel, SubmissionModel)


admin.site.register(
	(ProjectModel, SubmissionModel)
)
