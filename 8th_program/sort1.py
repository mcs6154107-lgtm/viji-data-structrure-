def quick_sort(bookings):
    if len(bookings) <= 1:
        return bookings

    pivot = bookings[0][4]

    left = [x for x in bookings[1:] if x[4] <= pivot]
    right = [x for x in bookings[1:] if x[4] > pivot]

    return quick_sort(left) + [bookings[0]] + quick_sort(right)


bookings = [
    [101, "Ravi", "Leo", 2, 300],
    [102, "Arun", "Jailer", 3, 450],
    [103, "Priya", "Vikram", 1, 150],
    [104, "Kumar", "Beast", 4, 600]
]

sorted_bookings = quick_sort(bookings)

print("Bookings sorted by Ticket Price:")
for b in sorted_bookings:
    print("ID:", b[0], "| Name:", b[1],
          "| Movie:", b[2], "| Tickets:", b[3],
          "| Price:", b[4])