# Kubernetes-Project-Telaverge
```
                         +---------------------+
                         |   Client (Round-    |
                         | Robin Scheduler)    |
                         |  - Sends HTTP POST  |
                         |    Requests         |
                         +---------------------+
                                   |
                   +---------------|------------------+
                   |                                  |
       +-------------------+                +-------------------+
       | Server Pod 1      |                | Server Pod 2      |
       | (Round-Robin      |                | (Round-Robin      |
       | Worker Assignment)|                | Worker Assignment)|
       +-------------------+                +-------------------+
                   |                                  |
                   +---------------|------------------+
                                   |
                            +------------------+
                            | Kubernetes Service|
                            | - Load Balances  |
                            | - ClusterIP      |
                            +------------------+
                                   |
                           +------------------+
                           | Kubernetes       |
                           | Orchestration    |
                           +------------------+
                                   |
                   +---------------|------------------+
                   |                                  |
           +------------------+               +------------------+
           | Docker Container |               | Docker Container |
           | Server Instance  |               | Server Instance  |
           +------------------+               +------------------+
```
