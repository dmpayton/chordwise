import os

# Directories
APP_DIR = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2])
ASSETS_DIR = os.path.join(APP_DIR, 'assets')
KV_DIR = os.path.join(APP_DIR, 'kv')
