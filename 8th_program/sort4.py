def quick_sort(bookings):
    if len(bookings) <= 1:
        return bookings

    pivot = bookings[-1][3]

    left = []
    right = []

    for booking in bookings[:-1]:
        if booking[3] <= pivot:
            left.append(booking)
        else:
            right.append(booking)

    return quick_sort(left) + [bookings[-1]] + quick_sort(right)


n = int(input("Enter number of bookings: "))

bookings = []

for i in range(n):
    print("\nBooking", i + 1)

    booking_id = int(input("Enter Booking ID: "))
    name = input("Enter Customer Name: ")
    movie = input("Enter Movie Name: ")
    tickets = int(input("Enter Number of Tickets: "))

    bookings.append([booking_id, name, movie, tickets])


result = quick_sort(bookings)

print("\n--- Sorted Booking Details ---")

for b in result:
    print(
        "ID:", b[0],
        "| Name:", b[1],
        "| Movie:", b[2],
        "| Tickets:", b[3]
    )
