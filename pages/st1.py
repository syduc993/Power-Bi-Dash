import dash
from dash import dcc, html
import plotly.graph_objs as go
import numpy as np

dash.register_page(__name__, path='/store/item1', name='Procurement')

layout = html.Div(
    [
        dcc.Markdown('# Liên hệ user 201353 để oder chức năng - 500k/Task!')
    ]
)

# Tạo dữ liệu giả tưởng
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

layout = html.Div(
    [
        dcc.Graph(
            id='3d-graph',
            figure={
                'data': [
                    go.Surface(
                        x=x,
                        y=y,
                        z=Z,
                        colorscale='Viridis',  # Màu sắc của biểu đồ
                        contours=dict(
                            z=dict(show=True, usecolormap=True, highlightcolor="limegreen", project=dict(z=True))
                        ),  # Vẽ đường contour
                        colorbar=dict(title='Độ cao'),  # Tiêu đề của colorbar
                    )
                ],
                'layout': go.Layout(
                    title='Biểu đồ 3D',
                    scene=dict(
                        xaxis=dict(title='Trục X'),
                        yaxis=dict(title='Trục Y'),
                        zaxis=dict(title='Trục Z'),
                    )
                )
            }
        )
    ]
)