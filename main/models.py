from django.db import models


class ProjectModel(models.Model):
	title = models.CharField(max_length=200)
	info = models.TextField()
	rules = models.TextField(null=True, blank=True)
	prizes = models.TextField()
	deadline = models.DateTimeField()
	isactive = models.BooleanField(default='false')
	cover = models.ImageField(null=True, upload_to='project_hub')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('-isactive', )


class SubmissionModel(models.Model):
	project = models.ForeignKey('ProjectModel', on_delete=models.CASCADE, related_name='submissions')
	fullname = models.CharField(max_length=200)
	email = models.EmailField()
	testinglink = models.CharField(max_length=200)
	repositories = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('created_at', )
		unique_together = ('project', 'email', )
