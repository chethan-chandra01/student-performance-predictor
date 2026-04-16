import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.title("Student Performance Predictor")
st.write("Welcome Dear !")
name=st.text_input("Enter your Name here")

df=pd.read_csv("student_data.csv")

st.write("Hi ",name,"Please fill the follwing values ")
age=st.slider("Select  your  age",0,int(df.age.max()),int(df.age.mean()))
traveltime=st.slider("Select your travel time:",0,int(df.traveltime.max()),int(df.traveltime.mean()))
freetime=st.slider("Select your free time",0,int(df.freetime.max()),int(df.freetime.mean()))
health=st.slider("Rate your health",0,int(df.health.max()),int(df.health.mean()))
studytime=st.slider("select your study time",0,int(df.studytime.max()),int(df.studytime.mean()))
activities=st.selectbox("Do participate in co-curricular activites:",['Yes','No'])
activities = {"Yes": 1, "No": 0}[activities]
internet=st.selectbox("Do you have an internet access ?",['Yes','No'])
internet = {"Yes": 1, "No": 0}[internet]
absences=st.slider("select your number of absences:",0,int(df.absences.max()),int(df.absences.mean()))
g1=st.slider("select your G1 Marks:",0,20)
g2=st.slider("select your G2 Marks :",0,20)
failures=st.slider("select  number of failures:",0,int(df.failures.max()),int(df.failures.mean()))
romantic=st.selectbox("Are you romantic ",['Yes','No'])
romantic = {"Yes": 1, "No": 0}[romantic]

#features=['age','traveltime','freetime','health','studytime','activities','internet','absences','G1','G2','failures','romantic']

st.write("Hi",name,",\n\nHere is the data you entered , Please check once\n\n"
, "Your age:",age,"\n\n","Your traveltime is:",traveltime,"\n\n","Your study time is:",studytime,"\n\n","Internet Access:",internet,"\n\n","Number of failures:",failures,"\n\n","Number of absences:",absences,"\n\n","Your G1 Marks:",g1,"\n\n","Your G2 Marks :",g2,"\n\n","Your health:",health,"\n\n","Activities:",activities,"\n\n","Romantic:",romantic,'\n\n'
            )

data=joblib.load("model.pkl")
model=data["model"]
new_info=[age,traveltime,freetime,health,studytime,activities,internet,absences,g1,g2,failures,romantic]
#[13,2,1,2,8,1,1,0,10,15,0,0]
if st.button("Predict Performance"):
    prediction=model.predict([new_info])
    prediction=float(prediction)
    if(prediction>20):
        st.success(f'Your predicted Score is 20')
    else:
        st.success(f'Expected Score is :{round(prediction,2)}')
    if(prediction>=15):
        st.success("Excellent performance is expected!!")
    elif( prediction>=10):
        st.info("Average performance is expected")
    else:
        st.warning("Improvement needed!!")