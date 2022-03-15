import string, random

def stringToFunction(string):
  return lambda: string

def getRandomId(length=5):
  return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))

def formatedStyleProperties(_style_properties):
    return ";".join(["{}:{}".format(key.replace("_", "-"), value) for key, value in _style_properties.items()])

def deFormatedStyleProperties(style):
  return dict(map(lambda x: x.split(":"), style.split(";")))