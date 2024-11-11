from PIL import Image

image = Image.open('cat.png')

width, height = image.size

image_resized = image.resize((width // 3, height // 3))

image_horizontal_mirror = image.transpose(Image.FLIP_LEFT_RIGHT)

image_vertical_mirror = image.transpose(Image.FLIP_TOP_BOTTOM)

image_resized_rgb = image_resized.convert('RGB')
image_horizontal_mirror_rgb = image_horizontal_mirror.convert('RGB')
image_vertical_mirror_rgb = image_vertical_mirror.convert('RGB')

image_resized_rgb.save('resized_image.jpg')
image_horizontal_mirror_rgb.save('horizontal_mirror_image.jpg')
image_vertical_mirror_rgb.save('vertical_mirror_image.jpg')

image_resized_rgb.show()
image_horizontal_mirror_rgb.show()
image_vertical_mirror_rgb.show()
