from Extensions.email_actions import EmailActions
from Extensions.files_actions import FileActions
from Utilities.common_ops import get_data
import logging


class EmailFlows:
    @staticmethod
    def Send_email_with_maximum_Bitcoin_price():
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        data = FileActions.read_and_convert_JSON_file(get_data('data_file'))
        rate = data['rate_float']
        max_rate = max(rate)
        message = f"Subject: maximum Bitcoin price for the last hour \n\n{max_rate}"
        logging.info("sending an email")
        EmailActions.send_new_email("alina@test.com",message)

