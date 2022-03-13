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
