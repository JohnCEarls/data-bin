#!/usr/bin/env python
import datautils
import logging
import socket
datautils.init_logging()

host_name = socket.gethostname()
with open('mpi.hosts', 'w') as temp:
    temp.write(host_name + '\n')
    my_nodes =  datautils.get_nodes()
    temp.write('\n'.join(my_nodes) + '\n')
logging.info('simple mpi.hosts written')
