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
st.write(st.secrets(['test_secrets_key']))
