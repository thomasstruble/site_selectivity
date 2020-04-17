# Multi-task model for prediction of C-H functionalization reactions
Original publication can be found [here](https://pubs.rsc.org/en/content/articlelanding/2020/RE/D0RE00071J#!divAbstract)

This repository contains the trained model of the publication listed above. It also contains the code to make predictions or deploy a web-based GUI for making predictions.

## Setting up enviorment using docker
Build the docker container from site_selectivity directory:
`docker build -t sites .`

To run one prediction use replacing the smiles with your molecule:
`docker run -t sites bash -c "source activate sites && python selectivity/site_selectivity.py --smiles <smiles>"`

To run the web GUI there are two options:
* Using docker-compose where using localhost is hard coded
`docker-compose up -d` and to kill container `docker-compose down -v`

* Using docker run where you can specify the host and the port
`docker run -p <host port>:<port> -d sites bash -c "source activate sites && python web/run.py --host <host> --port <port>"`


## Setting up environment using conda
`conda create -n sites python=2.7 && conda activate sites`
OR
`conda create -n sites python=2.7 && source activate sites`

Then install dependencies
`conda install -n sites -c rdkit rdkit && conda install -n sites pip`
`pip install -r requirements.txt`

If installing requirements manually, be sure that the version of tensorflow is 1.14. Newer versions enable eager execution by default and the code will not run.

## Webapp deployment
You can run predictions from a web GUI. To start it run:
`python web/run.py --host <IP of host> --port <port>`

## Command line deployment
Run a prediction and output to the terminal. In home folder run (predictions here for toluene):
`python selectivity/site_selectivity.py --smiles Cc1ccccc1`

## Data processing pipeline
Unfortunately, the data used to train this model is not publicly available. However we are putting together a representative pipeline with USPTO open source data.