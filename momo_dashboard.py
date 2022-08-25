#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 15:09:44 2022

@author: momo
"""
#import libs
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
from datetime import time, datetime

st.header('Day 17 of #30 Days of Streamlit:hatched_chick:')
st.title('st.secrets')
st.write(st.secrets('test_secrets_key'))



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

if Kenya:
    st.write('You should go Masai Mara 🐘')
if Tanzania:
    st.write('You should go Zanzibar 🌴')
if Uganda:
    st.write('You should go Bwindi Impenetrable National Park 🦍')
