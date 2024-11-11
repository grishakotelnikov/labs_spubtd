def is_lucky_ticket(ticket_number):
    ticket_number = ticket_number.strip()
    half_length = len(ticket_number) // 2
    first_half = sum(int(digit) for digit in ticket_number[:half_length])
    second_half = sum(int(digit) for digit in ticket_number[half_length:])

    if first_half == second_half:
        print("Билет счастливый!")
        return True
    else:
        print("Билет не счастливый.")
        return False


ticket_number = input("Введите номер билета: ")
is_lucky_ticket(ticket_number)
