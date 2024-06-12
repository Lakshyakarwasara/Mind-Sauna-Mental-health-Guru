from flask import Flask, request, render_template,flash,redirect,session,abort,jsonify
from models import Model
# from depression_detection_tweets import DepressionDetection
#from TweetModel import process_message
import os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
# @app.route('/')
# def root():
#     if not session.get('logged_in'):
#         return render_template('login.html')
#     else:
#         return render_template('index.html')

@app.route('/')
def root():
    return render_template('index.html')


@app.route('/Links')
def Links():                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    # if not session.get('logged_in'):
    #     return render_template('login.html')
    # else:
        # return render_template('index.html')
    return render_template('Links.html')


@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'admin' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else :
        flash('wrong password!')
    return root()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return root()


@app.route("/sentiment")
def sentiment():
    return render_template("sentiment.html")


@app.route("/predictSentiment", methods=["POST"])
def predictSentiment():
    message = request.form['form10']
    #pm = process_message(message)
    #result = DepressionDetection.classify(pm, 'bow') or DepressionDetection.classify(pm, 'tf-idf')
    def sentiment_scores(message):
        sid_obj = SentimentIntensityAnalyzer()
        sentiment_dict = sid_obj.polarity_scores(message)
        #print("Overall sentiment dictionary is : ", sentiment_dict)
        #print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
        #print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
        #print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")
        #print("Sentence Overall Rated As", end = " ")
        # decide sentiment as positive, negative and neutral
        result=0
        if sentiment_dict['compound'] >= 0 :
            #print("Positive")
            result=1
        elif sentiment_dict['compound'] <= 0 :
            #print("Negative")
            result=-1
        return result
    return render_template("tweetresult.html",result=sentiment_scores(message))


@app.route('/predict', methods=["POST"])
def predict():
    q1 = int(request.form['a1'])
    q2 = int(request.form['a2'])
    q3 = int(request.form['a3'])
    q4 = int(request.form['a4'])
    q5 = int(request.form['a5'])
    q6 = int(request.form['a6'])
    q7 = int(request.form['a7'])
    q8 = int(request.form['a8'])
    q9 = int(request.form['a9'])
    q10 = int(request.form['a10'])

    values = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
    model = Model()
    classifier = model.svm_classifier()
    prediction = classifier.predict([values])
    if prediction[0] == 0:
            result = 'Your Mental Health test result :\n No Risk'
    if prediction[0] == 1:
            result = 'Your Mental Heath test result : \n Mild Risk, Seek Help!'
    if prediction[0] == 2:
            result = 'Your Mental Health test result :\n Moderate Risk, Seek Help!'
    if prediction[0] == 3:
            result = 'Your Mental Health test result :\n Moderately severe Risk, Seek Help!'
    if prediction[0] == 4:
            result = 'Your Mental Health test result :\n Severe Risk, Seek Help!'
    return render_template("result.html", result=result)

app.secret_key = os.urandom(12)
app.run()
