"""
Question:
Explain how you would sort a 20 GB file with one string per line.

Solution:
External Sort
We can implement a variation of merge sort.
We will need to chunk the file into reasonable sizes that fit in memory.
We will sort and save each
After all chunks are sorted, we can merge the sorted chunks, one by one

Other thoughts:
MapReduce?
"""