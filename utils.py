import os
from PIL import Image, ImageDraw, ImageFont

def create_text_thumbnail(text, size=(100, 100), bg_color=(200, 200, 200), text_color=(0, 0, 0)):
    img = Image.new('RGB', size, color=bg_color)
    d = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    text_width, text_height = d.textsize(text, font=font)
    position = ((size[0]-text_width)/2, (size[1]-text_height)/2)
    d.text(position, text, fill=text_color, font=font)
    return img

def get_or_create_thumbnail(item_name, thumbnails_dir):
    thumbnail_path = os.path.join(thumbnails_dir, f"{item_name}.png")
    if not os.path.exists(thumbnail_path):
        img = create_text_thumbnail(item_name)
        img.save(thumbnail_path)
    return thumbnail_path