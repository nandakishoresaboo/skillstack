# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class SkillSetUser(User):
   stack_user = models.ForeignKey(StackUser)
   yahoo_user = models.ForeignKey(YahooUser)


class StackUser(models.Model):
    pass

class YahooUser(models.Model):
    pass





 
