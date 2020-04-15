print("-------------------Turn up the Temperature-------------------")
print("")

#define the function called f_to_c 
def f_to_c(f_temp):
  return (f_temp - 32) * 5/9
print("Converting 70 Fahrenheit to celsius: ")
print(f_to_c(70))
print()
print()

#Define the var f100_in_celsius and set it equal to the value of f_to_c with 100 as input
print("Converting 100 Fahrenheit to celsius: ")
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)
print()
print()

#Define function c_to_f has a input of temp in celsius and converts it into Fahrenheith
def c_to_f(c_temp):
  return (c_temp * (9/5)) + 32
print("Converting 0 Celsius in to Fahrenheit: ")
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit) 
print("")
print("")

print("-------------------USE THE FORCE--------------------------")
print("")
#define the function get_force that takes in mass and acceleration. and returns mass multiplied by acceleration
print("Force is mass multiplied by acceleration")
print("")




train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)

print ("The GE train supplies " + str(train_force) + " Newtons of force." )
print(train_force)
print("-------------------USE THE FORCE | Get energy --------->")
print("")

#Defining the function get_energy that taks in mass and c.
#Default value  c is 3 * 1^8
def get_energy(mass, c = 3 * 10**8):
  return mass * c**2

bomb_energy = get_energy(bomb_mass)

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")
print("")
print("-------------------Do the Work--------------------------")


#Defining get_work and take in mass, acceleration, and distance.
def get_work(mass, acceleration, distance):
  #Using get_force function and calculate the force and save
  force = get_force(mass, acceleration)

  return force * distance
  # step 12 Test get_work by using it on train_mass, train_acceleration, and train_ distance
  # and save the result to var train_work

train_work = get_work(train_mass, train_acceleration, train_distance)
#Print the string
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")

# Test function

def force(mass, acceleration):
	force_val = mass*acceleration
	return force_val

test_force = force(10, 9.81)

print("This is testing a new function called force and the force for that is: " + str(test_force) + "")

print("Hello World")


print(" <----------------------------------- Testing challenges ----------------------------------------->")
print("")

#Defining a refresh function 
def some_function(some_input1, some_input2):
	# ...do something with the inputs ...

	return output




print(" <----------------------------------- Testing challenges | Tenth Power----------------------------------------->")



# Write your tenth_power function here:
def tenth_power(s):
	tenth = s **10
	return  tenth

# Uncomment these function calls to test your 
#tenth_power function:
print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024

#s = 2
#p = 10
#print(s**p)


print("<----------------------------------- Testing challenges | Squere_root----------------------------------------->")
print("")


# Write your square_root function here:
def square_root(num):

	num = num**(1/2)
	return num


# Uncomment these function calls to test your square_root function:
print(square_root(16))
# should print 4
print(square_root(100))
# should print 10


print("<----------------------------------- Testing challenges | Win_Percentage----------------------------------------->")
print("")


#Create a function called win_percentage() that takes two parameters named wins and losses.
#This function should return out the total percentage of games won by a team based on these two numbers.
# Write your win_percentage function here:
def win_percentage(win, losses):

	percentage = win/losses

	return percentage, win, losses

# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100


#testing percentage print:







