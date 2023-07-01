import requests
headers = {'user-agent': 'MyStudyApp'}

class FipeIterator:
    def __init__(self, id_montadora: str):
        url = 'https://parallelum.com.br/fipe/api/v1/carros/marcas/{}/modelos'
        url = url.format(id_montadora)
        requisicao = requests.get(url, headers=headers)
        carros = requisicao.json()

        self.modelos = carros['modelos']
        self.current = 0
        self.end = len(self.modelos)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        lista_carros = self.modelos[self.current]
        self.current += 1
        return lista_carros
    
iterator = FipeIterator('48') 

for veiculo in iterator:
    print('MODELO:', veiculo['nome'], 'CÓDIGO:', veiculo['codigo'])