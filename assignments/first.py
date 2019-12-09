name = 'Paul'
age = '39'

def info():
  decades = int(age) // 10
  print('Hello ' + name + '.  You are ' + age + 'years old!')
  print('You have lived for ', decades,' decades')

def combo(x, y):
  print(str(x) + str(y))  


info()
combo(20, True)