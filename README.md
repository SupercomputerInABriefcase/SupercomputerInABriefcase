# Supercomputer in a Briefcase

## Introduction

Clearly it is impossible to fit a supercomputer in a briefcase. But it is a great label for the idea of
being able to construct ad hoc dynamic clusters of computers with a view to using them to play with
parallelism.

[Russel Winder](https://www.russel.org.uk/) gave a presentation at [PyCon UK 2016](http://2016.pyconuk.org/)
introducing the idea of the "Supercomputer in a Briefcase". The video of the presentation is on
YouTube [here](https://www.youtube.com/watch?v=EUA4GIiYg5w)

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

Some of the bits of code we have imported here from elsewhere have MIT or LGPL licences on the originals or
they are in the public domain. In the rush at the sprint at PyCon UK 2016, we were not quite as vigilant
about licences as perhaps we should have been. We will properly retrofit the correct licence statements to
the imported code as needed corrections are found. If you spot an infelicity of ours that needs correction,
please let us know via the issues and the corrections will be made.
