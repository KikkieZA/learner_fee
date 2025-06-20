# coutner that keeps track of students added to list
# also works as ID of student
id_counter = 1;

#create empty list of students
learner_list = []
felony_list = {}

# create our functions that will add or remove students
# add new student to list
def addNewLearner(Name, Surname, Amount):
  # you must declare a global variable as global before
  # you can make changes to it in a function
  global id_counter 
  
  # use the counter as the ID of the student
  # create the tuple to store the students
  new_learner = [id_counter, Name, Surname, Amount]
  # add the tuple to the list
  learner_list.append(new_learner)
  
  # we increase the coutner by 1 after student has been added
  id_counter += 1
  
# remove student function
def removeLearnerByID(ID):
  found = False
  ## we loop through the list and find the learner ID
  for learner in learner_list:
    # when we get the learners ID we remove the learner
    if learner[0] == ID: # this will check the ID
      learner_list.remove(learner)
      # when it finds the learner we force the programme
      # to stop the looping
      found = True
      break
  if found:
    print("Learner removed with ID: ", ID)
  else:
    print("learner not found")
  
# call add new learner function for learner details
addNewLearner("Mary", "Jane", 0)
addNewLearner("Chris", "Botha", 0)
addNewLearner("Owam", "Duna", 0)
addNewLearner("John", "Doe", 0)
addNewLearner("Jake", "Dawson", 0)

#remove student named Jake which will have ID: 5 to test
removeLearnerByID(5) 

# the following fucntions will make changes to the felony list
def addFelony(Name, Price):
  # this will add new felony to our dictionary of felonies
  felony_list[Name] = Price

# now we add some felonies
addFelony("Late", 5)
addFelony("Fighting", 500)
addFelony("Eating", 50)
addFelony("Cellphone", 50)


# the following functions will add or remove to what the learner owes
def addFelonyAmountToLearner(Felony, ID):
  # create temporary variable to store amount owed
  for learner in learner_list:
    if learner[0] == ID:
      # learner[3] is the amount location in the array/list of the learner
      # remember that arrays start at 0 
      # learner[0] is the ID
      # learner[1] is the Name
      # learner[2] is the Surname
      learner[3] += felony_list[Felony]
      break
      
def deductFelonyAmountToLearner(Amount, ID):
  for learner in learner_list:
    if learner[0] == ID:
      learner[3] -= Amount
      break

#to test the felonies are workign we add a late fee to Mary and others
addFelonyAmountToLearner("Late", 1)
addFelonyAmountToLearner("Fighting", 3)
addFelonyAmountToLearner("Late", 2)

# to test deduct
deductFelonyAmountToLearner(50, 3)

print("Late learner:") 
for learner in learner_list:
    print(  "ID: ", learner[0]," Surname:", learner[2], "Amount Owed:", learner[3])
    
print("Felony List")
# a dictionary consists of a key and value
for key, value in felony_list.items():
  print(key," R",value)

