import streamlit as st
import numpy as np
from joblib import load
import pandas as pd
scaler=load('scaler.joblib')
model=load('final_model.joblib')

def prediction(scaled_array):
   return str(float(model.predict(scaled_array)))+' '+'tons for 3 months'

def main():
    st.title('Shipping Weight Predictor:')
    st.subheader('Now predict the optimum weight of the product to be shipped to the warehouse each time with 99% accuracy.')
    st.text('\n')
    st.text('\n')
    st.markdown('##### Enter the details regarding the warehouse down below:')
    warehouse_size=st.selectbox('Specify the Size of the Warehouse:',['Small','Large','Mid'])
    st.text('\n')
    if warehouse_size=='Small':
        warehouse_size=1
    elif warehouse_size=='Mid':
        warehouse_size=2
    elif warehouse_size=='Large':
        warehouse_size=3
    num_refill_req=st.number_input('Specify the number of refills required in last 3 Months:')
    st.text('\n')
    transport_issue=st.number_input('Specify the number of transport issues in last 1 Year:')
    st.text('\n')
    retail_num=st.number_input('Specify the retail shops selling the product under the warehouse area:')
    st.text('\n')
    electric_supply=st.radio('Does the Warehouse have any kind of electric backup such as generator, etc.:',['Yes','No'])
    st.text('\n')
    if electric_supply=='Yes':
        electric_supply=1
    elif electric_supply=='No':
        electric_supply=0
    storage_issues_in_last_3_months=st.number_input('Specify the number of storage issues reported in last 3 months such as fungus because of moisture, etc.:')
    st.text('\n')
    temp_reg_mach=st.radio('Does the Warehouse have temperature regulating machine indicator:',['Yes','No'])
    st.text('\n')
    if temp_reg_mach=='Yes':
        temp_reg_mach=1
    elif temp_reg_mach=='No':
        temp_reg_mach=0
    approved_wh_govt_certificate=st.selectbox('Specify What kind of standard certificate has been issued to the warehouse from government regulatory body:',['A+','A','B+','B','C'])
    st.text('\n')
    if approved_wh_govt_certificate=='A+':
        approved_wh_govt_certificate=5
    elif approved_wh_govt_certificate=='A':
        approved_wh_govt_certificate=4
    elif approved_wh_govt_certificate=='B+':
        approved_wh_govt_certificate=3
    elif approved_wh_govt_certificate=='B':
        approved_wh_govt_certificate=2
    elif approved_wh_govt_certificate=='C':
        approved_wh_govt_certificate=1
    wh_breakdown_l3m=st.number_input('Specify the number of times the warehouse broke down in last 3 months:')
    st.text('\n')
    location=st.selectbox('Specify if the warehouse is located in a rural area or an urban area:',['Rural','Urban'])
    st.text('\n')
    if location=='Rural':
        location=0
    elif location=='Urban':
        location=1
    regional_zone=st.selectbox('Specify in which of these regional zone is the warehouse located',['Zone 2','Zone 4','Zone 5','Zone 6','None of these zones/Other'])
    st.text('\n')
    if regional_zone=='Zone 2':
        zone_2=1
        zone_4=0
        zone_5=0
        zone_6=0
    elif regional_zone=='Zone 4':
        zone_2=0
        zone_4=1
        zone_5=0
        zone_6=0
    elif regional_zone=='Zone 5':
        zone_2=0
        zone_4=0
        zone_5=1
        zone_6=0
    elif regional_zone=='Zone 6':
        zone_2=0
        zone_4=0
        zone_5=0
        zone_6=1
    else:
        zone_2=0
        zone_4=0
        zone_5=0
        zone_6=0
    geographic_zone=st.selectbox('Specify in which of these geographic zones is the warehouse located',['East','West','North','South'])
    if geographic_zone=='West':
        north=0
        south=0
        west=1
    elif geographic_zone=='North':
        north=1
        south=0
        west=0
    elif geographic_zone=='South':
        north=0
        south=1
        west=0
    else:
        north=0
        south=0
        west=0
    scaled_values=scaler.transform(np.array([[warehouse_size,num_refill_req,transport_issue,retail_num,electric_supply,storage_issues_in_last_3_months,temp_reg_mach,approved_wh_govt_certificate,wh_breakdown_l3m,location,zone_2,zone_4,zone_5,zone_6,north,south,west]]))
    st.markdown('---')
    st.write('click the button to predict the optimum weight of the product to be shipped to the warehouse')
    if st.button('Predict'):
        st.success(prediction(scaled_values))
        
if __name__=="__main__":
    main()