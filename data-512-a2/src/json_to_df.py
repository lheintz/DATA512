import os
from pprint import pprint
import pandas as pandas
from json import load

class ModelScore:
    __slots__ = ("identifier", "prediction", "probabilities", "stub")
    # slots used to choose which values will be a part of the object 

    def __init__(
        self, identifier: int = None, prediction: str = None, probabilities: dict = None
    ):
        self.identifier = identifier
        self.prediction = prediction
        self.probabilities = probabilities
        self.stub = self.probabilities.get("Stub")

    # Method to print outputs nicely if desired for debugging
    def __repr__(self):
        string = "{"
        for index, key in enumerate(self.__slots__):
            string += "{"
            string += f"{key}: {str(getattr(self, key, None))}"
            if index < len(self.__slots__) - 1:
                string += "}, "
            else:
                string += "}"
        return string

class JSONParser:
    @staticmethod
    def parse(path_to_json_file):
        """ 
        The sub-function to turn the json file of the raw
        outputs from the ORES API call in to a dictionary. 
  
        Parameters: 
            path_to_json_file (string): The path to the raw json file returned from the API call
          
        Returns: 
            json_as_dictionary (dictionary): A python dictionary object of the original json
        """

        # Returns json as a dictionary

        with open(path_to_json_file) as json_file:
            json_as_dictionary = load(json_file)
        return json_as_dictionary

def json_path_to_dataframe(path_to_json_file):
    """ 
        The function to turn the json file of the raw
        outputs from the ORES API call in to a clean df
        in the format that we want. 
  
        Parameters: 
            path_to_json_file (string): The path to the raw json file returned from the API call
          
        Returns: 
            model_scores (dataframe): Returns the predicted scores from the model for each Revision Id queried
    """
    # Use json parser class to parse json in to a dictionary

    json_parser = JSONParser()
    json_as_dictionary = json_parser.parse(path_to_json_file)
    
    all_scores = json_as_dictionary.get("enwiki").get("scores")
    
    all_score_ids_mapped_to_info = {}
    for score in all_scores:
        all_score_ids_mapped_to_info[score] = (
            all_scores.get(score).get("wp10").get("score")
        )
    
    # Use model score class to choose values we want to add to a df

    model_scores = []
    for key, value in all_score_ids_mapped_to_info.items():
        model_scores.append([key, value.get("prediction")])
    
    return pandas.DataFrame(model_scores)

# Run json to df function and do some clean up 

path = os.path.join("data_raw", "ores-json-data-raw.json")
df = json_path_to_dataframe(path)
df = df.rename(columns={0: 'rev_id', 1: 'prediction'})
df.to_csv('data_clean/ores-data-clean.csv', index=False)