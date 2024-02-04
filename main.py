
from src.cnn.logger import logging
from src.cnn.exception import CustomException
import sys

from src.cnn.pipeline.data_ingestion_pipeline import DataIngestionPipeline


try:
    
    logging.info("data ingestion as started")
    
    ingestion_obj = DataIngestionPipeline()
    ingestion_obj.main()
    
    logging.info("data ingestion  has completed")
    
except Exception as e:
    raise CustomException(e,sys)