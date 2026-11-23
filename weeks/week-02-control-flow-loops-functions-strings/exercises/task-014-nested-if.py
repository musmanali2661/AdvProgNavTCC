"""Task 14: Nested if (Week 2)."""

# Nested if statement
i = 10
if i == 10:
    if i < 15:
        print("i is smaller than 15")
    # Only executed if the statement above is true
    if i < 12:
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")
