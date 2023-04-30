from django.db import models

class Community(models.Model):
	community_name = models.CharField(max_length=200, unique=True)
	community_description = models.TextField()
	community_image = models.ImageField(upload_to='community_imgs/')
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.community_name


class CommunityPost(models.Model):
	community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name="communities")
	username = models.CharField(max_length=200)
	body = models.TextField()
	date_posted = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.body