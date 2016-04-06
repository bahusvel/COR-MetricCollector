import time
from subprocess import Popen

from cor.api import Message, CORModule
from cor.comm import static_router_factory

from collectd.collectd import Collectd
from viz3d.viz3d import Viz3D

p = Popen(["collectd", "-C", "/root/metric/collectd/collectd.conf", "-f"])

viz = Viz3D()
collector = Collectd(route_callback=static_router_factory({"SENSOR_READING":viz}))

while True:
	time.sleep(100)
