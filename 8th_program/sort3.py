def quick_sort(bookings):
    if len(bookings) <= 1:
        return bookings

    pivot = bookings[0]

    smaller = [x for x in bookings[1:] if x[0] < pivot[0]]
    greater = [x for x in bookings[1:] if x[0] >= pivot[0]]

    return quick_sort(smaller) + [pivot] + quick_sort(greater)


bookings = [
    [105, "Ravi", "Leo", 2],
    [102, "Arun", "Jailer", 3],
    [108, "Priya", "Vikram", 1],
    [101, "Kumar", "Beast", 4]
]

sorted_bookings = quick_sort(bookings)

print("Bookings sorted by Booking ID:")

for b in sorted_bookings:
    print(
        "Booking ID:", b[0],
        "| Customer:", b[1],
        "| Movie:", b[2],
        "| Tickets:", b[3]
    )
