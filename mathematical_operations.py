def  print_grades(grades_input):
  grades_input.sort()
  for grade in grades_input:
    print grade
    
def grades_sum(scores):
  total = 0
  for mark in scores:
    total = total + mark
  return total
  

def grades_mean(scores):
  mean = grades_sum(scores) / float(len(scores))
  return mean
  

def grades_median(marks):
  marks.sort()
  if len(marks) % 2 == 0:
    median = float(marks[len(marks)/2] + marks[(len(marks)/2) +1] / 2)
  else:
    median = marks[(len(marks)+1)/2]
  return median
  

def grades_mode(marks):
  marks.sort()
  i_grade = 0
  i_number = 0
  count = 0
  for grade in marks:
    count = marks.count(grade)
    if count > i_number:
      i_number = count
      i_grade = grade
  mode = i_grade
  return mode 
  
def grades_variance(scores):
  average = grades_mean(scores)
  variance = 0
  for score in scores:
    variance = variance + ((average - score)**2)
  return (variance/float(len(scores)))
  

def grades_std_deviation(variance):
  return (variance ** 0.5)
  
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

print_grades(grades)
print "Sum of grades: %.2f" % (grades_sum(grades))
print "Mean of grades: %.2f" % (grades_mean(grades))
print "Median of grades: %.2f" % (grades_median(grades))
print "Mode of grades: %d" % (grades_mode(grades))
print "Grades variance: %.2f" % (grades_variance(grades))
variance = grades_variance(grades)
print "Standard deviation of grades: %.2f" % (grades_std_deviation(variance))