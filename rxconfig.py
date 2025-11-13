import reflex as rx
import os

config = rx.Config(
    app_name="pagina_web",
    db_url=os.environ.get(
        "DATABASE_URL", "postgresql://mi_pagina_user:1QXSGYeVql8XEH0jl9ZmFPjM2bCoAVgZ@dpg-d49lmichg0os738t280g-a/mi_pagina"),
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)
