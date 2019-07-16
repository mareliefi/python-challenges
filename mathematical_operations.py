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
  mean = round(grades_sum(scores) / float(len(scores)),2)
  return mean
  
def grades_median(marks):
  marks = sorted(marks)
  lstLen = len(marks)
  index = (lstLen - 1) // 2
  if (lstLen % 2):
    return marks[index]
  else:
    return (marks[index] + marks[index + 1])/2.0

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
    variance += (average - score)**2
  variance = round(variance,2)  
  return variance

def grades_std_deviation(variance):
  std_deviation = variance ** 0.5
  return round(std_deviation,2)
  
