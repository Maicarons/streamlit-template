import streamlit as st
from PIL import Image


def page_config(title='Page', icon='./static/icon.png', lay='centered', menu=None):
    if menu is None:
        menu = {'Get Help': 'https://github.com/Maicarons/streamlit-template/issues',
                'Report a bug': "https://github.com/Maicarons/streamlit-template/issues",
                'About': "Maicarons"}
    pic = Image.open(icon)
    st.logo(pic)
    st.set_page_config(
        page_title=title,
        page_icon=pic,
        layout=lay,
        menu_items=menu
    )
