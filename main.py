from FlaskUI import FlaskUI
from FlaskUI.components import Container, Text, Link, Column, Spacer
from FlaskUI.DOM import DOM

app = FlaskUI(__name__)

@app.route("/")
def homePage():
  container = Container()
  Column(children=[
    Text("Hello Page").style(color="red").render(),
    Spacer().style(height="20px").render(),
    Link("Hello Page2", url="").style(color="blue").render()
  ]).render(container)
  container.render(app)

@app.route("/login")
def homePage():
  container = Container().style(backgroundColor="red")
  Text("Login Page").style(color="blue").render(container, "login1")
  Link("Login Page2", url="").style(color="blue").render(container, "login2")
  container.render(app, "login1")

app.run(debug=True, hotReload=False)