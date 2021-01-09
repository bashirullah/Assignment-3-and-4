def divide(x, y): 
	try: 
		
		input_val = x // y 
		print("Answer is:", input_val) 
	except ZeroDivisionError: 
		print("Sorry ! Zero error ") 

# Look at parameters and note the working of Program 
divide(5, 0) 
