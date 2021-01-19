import logging
import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    municipalities = req.params.get('municipalities')
    energy = req.params.get('energy')
    household = req.params.get('household')

household_input = str(input("Your Household Size: "))
household_size = {1: 1500, 2: 2500, 3: 3500, 4: 4250, 5: 5400} 
print(household_size[household_input])

sunshine_input = str(input("In which municipality do you live in? "))
sunshine_hours = [{'kommune': 'Aabenraa', 'total': 1590}, {'kommune': 'Aalborg', 'total': 1782}, {'kommune': 'Aarhus', 'total': 1699}, {'kommune': 'Æro', 'total': 1786}, {'kommune': 'Albertslund', 'total': 1747}, {'kommune': 'Allerød', 'total': 1743}, {'kommune': 'Assens', 'total': 1753}, {'kommune': 'Ballerup', 'total': 1747}, {'kommune': 'Billund', 'total': 1615}, {'kommune': 'Bornholm', 'total': 1909}, {'kommune': 'Brøndby', 'total': 1744}, {'kommune': 'Brønderslev', 'total': 1787}, {'kommune': 'Dragør', 'total': 1739}, {'kommune': 'Egedal', 'total': 1748}, {'kommune': 'Esbjerg', 'total': 1679}, {'kommune': 'Faaborg-Midtfyn', 'total': 1757}, {'kommune': 'Fanø', 'total': 1748}, {'kommune': 'Favrskov', 'total': 1658}, {'kommune': 'Faxe', 'total': 1750}, {'kommune': 'Fredensborg', 'total': 1747}, {'kommune': 'Fredericia', 'total': 1713}, {'kommune': 'Frederiksberg', 'total': 1739}, {'kommune': 'Frederikshavn', 'total': 1885}, {'kommune': 'Frederikssund', 'total': 1769}, {'kommune': 'Furesø', 'total': 1744}, {'kommune': 'Gentofte', 'total': 1741}, {'kommune': 'Gladsaxe', 'total': 1742}, {'kommune': 'Glostrup', 'total': 1745}, {'kommune': 'Greve', 'total': 1748}, {'kommune': 'Gribskov', 'total': 1767}, {'kommune': 'Guldborgsund', 'total': 1838}, {'kommune': 'Haderslev', 'total': 1658}, {'kommune': 'Halsnæs', 'total': 1791}, {'kommune': 'Hedensted', 'total': 1649}, {'kommune': 'Helsingør', 'total': 1754}, {'kommune': 'Herlev', 'total': 1745}, {'kommune': 'Herning', 'total': 1610}, {'kommune': 'Hillerød', 'total': 1745}, {'kommune': 'Hjørring', 'total': 1834}, {'kommune': 'Høje-Taastrup', 'total': 1747}, {'kommune': 'Holbæk', 'total': 1783}, {'kommune': 'Holstebro', 'total': 1666}, {'kommune': 'Horsens', 'total': 1627}, {'kommune': 'Hørsholm', 'total': 1744}, {'kommune': 'Hvidovre', 'total': 1740}, {'kommune': 'Ikast-Brande', 'total': 1579}, {'kommune': 'Ishøj', 'total': 1746}, {'kommune': 'Jammerbugt', 'total': 1798}, {'kommune': 'Kalundborg', 'total': 1809}, {'kommune': 'Kerteminde', 'total': 1799}, {'kommune': 'Københavns', 'total': 1739}, {'kommune': 'Køge', 'total': 1743}, {'kommune': 'Kolding', 'total': 1660}, {'kommune': 'Læso', 'total': 1952}, {'kommune': 'Langeland', 'total': 1801}, {'kommune': 'Lejre', 'total': 1766}, {'kommune': 'Lemvig', 'total': 1722}, {'kommune': 'Lolland', 'total': 1796}, {'kommune': 'Lyngby-Taarbæk', 'total': 1743}, {'kommune': 'Mariagerfjord', 'total': 1723}, {'kommune': 'Middelfart', 'total': 1757}, {'kommune': 'Morsø', 'total': 1803}, {'kommune': 'Næstved', 'total': 1773}, {'kommune': 'Norddjurs', 'total': 1771}, {'kommune': 'Nordfyn', 'total': 1774}, {'kommune': 'Nyborg', 'total': 1785}, {'kommune': 'Odder', 'total': 1755}, {'kommune': 'Odense', 'total': 1751}, {'kommune': 'Odsherred', 'total': 1805}, {'kommune': 'Randers', 'total': 1687}, {'kommune': 'Rebild', 'total': 1752}, {'kommune': 'Ringkøbing-Skjern', 'total': 1651}, {'kommune': 'Ringsted', 'total': 1760}, {'kommune': 'Rødovre', 'total': 1742}, {'kommune': 'Roskilde', 'total': 1752}, {'kommune': 'Rudersdal', 'total': 1744}, {'kommune': 'Samsø', 'total': 1919}, {'kommune': 'Silkeborg', 'total': 1612}, {'kommune': 'Skanderborg', 'total': 1635}, {'kommune': 'Skive', 'total': 1720}, {'kommune': 'Slagelse', 'total': 1788}, {'kommune': 'Solrød', 'total': 1746}, {'kommune': 'Sønderborg', 'total': 1730}, {'kommune': 'Sorø', 'total': 1771}, {'kommune': 'Stevns', 'total': 1747}, {'kommune': 'Struer', 'total': 1700}, {'kommune': 'Svendborg', 'total': 1779}, {'kommune': 'Syddjurs', 'total': 1745}, {'kommune': 'Tårnby', 'total': 1739}, {'kommune': 'Thisted', 'total': 1814}, {'kommune': 'Tønder', 'total': 1641}, {'kommune': 'Vallensbæk', 'total': 1745}, {'kommune': 'Varde', 'total': 1656}, {'kommune': 'Vejen', 'total': 1636}, {'kommune': 'Vejle', 'total': 1623}, {'kommune': 'Vesthimmerland', 'total': 1766}, {'kommune': 'Viborg', 'total': 1639}, {'kommune': 'Vordingborg', 'total': 1814}]
print(sunshine_hours[sunshine_input])

NoOfPanels = round(EnergyConsumption / (SunlightHours*0.3))
SystemSize = round((NoOfPanels * 0.3))
Message1 = 'Oh, your energy consumption is quite high - please contact us directly for an accurate offer.'
Message2 = 'Have you entered your household size (1-5)?'

if household_input = 1:
        NoOfPanels = round(1500 / (SunlightHours*0.3))
        SystemSize = round((NoOfPanels * 0.3))
elif household_input = 2:
        NoOfPanels = round(2500 / (SunlightHours*0.3))
        SystemSize = round((NoOfPanels * 0.3))
elif household_input = 3:
        NoOfPanels = round(3500 / (SunlightHours*0.3))
        SystemSize = round((NoOfPanels * 0.3))
elif household_input = 4:
        NoOfPanels = round(4250 / (SunlightHours*0.3))
        SystemSize = round((NoOfPanels * 0.3))
elif household_input = 5:
        NoOfPanels = round(5400 / (SunlightHours*0.3))
        SystemSize = round((NoOfPanels * 0.3))
else:
    Message2

if SystemSize <= 1.5:
    PriceOfPanel = 28500
    RoofSpace = 8.2
elif SystemSize <= 2.5:
    PriceOfPanel = 37600
    RoofSpace = 13
elif SystemSize <= 3.5:
    PriceOfPanel = 51100
    RoofSpace = 19.8
elif SystemSize <= 4.25:
    PriceOfPanel = 56500
    RoofSpace = 23.1
else:
    Message1

BreakEvenYear = (PriceOfPanel / (SunlightHours * SystemSize * 2.23))*2

    resp = {"panelprice": PriceOfPanel,
            "roofspace": RoofSpace
            "breakeven": BreakEvenYear
            "message1": Message1
            "message2": Message2
            }
            
    return func.HttpResponse(json.dumps(resp), status_code=200)

