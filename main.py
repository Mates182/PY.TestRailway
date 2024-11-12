from fasthtml.common import *

app, rt = fast_app()

@rt('/change')
def get(): return P('Nice to be here!')

@rt("/")
def get():
    return Titled(P("Welcome, This page is deployed on Railway"), hx_get="/change")

H2("By: Mateo Pillajo :D")

serve()
