#!/usr/bin/env python
"""
Hello World MPI program

e.g.
$ mpirun -np 4 ./helloworld.py
"""
from mpi4py import MPI


comm = MPI.COMM_WORLD

print("[{} of {}] Hello world! May the source be with you.".format(comm.rank, comm.size))
