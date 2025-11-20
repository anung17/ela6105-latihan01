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
import plotly.express as px
import numpy as np

st.title("Data Visualization")

# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)
# Plot data
fig, ax = plt.subplots()
ax.plot(x, y)
# Display the plot
st.pyplot(fig)



