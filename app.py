import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app = Flask(__name__)

##  Loading the model

regmodel = pickle.load(open("reg_model.pkl","rb"))
scale = pickle.load(open("scaling.pkl","rb"))
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict_api",methods = ["POST"])
def predict_api():
    data=request.json["data"]
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data = scale.transform(np.array(list(data.values())).reshape(1,-1))
    output = regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

if __name__ == "__main__":
    app.run(debug=True)
    

# @app.route("/predict_api",methods = ['POST'])
# def predict_api():
#     data = [float(x) for x in request.from.values()]
#     final_input=scale.transform(np.array(data).reshape(1,-1))
#     print(final_input)
#     output = regmodel.predict(final_input)[0]
#     return render_template("home.html",prediction_text = "The Hosue price Prediction is{}".format(output))