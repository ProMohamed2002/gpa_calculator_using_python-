def gpa_calculator():
  q='n'
  while q!='y': 
   print(take_data())
   q=input("\nquit y/n: ")
def take_data():
  sum=0
  print("GPA calculator")
  filename=input("file name:")
  csvfile=open(filename,'w')
  try:
   calculas=input("calculas: ")
   csvfile.write("calculas,"+calculas.upper())
   sum+=get_pounts(calculas)
   english=input("English:")
   csvfile.write("\nEnglish,"+english.upper())
   sum+=get_pounts(english)
   it=input("IT:")
   csvfile.write("\nIT,"+it.upper())
   sum+=get_pounts(it)
   ds=input("DS:")
   csvfile.write("\nDS,"+ds.upper())
   sum+=get_pounts(ds)
   prog=input("programming:")
   csvfile.write("\nprogramming,"+prog.upper())
   sum+=get_pounts(prog) 
   csvfile.write("\nGPA,"+str(sum/15))
   return sum/15
  except:
    print("Error!!")
def get_pounts(grade):
   point=0
   grade=grade.upper()
   if grade == 'A'or grade=='A+':
      points=12
   elif grade=='A-':
      points=11
   elif grade == 'B+':
      points=10
   elif grade=='B':
      points=9
   elif grade=='B-':
      points=8
   elif grade=='C+':
      points=7
   elif grade=='C':
      points=6
   elif grade=='C-':
       points=5
   elif grade=='D':
      points=4
   else:
      points=0
   return points

