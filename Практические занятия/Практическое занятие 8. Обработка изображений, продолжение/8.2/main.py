from PIL import Image

holiday_cards = {
    "New Year": "new_year.jpg",
    "Christmas": "christmas.jpeg",
    "Birthday": "birthday.jpeg",
}

def display_card(holiday):
    if holiday in holiday_cards:
        image = Image.open(holiday_cards[holiday])
        image.show()
    else:
        print("No card found for this holiday.")

holiday = input("Enter the holiday (New Year, Christmas, Birthday): ")
display_card(holiday)
