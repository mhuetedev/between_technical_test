import logging
from sys import stderr
import requests

logger = logging.getLogger(__name__)


class ApiService:
    def __init__(self, api_url):
        self.api_url = api_url

    def get_todos(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()

            todos = response.json()
            return todos
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving TODOs: {e}", file=stderr)
            logger.info(f"Error retrieving TODOs: {e}", file=stderr)
            return None
        
    def run(self):
        print('Running ApiService', file=stderr)

        todos = self.get_todos()
    
