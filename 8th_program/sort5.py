def quick_sort(bookings):
    if len(bookings) <= 1:
        return bookings

    pivot = bookings[0][4]

    low = []
    high = []

    for booking in bookings[1:]:
        if booking[4] <= pivot:
            low.append(booking)
        else:
            high.append(booking)

    return quick_sort(low) + [bookings[0]] + quick_sort(high)


n = int(input("Enter number of bookings: "))

bookings = []

for i in range(n):
    print("\nBooking", i + 1)

    booking_id = int(input("Booking ID: "))
    customer = input("Customer Name: ")
    movie = input("Movie Name: ")
    tickets = int(input("Number of Tickets: "))
    price = int(input("Price per Ticket: "))

    total = tickets * price

    bookings.append([
        booking_id,
        customer,
        movie,
        tickets,
        total
    ])


result = quick_sort(bookings)

print("\n--- Movie Ticket Booking Details ---")
print("ID\tCustomer\tMovie\tTickets\tTotal")

for b in result:
    print(
        b[0], "\t",
        b[1], "\t\t",
        b[2], "\t",
        b[3], "\t",
        b[4]
    )
