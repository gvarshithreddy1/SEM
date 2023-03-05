def student_finder(studentlist):
    students_file = open(studentlist)
    student_names = []
    student_rolls = []
    for student in students_file:
        student_str = str(student)
        student_info = student_str.split()
        # print(student_info)
        student_rollno = int(student_info[0])
        student_name = student[student.index("-")+1:].strip()
        # print(student_name)
        student_names.append(student_name)
        student_rolls.append(student_rollno)
    return student_names, student_rolls

def print_results(allotted_results):
    for i in range(len(allotted_results)):
        print("Experement",allotted_results[i][0],":")
        print(end="")
        for j in allotted_results[i][1]:
            print(j, end=" ")
        print()
def append_results(allotted_results, allotments):
    for i in range(len(allotted_results)):
        allotments.write("Experement"+str(allotted_results[i][0])+":\n")
        for j in allotted_results[i][1]:
            allotments.write(str(j)+" \n")
        allotments.write("")

def roll_name_map(studentlist,allotment_result):
  names, rolls = student_finder(studentlist)
  last_two = []
  for i in rolls:
    last_two.append(int(i)%100)
  # print(last_two)  
  file = open(allotment_result)
  # with open('final_allotments.txt','w'):
  rolls_names = {}
  for line in file:
    line = line.strip()
    if line.isnumeric():
        line = int(line)
        rolls_names[rolls[last_two.index(line)]] = names[last_two.index(line)]
  # print(rolls_names)
  return rolls_names,last_two
      

  # print(rolls_names)
def final_result(allotted_results,allotments, studentlist):
  rolls_names, last_two = roll_name_map(studentlist,allotted_results)
  rolls = list(rolls_names.keys())
  names = list(rolls_names.values())
  x=0
  allotted_results_file = open(allotted_results)
  for i in allotted_results_file:
    i = i.strip()
    if not i.isnumeric():
      allotments.write("Experiment "+str(x+1)+":\n")
    
    else:
      i = int(i)
      allotments.write(str(rolls[last_two.index(i)])+" - "+ names[last_two.index(i)] +" \n")
      allotments.write("") 
    print("\n")
    x+=1
        


        