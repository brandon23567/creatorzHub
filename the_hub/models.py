from django.db import models

class Content(models.Model):
	title = models.CharField(max_length=200)
	short_description = models.TextField(max_length=250)
	video_link = models.URLField(max_length=360)
	date_posted = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.short_description
