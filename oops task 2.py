"""Task 2 for oops concept,use all the oops concept and implement the example with ineuron,internship,job ,etc-create total 10 example"""
import logging
logging.basicConfig(filename="test2.log",level=logging.INFO,format='%(asctime)s %(message)s %(name)s %(levelname)s')
logging.info("we are inside the main log")

#1st example-Inheritance
class ineuron:
    def __init__(self):
        logging.info("we are inside ineuron class")
        self.student_name="Sharanya"
        self.user_id=234567890654
        self.passwd=234567

class internship:
    def __init__(self):
        logging.info("we are inside internship class")
        self.mail_id="asdfghj@gmail.com"
        self.website_passwd=234567

class placement(ineuron,internship):
    logging.info("we are inheritating ineuron and internship class")
    pass

i=ineuron()
j=internship()
p=placement()
print(p.student_name)



#2nd example-Inheritance
class ineuron:
    batch=2022
    name_of_course="Full stack Data science"
    def __init__(self,ineuron_batch,ineuron_name_of_course):
        logging.info("We are inside ineuron class")
        self.ineuron_batch=ineuron_batch
        self.ineuron_name_of_course=ineuron_name_of_course

class student(ineuron):
    logging.info("WE are inheritating parent class that is ineuron class")
    #print(ineuron.batch)



#Inheritance-3rd example
class iNeuron:
    logging.info("we are inside iNeuron class")
    number_of_course=50
    year_of_establishment=2018

class job_portal(ineuron):
    logging.info("we are inside job portal class where we are inheritating ineuron class")
    def __init__(self):
        self.job_offer=20
        print("TOtal number of job offer ",self.job_offer,"from the number of course",self.number_of_course)

J=job_portal()
print(J)


#Encapsulation-1st example
class ineuron:
    def __init__(self,student_name,user_id,passwd):
        logging.info("we are inside ineuron class")
        self.student_name=student_name
        self.user_id=user_id
        self.passwd=passwd

    def __str__(self):
        return "This belongs to ineuron class"


class internship:
    def __init__(self,mail_id,website_passwd):
        logging.info("we are inside internship class")
        self.mail_id=mail_id
        self.website_passwd=website_passwd

    def __str__(self):
        return "This belongs to internship class"

class job:
    def __init__(self,degree_certificate,work_experience):
        logging.info("we are inside internship class")
        self.degree_certificate=degree_certificate
        self.work_experience=work_experience

    def __str__(self):
        return str(self.degree_certificate) + "  ####   without inheritance we can call two class  #### " +str(self.work_experience)

i=ineuron("sharanya",90153222334,2345678)
j=internship("asdfghj@gmail.com",23456789)
k=job(i,j)
#print(k)



#Encapsulation-2nd example
class ineuron:
    batch=2022
    name_of_course="Full stack Data science"
    def __init__(self,ineuron_batch,ineuron_name_of_course):
        logging.info("WE are inside ineuron class")
        self.ineuron_batch=ineuron_batch
        self.ineuron_name_of_course=ineuron_name_of_course

class student():
    logging.info("Without inheritating we can access the data that is called encapsulation")
    print(ineuron.batch)




#overriding & inheritance-1st example
class ineuron:
    def __init__(self):
        logging.info("we are inside ineuron class for overriding")
        self.student_name = "abc"
        self.user_id = 234567
        self.passwd = 123

class internship(ineuron):
    def __init__(self):
        logging.info("we are inside internship class for overiding")
        self.student_name = "xyz"
        self.login_id = 234567

i=ineuron()
j=internship()
j.student_name="mno"  #overriding is ocurred
#print(j.student_name)



#Public,protected,private-1st example

class one_neuron:
    def __init__(self,recordings,assignments,online_registeration):
        logging.info("we are inside one_neuron class")
        self._recordings=recordings
        self._assignments=assignments#protected
        self.online_registeration=online_registeration#(public)

class Ineuron:
    def __init__(self,live_class,live_task,recordings,assignments):
        logging.info("We are inside Ineuron class")
        self.__live_class=live_class#private
        self.__live_task=live_task
        self._recordings=recordings
        self._assignments=assignments

o=one_neuron("this is one neuron recording","this is one neuron assignments")
i=Ineuron("ineuron live class","ineuron live task","ineuron recordings","ineuron assignments")
#print(i._Ineuron__live_class)



#Operator overriding
class multiply:
    def __init__(self,a):
        self.a=a

    def __mul__(self, other):
        return self.a + self.other
mul1=multiply(2)
mul2=multiply(10)
#print(mul1*mul2)#as over here we are doing multiplication but still it will add as created on the method

"""Modules extraction
import test"""

#Polymorphism
class ineuron:
    def msg(self):
        return "this is ineuron message"
class internship:
    def msg(self):
        return "this is internship message"
def test(check):
    check.msg()
i=ineuron()
j=internship()
#test(i)
