import os.path
import sys
import boto
import boto.ec2
import boto.utils
import re
import logging
import subprocess
def get_region(region_name):
    for region in boto.ec2.regions():
        if region_name == region.name:
            logging.info("node region[%s]" % region.name)
            return region

def get_my_alias():
    identity = boto.utils.get_instance_identity()
    conn = boto.connect_ec2(region=get_region( identity['document']['region']))
    mytags = conn.get_all_tags(filters={'resource-id':identity['document']['instanceId'], 'key':'alias'})
    for tag in mytags:
        if tag.name == 'alias':
            logging.info("my alias[%s]" % tag.value)
            return tag.value

def get_nodes(include_me=False):
    nodes = []
    my_alias = get_my_alias()
    identity = boto.utils.get_instance_identity()
    conn = boto.connect_ec2(region=get_region( identity['document']['region']))
    m = re.match(r'(?P<cluster>\w*-?)(master|node\d\d\d)', my_alias)
    if m:
        mycluster = m.groupdict()['cluster']
        aliases = conn.get_all_tags(filters={'resource-type':'instance', 'key':'alias'})
        for alias in aliases:
            my_str = mycluster + r'((master)|(node\d\d\d))'
            
            if re.match(my_str, alias.value) and (alias.value != my_alias or
                include_me):
                nodes.append(alias.value)
    logging.info( "Cluster nodes [%s]" % ' ,'.join( nodes ))
    return nodes
def init_logging(fname="~/bin/local.log"):
    fname = os.path.expanduser(fname)
    logging.basicConfig(filename=fname,level=logging.DEBUG, 

            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    rLogger = logging.getLogger('')
    bLogger = logging.getLogger('boto')
    bLogger.setLevel(logging.ERROR)
    so_handler = logging.StreamHandler(sys.stdout)
    so_handler.setLevel( logging.ERROR )
    so_handler.setFormatter( logging.Formatter(
                        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    rLogger.addHandler(so_handler)
