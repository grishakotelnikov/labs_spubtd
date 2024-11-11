from PIL import Image

def crop_image(image_path, crop_area):
    image = Image.open(image_path)
    cropped_image = image.crop(crop_area)
    cropped_image.show()
    cropped_image.save('cropped_cat.jpg')

crop_area = (50, 50, 300, 300)
crop_image('cat2.jpg', crop_area)
