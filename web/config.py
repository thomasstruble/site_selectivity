"""
Sets the config parameters for the flask app object.
These are accessible in a dictionary, with each line defining a key.
"""

import os

DEFAULT_USER_ID = 1
ROOT_FOLDER = os.path.dirname(os.path.realpath(__file__))
DATA_FOLDER = os.path.join(ROOT_FOLDER, 'app/web_data')

