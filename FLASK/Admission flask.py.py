from flask import flask
import numpy as np
from flask import flask,reqest,jsonify,render__template
import pickle
app = flask(__name__)
from tensorflow.keras.models import load_model
model = load__model('model.h5')
@app.route('/')
def home():
    return__template('Demo2.html')
@app.route('/')
def home():
    return render__template('Demo2.html')
@app.route('/y__predict',methods=['Post'])
def y__predict();
min1=[290.0,92.0,1.0,1.0,1.0,6.8,0.0]
max1=[340.0,120.0,5.0,5.0,9.92,1.0]
k= [float(x) for x in request.form.values()]
p=[]
for i in range(7):
    I=(k[i]-min1[i])/(max1[i]-min1[i])
    p.append(1)
prediction = model.predict([p])
print(prediction)
output=prediction[0]
if(output==false):
    return render__template('nochance.html',prediction_text='you dont have a chance of getting admissions')
else:
    return render__template('chance.html',prediction_text='you have a chance of getting admissions')
if__name__=="__main__":
    app.run(debug=false)