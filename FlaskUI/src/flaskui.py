from flask import Flask
from FlaskUI.src.helper_functions import stringToFunction

class FlaskUI:
    def __init__(self, name):
        self._app = Flask(name)
        self._url_mapping = {}
        self._components = {}
        self._html = ""
        self._currentWorkingRoute = ""

    def getHtmlOfPage(self):
        listOfComponents = self._components[self._currentWorkingRoute]
        tempHtml = ""
        for listOfComponent in listOfComponents:
            tempHtml += listOfComponent['component']
        return tempHtml

    def _add(self, component):
        if(self._currentWorkingRoute in self._components):
            self._components[self._currentWorkingRoute].append({"id": component.id, "component": component.html, "type": component.type})
        else:
            self._components[self._currentWorkingRoute] = [{"id": component.id, "component": component.html, "type": component.type}]

    def __runAll(self, hotReload=False, reloadSeconds = 1):
        self._currentWorkingRoute = ""
        for key, value in self._url_mapping.items():
            self._currentWorkingRoute = key
            value()
        for key, value in self._url_mapping.items():
            self._currentWorkingRoute = key
            widgets = self._components[self._currentWorkingRoute]
            tempHtml = ""
            if(hotReload):
                tempHtml = f'<meta http-equiv="refresh" content="{reloadSeconds}" />'
            for widget in widgets:
                tempHtml += widget['component']
            self._app.add_url_rule(key, key, stringToFunction(tempHtml))
        self._currentWorkingRoute = ""

    def route(self, path):
        def route_wrapper(func):
            self._url_mapping[path] = func
        return route_wrapper

    def run(self, debug=False, hotReload=False, reloadSeconds = 1):
        self.__runAll(hotReload, reloadSeconds)
        self._app.run(debug=debug)
        # self.app.run()