#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyleft © 2025 Anung <anung@trisakti.ac.id>
# 2025-11-18 10:20
# Distributed under terms of the MIT license.

"""
Exampe from
https://msaqib-genai.medium.com/how-to-create-a-multi-page-app-in-streamlit-7f788e715db4
"""

import streamlit as st
import pandas as pd

st.title("Settings")
st.write("This page allows you to customize your preferences.")

df = pd.read_csv('data/datagojekcopy.csv')
st.write(df.tail())

st.write("Simulasi error")

