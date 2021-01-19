import logging
import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    municipalities = req.params.get('municipalities')
    energy = req.params.get('energy')
    household = req.params.get('household')

energy = int(input('No. in kWh'))

household = input('No. of people')
household_size = {'1': 1500, '2': 2500, '3': 3500, '4': 4250, '5': 5400} 

municipalities = str(input('In which municipality do you live?'))
sunshine_hours = {'Aabenraa': 1590, 'Aalborg': 1782, 'Aarhus': 1699, 'Æro' : 1786, 'Albertslund' : 1747, 'Allerød': 1743, 'Assens': 1753, 'Ballerup': 1747, 'Billund': 1615, 'Bornholm': 1909, 'Brøndby': 1744, 'Brønderslev': 1787, 'Dragør': 1739, 'Egedal': 1748,'Esbjerg': 1679, 'Faaborg-Midtfyn' : 1757, 'Fanø' : 1748, 'Favrskov' : 1658, 'Faxe' : 1750, 'Fredensborg' : 1747, 'Fredericia' : 1713, 'Frederiksberg' : 1739, 'Frederikshavn' : 1885, 'Frederikssund' : 1769, 'Furesø' : 1744, 'Gentofte' : 1741, 'Gladsaxe' : 1742, 'Glostrup': 1745, 'Greve': 1748, 'Gribskov' : 1767, 'Guldborgsund' : 1838, 'Haderslev' : 1658, 'Halsnæs' : 1791, 'Hedensted' : 1649, 'Helsingør' : 1754, 'Herlev' : 1745, 'Herning' : 1610, 'Hillerød' : 1745, 'Hjørring' : 1834, 'Høje-Taastrup': 1747, 'Holbæk': 1783, 'Holstebro' : 1666, 'Horsens' : 1627, 'Hørsholm' : 1744, 'Hvidovre' : 1740, 'Ikast-Brande' : 1579, 'Ishøj' : 1746, 'Jammerbugt' : 1798, 'Kalundborg' : 1809, 'Kerteminde' : 1799, 'Københavns' : 1739, 'Køge' : 1743, 'Kolding' : 1660, 'Læso' : 1952, 'Langeland' : 1801, 'Lejre' : 1766, 'Lemvig' : 1722, 'Lolland' : 1796, 'Lyngby-Taarbæk' : 1743, 'Mariagerfjord' : 1723, 'Middelfart' : 1757, 'Morsø' : 1803, 'Næstved' : 1773, 'Norddjurs' : 1771, 'Nordfyn' : 1774, 'Nyborg' : 1785, 'Odder' : 1755, 'Odense' : 1751, 'Odsherred' : 1805, 'Randers' : 1687, 'Rebild' : 1752, 'Ringkøbing-Skjern' : 1651, 'Ringsted' : 1760, 'Rødovre' : 1742, 'Roskilde' : 1752, 'Rudersdal' : 1744, 'Samsø' : 1919, 'Silkeborg' : 1612, 'Skanderborg' : 1635, 'Skive' : 1720, 'Slagelse' : 1788, 'Solrød' : 1746, 'Sønderborg' : 1730, 'Sorø' : 1771, 'Stevns' : 1747, 'Struer' : 1700, 'Svendborg' : 1779, 'Syddjurs' : 1745, 'Tårnby' : 1739, 'Thisted' : 1814, 'Tønder' : 1641, 'Vallensbæk' : 1745, 'Varde' : 1656, 'Vejen' : 1636, 'Vejle' : 1623, 'Vesthimmerland' : 1766, 'Viborg' : 1639, 'Vordingborg' : 1814}

def NoOfPanels (energy, sunshine_hours)
 """ This function calculates the number of panels needed. If the user puts in any int for his individual energy consumption the formular"""
    if energy != "":
        return NoOfPanels = round(energy / ((float(sunshine_hours.get('municipalities'))*0.3))
    else:
        return NoOfPanels = round(float(household_size.get('household')) / ((float(sunshine_hours.get('municipalities'))*0.3))

def SystemSize (NoOfPanels)
SystemSize = round((NoOfPanels * 0.3))

PriceOfPanel = {SystemSize : [28500, 37600, 51100, 56500, 69000]}
RoofSpace = {SystemSize : [8.2, 13, 19.8, 23.1, 30]}

def breakeven (energy, household_size, sunshine_hours)
""" This function calculates the breakeven """
breakeven = PriceOfPanel/(sunshine_hours*0.3*2.23*NoOfPanels)

Message1 = 'Oh, your energy consumption is quite high - please contact us directly for an accurate offer.'
Message2 = 'Have you entered your household size (1-5)?'

    resp = {"panelprice": PriceOfPanel,
            "roofspace": RoofSpace
            "breakeven": BreakEvenYear
            "message1": Message1
            "message2": Message2
            }
            
    return func.HttpResponse(json.dumps(resp), status_code=200)

