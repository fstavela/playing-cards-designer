from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class Card:
    MARK_RATIO = 0.25
    FONT_SIZE_RATIO = 0.20

    def __init__(self, bg_color, bg_img_path, mark_img_path, side_marks_pos, central_marks_pos, text="", text_pos=(0, 0), text_font="test-data/times-ro.ttf"):
        self.bg_color = bg_color
        self.bg_img = Image.open(bg_img_path)
        self.mark_img = Image.open(mark_img_path)
        self.side_marks_pos = side_marks_pos
        self.central_marks_pos = central_marks_pos
        self.text = text
        self.text_pos = text_pos
        self.text_font = text_font

    def create_image(self, width, height):
        top = self.generate_half_card(width, height // 2)
        bottom = top.rotate(180)

        card = Image.new("RGB", (width, height), self.bg_color)
        card.paste(top)
        card.paste(bottom, (0, height // 2))
        return card

    def generate_half_card(self, width, height):
        mark_size = int(width * Card.MARK_RATIO)
        mark_img = self.mark_img.resize((mark_size, mark_size))
        bg_img = self.bg_img.resize((width, height))

        card = Image.new("RGB", (width, height), self.bg_color)
        card.paste(bg_img, mask=bg_img)
        for mark_pos in self.side_marks_pos:
            card.paste(mark_img, (int(width * mark_pos[0]), int(height * mark_pos[1])), mark_img)
            card.paste(mark_img, (int(width * (1 - mark_pos[0])) - mark_size, int(height * mark_pos[1])), mark_img)
        for mark_pos in self.central_marks_pos:
            card.paste(mark_img, ((width - mark_size) // 2, int(height * mark_pos)), mark_img)

        draw = ImageDraw.Draw(card)
        font = ImageFont.truetype(self.text_font, int(height * Card.FONT_SIZE_RATIO))
        draw.text((self.text_pos[0] * width, self.text_pos[1] * height), self.text, "black", font)

        return card
