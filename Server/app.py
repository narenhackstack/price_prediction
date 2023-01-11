

from flask import Flask,jsonify,request
#creating an flask app
from Server import Util

app=Flask(__name__)
#__name__ is built-in special variable that evaluates the name of the current module
@app.route('/hello')
#route() decorator to tell Flask what URL should trigger our function.
def hello():
    return "hi friend"

#The function is given a name which is also used to generate URLs for
#that particular function, and returns the message we want to display in the user’s browser.

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': Util.get_location_names()
    })
    #standard for returning the requested data --> permission like thing
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_predicted_price',methods=['POST'])
def predict_home_price():
    total_sqft=request.form['total_sqft']
    location=request.form['location']

    response=jsonify({
        'estimated_price':Util.predictprice(location,total_sqft)
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__=='__main__':
    Util.loadsavedartifacts()
    print("Starting Flask Server for price prediction")
    app.run()