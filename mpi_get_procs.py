#!/usr/bin/env python
from mpi4py import MPI
import socket
import multiprocessing
comm = MPI.COMM_WORLD

cpus = multiprocessing.cpu_count()
host_name = socket.gethostname()
rfs = comm.gather((host_name, cpus))
if comm.rank == 0:
    rfs.sort()
    fmt = "%s\tslots=%i\n"
    with open('mpi.hosts', 'w') as hfile:
        for r in rfs:
            hfile.write(fmt % r)
