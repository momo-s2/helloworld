#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 15:09:44 2022

@author: momo
"""
#import libs
import streamlit as st

st.title('st.form')

# Full example of using the with notation
st.header('Day 22 of #30 Days of Streamlit:hatched_chick:')


with st.form('my_form'):
    st.subheader('What would you want to drink?')

    product = st.selectbox('Product', ['-', 'Caffé Latte', 'Caffé Americano', 'Cappuccino', 'Espresso'])
    serving_format = st.selectbox('Serving format', ['-','Hot', 'Iced'])
    size= st.selectbox('Size', ['-', 'Short', 'Tall', 'Grande','Venti'])
    milktype = st.selectbox('Type of milk',['-', 'Whole milk', 'Non-fat milk', 'Soy milk','Oat milk', 'Almond milk'])
    customize = st.multiselect(
        'Customize',
        ['honey', 'cinnamon', 'whipped cream', 'espresso shot']
        )
    owncup = st.checkbox('Bring own cup')

    submitted = st.form_submit_button('Submit')

if submitted:
    st.markdown(f'''
        ☕ You have ordered:
        - Product: '{product}'
        - Serving format: '{serving_format}'
        - Size: '{size}'
        - Type of milk: '{milktype}'
        - Cuztomize: '{customize}'
        - Bring own cup: '{owncup}'
        ''')
        
else:
    st.write('☝️ Place your order!')
