import itertools
import csv

# function to read data from csv file an
def read_data():
    with open('testdata.csv', 'rU') as data:
        reader = csv.reader(data)
        for row in reader:
            yield [ float(i) for i in row ]
for i in read_data():
	variable_1 = list(read_data())

variable = list(itertools.chain.from_iterable(variable_1))


#prompting the user to enter the target price
print " Enter Target Value:"
target = float(raw_input())

## Target Price for beyond range, handling that error.
if(target>21.8):
	print("Target Price Beyond Range")
if(target<2.15):
	print("Can't get any item with the price")

## Created different variable names for the target price, since we are iterating through the list of items with all their combinations

target1=target
target2=target
target3=target
target4=target
target5=target

#below was used before reading data from csv file
#variable =[2.15, 2.75, 3.35, 3.55, 4.20, 5.80]

#combination of one item, it basically yields, one item list, with its sum
l1=list(itertools.combinations(variable, 1))
for i in range(len(l1)):
	if(target5 == l1[i][0]):
		print "Yes", l1[i][0]
		lo1 = l1[i][0]

	
#combination of two items, it basically creates multiple items with all their probability combinations and in all their cases evaluates the sum and matches with the target price, if match then prints out the values
l2=list(itertools.combinations(variable, 2))

for i in range(len(l2)):

	if(target == l2[i][0]+l2[i][1]):
		print "Yes", l2[i][0], l2[i][1]
		lo2 = [l2[i][0], l2[i][1]]


#combination of three item,  it basically creates multiple items with all their probability combinations and in all their cases evaluates the sum and matches with the target price, if match then prints out the values

l3= list(itertools.combinations(variable, 3))
for i in range(len(l3)):

	if(target1 == l3[i][0]+l3[i][1]+l3[i][2]):

		print "Yes", l3[i][0], l3[i][1], l3[i][2]
		lo3 = [l3[i][0], l3[i][1], l3[i][2]]


#combination of four item  it basically creates multiple items with all their probability combinations and in all their cases evaluates the sum and matches with the target price, if match then prints out the values

l4= list(itertools.combinations(variable, 4))
for i in range(len(l4)):

	if(target2 == l4[i][0]+l4[i][1]+l4[i][2]+l4[i][3]):

		print "Yes", l4[i][0], l4[i][1], l4[i][2], l4[i][3]
		lo4 = [l4[i][0], l4[i][1], l4[i][2], l4[i][3]]


#combination of five item,  it basically creates multiple items with all their probability combinations and in all their cases evaluates the sum and matches with the target price, if match then prints out the values
l5= list(itertools.combinations(variable, 5))
for i in range(len(l5)):

	if(target3 == l5[i][0]+l5[i][1]+l5[i][2]+l5[i][3]+l5[i][4]):

		print "Yes", l5[i][0], l5[i][1], l5[i][2], l5[i][3], l5[i][4]
		lo5 =[ l5[i][0], l5[i][1], l5[i][2], l5[i][3], l5[i][4] ]




#combination of six item,  it basically creates multiple items with all their probability combinations and in all their cases evaluates the sum and matches with the target price, if match then prints out the values
l6 =list(itertools.combinations(variable, 6))
for i in range(len(l6)):
	
	if(target4 == l6[i][0]+l6[i][1]+l6[i][2]+l6[i][3]+l6[i][4]+l6[i][5]):

		print "Yes", l6[i][0], l6[i][1], l6[i][2], l6[i][3], l6[i][4], l6[i][5]

		lo6 = [ l6[i][0], l6[i][1], l6[i][2], l6[i][3], l6[i][4], l6[i][5] ]


# however we might probably might need to add more combinations, however in our case since we have only 6 items, we added 6 combinations. For higher values need to modify the above functionality
# Due to little time constraint, didnt focus much on variable nomenclature and modularity.



