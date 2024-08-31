a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[9,8,7],[6,5,4],[3,2,1]]
c = [[0 for _ in range(3)] for _ in range(3)]

def ShowArrays(array):
  for i in array:
    for j in i:
      print(j)

def suma(a,b,c):
  for i in range(3):
    for j in range(3):
      c[i][j] = a[i][j] + b[i][j]
      
def resta(a,b,c):
  for i in range(3):
    for j in range(3):
      c[i][j] = a[i][j] - b[i][j]

def multip(a,b,c):
  for i in range(3):
    for j in range(3):
      c[i][j] = (a[i][0] * b[0][j]) + (a[i][1]*b[1][j]) + (a[i][2] * b[2][j])

#suma(a,b,c)
#resta(a,b,c)
multip(a,b,c)
print(c)
