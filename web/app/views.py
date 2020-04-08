"""Defines a number of routes/views for the flask app."""
import os
import sys
from flask import render_template, request
from rdkit import Chem
import rdkit.Chem.Draw as Draw
from rdkit.Chem import rdDepictor
from rdkit.Chem.Draw import rdMolDraw2D
from rdkit import Geometry

from app import app


from selectivity.site_selectivity import Site_Predictor

pred = Site_Predictor()

@app.route('/')
def home():
    """Renders the home page."""
    return render_template('home.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """Renders the predict page and makes predictions if the method is POST."""
    if request.method == 'GET':
        return render_template('predict.html')

    if request.form['textSmiles'] != '':
        smiles = request.form['textSmiles']
    elif request.form['drawSmiles'] != '':
        smiles = request.form['drawSmiles']
   
    if Chem.MolFromSmiles(smiles) == None:
        return render_template('predict.html',
                                errors=['SMILES is invalid'])

    # Run predictions
    preds = pred.predict(smiles)
    print(preds)
    
    return render_template('predict.html',
                         predicted=True,
                          smiles=smiles,
                          preds=preds,
                          warnings=["List contains invalid SMILES strings"] if None in preds else None,
                          errors=["No SMILES strings given"] if len(preds) == 0 else None)


def get_scaled_drawer(mol):
    '''This function takes a rdkit mol object and scales the drawing so that 
    all of the drawings come out with the same proportions'''
    dpa = 24
    rdDepictor.Compute2DCoords(mol)
    conf = mol.GetConformer()
    xs = [conf.GetAtomPosition(i).x for i in range(mol.GetNumAtoms())]
    ys = [conf.GetAtomPosition(i).y for i in range(mol.GetNumAtoms())]
    point_min = Geometry.rdGeometry.Point2D()
    point_max = Geometry.rdGeometry.Point2D()
    point_min.x = min(xs) - 1
    point_min.y = min(ys) - 1
    point_max.x = max(xs) + 1
    point_max.y = max(ys) + 1
    w = int(dpa * (point_max.x - point_min.x))
    h = int(dpa * (point_max.y - point_min.y))
    drawer = rdMolDraw2D.MolDraw2DSVG(w, h)
    drawer.SetScale(w, h, point_min, point_max)
    return drawer


@app.route('/draw', methods=['GET'])
def draw():
    '''This function takes a request and generates the image and highlights the images
    with the atom scores'''
    mol = Chem.MolFromSmiles(str(request.args.get('smiles')))
    d2 = get_scaled_drawer(mol)
    dopts = d2.drawOptions()
    atom_scores = [float(x) for x in request.args.getlist('atom_scores')]
    print(atom_scores)
    
    highlightAtoms = list(range(mol.GetNumAtoms()))
    highlightAtomColors = {x: (1, 1, 1) for x in highlightAtoms}

    if len(atom_scores) != 0:
        for i, j in enumerate(mol.GetAtoms()):
            # cutoff to make the images better
            if round(atom_scores[i] * 100) > 5 and j.GetIsAromatic():
                highlightAtomColors[i] = ((1 - atom_scores[i], 1, 1 - atom_scores[i]))
                dopts.atomLabels[i] = '{}%'.format(int(round(atom_scores[i] * 100)))

    #Clear atom mapping
    [a.SetAtomMapNum(0) for a in mol.GetAtoms()]
    m2=Draw.PrepareMolForDrawing(mol)
    d2.DrawMolecule(m2,highlightAtoms=highlightAtoms, \
        highlightBonds=[], highlightAtomColors=highlightAtomColors)
    d2.FinishDrawing()
    txt = d2.GetDrawingText()

    return txt
