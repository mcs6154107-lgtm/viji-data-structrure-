def quick_sort(bookings):
    if len(bookings) <= 1:
        return bookings

    pivot = bookings[len(bookings) // 2][1]

    left = [x for x in bookings if x[1].lower() < pivot.lower()]
    middle = [x for x in bookings if x[1].lower() == pivot.lower()]
    right = [x for x in bookings if x[1].lower() > pivot.lower()]

    return quick_sort(left) + middle + quick_sort(right)


bookings = [
    [101, "Ravi", "Leo", 2],
    [102, "Arun", "Jailer", 3],
    [103, "Priya", "Vikram", 1],
    [104, "Kumar", "Beast", 4]
]

result = quick_sort(bookings)

print("Bookings sorted by Customer Name:")

for b in result:
    print(b)
