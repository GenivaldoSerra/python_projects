from sql_alchemy import data


class HotelModel(data.Model):  # type: ignore
    __tablename__ = 'hoteis'
    
    id = data.Column(data.String, primary_key=True)
    nome = data.Column(data.String(80))
    estrelas = data.Column(data.Float(precision=1))
    diaria = data.Column(data.Float(precision=2))
    cidade = data.Column(data.String(40))
    
    def __init__(self, id, nome, estrelas, diaria, cidade):
        self.id = id
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade
    
    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'estrelas': self.estrelas,
            'diaria': self.diaria,
            'cidade': self.cidade
        }
