from Engine.Entity import Entity


class Mission(Entity):
    """
    A mission on the game field
    """

    def __init__(self, x, y, width, height,  name, heading=0):
        """
        :param x: The x position of the mission
        :param y: The y position of the mission
        :param width: The width of the mission
        :param height: The height of the mission
        :param texture_path: The texture path to mission texture
        :param name: The name of the mission
        :param heading: The rotation of the mission
        """
        super(Mission, self).__init__(x, y, width, height, "", heading)
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def __str__(self):
        return f"Mission {self._name}, width {self.w}, height {self.h}"

    def update(self):
        pass
