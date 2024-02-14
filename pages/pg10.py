import dash
from dash import dcc, html

import dash_html_components as html

dash.register_page(__name__, path='/procurement/item10', name='Procurement')

layout = html.Div(
    [
        html.H1("Sơ yếu lý lịch"),
        html.H2("Thông tin cá nhân"),
        html.P("Họ và tên: Nguyễn Văn A"),
        html.P("Ngày sinh: 01/01/1990"),
        html.P("Địa chỉ: Hà Nội, Việt Nam"),
        html.H2("Quá trình học tập"),
        html.Ul(
            [
                html.Li("2010-2014: Đại học ABC - Khoa Công nghệ thông tin"),
                html.Li("2007-2010: Trung học phổ thông XYZ"),
            ]
        ),
        html.H2("Kinh nghiệm làm việc"),
        html.Ul(
            [
                html.Li("2015-2017: Công ty ABC - Lập trình viên"),
                html.Li("2013-2015: Công ty XYZ - Thực tập sinh"),
            ]
        ),
        html.H2("Kỹ năng"),
        html.Ul(
            [
                html.Li("Python"),
                html.Li("HTML/CSS"),
                html.Li("JavaScript"),
                html.Li("C/C++"),
            ]
        ),
    ]
)
