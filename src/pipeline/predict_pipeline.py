# web app to interact with the pkl files
# the data gn in the web app interacts with the model/pkl files and yields the prediction

import sys # for exeption handling
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

# maps the input data to the backend
class CustomData:
    def __init__(self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):

        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    # return all the inputs as a data frame
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)


class PredictPipeline:
    # empty constructor
    def __init__(self):
        pass

    # model prediction using pkl files
    def predict(self,features):
        try:
            model_path='artifacts\model.pkl'
            
            # preprocessor.pkl for handling categorical, feature scaling, preprocessing
            preprocessor_path='artifacts\preprocessor.pkl'
            
            # load_object from the utils.py to load the pkl file
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            
            data_scaled=preprocessor.transform(features)
            prediction=model.predict(data_scaled)
            
            return prediction
        
        except Exception as e:
            raise CustomException(e,sys)
