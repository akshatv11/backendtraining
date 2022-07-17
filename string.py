#first_name = 'akshat'
#last_name = 'verma'

#print(first_name + ' ' + last_name)

#full_name = '{fname} {lname}'.format(fname='akshat', lname='verma')
#print(full_name)


name = input('enter your name\n')
sem = int(input('enter your semester\n'))
clg = input('enter your college name\n')

data = '{name} {sem} {clg}'.format(name=name, sem=sem, clg=clg)

print(data)
