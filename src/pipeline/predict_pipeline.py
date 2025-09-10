import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import os


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")

            features = features.fillna("Unknown")
            print("Features after fillna:\n", features)

            data_scaled=preprocessor.transform(features)    
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
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

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender if self.gender is not None else "Unknown"],
                "race_ethnicity": [self.race_ethnicity if self.race_ethnicity is not None else "Unknown"],
                "parental_level_of_education": [self.parental_level_of_education if self.parental_level_of_education is not None else "Unknown"],
                "lunch": [self.lunch if self.lunch is not None else "Unknown"],
                "test_preparation_course": [self.test_preparation_course if self.test_preparation_course is not None else "Unknown"],
                "reading_score": [self.reading_score if self.reading_score is not None else 0],
                "writing_score": [self.writing_score if self.writing_score is not None else 0   ],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)