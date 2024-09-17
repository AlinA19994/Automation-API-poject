from Extensions.files_actions import FileActions
from Extensions.graph_actions import GraphActions
from Utilities.common_ops import get_data


class Graph:
    @staticmethod
    def create_graph_from_Bitcoin_data():
        data = FileActions.read_and_convert_JSON_file(get_data('data_file'))
        x = data['time']
        y = data['rate_float']
        GraphActions.create_graph_from_file(x, y, "Bitcoin Price Index(BPI)", "time", "rate")





