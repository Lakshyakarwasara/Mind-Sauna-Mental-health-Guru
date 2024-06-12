# Mind-Sauna_Mental-Health-Guru
## Inspiration
Finding mental health treatments can be difficult, especially in today's technologically advanced society with so many possibilities. If you've wanted to address a mental health issue but have been hesitant to do so in person, simple software that is meant to help you navigate your mental health journey and take the uncertainty out of obtaining the help you need.

'Sauna' is a small room used as a hot-air or steam bath for cleaning and refreshing the body. MIND SAUNA is the place where you can come and flush out your toxins thereby cleansing your mind and getting some solutions on how to refresh/ calm yourself.


## Abstract
The increase of mental health problems and the need for effective medical health care have led to an investigation of machine learning that can be applied in mental health problems. Mental health problems detected at earlier stage helps the psychologist to medicate and enhance the patient’s life. As such, it becomes important to track and remedy any problems before they get too serious. We try achieving this using Mind Sauna. 
This project provides an evaluation of machine learning in mental healthcare. We performed a thorough analysis of the dataset to characterize the subjects’ behaviour based on different aspects of their PHQ9 question answering and textual inputs. Quiz Based Analysis is done using multiple machine learning algorithms (SVM, Naïve Bayes, KNN, DT, Random Forest) and TextBlob is used for detecting depression from sentiments.

## How we built it
This project has been built with a lot of love, consideration to help others with their mental health using:

* Flask
* Python
* HTML/CSS

## Challenges we ran into
* FLASK API was very new to us. It took us a while to learn it to comprehensively create the website.
* Sentiment based analysis presented several difficulities as Natural Language Processing was a new domain to explore for all of us.

## How Run the Project 
* Install all libraries $ pip install -r requirements.txt

* Run the application $ python server.py

* In Browser open URL localhost:5987

## How to Make Use of The Project

![Screenshot (1)](https://user-images.githubusercontent.com/113436694/207954953-da427195-7450-4499-88ba-904a14f05ce1.png)

![Screenshot (2)](https://user-images.githubusercontent.com/113436694/207954160-4a4f7644-360c-473b-bcbf-5ef058cc9b23.png)

![Screenshot (3)](https://user-images.githubusercontent.com/113436694/207954208-8506541a-08b3-432e-9365-05e8c5209bd1.png)

![Screenshot (4)](https://user-images.githubusercontent.com/113436694/207954226-fcc5ef88-ad5b-4a7c-b687-a32df7e7471c.png)

![Screenshot (5)](https://user-images.githubusercontent.com/113436694/207954240-45d4f2bc-77f6-4a59-a602-ea3bfbfe4b5d.png)

![Screenshot (6)](https://user-images.githubusercontent.com/113436694/207954260-69cfe2a1-9b90-410e-9c07-600520b90651.png)

![Screenshot (7)](https://user-images.githubusercontent.com/113436694/207954285-75a3abb8-24a9-4e08-9eec-7c001f511431.png)

![Screenshot (8)](https://user-images.githubusercontent.com/113436694/207954305-3f859d44-c0a0-4f09-b9b4-f6007d368896.png)

## Contribution
The project work was divided into two broad categories- Frontend and Backend. 

•	Backend work was further divided into two parts- 
Text Based Analysis (Sentiment Analysis) and Quiz Based Analysis (PHQ9 survey dataset analysis). I and Mansi worked on this part. We researched the available data, applied pre-processing, EDA, data manipulation and feature engineering, selected the appropriate model and tuned it.

Quiz Based Analysis was performed by me. The dataset was PHQ-9(Patient Health Questionnaire-9) Survey. I’ve applied 5 different ML algorithm/ classifier- Support Vector Machine, Naïve Bayes, KNN, Decision Tree, Random Forest on the dataset. SVM provided the best results with the highest F1 score and lowest log loss which were my chosen performance metric. The dataset was balanced, hence using these were justified. The results also conveyed that the more features are used, the higher the accuracy and F-measure scores in detecting depressed. However, the data set was very minimal and in the future, the research may be applied to a large data set to obtain more accuracy

Sentiment Based Analysis was performed by Mansi. It was a Natural Language Processing task and was performed using TextBlob. No dataset is required for this. TextBlob is one of the most prominent and easy-to-use libraries. As the official documentation suggests: TextBlob is a Python (2 and 3) library for processing textual data. It provides a simple API for diving into common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.

•	Frontend work was performed by Lakshya. Our ML model is deployed to production using FLASK as an API. In order to get user input and then render your predictions as output, we needed a web-page structure and some aesthetics for better user experience. He integrated HTMM/CSS with Python by Flask. HTML is used to provide base structure and CSS gave aesthetics to it. He has written the code creating 6 HTML files in template folder i.e. “index.html”, “link.html”, “error.html”, “result.html”, “sentiment.html” and “tweetresult.html”. We have communicated with html files from our server.py file  which is heart of the project and links to our other files.

## Accomplishments that we're proud of
We were able to create a functional website with the visual we intended. We are very proud of our product at the end.

## What we learned
* We learned new technology like flask and one of the most exciting fields in AI i.e. Natural Language Processing (NLP).
* By working closely at a team, we can achieve new goals in a short amount of time.



