from text_summerization_project_nlp.config.configuration import ConfigurationManager
from text_summerization_project_nlp.components.data_validation import DataValidation
from text_summerization_project_nlp.logging import logger


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()