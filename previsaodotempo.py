import requests
import json
import pprint

accuweatherAPIKey = "nTH7fJFVxdSwAa1NAXxR6XAFTJ92oU7R"

r = requests.get('http://www.geoplugin.net/json.gp')
if (r.status_code != 200):
    print("Não foi possivel obter localização!")
else:
    localizacao = json.loads(r.text)
    lat = localizacao['geoplugin_latitude']
    long = localizacao['geoplugin_longitude']
    print(pprint.pprint(localizacao))
    LocationAPIUrl = "http://dataservice.accuweather.com/locations/v1/" \
    + "cities/geoposition/search?apikey=" + accuweatherAPIKey \
    + "&q=" + lat + "%2C" + long +"&language=pt-br"

    r2 = requests.get(LocationAPIUrl)
    if (r2.status_code != 200):
        print("Não foi possivel obter Código do local !")
    else:
        locationResponse = json.loads(r2.text)
        nomeLocal = locationResponse['LocalizedName'] + ", " \
            + locationResponse['AdministrativeArea']['LocalizedName'] + ". " \
            + locationResponse['Country']['LocalizedName'] + "."
        codigoLocal = locationResponse['Key']
        print("Obtendo clima do local ", nomeLocal)

    CurrentConditionsAPIUrl = "http://dataservice.accuweather.com/" \
    + "currentconditions/v1/" + codigoLocal + "?apikey=" + accuweatherAPIKey \
    + "&language=pt-br"
    r3 = requests.get(CurrentConditionsAPIUrl)
    if (r3.status_code != 200):
        print("Não foi possivel obter Código do local !")
    else:
        CurrentConditionsResponse = json.loads(r3.text)
        textoClima = CurrentConditionsResponse[0]['WeatherText']
        temperatura = CurrentConditionsResponse[0]['Temperature']['Metric']['Value']
        print('Clima no momento: ', textoClima)
        print('Temperatura: ' + str(temperatura) + " graus Celcius")
