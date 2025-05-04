import sys
import stdio

user_input = sys.stdin.read().strip().replace("'", "").split(",")

for i in range(len(user_input)):
    if i % 10 == 0:
        stdio.writeln()
    stdio.writef('%3d  ', int(user_input[i]))