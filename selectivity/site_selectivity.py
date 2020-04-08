import argparse
from selectivity.multitask_model import tf_predictor
import rdkit.Chem as Chem 
import sys
import os 

def parse_args():
    """
    Argument parser so this can be run from the command line
    """
    parser = argparse.ArgumentParser(description='Run site selectivity predictions from the command line')
    parser.add_argument('-s', '--smiles', help='SMILES input for site selectivity')
    return parser.parse_args()


class Site_Predictor():
	def __init__(self):
		self.site_predictor = tf_predictor()
		self.site_predictor.build()
		print('Loaded recommendation model')
		print('### RECOMMENDER STARTED UP ###')

	def predict(self, smi):
		res = self.site_predictor.web_predictor([smi]) #has to be a list
		return res


#for command line use
if __name__ == "__main__":
	args = parse_args()
	predictor = Site_Predictor()
	res = predictor.predict(args.smiles)
	for i in res:
		print('Task {}'.format(i['task']))
		print('Atom scores {}\n'.format(i['atom_scores']))


