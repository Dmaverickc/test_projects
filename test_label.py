import csv
from docx import Document
from collections import OrderedDict


document = Document()


def csv_reader(file_obj):

	reader = csv.DictReader(file_obj, delimiter =',') # reads in csv file
	prev_row = None   # sets the preivous version to null 
	prev_item = None
	count = 0
	label = []   # empty array
	odd_label = []


	for idx, row in enumerate(reader):       # goes through the rows of the csv
		
		item = row["time"]   # set item as row on time from csv file
		

		
		if row["name"] == prev_row:

	
			label.append(item)     # appends item to the label list
		 	label.append(prev_item)   # appends the last item to the list so it does skip any
		 	label = sorted(set(label))  # sorts the removes doubles
			

			odd_label = []  # clears the single odd_label list
			# might get away with this being a str instead of a list
			


		elif row["name"] != prev_row:  
			odd_label.append(item)     
			if len(odd_label) == 2:   # keeps the odd_labels list limited to one
				odd_label.remove(prev_item) # removes the previous item to keep odd_label single digit 


			
			label_len = len(label)
			printer(label_len, label)

			label_neg = len(odd_label)
			odd_printer(odd_label, label)

			# need to do a check to see if item is in odd_label and label and then delete it from odd_label if it is
			# might be able to change odd_label to just a string and set it none eack time 		

		

		 	label = [] # clears the list of labels

		
		

		prev_row = row["name"]     # sets the current version equal to to previous vresion before next increment
		prev_item = row["time"]

def printer(amount, place):

	#print place
	if amount == 1:
		print place
	elif amount == 2:
		print place
	elif amount == 3:
		print place
	elif amount == 4:
		print place
	#document.add_paragraph(place)



def odd_printer(odd_filter, pos_filter):

	if odd_filter not in pos_filter:  # something has to be done here 02/01/18
		print odd_filter
	elif odd_filter in pos_filter:
		print 'test'




if __name__ == "__main__":
	

	with open("test.csv") as f_obj:   # opens the csv file
		csv_reader(f_obj)             # sends the csv_reader function the csv data file 



#	document.save('test.docx')