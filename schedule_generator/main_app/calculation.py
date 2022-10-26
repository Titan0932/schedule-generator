""" Data
    	number of subjects
    	Days to study
    	Subjects
    	School Start Time
    	School End Time """


#-----------------------------------------------------

""" 
Limits:
    	No tuition before 5 am
    	No tuition after 8 pm
        no tution 30 minutes prior school starts
    	30 minutes break after school ends
    	Tuition time in avg=1 hour 
		No Exceptions for weekwends: school time 

"""
#-----------------------------------------------------

""" 
Process:
    	-Calculate how much time available
        	Before school
        	After school
    	-Find Total tuition hours and remaining minutes
    	-Compare total hours and subject number
            Case I
	            If total hours > subject number
	                find the extra hours by (total hours - subject number)
                    divide the extra hours by the subject number and allocate to each subject. Divide them as break between every 2 subjects
                    
            Case II

	            If total hours = subject number
                    allocate an hour to each subject
                    if extra minutes available,divide them as break between every 2 subjects.

                -for each CASE I and II have the same routine in all the days Except:

            Case III    
	            If total hours < subject number
	                - allocate an hour to each subject
                    -for the subjects that dont fit in the day allocate the time from the next day
                    -continue the same until all the subjects are allocated with study time
                    - if some time is still remaining then start the checking again to all the CASES
"""
#-----------------------------------------------------

    	

def time_calc(startTime,endTime):
	morning=startTime-5
	evening=8-endTime


def caseI(subj):
	pass

def caseII():
	pass


def caseIII():
	pass

def sched_calc(id,numofSubs,subjects,start,end):
	print('hello')
	print(id,numofSubs,subjects,start,end)