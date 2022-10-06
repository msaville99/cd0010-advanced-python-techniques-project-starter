"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
from csv import DictReader
import json

from models import NearEarthObject, CloseApproach

def load_neos(neo_csv_path="data/neos.csv"):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # TODO: Load NEO data from the given CSV file.
    with open(neo_csv_path, 'r') as file:
        return [NearEarthObject(designation=row['pdes'], name=row['name'], 
            diameter=row['diameter'], hazardous=row['pha']) for row in DictReader(file)]

def load_approaches(cad_json_path="data/cad.json"):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.
    with open(cad_json_path, 'r') as file:
        contents = json.load(file)
    file.close()
    return [CloseApproach(_designation=ca[0], time=ca[3], distance=ca[4], velocity=ca[7]) 
        for ca in [value for value in contents.values()][1]]
