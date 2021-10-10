
# CP Lab 7
# Hitesh Kumar Sharma
# 189876


def getMinMax(arr):
	
	n = len(arr)
	
	
	if(n % 2 == 0):
		mx = max(arr[0], arr[1])
		mn = min(arr[0], arr[1])
		
		# set the starting index for loop
		i = 2
		
	
	else:
		mx = mn = arr[0]
		
		
		i = 1
		

	while(i < n - 1):
		if arr[i] < arr[i + 1]:
			mx = max(mx, arr[i + 1])
			mn = min(mn, arr[i])
		else:
			mx = max(mx, arr[i])
			mn = min(mn, arr[i + 1])
			
	
		i += 2
	
	return (mx, mn)

if __name__ =='__main__':
	
	arr = [1, 3, 5, 2, 10, 0]
	mx, mn = getMinMax(arr)
	print("Minimum element is", mn)
	print("Maximum element is", mx)

