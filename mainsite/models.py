# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import time, hashlib

# Create your models here.

def create_id():
	md5 = hashlib.md5(str(time.clock()).encode('utf-8'))
	return md5.hexdigest()

class Post(models.Model):
	title = models.CharField(max_length=200)
	slug = models.CharField(max_length=33, default=create_id(), editable=False)
	body = models.TextField()
	pub_date= models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ('-pub_date',)
	
	def __unicode__(self):
		return self.title
