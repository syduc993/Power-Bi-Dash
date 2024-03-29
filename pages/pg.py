import dash
from dash import dcc, html

dash.register_page(__name__, path='/', name='Procurement')

layout = html.Iframe(
    #src='https://app.powerbi.com/view?r=eyJrIjoiMzAwN2E3YTEtNjdkZS00NWNkLWJkZDEtOTIyMzIzNDkwNzJlIiwidCI6IjkwYjY0ZWVlLTg0M2UtNDBiZi04ODZkLWZjMmMxNDk2NjE3NiIsImMiOjEwfQ%3D%3D',
    src='https://app.powerbi.com/view?r=eyJrIjoiMTkzZjU2ZWYtYmNkMC00YmM2LTkzNTUtOTU5YjMxYjQ2ZjY2IiwidCI6IjkwYjY0ZWVlLTg0M2UtNDBiZi04ODZkLWZjMmMxNDk2NjE3NiIsImMiOjEwfQ%3D%3D',
    style={
        'height': '95vh',
        'width': '100%',
        'position': 'relative',
        'zIndex': '1000',
        'transform': 'translateY(-10px)',
        'backgroundColor': 'white',
        'clipPath': 'polygon(0% 0%, 100% 0%, 100% calc(100% - 60px), 0% calc(100% - 60px))',
        'margin': 'auto auto auto 0'
    }
)