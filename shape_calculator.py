class Rectangle:
    width: int
    height: int

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def set_width(self, width: int):
        self.width = width

    def set_height(self, height: int):
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):

        output: str = ""
        if self.width > 50 or self.height > 50:
            output = "Too big for picture."
        
        else:
            for i in range(self.height):
                output += self.width * "*" + "\n"
            
        return output

    def get_amount_inside(self, shape):
        area_shape = shape.get_area()
        area_self = self.get_area()

        return area_self // area_shape

class Square(Rectangle):
    side: int

    def __init__(self, side: int):
        self.width = side
        self.height = side
        self.side = side

    def __repr__(self):
        return f"Square(side={self.width})"

    def set_side(self, side: int):
        self.width = side
        self.height = side

    def set_width(self, width: int):
        self.width = width
        self.height = width
        self.side = width
    
    def set_height(self, height: int):
        self.width = height
        self.height = height
        self.side = height

    
