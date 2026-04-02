import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import yaml
from src.entity.config_entity import DataIngestionConfig
from src.components.data_ingestion import DataIngestion
#load file

with open("config/config.yaml") as f:
    config=yaml.safe_load(f)

#create config entity
ingestion_config=DataIngestionConfig(
    source=config["data_ingestion"]["source"],
    train_ratio=config["data_ingestion"]["train_ratio"],
    artifact_dir=config["data_ingestion"]["artifact_dir"]
)

#run ingeation

ingestion = DataIngestion(ingestion_config)
artifact = ingestion.initiate_data_ingestion()

print("Train path:", artifact.train_path)
print("Test path:", artifact.test_path)