import dash
from dash import dcc, html
# import streamlit as st

dash.register_page(__name__, path='/', name='Tỉ lệ bán giảm giá')

layout = html.Iframe(src='https://app.powerbi.com/view?r=eyJrIjoiZTlmOTMwYjAtNDgzYy00ZmJkLWJkYjItODEzZDI1NThiNGFmIiwidCI6IjkwYjY0ZWVlLTg0M2UtNDBiZi04ODZkLWZjMmMxNDk2NjE3NiIsImMiOjEwfQ%3D%3D',
                         style={'height': '85vh', 'width': '100%'})
