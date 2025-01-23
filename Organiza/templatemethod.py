from abc import ABC, abstractmethod

class BaseLayout():

    def header(self):
        pass
    
    @abstractmethod
    def body(self):
        pass

    def footer(self):
        pass

    def render(self):
        self.header()
        self.body()
        self.footer()