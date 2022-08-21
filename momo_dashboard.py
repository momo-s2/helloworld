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


st.header('Day 5 CHALLENGE:hatched_chick:')


st.write('DataFrame-list')
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],
                   columns = ['col1','col2','col3'],
                   index = ['i1','i2','i3'])
st.write(df)

st.write('DataFrame-NumPy')
df = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]),
                   columns = ['col1','col2','col3'],
                   index = ['i1','i2','i3'])
st.write(df)

st.write('DataFrame-dictionary')
df = pd.DataFrame({'col1':[1,2,3],
                   'col2':[4,5,6],
                   'col3':[7,8,9]}
                    ,index = ['i1','i2','i3'])
st.write(df)


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

