def count_down(num):
    if num > 0:
        print(num)
        count_down(num - 1)
  


count_down(20)