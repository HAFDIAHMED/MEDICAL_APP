import shifaa.db.models as models


#######
# A list of constant that we'll be used inside the database

class BaseConstantClass:
    _name = 'base_class'
    _class_source = None

    # TODO : Search for better syntax

    def get_name(self):
        return self._name

    def get_class_source(self):
        """
        # TODO : Find a better naming here
        The class used to instantiate the constant
        """
        return self._class_source


CONSTANTS = []
