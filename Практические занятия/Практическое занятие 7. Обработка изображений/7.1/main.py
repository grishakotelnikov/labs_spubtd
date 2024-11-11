from PIL import Image

image = Image.open('cat.png')

image.show()

width, height = image.size
format = image.format
mode = image.mode

print(f"Размер изображения: {width}x{height}")
print(f"Формат изображения: {format}")
print(f"Цветовая модель: {mode}")
