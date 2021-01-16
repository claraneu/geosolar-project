import logging
import azure.functions as func
import json


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")
    municipalities = req.params.get("municipalities")
    energy = req.params.get("energy")
    household = req.params.get("household")
    # Dictionary with panel prices
    #Creating dataframe for solar panal system prices and required roof space
    #panel_prices = {‘System Size in kWp
    # ’:[‘1,5kWp’,‘2,5kWp’,‘3,5kWp’,‘4,25kWp’],‘Price in DKK’:[28500,37600,51100,56500],‘Roof space in sqm’: [8.2,13,19.8,23.1]}
    #Insert our code here (3 step breakeven calculation)
    #Calculate yearly production for 1 panel at a certain location
    #production = sunshine_hours * 300
    #municipalities=test&energy=test&household=test
    resp = {"Hello" : "World", "test" : municipalities+energy+household}
    return func.HttpResponse(json.dumps(resp), status_code=200)