# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#               Benefit: Add additional logic when read, write, or delete attributes.
#               Gives you getter, setter, and deleter method.

class Rectangle:
    def __init__(self, width, height):
        self._width = width # _name is internal private protected
        self._height = height

    # GETTER METHOD
    @property
    def width(self):
        return f"{self._width:.1f}cm"

    # GETTER METHOD
    @property
    def height(self):
        return f"{self._height:.1f}cm"

    # SETTER METHOD
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than 0")

    # SETTER METHOD
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than 0")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")


def main():
    rectangle = Rectangle(width=10, height=30)
    # SETTERS
    rectangle.width = 190
    rectangle.height = 999
    # GETTERS
    print(rectangle.width)
    print(rectangle.height)
    # DELETE
    del rectangle.width
    del rectangle.height

if __name__ == "__main__":
    main()

# OUTPUT:
# 190.0cm
# 999.0cm
# Width has been deleted
# Height has been deleted
