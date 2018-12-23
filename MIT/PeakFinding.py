class Algorithms():

  def PeakFinder(self, arr):
    arr = [-10**10] + arr
    arr.append(-10**10)
    peaks = []
    for x in range(1, len(arr) - 1):
      if arr[x - 1] <= arr[x] and arr[x] >= arr[x + 1]:
        peaks.append(arr[x])
    return peaks
    


test = Algorithms()

print(test.PeakFinder([6,7,4,3,2,1,4,5]))