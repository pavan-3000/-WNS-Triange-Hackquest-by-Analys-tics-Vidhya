
from src.cnn.logger import logging
from src.cnn.exception import CustomException
import sys


from src.cnn.entity.config_entity import DataIngestionConfig
from src.cnn.config.configuration import ConfigManger
from src.cnn.components.data_ingestion import DataIngestion



class DataIngestionPipeline:
    def __init__(self):
        pass
    
    
    
    def main(self):
        try:
            logging.info("initating stage 1")
            
            ing_config = ConfigManger()
            ing_config = ing_config.DataIngestionManager()
            data_ingestion = DataIngestion(config=ing_config)
            data_ingestion.download_zip()
            data_ingestion.exctract_zip()
            
            logging.info("stage 1 is completed sucessfully")
            
        
        except Exception as e:
            raise CustomException(e,sys)