from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

class IndexView(TemplateView):
    template_name = 'index.html'

class DadosJSONView(BaseLineChartView):

    def get_labels(self):

        labels = [
            "janeiro",
            "fevereiro",
            "março",
            "abril",
            "maio",
            "junho",
            "julho",
            "agosto",
            "setembro",
            "outubro",
            "novembro",
            "dezembro",
        ]

        return labels
    
    def get_providers(self):

        datasets = [
            "Programação para leigos",
            "Algoritimo e logíca e programação",
            "Programação em C",
            "Programação em Java",
            "Programação em Python",
            "Banco de dados"
        ]
        return datasets

    def get_data(self):

        dados = []

        for l in range(6):
            for c in range(12):
                dado = [
                    randint(1, 200), #jan
                    randint(1, 200), #fev
                    randint(1, 200), #mar
                    randint(1, 200), #abr
                    randint(1, 200), #mai
                    randint(1, 200), #jun
                    randint(1, 200), #jul
                    randint(1, 200), #ago
                    randint(1, 200), #set
                    randint(1, 200), #out
                    randint(1, 200), #nov
                    randint(1, 200)  #dez 
                ]
            dados.append(dado)
        return dados
    