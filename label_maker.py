import csv
from docx import Document
from collections import OrderedDict

document = Document()


def csv_reader(file_obj):

	reader = csv.DictReader(file_obj, delimiter =',') # reads in csv file
	prev_row = None   # sets the preivous version to null 
	prev_item = None
	label = []   # empty array
	odd_label = None

	for idx, row in enumerate(reader):       # goes through the rows of the csv
		
		item = row["time"]   # set item as row on time from csv file
		
	
		if row["name"] == prev_row:

	
			label.append(item)     # appends item to the label list
		 	label.append(prev_item)   # appends the last item to the list so it does skip any
		 	label = sorted(set(label))  # sorts the removes doubles
				


		elif row["name"] != prev_row:  
		

			odd_label = item # makes odd_label equal to the current item 
			#if odd_label in label:
			odd_printer(odd_label, label)
				
				
	
		 	
			label_len = len(label)
			printer(label_len, label)
		

		 	label = [] # clears the list of labels
		 
		



		prev_row = row["name"]     # sets the current version equal to to previous vresion before next increment
		prev_item = row["time"]

def printer(amount, place):


# going to be used for positioning the items in the square
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


def odd_printer(odd_position, test):

	if odd_position not in test:
		print odd_position
	elif odd_position in test:
		odd_position = None   # need to figure out how to



if __name__ == "__main__":
	

	with open("test.csv") as f_obj:   # opens the csv file
		csv_reader(f_obj)             # sends the csv_reader function the csv data file 


#	document.save('test.docx')