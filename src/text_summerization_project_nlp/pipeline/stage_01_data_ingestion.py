from text_summerization_project_nlp.config.configuration import ConfigurationManager
from text_summerization_project_nlp.components.data_ingestion import DataIngestionManager
from text_summerization_project_nlp.logging import logger


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestionManager(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()