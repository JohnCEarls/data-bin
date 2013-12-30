#!/usr/bin/env python
import sys
import boto
import boto.ec2
import boto.utils
import re
import logging
import subprocess
import datautils
def rsync_home( nodes ):
    for node in nodes:
        node_str = 'sgeadmin@%s:~/' % node
        command = ['rsync', '-avz', '~/', node_str]
        logging.info("Command: %s" % ' '.join(command))
        result = subprocess.check_output(' '.join(command), shell=True)
        logging.info("Response:")
        logging.info("=" * 50)
        logging.info(result)

if __name__ == '__main__':
    datautils.init_logging()
    try:
        nodes = datautils.get_nodes()
        rsync_home( nodes )
    except:
        logging.exception("********ERROR in rsync***********")
        raise
