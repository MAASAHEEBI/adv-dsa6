# program to find k'th largest and smallest element

def kthSmallest(arr, n, k):

	# Sort the given array
	arr.sort()

	# Return k'th element in the sorted array
	return arr[k-1]
def kthlargest(arr,n,k):
        arr.sort()
        return arr[n-k]

# Driver code
if __name__=='__main__':
	arr = [12, 3, 5, 7, 19,2]
	n = len(arr)
	k = 1

	print("K'th largest element is",
		kthlargest(arr, n, k))


	print("K'th smallest element is",
		kthSmallest(arr, n, k))

