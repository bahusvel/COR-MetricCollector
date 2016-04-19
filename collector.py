from cor.api import Launcher
from csvdumper.metricjsondumper import MetricJsonDumper
from cor.comm import TCPSocketNetworkAdapter

collector = Launcher()
collector.launch_module(MetricJsonDumper, network_adapter=TCPSocketNetworkAdapter(hostport="0.0.0.0:6090"), path="/root/dump")
