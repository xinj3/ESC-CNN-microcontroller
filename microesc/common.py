
import os.path

import yaml

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def ensure_directories(*dirs):
    for dir in dirs:
        ensure_dir(dir)


def add_arguments(parser):
    a = parser.add_argument

    a('--datasets', dest='datasets_dir', default='./data/datasets',
        help='%(default)s')
    a('--features', dest='features_dir', default='./data/features',
        help='%(default)s')
    a('--models', dest='models_dir', default='./data/models',
        help='%(default)s')

    a('--settings', dest='settings_path', default='./experiments/ldcnn20k60.yaml',
        help='%(default)s')

def load_settings_path(path):
    with open(path, 'r') as config_file:
        settings = yaml.load(config_file.read())    
   
    return settings
