from FlaskUI import FlaskUI
from FlaskUI.src.helper_functions import formatedStyleProperties, getRandomId

class Text:
  def __init__(self, text: str):
    self.text = text
    self.html = ""
    self.id = ""
    self.type = "text"
    self._style_properties = {}

  def __getHtml(self):
    return "<span style='{}' id='{}'>{}</span>".format(formatedStyleProperties(self._style_properties), self.id, self.text)

  def style(self, **kwargs):
    for key, value in kwargs.items():
      self._style_properties[key] = value
    return self

  def render(self, container, id=None):
    if id is None:
      id = getRandomId()
    self.id = id
    self.html = self.__getHtml()
    container._add(self)

class Link:
  def __init__(self, text: str, url: str):
    self.text = text
    self.link = url
    self.html = ""
    self.id = ""
    self.type = "text"
    self._style_properties = {}

  def __getHtml(self):
    return "<a href='{}' style='{}' id='{}'>{}</a>".format(self.link, formatedStyleProperties(self._style_properties), self.id, self.text)

  def style(self, **kwargs):
    for key, value in kwargs.items():
      self._style_properties[key] = value
    return self

  def render(self, container, id=None):
    if id is None:
      id = getRandomId()
    self.id = id
    self.html = self.__getHtml()
    container._add(self)


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