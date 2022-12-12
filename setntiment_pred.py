import pandas as pd
import pickle
import numpy as np
count_vect = pickle.load(open(r'sentiment\count_vect.p', 'rb'))
model=pickle.load(open(r'sentiment\naive_bayes.p','rb'))



def predict_emotion(sample_text,cv,model):
    myvect=cv.transform(sample_text).toarray()
    prediction=model.predict(myvect)
    pred_proba=model.predict_proba(myvect)
    pred_percentage_for_all=dict(zip(model.classes_,pred_proba[0]))
    # print("prediction: {}, prediction Score {}".format(prediction[0],np.max(pred_proba)))
    # return pred_percentage_for_all
    return (prediction[0],np.max(pred_proba))


# sample_text = ['I love coding ']
# predict_emotion(sample_text, count_vect,model)