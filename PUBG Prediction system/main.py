from flask import Flask,request,render_template
from data_Per import *
from data_process import *
from get_data import *
from load_predict import *





'''
This is the main file through which the servers run 
'''
app = Flask(__name__)
@app.route('/')
def welcome():
    return render_template("index.html")

@app.route("/predict", methods = ["POST"])
def predict():
    user_name = request.form['userId']
    print(user_name)
    data = get_data_to_predict(user_name)
    res = predict_res(data,model)
    res= res *100
    res = float("{0:.4f}".format(res))
    res = "You have "+ str(res) + "%  Chance Winning the next match" 

    return render_template("index.html",output = res)

@app.errorhandler(500)
def internal_error(error):

    return render_template("index.html",output = "Please provide a correct user ID !!!")



if __name__ == "__main__":
    model = load()
    app.run(port =5050) # app.run(host="0.0.0.0")