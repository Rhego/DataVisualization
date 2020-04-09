import requests
import datetime

from plotly.graph_objs import Bar
from plotly import offline
#Hacer la llamada al API y almacenar la respuesta

url = 'https://pomber.github.io/covid19/timeseries.json'
r = requests.get(url)
print(r.status_code)

response_dic = r.json()
#print(response_dic[0])
#print(len(response_dic.keys()))
#Procesando Resultados
country_dic, deaths_dic = [], []
for country in (response_dic.keys()):
    #print(country)
    country_dic.append(country)
    deaths_dic.append(response_dic[country][-1]['deaths'])
    

data = [{
    'type': 'bar',
    'x': country_dic,
    'y': deaths_dic,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width':  1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Cantidad de Muertes por Pais',
    'xaxis': {
        'title': 'Paises',
        'titlefont': {'size': 10},
        'tickfont': {'size': 10}
    },
    'yaxis': {
        'title': 'Muertes',
        'titlefont': {'size': 10},
        'tickfont': {'size': 10}
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='covid.html')