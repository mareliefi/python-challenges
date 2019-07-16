import mathematical_operations

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

mathematical_operations.print_grades(grades)
print "Sum of grades: %.2f" % (mathematical_operations.grades_sum(grades))
print "Mean of grades: %.2f" % (mathematical_operations.grades_mean(grades))
print "Median of grades: %.2f" % (mathematical_operations.grades_median(grades))
print "Mode of grades: %d" % (mathematical_operations.grades_mode(grades))
print "Grades variance: %.2f" % (mathematical_operations.grades_variance(grades))
variance = mathematical_operations.grades_variance(grades)
print "Standard deviation of grades: %.2f" % (mathematical_operations.grades_std_deviation(variance))