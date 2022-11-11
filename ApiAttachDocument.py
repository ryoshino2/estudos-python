
import requests


class ApiAttachDocument:

    def request_valid(self):
        url = 'https://localhost:7062/Rh/incluir-documento'
        file = 'teste-imagem.tif'
        return url, file

    def send_request(self, url, file):
        response = requests.request("POST", url, files={'arquivo': file}, verify=False)
        return response.status_code
