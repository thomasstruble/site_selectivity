# Multi-task model for prediction of C-H functionalization reactions
Original publication can be found [here](https://chemrxiv.org/articles/Multitask_Prediction_of_Site_Selectivity_in_Aromatic_C-H_Functionalization_Reactions/9735599)


## Webapp deployment
You can run predictions from a web GUI. To start it run:
`python web/run.py --host <IP of host> --port <port>`

## Command line deployment
Run a prediction and output to the terminal. In home folder run (predictions for toluene):
` python selectivity/site_selectivity.py --smiles Cc1ccccc1`

## Data processing pipeline
Unfortunately, the data used to train this model is not publicly available. However we are putting together a representative pipeline with USPTO open source data.