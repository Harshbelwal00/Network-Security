from network_security.entity.artifact_entity import DataIngestionArtifact , DataValidationArtifact
from network_security.entity.config_entity import DataValidationConfig
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging
from network_security.constant.training_pipeline import SCHEMA_FILE_PATH
from scipy.stats import ks_2samp
from network_security.utils.main_utils.utilis import read_yaml_file
import pandas as pd
import os
import sys

class DataValidation:
    def __init__(self,data_ingestion_artifact:DataValidationArtifact,data_validation_config:DataValidationConfig):
        try:
            self.data_ingestion_artifact=data_ingestion_artifact
            self.data_ingestion_config=data_validation_config
            self._schema_config=read_yaml_file(SCHEMA_FILE_PATH)

        except Exception as e:
            raise NetworkSecurityException(e,sys)