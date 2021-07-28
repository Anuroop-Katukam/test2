
from celery import shared_task


import csv
@shared_task(name="sum_two_numbers")
def add(data):
    print(data.field_name.path)
    

import requests
from celery.decorators import task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)
from testapp import views

@task(name='my_first_task')
def my_first_task(duration):
    print(duration)
    a = views.task()
    
    return("first done")