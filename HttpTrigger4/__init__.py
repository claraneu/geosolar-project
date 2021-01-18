import logging
import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    municipalities = req.params.get('municipalities')
    energy = req.params.get('energy')
    household = req.params.get('household')
    householdDatabase = {1: 1500, 2: 2500, 3: 3500, 4: 4250}

    sunshineHoursDatabase= {
    "Aabenraa" : 1590, "Aalborg": 1782, "Aarhus" : 1699, "Æro" : 1786, 
    "Albertslund":  1747, "Allerød" :1743,"Assens": 1753,"Ballerup": 1747,
    "Billund" : 1615,"Bornholm":  1909,"Brøndby": 1744, "Brønderslev": 1787,
    "Dragør": 1739,"Egedal": 1748, "Esbjerg": 1679,  "Faaborg-Midtfyn": 1757,
    "Fanø": 1748,"Favrskov": 1658,"Faxe": 1750,"Fredensborg": 1747,
    "Fredericia": 1713,
    "Frederiksberg": 1739,
    "Frederikshavn": 1885,
    "Frederikssund": 1769,
    "Furesø": 1744,
    "Gentofte": 1741,
    "Gladsaxe": 1742,
    "Glostrup": 1745,
    "Greve": 1748,
    "Gribskov": 1767,
    "Guldborgsund": 1838,
    "Haderslev": 1658,
    "Halsnæs": 1791,
    "Hedensted": 1649,
    "Helsingør": 1754,
    "Herlev": 1745,
    "Herning": 1610,
    "Hillerød": 1745,
    "Hjørring": 1834,
    "Høje-Taastrup": 1747,
    "Holbæk": 1783,
    "Holstebro": 1666,
    "Horsens": 1627,
    "Hørsholm": 1744,
    "Hvidovre": 1740,
    "Ikast-Brande": 1579,
    "Ishøj": 1746,
    "Jammerbugt": 1798,
    "Kalundborg": 1809,
    "Kerteminde": 1799,
    "Københavns": 1739,
    "Køge": 1743,
    "Kolding": 1660,
    "Læso": 1952,
    "Langeland": 1801,
    "Lejre": 1766,
    "Lemvig": 1722,
    "Lolland": 1796,
    "Lyngby-Taarbæk": 1743,
    "Mariagerfjord": 1723,
    "Middelfart": 1757,
    "Morsø": 1803,
    "Næstved": 1773,
    "Norddjurs": 1771,
    "Nordfyn": 1774,
    "Nyborg": 1785,
    "Odder": 1755,
    "Odense": 1751,
    "Odsherred": 1805,
    "Randers": 1687,
    "Rebild": 1752,
    "Ringkøbing-Skjern": 1651,
    "Ringsted": 1760,
    "Rødovre": 1742,
    "Roskilde": 1752,
    "Rudersdal": 1744,
    "Samsø": 1919,
    "Silkeborg": 1612,
    "Skanderborg": 1635,
    "Skive": 1720,
    "Slagelse": 1788,
    "Solrød": 1746,
    "Sønderborg": 1730,
    "Sorø": 1771,
    "Stevns": 1747,
    "Struer": 1700,
    "Svendborg": 1779,
    "Syddjurs": 1745,
    "Tårnby": 1739,
    "Thisted": 1814,
    "Tønder": 1641,
    "Vallensbæk": 1745,
    "Varde": 1656,
    "Vejen": 1636,
    "Vejle": 1623,
    "Vesthimmerland": 1766,
    "Viborg": 1639,
    "Vordingborg": 1814
  }

    if energy != "":
        EnergyConsumption = energy
       #use energy
    else:
        EnergyConsumption = householdDatabase[household]
        #use household


    SunlightHours = sunshineHoursDatabase[municipalities]
    NoOfPanels = round(EnergyConsumption / (SunlightHours*0.3))
    SystemSize = round((NoOfPanels * 0.3))
    
    message = ""
    if SystemSize <= 1.5:
        PriceOfPanel = 28500
        RoofSpace = 8.2
        message = "Success"
    elif SystemSize <= 2.5:
        PriceOfPanel = 37600
        RoofSpace = 13
        message = "Success"
    elif SystemSize <= 3.5:
        PriceOfPanel = 51100
        RoofSpace = 19.8
        message = "Success"
    elif SystemSize <= 4.25:
        PriceOfPanel = 56500
        RoofSpace = 23.1
        message = "Success"
    else:
        PriceOfPanel = -1
        RoofSpace = -1
        message = 'Oh, your energy consumption is quite high - please contact us directly for an accurate offer'
    
    BreakEvenYear = (PriceOfPanel / (SunlightHours * SystemSize * 2.23))*2
    
    resp =  {
        "solarpanels" : PriceOfPanel, 
        "investmentcost" : RoofSpace,
        "breakeven" : BreakEvenYear,
        "message": message
    }    
    return func.HttpResponse(json.dumps(resp), status_code=200)


   
   
   

   