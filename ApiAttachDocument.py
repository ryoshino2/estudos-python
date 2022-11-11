
import requests


class ApiAttachDocument:

    def request_valid(self):
        url = 'https://localhost:7062/Rh/incluir-documento'
        file = 'teste-imagem.tif'
        return url, file

    def request_invalid(self):
        url = 'http://localhost:7062/Rh/incluir-documento'
        return url

    def send_request(self, url, file):
        response = requests.request("POST", url, files={'arquivo': file}, verify=False)
        return response.status_code

    def send_request_invalid(self, url):
        response = requests.request("POST", url, files=None, verify=False)
        return response.status_code
