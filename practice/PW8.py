import re

def task1():
    text = '''
Writing programs or programming is a very creative
and rewarding activity  You can write programs for
many reasons ranging from making your living to solving
a difficult data analysis problem to having fun to helping
someone else solve a problem  This book assumes that
{\em everyone} needs to know how to program and that once
you know how to program, you will figure out what you want
to do with your newfound skills

We are surrounded in our daily lives with computers ranging
from laptops to cell phones  We can think of these computers
as our personal assistants who can take care of many things
on our behalf  The hardware in our current-day computers
is essentially built to continuously ask us the question
What would you like me to do next

Our computers are fast and have vasts amounts of memory and 
could be very helpful to us if we only knew the language to 
speak to explain to the computer what we would like it to 
do next If we knew this language we could tell the 
computer to do tasks on our behalf that were reptitive  
Interestingly, the kinds of things computers can do best
are often the kinds of things that we humans find boring
and mind-numbing
    '''
    
    with open("words.txt", "w") as file:
        file.write(text)
        
    keys = dict()
    with open("words.txt", "r") as file:
        for i in file.read().split():
            keys[i] = 0
            
    print(keys)

def task2():
    logs='''
From biba@mail.ru Sat Jan 5:07:14:16 2008
From biba@mail.ru Mon Jan 5:06:13:16 2008
From biba@mail.ru Fri Jan 5:09:14:16 2008
From biba@mail.ru Sat Jan 5:08:16:16 2008
From biba@mail.ru Sat Jan 5:09:15:16 2008
'''

    with open("logs.txt", "w") as file:
        file.write(logs)
    
    email_pattern = "From [A-Za-z0-9.]+@[A-Za-z.]+ [A-Za-z]{3}"
    with open("logs.txt", "r") as file:
        content = file.read()
        days = [x[-3:] for x in re.findall(email_pattern, content)]
        unique_days = set(days)
        
        count = dict()
        
        for day in unique_days:
            count[day] = days.count(day)
      
        print(count)


def task3():

    logs ='''
From biba.boba@mail.ru hello
From biba.boba@mail.ru hi
From biba.boba@mail.ru bye
From biba.boba@mail.ru chikibamboni

From abrakadabra@mail.ru hello
From abrakadabra@mail.ru yes, yes, yes
From abrakadabra@mail.ru no no no!
    '''

    with open("logs.txt", "w") as file:
        file.write(logs)
    
    email_pattern = "[A-Za-z0-9.]+@[A-Za-z.]+"
    with open("logs.txt", "r") as file:
        content = file.read()
        emails = re.findall(email_pattern, content)
        unique_emails = set(emails)
        
        count = dict()
        
        for email in unique_emails:
            count[email] = emails.count(email)
      
        print(count)
        

def task4():

    logs ='''
From biba.boba@mail.ru hello
From biba.boba@mail.ru hi
From biba.boba@mail.ru bye
From biba.boba@mail.ru chikibamboni

From abandana@mail.ru hihihaha
From abandana@mail.ru hihihaha
From abandana@mail.ru hihihaha
From abandana@mail.ru hihihaha
From abandana@mail.ru hehehe
From abrakadabra@mail.ru yes, yes, yes
From abrakadabra@mail.ru no no no!
    '''

    with open("logs.txt", "w") as file:
        file.write(logs)
    
    email_pattern = "[A-Za-z0-9.]+@[A-Za-z.]+"
    with open("logs.txt", "r") as file:
        content = file.read()
        emails = re.findall(email_pattern, content)
        unique_emails = set(emails)
        
        count = dict()
        
        for email in unique_emails:
            count[email] = emails.count(email)
      
        f = sorted(count.items(), key=lambda x:x[1])
        print(f[-1])


def task5():
    logs ='''
From biba.boba@mail.ru hello
From biba.boba@mail.com hi
From biba.boba@gmail.ru bye
From biba.boba@gmail.com chikibamboni

From abandana@ain.cw.kz hihihaha
From abandana@bz.kz.mz hihihaha
From abandana@mail.org hihihaha
From abandana@yahoo.com hihihaha
From abandana@mail.ru hehehe
From abrakadabra@mail.ru yes, yes, yes
From abrakadabra@gmail.ru no no no!
    '''

    with open("logs2.txt", "w") as file:
        file.write(logs)
    
    email_pattern = "@[A-Za-z.]+"
    with open("logs2.txt", "r") as file:
        content = file.read()
        emails = re.findall(email_pattern, content)
        unique_emails = set(emails)
        
        count = dict()
        
        for email in unique_emails:
            count[email] = emails.count(email)
      
        print(count)

