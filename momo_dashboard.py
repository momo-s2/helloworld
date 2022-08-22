#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 15:09:44 2022

@author: momo
"""
import streamlit as st

st.title('#30 Days of Streamlit')
st.header('Day 10-12 CHALLENGE:hatched_chick:')

st.subheader('st.selectbox')

option = st.selectbox(
    'which area would you like to go?',
    ('Africa','America','Antarctica','Asia','Europe','Oceania'))

st.write('Where you want to go is', option)


st.subheader('st.multiselect')

options = st.multiselect(
    'which country would you like to go?',
    ['Kenya','Uganda','Tanzania','Rwanda','Brundi','Somalia'],
    )

st.write('You selected:',options)

st.subheader('st.checkbox')

st.write('which country would you like to go?')

Kenya = st.checkbox('Kenya')
Tanzania = st.checkbox('Tanzania')
Uganda = st.checkbox('Uganda')
s
if Kenya:
    st.write('You should go Masai Mara 🐘')
if Tanzania:
    st.write('You should go Zanzibar 🌴')
if Uganda:
    st.write('You should go Bwindi Impenetrable National Park 🦍')

#chart
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

#slidebar
add_sidebar = st.sidebar.selectbox('Chart Type',('Line Chart','Bar Chart'))

#switchedchart
if add_sidebar == 'Line Chart':
    st.header('Line Chart')
    data = {
        'x': np.random.random(20),
        'y': np.random.random(20) - 0.5,
        'z': np.random.random(20) - 1.0,
    }
    df = pd.DataFrame(data)
    st.line_chart(df)

if add_sidebar == 'Bar Chart':
    st.header('Bar Chart') 
    data = {
        'x': np.random.random(20),
        'y': np.random.random(20) - 0.5,
        'z': np.random.random(20) - 1.0,
    }
    df = pd.DataFrame(data)
    st.bar_chart(df)

