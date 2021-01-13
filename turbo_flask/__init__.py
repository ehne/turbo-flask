from flask import current_app
from jinja2 import Markup as M


class Turbo:
    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        self.app = app

        self.app.template_global("turbo_js")(self.turbo_js)

    def turbo_js(self):
        return M(
            """
            <script type="module">
                addEventListener("load", () => import("https://cdn.skypack.dev/@hotwired/turbo?min"))
            </script>
            """
        )