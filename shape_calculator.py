class Rectangle:
    def __init__(self, width_var, height_var):
        self.width = width_var
        self.height = height_var

    def __str__(self):
        return 'Rectangle(width={}, height={})'.format(self.width, self.height)

    def set_width(self, width_var):
        self.width = width_var
        return self.width

    def set_height(self, height_var):
        self.height = height_var
        return self.height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = (self.width + self.height) * 2
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return diagonal

    def get_picture(self):
        picture = []
        line = 1
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        while line <= self.height:
            if line == self.height:
                picture.append('*' * self.width + '\n')
            else:
                picture.append('*' * self.width)
            line += 1
        return '\n'.join(picture)

    def get_amount_inside(self, rectangle):
        amount = self.get_area() // rectangle.get_area()
        return amount


class Square(Rectangle):

    def __init__(self, side_var, width_var=0, height_var=0):
        super().__init__(width_var, height_var)
        self.height, self.width, self.side = side_var, side_var, side_var

    def __str__(self):
        return 'Square(side={})'.format(self.side)

    def set_side(self, side_var):
        self.side, self.width, self.height = side_var, side_var, side_var
        return self.side, self.width, self.height
    
    def set_width(self, width_var):
        self.side, self.width, self.height = width_var, width_var, width_var
        return self.side, self.width, self.height
    
    def set_height(self, height_var):
        self.side, self.width, self.height = height_var, height_var, height_var
        return self.side, self.width, self.height        
