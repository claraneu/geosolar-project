import logging
import azure.functions as func
import json


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    sunshineHoursDatabase= ["Aabenraa" , "Aalborg", "Aarhus", "Æro","Albertslund","Allerød","Assens","Ballerup","Billund","Bornholm","Brøndby", "Brønderslev","Dragør","Egedal", "Esbjerg",  "Faaborg-Midtfyn","Fanø","Favrskov","Faxe","Fredensborg","Fredericia","Frederiksberg","Frederikshavn","Frederikssund","Furesø","Gentofte","Gladsaxe","Glostrup","Greve","Gribskov","Guldborgsund","Haderslev","Halsnæs","Hedensted","Helsingør","Herlev","Herning","Hillerød","Hjørring","Høje-Taastrup","Holbæk","Holstebro","Horsens","Hørsholm","Hvidovre","Ikast-Brande","Ishøj","Jammerbugt","Kalundborg","Kerteminde","Københavns","Køge","Kolding","Læso","Langeland","Lejre","Lemvig","Lolland","Lyngby-Taarbæk","Mariagerfjord","Middelfart","Morsø","Næstved","Norddjurs","Nordfyn","Nyborg","Odder","Odense","Odsherred","Randers","Rebild","Ringkøbing-Skjern","Ringsted","Rødovre","Roskilde","Rudersdal","Samsø","Silkeborg","Skanderborg","Skive","Slagelse","Solrød","Sønderborg","Sorø","Stevns","Struer","Svendborg","Syddjurs","Tårnby","Thisted","Tønder","Vallensbæk","Varde","Vejen","Vejle","Vesthimmerland","Viborg","Vordingborg"]


    resp = {'kommuner':sunshineHoursDatabase}
    return func.HttpResponse(json.dumps(resp), status_code=200)