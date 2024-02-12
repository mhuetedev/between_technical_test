from src.Services.ApiService import ApiService

API_URL = 'https://jsonplaceholder.typicode.com/todos/'
class App:
    def __init__(self):
        self._api_service = ApiService(API_URL)

    def api_service(self) -> ApiService:
        return self._api_service
