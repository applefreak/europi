from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from rotary_class import RotaryEncoder

class Display():
    def __init__(self, disp):
        self.disp = disp
        self.dimensions = (disp.width, disp.height)
        self.image = Image.new('1', self.dimensions)
        self.draw = ImageDraw.Draw(self.image)
        self.font = ImageFont.truetype("./DejaVuSansMono.ttf", 10)

    def display_clear(self):
        self.draw.rectangle((0, 0) + self.dimensions, outline = 0, fill = 0)

    def init_display(self):
        self.disp.begin()
        self.disp.clear()
        self.disp.display()
        self.display_clear()

        self.disp.image(self.image)
        self.disp.display()

    def draw_rows(self, rows, inv_col):
        self.display_clear()

        for idx, row in enumerate(rows):
            if inv_col == idx:
                self.draw.rectangle([(0, 10 * idx), (10 * idx + self.dimensions[0], 1 + 10 * idx + 10)], outline = 0, fill = 255)
                self.draw.text((1, 10 * idx), row, font = self.font, fill = 0)
            else:
                self.draw.rectangle([(0, 10 * idx), (10 * idx + self.dimensions[0], 1 + 10 * idx + 10)], outline = 0, fill = 0)
                self.draw.text((1, 10 * idx), row, font = self.font, fill = 255)

        self.disp.image(self.image)
        self.disp.display()

class Menu():
    def __init__(self, disp, encoder, items = []):
        self.items = items
        self.pointer = 0
        self.row = 0
        self.last_row = 0
        self.last_slice = None
        self.disp = Display(disp)
        self.disp.init_display()
        self.draw()

        def encoder_ev (direction):
            if direction == 1:
                self.prev()
            elif direction == 2:
                self.next()
            elif direction == 3:
                self.exec_item()
        self.encoder = RotaryEncoder(encoder["pin1"], encoder["pin2"], encoder["sw"], encoder_ev)

    def draw(self):
        tmp_slice = None
        if self.row == self.last_row:
            if self.last_row == 0:
                tmp_slice = self.items[self.pointer:self.pointer + 3]
            else:
                tmp_slice = self.items[self.pointer - 2:self.pointer + 1]
            self.disp.draw_rows(tmp_slice, self.row)
            self.last_slice = tmp_slice
        else:
            self.disp.draw_rows(self.last_slice, self.row)
        self.last_row = self.row

    def next(self):
        if self.pointer + 1 <= len(self.items) - 1:
            self.pointer += 1
        if self.row < 2:
            self.row += 1
        self.draw()

    def prev(self):
        if self.pointer - 1 >= 0:
            self.pointer -= 1
        if self.row > 0:
            self.row -= 1
        self.draw()

    def exec_item(self):
        print("Item selcted", str(self.pointer))
