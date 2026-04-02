import pandas as pd
from sklearn.model_selection import train_test_split
import os
from src.config.configuration import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact
os.makedirs("artifacts/data_ingestion", exist_ok=True)

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
        
    def initiate_data_ingestion(self):
        df=pd.read_csv(self.config.source)
        train_df,test_df=train_test_split(
            df,
            test_size=1-self.config.train_ratio,
            random_state=42
        )
        os.makedirs(self.config.artifact_dir, exist_ok=True)

        train_path=os.path.join(self.config.artifact_dir,"train.csv")
        test_path=os.path.join(self.config.artifact_dir,"test.csv")

        train_df.to_csv(train_path,index=False)
        test_df.to_csv(test_path,index=False)

        return DataIngestionArtifact(train_path=train_path,test_path=test_path) 


