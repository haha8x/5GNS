#!/usr/bin/python
# flowvisor_topo.py
from mininet.topo import Topo
class FVTopo(Topo):
    def __init__(self):
        # Initialize topology
        Topo.__init__(self)
        # Create template host, switch, and link
        hconfig = {'inNamespace':True}
        LBW_path = {'bw': 1}
        HBW_path = {'bw': 10}
        host_link_config = {}
        # Create switch nodes
        for i in range(4):
            sconfig = {'dpid': "%016x" % (i+1)}
            self.addSwitch('s%d' % (i+1), **sconfig)
        # Create host nodes (h1, h2, h3, h4)
        for i in range(4):
            self.addHost('h%d' % (i+1), **hconfig)
        # Add switch links according to the topology
        self.addLink('s1', 's2', **LBW_path)
        self.addLink('s2', 's4', **LBW_path)
        self.addLink('s1', 's3', **HBW_path)
        self.addLink('s3', 's4', **HBW_path)
        # Add host links
        self.addLink('h1', 's1', **host_link_config)
        self.addLink('h2', 's1', **host_link_config)
        self.addLink('h3', 's4', **host_link_config)
        self.addLink('h4', 's4', **host_link_config)
topos = { 'slicingtopo': ( lambda: FVTopo() ) }