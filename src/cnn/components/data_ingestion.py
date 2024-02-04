
from src.cnn.logger import logging
from src.cnn.exception import CustomException
import sys


from src.cnn.entity.config_entity import DataIngestionConfig
from src.cnn.config.configuration import ConfigManger
import pandas as pd
import os
import zipfile
import gdown

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config
        
        
    def download_zip(self):
        try:
            data = self.config.source_URL
            download_path = self.config.local_data_file
            
            os.makedirs("artifacts/data_ingestion",exist_ok=True)
            
            file_id = data.split('/')[-2]
            prefix = 'https://drive.google.com/uc?export=download&id='
            
            gdown.download(prefix+file_id,download_path)
            
            logging.info("zip file is successfully downloaded from drive")
            
        except Exception as e:
            raise CustomException(e,sys)
        
        
    def exctract_zip(self):
        try:
            data_path = self.config.unzip_path
            
            os.makedirs(data_path,exist_ok=True)
            
            with zipfile.ZipFile(self.config.local_data_file,'w') as f:
                f.extractall(data_path)
                
            logging.info('data is exctracted from the zip file')
            
        except Exception as e:
            raise CustomException(e,sys)