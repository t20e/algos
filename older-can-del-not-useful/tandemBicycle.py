# A tandem bicycle is a bicycle that's operated by two people: person A and person В. Both people pedal the bicycle, but the
#  person that pedals faster dictates the speed of the bicycle. So if person A pedals at a speed of 5 and person В pedals at a
#  speed of 4 S , the tandem bicycle moves at a speed of
#                                                        5 (i.e., tandemSpeed = max (speedA, speedB)

# pair redShirts and blueShirts, the one with a higher int value is considered the faster on and makes the bicycle faster
# MY SOLUTION
# def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
#     # Write your code here.
#     if fastest:
#         maxTotalSpeed = 0
#         redShirtSpeeds.sort(reverse=True)
#         blueShirtSpeeds.sort()
#         for idx in range(0, len(redShirtSpeeds)):
#             maxTotalSpeed += max(redShirtSpeeds[idx], blueShirtSpeeds[idx])
#             # return the maximum possible total speed which multiples the total speed fo the all the fastest riders
#         return maxTotalSpeed
#     else:
#         minTotalSpeed = 0
#         redShirtSpeeds.sort(reverse=True)
#         blueShirtSpeeds.sort(reverse=True)
#         for idx in range(0, len(redShirtSpeeds)):
#             print(redShirtSpeeds[idx])
#             minTotalSpeed += max(redShirtSpeeds[idx], blueShirtSpeeds[idx])
#             # return the maximum possible total speed which multiples the total speed fo the all the fastest riders
#         return minTotalSpeed


# SOMEONE ELSES SOLUTION
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    if not fastest:  # checks if fastest is False
        # reverse one of the arrays if fastest is false which means we are returning the minimum possible total
        # which is us pairing all the high values from the arrays together
        # else pair the high values from one array to the min values from the other array
        reverseArrayInPlace(redShirtSpeeds)
    totalSpeed = 0
    for idx in range(0, len(redShirtSpeeds)):
        rider1 = redShirtSpeeds[idx]
        rider2 = blueShirtSpeeds[len(blueShirtSpeeds)-idx-1]
        totalSpeed += max(rider1, rider2)
    return totalSpeed

def reverseArrayInPlace(array):  # instead of using the .sort()
    start = 0
    end = len(array) - 1
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
    return array


redShirtSpeeds = [5, 5, 3, 9, 2]
blueShirtSpeeds = [3, 6, 7, 2, 1]
fastest = True

print(tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest))
