from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class QuestionAnswered(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    was_right = models.BooleanField()
    
#    answer = models.OneToMany(
#        User,
#        username = was_right
#    
#    )


# How to use this SOB
# in views.py:
# Record a user answered something correctly
# QuestionAnswered.objects.create(
#    user=request.user,
#    was_right=True,
# )

# Getting "correct count"
# number_they_got_right = QuestionAnswered.objects.filter(
#    user=request.user,
#    was_right=True,
# ).count()



