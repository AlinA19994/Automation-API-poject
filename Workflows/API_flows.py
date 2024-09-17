import time
from Extensions.api_actions import APIActions
from Extensions.files_actions import FileActions
from Utilities.common_ops import get_data


url = get_data('url')


class APIFlows:
    @staticmethod
    def get_rate_float_from_USD(sec, duration=3600):
        FileActions.create_folder(get_data('folder_name'))
        FileActions.create_file(get_data('data_file'))
        start_time = time.time()
        while time.time() - start_time < duration:
            response = APIActions.get(url)
            nodes = ["bpi", "USD", "rate_float"]
            value = APIActions.extract_value_from_response(response, nodes)
            FileActions.update_json_file(get_data('data_file'), value, 'rate_float')
            time.sleep(sec)













