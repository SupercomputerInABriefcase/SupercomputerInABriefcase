# Supercomputer in a Briefcase

## Introduction

Clearly it is impossible to fit a supercomputer in a briefcase. But it is a great label for the idea of
being able to construct ad hoc dynamic clusters of computers with a view to using them to play with
parallelism.

## Purpose

This repository is for software to control and manage an ad hoc, dynamic cluster of computers.

### Service discovery

- avahi configured to advertise service `sciabc.service`
- zeroconf listener `zeroconf_listener.py` writes IP adddress to nodes.txt
- diagnostic tool: `zeroconf_find_services.py`

### Initialising Supercomputer

- Todo: automate installation of configuration and required packages
    - copy over `sciabc.service`
    - copy manager's ssh public key to authorized keys file
    - install MPI

### Supercomputer manager setup

- install on manager: `sudo apt-get install python3-mpi4py`
- mpirun -v --hostfile nodes.txt <cmd>

## Issues

- how to specify the ssh user of each node?
- create a new user, or ask administrator?

## Licence

All the software here is licenced under GPLv3.
