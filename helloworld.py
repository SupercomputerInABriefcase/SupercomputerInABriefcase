#!/usr/bin/env python
from mpi4py import MPI


comm = MPI.COMM_WORLD

print("[{} of {}] Hello world! May the source be with you.".format(comm.rank, comm.size))
