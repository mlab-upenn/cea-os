# cea-os
Operating System for Controlled Environment Agriculture developed by researchers at the University of Pennsylvania's xLab group. This package is used to manage all sensors needed in an agriculture environment and streams data into an InfluxDB database. This data can be directly displayed onto a Grafana dashboard for viewing and analysis.\
Please reach out to Kevin Xu (xukev@seas.upenn.edu) or Nandan Tumu with questions about the repo.

# Physical Setup
This notion page contains all of the information regarding our physical device system: 
https://www.notion.so/Pennovation-Setup-Documentation-d710dfbb30794bef89b65308d11cdc5c

# Installation

1. Install Python3 (version >= 3.7)

2. Clone the cea-os repository
    ```sh
    git clone https://github.com/mlab-upenn/cea-os.git
    ```
    
# Usage

1. Navigate to cea-os folder

    ```sh
    cd cea-os
    ```
2. Spin up docker containers for cea-os, InfluxDB, and Grafana

    ```sh
    docker-compose up --build
    ```
    
3. Access to Grafana dashboard found at http://localhost:3000

