from FlaskUI.src.helper_functions import formatedStyleProperties, getRandomId

class Column:
  def __init__(self, children: list):
    self.children = children
    self.html = ""
    self.id = ""
    self.type = "column"
    self._style_properties = {}

  def __getHtml(self):
    bodyText = "\n".join([child.html for child in self.children])
    return "<div style='display: grid;grid-template-columns:repeat(1, 1fr){}' id='{}'>{}</div>".format(formatedStyleProperties(self._style_properties), self.id, bodyText)

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
