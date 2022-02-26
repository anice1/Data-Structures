class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


cookie_1 = Cookie('green')
cookie_2 = Cookie('blue')

print('Cookie 1 is :', cookie_1.get_color())
print('Cookie 2 is :', cookie_2.get_color())

# set cookie colors
cookie_1.set_color('red')
cookie_2.set_color('yellow')

print()
print('Cookie 1 is now :', cookie_1.get_color())
print('Cookie 2 is now :', cookie_2.get_color())
