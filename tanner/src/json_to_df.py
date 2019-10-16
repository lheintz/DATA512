import os
from pprint import pprint
import pandas as pandas
from json import load

class ModelScore:
    __slots__ = ("identifier", "prediction", "probabilities", "stub")
    # slots are a way to tell python what values you'll allow as part of the object
    # this allows me to do what you see below with __repr__, which is just
    # me over-riding how the object will print out for the sake of explanation

    def __init__(
        self, identifier: int = None, prediction: str = None, probabilities: dict = None
    ):
        # I made these names up, guessing what these mean
        # Something else could make more sense
        # You could also break the probabilities out more, I've shown one example
        self.identifier = identifier
        self.prediction = prediction
        self.probabilities = probabilities
        self.stub = self.probabilities.get("Stub")

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
        with open(path_to_json_file) as json_file:
            json_as_dictionary = load(json_file)
            # returns a dictionary, included in the standard python library
            # https://docs.python.org/3/library/json.html#json.load
        return json_as_dictionary

def json_path_to_dataframe(path_to_json_file):
    json_parser = JSONParser()
    json_as_dictionary = json_parser.parse(path_to_json_file)
    
    all_scores = json_as_dictionary.get("enwiki").get("scores")
    
    all_score_ids_mapped_to_info = {}
    for score in all_scores:
        all_score_ids_mapped_to_info[score] = (
            all_scores.get(score).get("wp10").get("score")
        )
    
    model_scores = []
    for key, value in all_score_ids_mapped_to_info.items():
        model_scores.append([key, value.get("prediction")])
    
    return pandas.DataFrame(model_scores)


path = os.path.join("data_raw", "ores-json-data-raw.json")
df = json_path_to_dataframe(path)
df = df.rename(columns={0: 'rev_id', 1: 'prediction'})
df.to_csv('data_clean/ores-data-clean.csv', index=False)