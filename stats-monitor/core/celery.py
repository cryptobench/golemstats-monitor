from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
import logging
from celery.schedules import crontab


logger = logging.getLogger("Celery")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    from collector.tasks import NetworkUtilization, NetworkComputing, NodeDetailed, NodeComputing, NodeEarnings, NodeActivity, ProviderAverageEarnings, NetworkEarnings6h, NetworkEarnings24, NetworkEarnings365d, NetworkOnline, NetworkOnlineStats, NetworkVersions, NetworkHistoricalStats, NodeOperator
    sender.add_periodic_task(
        15.0,
        NetworkUtilization.s(),
    )
    sender.add_periodic_task(
        15.0,
        NetworkComputing.s(),
    )
    sender.add_periodic_task(
        15.0,
        NodeDetailed.s(),
    )
    sender.add_periodic_task(
        15.0,
        NodeComputing.s(),
    )
    sender.add_periodic_task(
        15.0,
        NodeEarnings.s(),
    )
    sender.add_periodic_task(
        15.0,
        NodeActivity.s(),
    )
    sender.add_periodic_task(
        15.0,
        ProviderAverageEarnings.s(),
    )
    sender.add_periodic_task(
        15.0,
        NetworkEarnings6h.s(),
    )
    sender.add_periodic_task(
        15.0,
        NetworkEarnings24.s(),
    )
    sender.add_periodic_task(
        15.0,
        NetworkEarnings365d.s(),
    )
    sender.add_periodic_task(
        15.0,
        NetworkOnline.s(),
    )
    sender.add_periodic_task(
        15.0,
        NetworkOnlineStats.s(),
    )
    sender.add_periodic_task(
        15.0,
        NetworkVersions.s(),
    )
    sender.add_periodic_task(
        15.0,
        NetworkHistoricalStats.s(),
    )
    sender.add_periodic_task(
        15.0,
        NodeOperator.s(),
    )


app.conf.broker_url = 'redis://redis:6379/0'
app.conf.result_backend = 'redis://redis:6379/0'
