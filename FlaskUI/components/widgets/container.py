from FlaskUI.src.helper_functions import formatedStyleProperties, getRandomId
from FlaskUI import FlaskUI

class Container:
  def __init__(self, html='', id=''):
    self._components = {}
    self._style_properties = {}
    self.html = html
    self.id = id
    self.type = "container"

  def __getHtml(self):
    return "<div id='{}' style='{}'>{}</div>".format(self.id, formatedStyleProperties(self._style_properties), "".join(self._components.values()))

  def _add(self, component):
    self._components[component.id] = component.html

  def style(self, **kwargs):
    for key, value in kwargs.items():
      self._style_properties[key] = value
    return self
  
  def render(self, app: FlaskUI, id=None):
    if id is None:
      id = getRandomId()
    self.id = id
    self.html = self.__getHtml()
    app._add(self)