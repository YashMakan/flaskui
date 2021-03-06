from FlaskUI.src.helper_functions import formatedStyleProperties, getRandomId

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

  def render(self, container=None, id=None):
    if id is None:
      id = getRandomId()
    self.id = id
    self.html = self.__getHtml()
    if container is not None:
      container._add(self)
    else:
      return self
