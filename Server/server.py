from flask import Flask, request
from flask.ext.cors import cross_origin
import json
from time import sleep


app = Flask(__name__)

results = [
            {
              "url": "https://pl.wikipedia.org/wiki/EB_%28piwo%29",
              "title": "EB (piwo) - Wikipedia",
              "content": "EB Specjal Pils – popularna w latach 90. XX wieku marka jasnego piwa produkowana w browarach w Elblągu i Braniewie."
            },
            {
              "url": "http://wiadomosci.onet.pl/olsztyn/piwo-eb-wraca-na-polski-rynek-to-odpowiedz-na-oferte-browaru-w-braniewie/096djl",
              "title": "Piwo EB wraca na polski rynek.",
              "content": "Piwo EB wraca na polski rynek. To odpowiedź na ofertę browaru w Braniewie. Słynne w Elblągu, regionie i całej Polsce..."
            },
            {
              "url": "http://natemat.pl/140833,legendarne-piwo-eb-wraca-na-rynek",
              "title": "Legendarne piwo EB wraca na rynek.",
              "content": "Legendarne piwo EB - symbol lat 90. wraca do sklepów. Już pod koniec kwietnia kupimy je w niemal identycznym opakowaniu..."
            },
            {
              "url": "https://www.facebook.com/PiwoEB/",
              "title": "EB Wróć",
              "content": "Polub EB Wróć, jeśli pamiętasz smak złotego trunku. Jest to kompletnie niekomercyjny fanklub piwa EB. Na zdrowie!"
            }
          ]

@app.route("/search/", methods=['POST', 'OPTIONS'])
@cross_origin(allow_headers=['Content-Type'])
def post_search():
    search_data = request.get_json()
    query = search_data["query"]
    # search for query in titles
    search_results = [result for result in results if query in result["title"].lower()]
    return json.dumps(search_results, ensure_ascii=False)

@app.route("/contest/", methods=['POST', 'OPTIONS'])
@cross_origin(allow_headers=['Content-Type'])
def post_contest_data():
    # do something with posted data
    contest_data = request.get_json()
    sleep(1) # sleep to slow things down
    print(contest_data)
    return "Done"

if __name__ == "__main__":
    app.run(port=2137) # localhost