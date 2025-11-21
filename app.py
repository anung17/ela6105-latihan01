#! /usr/bin/env python3
# vim:fenc=utf-8
#
# Copyleft © 2025 Anung <anung@trisakti.ac.id>
# 2025-11-18 10:18
# Distributed under terms of the MIT license.

"""
Example from
https://msaqib-genai.medium.com/how-to-create-a-multi-page-app-in-streamlit-7f788e715db4
"""

import streamlit as st

pages = [
    st.Page(page="pages/page1.py", title="Home", icon="🏠"),
    st.Page(page="pages/page2.py", title="Visualisasi Data", icon="📊"),
    st.Page(page="pages/page3.py", title="Settings", icon="⚙️")
]

pg = st.navigation(
    pages,
    position="sidebar",
    expanded=True
)

pg.run()

