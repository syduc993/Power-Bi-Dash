import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash_auth

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SPACELAB])

VALID_USERNAME_PASSWORD_PAIRS = {
    'admin': '123456',
    'procurement': 'password'
}

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)


SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

sidebar = html.Div(
    [
        html.H2("Menu", className="display-4",style={'color': '#4F73B8'}),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Procurement",href="/",active="partial", id="procurement-link"),
                dbc.Collapse(
                    dbc.Nav([
                        dbc.NavLink("Tháng 9 - 2023", href="/procurement/item9", active="exact"),
                        dbc.NavLink("Tháng 10 - 2023", href="/procurement/item10", active="exact"),
                        # Thêm các mục menu khác nếu cần
                    ], vertical=True, pills=True),
                    id="procurement-collapse",
                    is_open=False,  # Đặt mặc định là False để ẩn Procurement Collapse ban đầu
                ),
                dbc.NavLink("Store", href="/store/item1", active="exact"),
            ],
            vertical=True,
            pills=True,
            className="bg-light",
        )
    ],
    style=SIDEBAR_STYLE,
)


app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.Div("Tổng hợp báo cáo Procurement",
                         style={'fontSize': 50, 'textAlign': 'right','color': '#4F73B8', 'paddingRight': '280px','height': '98px'}))
    ]),

    html.Hr(),

    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            dbc.Col(
                [
                    dash.page_container
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    )
], fluid=True)


@app.callback(
    Output("procurement-collapse", "is_open"),
    [Input("procurement-link", "n_clicks")],
    [State("procurement-collapse", "is_open")]
)
def toggle_procurement_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


if __name__ == "__main__":
    app.run(debug=False)