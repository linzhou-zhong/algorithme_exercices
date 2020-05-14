def findDuplicate(nums):
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]

        print(str(tortoise) + " " + str(hare))

        if tortoise == hare:
            break

    mu = 0
    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]   # Hare and tortoise move at same speed
        mu += 1
    print(mu)

findDuplicate([5,1,2,3,4,2])

# https://cs.stackexchange.com/questions/10360/floyds-cycle-detection-algorithm-determining-the-starting-point-of-cycle