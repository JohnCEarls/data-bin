#!/usr/bin/env bash
simple_mpi_hosts.py
mpiexec --hostfile mpi.hosts ~/bin/mpi_get_procs.py
