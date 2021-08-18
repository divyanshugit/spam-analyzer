import pickle
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import CountVectorizer

classifier = pickle.load(open('models/model.pkl', 'rb'))
encoder = pickle.load(open('models/transformer.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def home():
        return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
    	message = request.form['message']

    	vect = encoder.transform([message]).toarray()
    	my_prediction = classifier.predict(vect)
    	return render_template('prediction.html', prediction=my_prediction)

@app.route('/source')
def source():
        return render_template("source.html")
if __name__ == '__main__':
        app.run(debug=True)