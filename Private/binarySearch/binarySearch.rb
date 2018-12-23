# binary search in ruby
require 'backports/2.0.0/array/bsearch'

arr=[1,2,8,2,5,4,2,5,8,3,2,6,8,1]
n=4

def binary_search(array, number)
  sorted = array.sort
  if array.include?(number)
    puts true
    puts array.index(number)
  elsif
    puts false
  end
end
binary_search(arr, n)

p arr.bsearch(n);