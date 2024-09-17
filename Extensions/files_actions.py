import os
import json
import time
from datetime import datetime
from Utilities.common_ops import get_data


class FileActions:
    @staticmethod
    def create_folder(folder_name):
        parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        full_path = os.path.join(parent_dir, folder_name)
        if not os.path.exists(folder_name):
            os.makedirs(full_path)

    @staticmethod
    def create_file(file_name):
        if not os.path.exists(file_name):
            os.path.join(get_data('data_folder')+file_name)
        print(get_data('data_folder')+file_name)
        file = open(("../Data_files/"+file_name), "w")
        file.write(f'{{"rate_float": [], "time":[]}}')
        file.close()

    @staticmethod
    def read_and_convert_JSON_file(file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)  
                return data
        except FileNotFoundError:
            raise FileNotFoundError(f"File doesn't exist in {file_path}")




    @staticmethod
    def update_json_file(file_path, new_value, key):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file) 
        except FileNotFoundError:
            raise FileNotFoundError(f"File doesn't exist in {file_path}")

        if key in data:
            data_list = data[key]
            data_list.append(new_value)
        else:
            raise FileNotFoundError(f"'{key}' key not found in the JSON.")

        if "time" in data:
            current_time = datetime.now().strftime("%H:%M")
            hours, minutes = map(int,current_time.split(':'))
            decimal_format_time = hours + round((minutes / 60), 2)
            time_list = data['time']
            time_list.append(decimal_format_time)

        with open(file_path, 'w') as file:
            json.dump(data, file)
