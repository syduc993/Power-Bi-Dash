import dash
from dash import dcc, html
# import streamlit as st

dash.register_page(__name__, name='Update')

layout = html.Div(
    [
        html.H1("Power BI Report"),  # Thêm tiêu đề vào trang web
        html.Iframe(
            src='https://app.powerbi.com/view?r=eyJrIjoiZTg5NTU5YTEtNzI4MC00NjI5LWE1NTUtZWM3ZjZiMjU5YTVmIiwidCI6IjkwYjY0ZWVlLTg0M2UtNDBiZi04ODZkLWZjMmMxNDk2NjE3NiIsImMiOjEwfQ%3D%3D',
            style={'height': '100vh', 'width': '100%'}
        )
    ]
)