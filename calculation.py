
from sem_methods import *
import random
import json

def calculation(studentlist):
# from the file names and rolls are taken
  names, rolls = student_finder(studentlist)
  l = [i%100 for i in rolls] # list of last 2 digit rollnumbers
  
  
  # the actual calculation and code
  exp=[1,2,3,4,5,6,7,8,9,10,11,12]
  exp1=exp.copy()
  exp11=exp.copy()
  x=[]
  
  z=l.copy()
  b={}
  c={}
  for i in range((len(l))//5):
      x.clear()    
      while(len(x)<=4):
          a=random.choice(z)
          if(a  not in x):
              if(i<=11):
                  x.append(a)
                  z.remove(a)
              elif(i>11):
                  x.append(a)
          else:
              continue
          q=x.copy()
      if(i<=11):
          r1=random.choice(exp1)
          b.update({r1:q})
          exp1.remove(r1)
  if(len(l)<=59):
      b.update({random.choice(exp1):z})
  elif(len(l)==60):
      print("all roll numbers are assigned")
  else:
      for i in z:
          r2=random.choice(exp11)
          c.update({r2:i})
          exp11.remove(r2)
  allotted_results = sorted(b.items(),key=lambda t:t[0])
  allotted_results_extra = sorted(c.items(),key=lambda t:t[0])
  # allotted_results.append(allotted_results_extra)
  
  
  # printing the results
  # if len(allotted_results_extra)!=0:
  #     print("The remaining roll numbers have been allotted to random experiments:")
  #     print_results(allotted_results_extra)
  
  #writing a new json file
  # data = json.dumps(allotted_results)
  # data_extra = json.dumps(allotted_results_extra)
  
  # with open("student_data.json", "w") as student_data:
  #     json.dump(allotted_results, student_data )

  #creating files 
  with open("allotment_results.txt","w") as allotments:
    append_results(allotted_results,allotments)
    allotments.close()

  with open("allotment_results_extra.txt","w") as allotments:
    append_results(allotted_results_extra,allotments)
    allotments.close()

  with open("final_allotment.txt","w") as allotments:
    final_result("allotment_results.txt",allotments, "studentlist.txt")
    allotments.close()  
    


    
        

