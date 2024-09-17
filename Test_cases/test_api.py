from Workflows.API_flows import APIFlows
from Workflows.API_graph import Graph
from Workflows.Email_flows import EmailFlows



class TestAPI:
    def test_01_create_graph_and_send_email_with_data(self):
        APIFlows.get_rate_float_from_USD(60)
        Graph.create_graph_from_Bitcoin_data()
        EmailFlows.Send_email_with_maximum_Bitcoin_price()




