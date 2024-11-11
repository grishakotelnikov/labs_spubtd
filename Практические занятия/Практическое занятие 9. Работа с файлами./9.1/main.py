import os
from pathlib import Path
from PIL import Image

input_folder = '/home/g/PycharmProjects/labs_spubtd/Практические занятия/Практическое занятие 9. Работа с файлами./9.1/input_images'
output_folder = '/home/g/PycharmProjects/labs_spubtd/Практические занятия/Практическое занятие 9. Работа с файлами./9.1/output_images'

Path(output_folder).mkdir(parents=True, exist_ok=True)

def process_image(input_path, output_path):
    with Image.open(input_path) as img:
        img = img.resize((800, 800))
        img.save(output_path)

for file in os.listdir(input_folder):
    input_path = os.path.join(input_folder, file)
    if os.path.isfile(input_path):
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            output_path = os.path.join(output_folder, file)
            process_image(input_path, output_path)
            print(f"Изображение обработано: {file}")

process_image(input_path, output_path)