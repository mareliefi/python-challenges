
def obtain_n():
  n = raw_input("Enter the amount of terms you wish to have in your sequence (only integers): ")
  if n.isdigit() == False:
    n = 100
  else:
    n = int(n)
  return n


def generate_fibonnaci_up_to_n(n):
  fibo = [0,1]
  i = 2
  new_addition = 0
  if n == 1:
    return fibo[0]
  elif n == 2:
    return fibo
  else:
    while i<n:
      new_addition = fibo[-1]+fibo[-2]
      fibo.append(new_addition)
      i += 1
  return fibo


#n = obtain_n()
#fibonnaci(n)
