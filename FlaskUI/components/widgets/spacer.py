from FlaskUI.src.helper_functions import formatedStyleProperties, getRandomId
from FlaskUI import FlaskUI

class Spacer:
  def __init__(self, html='', id=''):
    self._style_properties = {}
    self.html = html
    self.id = id
    self.type = "spacer"

  def __getHtml(self):
    return "<div id='{}' style='{}'></div>".format(self.id, formatedStyleProperties(self._style_properties))

  def style(self, **kwargs):
    for key, value in kwargs.items():
      self._style_properties[key] = value
    return self
  
  def render(self, app=None, id=None):
    if id is None:
      id = getRandomId()
    self.id = id
    self.html = self.__getHtml()
    if app is not None:
      app._add(self)
    else:
      return self