import stdio

counter = 0
tracker = 0
highestCount = 0
highestCountTracker = 0
nums = []

while not stdio.isEmpty():
    num = stdio.readInt()
    nums.append(num)

for i in range(len(nums)):
    if counter == 0:
        tracker = nums[i]
        counter += 1
        highestCount += 1
        highestCountTracker += 1
        continue
    if tracker == nums[i]:
        counter += 1

        if (i != len(nums) - 1):
            continue
    if counter > highestCount:
        highestCountTracker = tracker
        highestCount = counter
        counter = 1
        tracker = nums[i]
        continue
    if counter <= highestCount:
        counter = 1
        tracker = nums[i]
        continue
stdio.writeln("Longest run: " + str(highestCount) + " consecutive " + str(highestCountTracker) + "s")
