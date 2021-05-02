from flask import Flask, url_for, render_template, redirect
from forms import PredictForm
from flask import request, sessions
import requests
from flask import json
from flask import jsonify
from flask import Request
from flask import Response
import urllib3
import json

app = Flask(__name__, instance_relative_config=False)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = 'development key'
if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')

@app.route('/', methods=('GET', 'POST'))
def startApp():
    form = PredictForm()
    return render_template('index.html', form = form)

@app.route('/predict', methods=('GET', 'POST'))
def predict():
    form = PredictForm()
    if form.submit():

        header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + "<IAM ACCESS TOKEN>"}

        python_object = [form.Gender.data, form.CustomerType.data, form.Age.data,
          form.TypeOfTravel.data, form.Class.data, form.FlightDistance.data,
          form.SeatComfort.data, form.DepartureArrivalTimeConvenient.data, form.FoodAndDrink.data,
          form.GateLocation.data, form.InflightWifiService.data, form.InflightEntertainment.data,
          form.OnlineSupport.data, form.EaseOfOnlineBooking.data, form.OnboardService.data,
          form.LegRoomService.data, form.BaggageHandling.data, form.CheckinService.data,
          form.Cleanliness.data, form.OnlineBoarding.data]
        userInput = []
        userInput.append(python_object)

        payload_scoring = {"input_data": [{"fields": ["Gender", "CustomerType", "Age",
          "TypeOfTravel", "Class", "FlightDistance","SeatComfort","DepartureArrivalTimeConvenient",
          "FoodAndDrink","GateLocation","InflightWifiService","InflightEntertainment","OnlineSupport",
          "EaseOfOnlineBooking","OnboardService","LegRoomService","BaggageHandling","CheckinService",
          "Cleanliness","OnlineBoarding"], "values": userInput }]}

        response_scoring = requests.post('<ENDPOINT DIRECT LINK>', json=payload_scoring, headers={'Authorization': 'Bearer ' + "<IAM ACCESS TOKEN>"})

        output = json.loads(response_scoring.text)
        for key in output:
          tempVar = output[key]

        for key in tempVar[0]:
          tempVar_2 = tempVar[0][key]
          
        form.sat = tempVar_2[0][0]
        form.satProbability = format(tempVar_2[0][1][1]*100,".2f")
        return render_template('index.html', form = form)
