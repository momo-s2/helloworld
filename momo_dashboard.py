#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 15:09:44 2022

@author: momo
"""
#import libs
import streamlit as st
import pandas as pd

st.header('Day 18 of #30 Days of Streamlit:hatched_chick:')

st.title('st.file_uploader')

st.subheader('Input CSV')
uploaded_file = st.file_uploader('Choose a file')

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Descriptive Statistics')
  st.write(df.describe())
  st.write(df.describe())
else:
  st.info('☝️ Upload a CSV file')
      
