import os
from PIL import Image, ImageFilter

output_folder = 'filtered_images'
os.makedirs(output_folder, exist_ok=True)

images = ['1.png', '2.png', '3.png', '4.png', '5.png']

for image_file in images:
    image = Image.open(image_file)

    filtered_image = image.filter(ImageFilter.CONTOUR)

    new_name = os.path.join(output_folder, f"filtered_{image_file}")
    filtered_image.save(new_name)

    filtered_image.show()
