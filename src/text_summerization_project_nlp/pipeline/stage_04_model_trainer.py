from text_summerization_project_nlp.config.configuration import ConfigurationManager
from text_summerization_project_nlp.components.model_trainer import ModelTrainer
from text_summerization_project_nlp.logging import logger


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()