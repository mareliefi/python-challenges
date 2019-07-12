def haiku_checker():
  line_1 = raw_input("First line of your haiku:").split(" ")
  line_2 = raw_input("Second line of your haiku:").split(" ")
  line_3 = raw_input("Third line of your haiku:").split(" ")
  vowel = "aeiouyAEIOUY"
  syllable2 = "aiouyAIOUY"
  total_1 = 0
  total_2 = 0
  total_3 = 0

  for item in line_1:
    if len(item) == 1:
      total_1 += 1
    else:
      if item[0] in vowel:
        total_1 += 1
      for i in range(1, len(item)):
        if item[i] in vowel and item[i-1] not in vowel:
          total_1 += 1
      if item[len(item)-1] == "e" or item[len(item)-1] == "E":
        total_1 -= 1    
  print "Syllables in line 1: %d" % total_1     
        
  for item in line_2:
    if len(item) == 1:
      total_2 += 1
    else:
      if item[0] in vowel:
        total_2 += 1
      for i in range(1, len(item)):
        if item[i] in vowel and item[i-1] not in vowel:
          total_2 += 1
      if item[len(item)-1] == "e" or item[len(item)-1] == "E":
        total_2 -= 1 
  print "Syllables in line 2: %d" % total_2        

  for item in line_3:
    if len(item) == 1:
      total_3 += 1
    else:
      if item[0] in vowel:
        total_3 += 1
      for i in range(1, len(item)):
        if item[i] in vowel and item[i-1] not in vowel:
          total_3 += 1
      if item[len(item)-1] == "e" or item[len(item)-1] == "E":
        total_3 -= 1 
  print "Syllables in line 3: %d" % total_3     
          

  if total_1 == 5 and total_2 == 7 and total_3 == 5:
    print "This is a haiku"
  else:
    print "This is not a haiku as the correct syllables per line has not been met"

haiku_checker()

