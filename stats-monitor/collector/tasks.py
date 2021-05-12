from core.celery import app
from celery import Celery
from .models import ResponseLog
import requests


@app.task
def NetworkUtilization():
    r = requests.get("https://api.golemstats.com/v1/network/1/1")
    time = r.elapsed
    responsecode = r.status_code
    ResponseLog.objects.create(
        ResponseTime=time, ResponseCode=responsecode, Url="https://api.golemstats.com/v1/network/1/1", Name="Network Utilization")
