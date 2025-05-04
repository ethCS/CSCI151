import stdio

def Q2(n):
   if (n <= 0):
      return 1
   return 1 + Q2(n-2) + Q2(n-3)

stdio.writeln(Q2(4))

#iteration1: 1 + q2(2) + q2(1)
#iteration2: 1 + q2(0) + q2(-1)