from dash import Dash, Input, Output
import dash_leaflet as dl
from dash_extensions.enrich import html, DashProxy
import dash_bootstrap_components as dbc



# Some shapes.
markers = dl.Marker(position=[56, 10])
circle = dl.CircleMarker(center=[55, 10])
polygon = dl.Polygon(positions=[[57, 10], [57, 11], [56, 11], [57, 10]])

# Some tile urls.
keys = ["watercolor", "toner", "terrain"]
url_template = "http://{{s}}.tile.stamen.com/{}/{{z}}/{{x}}/{{y}}.png"
attribution = 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, ' \
              '<a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data ' \
              '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'

# Create aempy map.
app = Dash()
app.layout = html.Div([dbc.Switch(id="markerswitch", value=False, label="Markers"),
                       dbc.Switch(id="circleswitch", value=False, label="Circle"),
                       dbc.Switch(id="polygonswitch", value=False, label="Polygon"),
                       dl.Map([
                            dl.LayersControl(
                                [dl.BaseLayer(dl.TileLayer(url=url_template.format(key), attribution=attribution),
                                              name=key, checked=key == "toner") for key in keys]
                            , id="layercontrol", collapsed=False)],
                            zoom=7, center=(56, 10))],
                            style={'width': '100%', 'height': '50vh', 'margin': "auto", "display": "block"}
                      )


@app.callback(
    Output("layercontrol", "children"),
    Input("markerswitch", "value"),
    Input("circleswitch", "value"),
    Input("polygonswitch", "value")
)
def update_output_src(markerswitch, circleswitch, polygonswitch):
    baselayers = [dl.BaseLayer(dl.TileLayer(url=url_template.format(key), attribution=attribution),
                                              name=key, checked=key == "toner") for key in keys]

    overlays = []

    if markerswitch is True:
        overlays.append(
            dl.Overlay(dl.LayerGroup(markers), name="markers", checked=True)
        )

    if circleswitch is True:
        overlays.append(
            dl.Overlay(dl.LayerGroup(circle), name="circle", checked=True)
        )

    if polygonswitch is True:
        overlays.append(
            dl.Overlay(dl.LayerGroup(polygon), name="polygon", checked=True)
        )

    finalayers = baselayers + overlays

    return finalayers

if __name__ == '__main__':
    app.run_server()