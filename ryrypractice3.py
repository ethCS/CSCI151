#what is the result on iteration 7 when n=10

n=10

def sequence_maker(n):
    result = 0
    counter = 1

    while counter <= n:
        if counter % 3 == 0:
            result = result + (counter * 2)
        else:
            result = result + counter

        print(f"Iteration {counter}: result = {result}")
        counter += 1

    return result

print(sequence_maker(n))
