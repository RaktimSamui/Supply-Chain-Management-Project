import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
df=pd.read_csv('Data.csv')
avg_product_weight_location_wise=df.groupby('Location_type').aggregate({'product_wg_ton':lambda x: x.mean()}).reset_index()
avg_product_weight_location_wise.rename(columns={'product_wg_ton':'Average Weight of product in tons'},inplace=True)
st.write('# Demand of Product Location Wise:')
fig1 = px.pie(avg_product_weight_location_wise, values='Average Weight of product in tons', names='Location_type')
st.plotly_chart(fig1)
st.write('Slightly Higher Demand in Urban Areas Compared to Rural Areas')
st.markdown('---')

avg_product_weight_zone_wise=df.groupby('zone').aggregate({'product_wg_ton':lambda x: x.mean()}).reset_index()
avg_product_weight_zone_wise.rename(columns={'product_wg_ton':'Average Weight of product in tons'},inplace=True)
st.write('# Demand of Product Zone Wise:')
fig2 = px.pie(avg_product_weight_zone_wise, values='Average Weight of product in tons', names='zone')
st.plotly_chart(fig2)
st.write('Demand is Approximately Same in All the Zones')
st.markdown('---')

avg_product_weight_regional_zone_wise=df.groupby('WH_regional_zone').aggregate({'product_wg_ton':lambda x: x.mean()}).reset_index()
avg_product_weight_regional_zone_wise.rename(columns={'product_wg_ton':'Average Weight of product in tons'},inplace=True)
st.write('# Demand of Product Regional Zone Wise:')
fig3=px.pie(avg_product_weight_regional_zone_wise, values='Average Weight of product in tons', names='WH_regional_zone')
st.plotly_chart(fig3)
st.write('Demand is Approximately Same in All the Regional Zones')
st.markdown('---')