#!/usr/bin/python3
""" Module base.py: Defines the Base class, which is the foundation for all other model classes. """
import turtle


class Base:
    """
    The foundational class for all other classes in this project.
    It handles the id management, ensuring uniqueness and reducing redundancy in the code.
    """

    __nb_objects = 0  # Tracks the number of created instances

    def __init__(self, id=None):
        """
        Constructor for Base class.

        Parameters:
            id (int, optional): Unique identifier for the instance. If not provided, an auto-generated id is assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON string.

        Parameters:
            list_dictionaries (list): A list containing dictionaries.

        Returns:
            str: JSON string representation of the list_dictionaries.
        """
        import json

        if list_dictionaries is None or not list_dictionaries:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of objects to a JSON file.

        Parameters:
            list_objs (list): A list of Base-inherited instances.
        """
        import json

        filename = cls.__name__ + ".json"
        json_list = [obj.to_dictionary() for obj in list_objs or []]

        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Decodes a list of dictionaries from a JSON string.

        Parameters:
            json_string (str): JSON string of a list of dictionaries.

        Returns:
            list: A list of dictionaries represented by the JSON string.
        """
        import json

        if not json_string:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a new instance with all attributes set from a dictionary.

        Parameters:
            **dictionary (dict): Dictionary of attribute names and values.

        Returns:
            instance: An instance of the class with attributes set from the dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Loads instances from a JSON file.

        Returns:
            list: A list of instances created from the data in the JSON file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_data = file.read()
                dict_list = Base.from_json_string(json_data) if json_data else []
                return [cls.create(**d) for d in dict_list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes instances to a CSV file. """
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", encoding="utf-8") as file:
            fields = ["id", "width", "height", "x", "y"] if cls.__name__ == "Rectangle" else ["id", "size", "x", "y"]

            for obj in list_objs or []:
                csv_data = ",".join(str(getattr(obj, field)) for field in fields)
                file.write(csv_data + "\n")

    @classmethod
    def load_from_file_csv(cls):
        """ Deserializes instances from a CSV file. """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                instance_list = []
                for line in file:
                    line = line.strip()
                    if line:
                        data = line.split(",")
                        obj_data = {field: int(data[i]) for i, field in enumerate(fields)}
                        instance = cls.create(**obj_data)
                        instance_list.append(instance)
                return instance_list
        except FileNotFoundError:
            return []  # Return an empty list if the file doesn't exist

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Visualizes Rectangles and Squares using Turtle graphics. """
        window = turtle.Screen()
        window.title("Drawing Rectangles and Squares")

        for rect in list_rectangles + list_squares:
            pen = turtle.Turtle()
            pen.up()
            pen.goto(rect.x, rect.y)  # Moving to starting position
            pen.down()
            pen.color("black")

            for _ in range(2):
                pen.forward(rect.width)
                pen.left(90)
                pen.forward(rect.height)
                pen.left(90)

            pen.hideturtle()

        window.mainloop()
