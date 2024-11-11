from PIL import Image, ImageDraw, ImageFont


def add_watermark(image_path, watermark_text):
    image = Image.open(image_path).convert("RGBA")
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype("arial.ttf", 36)
    except IOError:
        font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    width, height = image.size
    position = (width - text_width - 10, height - text_height - 10)

    draw.text(position, watermark_text, font=font, fill=(255, 255, 255, 128))

    image.show()
    image.save(f'watermarked_{image_path}')


images = ['1.png', '2.png', '3.png', '4.png', '5.png']
for image_file in images:
    add_watermark(image_file, "Watermark")
