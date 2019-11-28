import requests
import json
from datetime import date

dias_semana = ['Domingo', 'Segunda-Feira', 'Terça-Feira', 'Quarta-Feira','Quinta-Feira', 'Sexta-Feira', 'Sábado']

accuweatherAPIKey = "nTH7fJFVxdSwAa1NAXxR6XAFTJ92oU7R"

def pegarCoordenadas():

        r = requests.get('http://www.geoplugin.net/json.gp')
        if (r.status_code != 200):
            print("Não foi possivel obter localização!")
            return None
        else:
            try:
                localizacao = json.loads(r.text)
                coordenadas = {}
                coordenadas['lat'] = localizacao['geoplugin_latitude']
                coordenadas['long'] = localizacao['geoplugin_longitude']
                return coordenadas
            except:
                return None

def pegarCodigoLocal(lat,long):

    LocationAPIUrl = "http://dataservice.accuweather.com/locations/v1/" \
    + "cities/geoposition/search?apikey=" + accuweatherAPIKey \
    + "&q=" + lat + "%2C" + long +"&language=pt-br"

    r = requests.get(LocationAPIUrl)
    if (r.status_code != 200):
        print("Não foi possivel obter Código do local !")
        return None
    else:
        try:
            locationResponse = json.loads(r.text)
            infoLocal = {}
            infoLocal['nomeLocal'] = locationResponse['LocalizedName'] + ", " \
            + locationResponse['AdministrativeArea']['LocalizedName'] + ". " \
            + locationResponse['Country']['LocalizedName'] + "."
            infoLocal['codigoLocal'] = locationResponse['Key']
            return infoLocal
        except:
            return None

def pegarTempoAgora(codigoLocal, nomeLocal):

    CurrentConditionsAPIUrl = "http://dataservice.accuweather.com/" \
    + "currentconditions/v1/" + codigoLocal + "?apikey=" + accuweatherAPIKey \
    + "&language=pt-br"

    r = requests.get(CurrentConditionsAPIUrl)
    if (r.status_code != 200):
        print("Não foi possivel obter Clima Atual !")
        return None
    else:
        try:
            CurrentConditionsResponse = json.loads(r.text)
            infoClima = {}
            infoClima['textoClima'] = CurrentConditionsResponse[0]['WeatherText']
            infoClima['temperatura'] = CurrentConditionsResponse[0]['Temperature']['Metric']['Value']
            infoClima['nomeLocal'] = nomeLocal
            return infoClima
        except:
            return None

def pegarPrevisao5Dias(codigoLocal):

    DailyAPIUrl = "http://dataservice.accuweather.com/" \
    + "forecasts/v1/daily/5day/" + codigoLocal + "?apikey=" + accuweatherAPIKey \
    + "&language=pt-br&metric=true"

    r = requests.get(DailyAPIUrl)
    if (r.status_code != 200):
        print("Não foi possivel obter previsão para 5 dias !")
        return None
    else:
        try:
            DailyResponse = json.loads(r.text)
            infoClima5Dias = []
            for dia in DailyResponse['DailyForecasts']:
                climaDia = {}
                climaDia['max'] = dia['Temperature']['Maximum']['Value']
                climaDia['min'] = dia['Temperature']['Minimum']['Value']
                climaDia['clima'] = dia['Day']['IconPhrase']
                diaSemana = int(date.fromtimestamp(dia['EpochDate']).strftime("%w"))
                climaDia['dia'] = dias_semana[diaSemana]
                infoClima5Dias.append(climaDia)
            return infoClima5Dias

        except:
            return None



try:
    coordenadas = pegarCoordenadas()
    local = pegarCodigoLocal(coordenadas['lat'], coordenadas['long'])
    climaAtual = pegarTempoAgora(local['codigoLocal'],local['nomeLocal'])
    print('Clima atual em: ' + climaAtual['nomeLocal'])
    print(climaAtual['textoClima'])
    print('temperatura: ' + str(climaAtual['temperatura']) + "\xb0" + "C")
    print('\nClima para hoje e para os próximos dias:\n')

    previsao5dias = pegarPrevisao5Dias(local['codigoLocal'])
    for dia in previsao5dias:
        print(dia['dia'])
        print('Mínima: ' + str(dia['min']) + "\xb0" + "C")
        print('Máxima: ' + str(dia['max']) + "\xb0" + "C")
        print('Clima: ' + dia['clima'])
        print('-'*20)


except:
    print("Erro ao processar a solicitação entre em contato com o Suporte!")

