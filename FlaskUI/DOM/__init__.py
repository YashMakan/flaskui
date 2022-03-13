from collections import namedtuple
from FlaskUI import FlaskUI
from bs4 import BeautifulSoup
from FlaskUI.components import Container, Text
from FlaskUI.src.helper_functions import deFormatedStyleProperties

class DOM:
  def __init__(self, app: FlaskUI):
    self.app = app

class Element:
  def __init__(self):
    pass