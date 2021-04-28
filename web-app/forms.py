from flask_wtf import FlaskForm
from flask_wtf import Form
from wtforms import StringField, TextField, SubmitField, IntegerField,TextAreaField,RadioField,SelectField, DecimalField
from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import ValidationError

class PredictForm(FlaskForm):
	Gender = StringField('Gender')
	CustomerType = StringField('Customer Type: ')
	Age = IntegerField('Age: ')
	TypeOfTravel = StringField('Type Of Travel: ')
	Class = StringField('Class: ')
	FlightDistance = IntegerField('Flight Distance: ')
	SeatComfort = IntegerField('Seat Comfort: ')
	DepartureArrivalTimeConvenient = IntegerField('Departure Arrival Time Convenient: ')
	FoodAndDrink = IntegerField('Food And Drink: ')
	GateLocation = IntegerField('Gate Location: ')
	InflightWifiService = IntegerField('Inflight Wifi Service: ')
	InflightEntertainment = IntegerField('Inflight Entertainment: ')
	OnlineSupport = IntegerField('Online Support: ')
	EaseOfOnlineBooking = IntegerField('Ease Of Online Booking: ')
	OnboardService = IntegerField('Onboard Service: ')
	LegRoomService = IntegerField('Legroom Service: ')
	BaggageHandling = IntegerField('Baggage Handling: ')
	CheckinService = IntegerField('Check-in Service: ')
	Cleanliness = IntegerField('Cleanliness: ')
	OnlineBoarding = IntegerField('Online Boarding: ')

	submit = SubmitField('Predict')
	abc = ""
