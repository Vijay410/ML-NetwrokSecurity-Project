import pandas as pd
import json
import os
class NetworkDataExtract():
    """
    This class is responsible for extracting network data from a CSV file
    """
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(str(e))

    def csv_to_json_converter(
        self, 
        file_path
        ):
        """
        Converts a CSV file to a JSON format.
        Args:
            file_path (str): The path to the CSV file.
        Returns:
            list: A list of dictionaries representing the JSON data.
        Raises:
            NetworkSecurityException: If an error occurs during the conversion process.
        """
        try:
            # read the csv file
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            final_data = list(json.loads(data.T.to_json()).values())
            return final_data
            # convert the dataframe to a dictionary
        except exception as e:
            raise NetworkSecurityException(str(e))


