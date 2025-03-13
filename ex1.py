def ex1(num):
    if num <= 1:
        return 1
    return num * ex1(num - 1)
  
print(ex1(5))
