from flet_mvc import FletController


class Controller(FletController):
    def example_function(self, e=None):
        if self.model.example() == "Flet":
            self.model.example.set_value("Hello")
        else:
            self.model.example.set_value("Flet")

        self.update()
