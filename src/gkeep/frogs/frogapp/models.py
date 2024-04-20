from django.db import models
from frogapp.common.constants import FROG_STATUS, TASK_STATUS

class Task(models.Model):
  '''
  Atomic version of a frog, cannot be divided further. A frog will consist of one or more tasks, if not provided, we take frog details as the task details.
  '''
  deadline = models.DateTimeField(blank=True)
  description = models.TextField()
  # estimated time taken to complete this task in seconds
  estimate = models.DurationField(blank=True)
  status = models.IntegerField(choices=TASK_STATUS)
  weight = models.PositiveIntegerField()

  def __str__(self) -> str:
    return self.description

 
class Frog(models.Model):
  '''
  A goal to be accomplished. Will always be divided into further tasks.
  '''
  deadline = models.DateTimeField()
  description = models.TextField()
  # this will be the sum of estimates of all tasks
  estimate = models.DurationField(blank=True)
  status = models.IntegerField(choices=FROG_STATUS)
  # all tasks inside a `Frog`
  # TODO: this shouldn't be a ForeignKey, something like ManyToMany with storing Task ids if not whole task.
  task = models.ForeignKey(Task, on_delete=models.CASCADE)