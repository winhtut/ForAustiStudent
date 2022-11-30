def hours_classes():
    tutes_and_lectures = 10 * 1.5 + 7
    return tutes_and_lectures
def total_hours(num_classes):
    total = hours_classes() * num_classes
    return total
# Ask the user how many classes there are
number_of_classes = int(input('How many classes are there? '))
print('Total Hours: %d.' %total_hours(number_of_classes))