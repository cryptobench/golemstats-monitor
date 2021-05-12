from core.celery import app
from celery import Celery
from .models import ResponseLog
import requests


@app.task
def NetworkUtilization():
    url = "https://api.golemstats.com/v1/network/1/1"
    r = requests.get(url)
    time = r.elapsed
    responsecode = r.status_code
    ResponseLog.objects.create(
        ResponseTime=time, ResponseCode=responsecode, Url=url, Name="Network Utilization")


@app.task
def NetworkComputing():
    url = "https://api.golemstats.com/v1/provider/computing"
    r = requests.get(url)
    time = r.elapsed
    responsecode = r.status_code
    ResponseLog.objects.create(
        ResponseTime=time, ResponseCode=responsecode, Url=url, Name="Network Computing")


@app.task
def NodeDetailed():
    url = "https://api.golemstats.com/v1/provider/node/0x0c248304d0e01ecb9317b973cb53d6ded61d7b06"
    r = requests.get(url)
    time = r.elapsed
    responsecode = r.status_code
    ResponseLog.objects.create(
        ResponseTime=time, ResponseCode=responsecode, Url=url, Name="Node Detailed")


@app.task
def NodeComputing():
    url = "https://api.golemstats.com/v1/provider/node/0x0c248304d0e01ecb9317b973cb53d6ded61d7b06/computing"
    r = requests.get(url)
    time = r.elapsed
    responsecode = r.status_code
    ResponseLog.objects.create(
        ResponseTime=time, ResponseCode=responsecode, Url=url, Name="Node Computing")


@app.task
def NodeEarnings():
    url = "https://api.golemstats.com/v1/provider/node/0x0c248304d0e01ecb9317b973cb53d6ded61d7b06/earnings/720"
    r = requests.get(url)
    time = r.elapsed
    responsecode = r.status_code
    ResponseLog.objects.create(
        ResponseTime=time, ResponseCode=responsecode, Url=url, Name="Node Earnings")


@app.task
def NodeActivity():
    url = "https://api.golemstats.com/v1/provider/node/0x0c248304d0e01ecb9317b973cb53d6ded61d7b06/activity"
    r = requests.get(url)
    time = r.elapsed
    responsecode = r.status_code
    ResponseLog.objects.create(
        ResponseTime=time, ResponseCode=responsecode, Url=url, Name="Node Activity")


@app.task
def ProviderAverageEarnings():
    url = "https://api.golemstats.com/v1/provider/average/earnings"
    r = requests.get(url)
    time = r.elapsed
    responsecode = r.status_code
    ResponseLog.objects.create(
        ResponseTime=time, ResponseCode=responsecode, Url=url, Name="Providers Average Earnings")


@app.task
def NetworkEarnings6h():
    url = "https://api.golemstats.com/v1/network/earnings/6"
    r = requests.get(url)
    time = r.elapsed
    responsecode = r.status_code
    ResponseLog.objects.create(
        ResponseTime=time, ResponseCode=responsecode, Url=url, Name="Network Earnings 6h")


@app.task
def NetworkEarnings24h():
    url = "https://api.golemstats.com/v1/network/earnings/24"
    r = requests.get(url)
    time = r.elapsed
    responsecode = r.status_code
    ResponseLog.objects.create(
        ResponseTime=time, ResponseCode=responsecode, Url=url, Name="Network Earnings 24h")


@app.task
def NetworkEarnings365d():
    url = "https://api.golemstats.com/v1/network/earnings/365d"
    r = requests.get(url)
    time = r.elapsed
    responsecode = r.status_code
    ResponseLog.objects.create(
        ResponseTime=time, ResponseCode=responsecode, Url=url, Name="Network Earnings 365d")


@app.task
def NetworkOnline():
    url = "https://api.golemstats.com/v1/network/online"
    r = requests.get(url)
    time = r.elapsed
    responsecode = r.status_code
    ResponseLog.objects.create(
        ResponseTime=time, ResponseCode=responsecode, Url=url, Name="Network Online")


@app.task
def NetworkOnlineStats():
    url = "https://api.golemstats.com/v1/network/online/stats"
    r = requests.get(url)
    time = r.elapsed
    responsecode = r.status_code
    ResponseLog.objects.create(
        ResponseTime=time, ResponseCode=responsecode, Url=url, Name="Network Online Stats")


@app.task
def NetworkVersions():
    url = "https://api.golemstats.com/v1/network/versions"
    r = requests.get(url)
    time = r.elapsed
    responsecode = r.status_code
    ResponseLog.objects.create(
        ResponseTime=time, ResponseCode=responsecode, Url=url, Name="Network Versions")


@app.task
def NetworkHistoricalStats():
    url = "https://api.golemstats.com/v1/network/stats"
    r = requests.get(url)
    time = r.elapsed
    responsecode = r.status_code
    ResponseLog.objects.create(
        ResponseTime=time, ResponseCode=responsecode, Url=url, Name="Network Historical Stats")


@app.task
def NodeOperator():
    url = "https://api.golemstats.com/v1/provider/wallet/0x347987a2da0069cbcb54eaf2ccd8b67a09e632eb"
    r = requests.get(url)
    time = r.elapsed
    responsecode = r.status_code
    ResponseLog.objects.create(
        ResponseTime=time, ResponseCode=responsecode, Url=url, Name="Node Operator")
