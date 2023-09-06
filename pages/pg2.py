import dash
from dash import dcc, html
import streamlit as st

dash.register_page(__name__, name='Comming Soon')

layout = html.Div(
    [
        html.H1("Power BI Report"),  # Thêm tiêu đề vào trang web
        html.Iframe(
            src='https://app.powerbi.com/view?r=eyJrIjoiY2Y2YWVkMmItYWU2Yi00OGNjLWE3MmQtMTg4MDM3MGIwY2NlIiwidCI6IjkwYjY0ZWVlLTg0M2UtNDBiZi04ODZkLWZjMmMxNDk2NjE3NiIsImMiOjEwfQ%3D%3D',
            style={'height': '100vh', 'width': '100%'}
        )
    ]
)