import os

# Project Information
APP_NAME = "CyberShield AI"
APP_VERSION = "1.0.0"

# Project Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATASET_DIR = os.path.join(BASE_DIR, "datasets")

MODEL_DIR = os.path.join(BASE_DIR, "models")

ASSET_DIR = os.path.join(BASE_DIR, "assets")

LOGO_PATH = os.path.join(ASSET_DIR, "logo.png")
