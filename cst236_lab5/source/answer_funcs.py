import getpass
import datetime
import math



def hal_20():
    return "I'm afraid I can't do that {0}".format(getpass.getuser())

def current_time():
    return datetime.datetime.now()

def get_fib(n):
    n = int(n)
    a, b = 0, 1
    for i in xrange(n):
        a, b = b, a + b
    return a


def unit_convert(n,key1,key2):
    n = float(n)
    print n
    print key1
    print key2

    conversions = {
                   
                    "megameters": 1000000,
                    "kilometers": 1000,
                    "hectometers": 100,
                    "decameters": 10,
                    "meters": 1,
                    "decimeters": 0.1,
                    "centimeters": 0.01,
                    "millimeters": 0.001,
                    "micrometers": 0.000001,
                    "nanometers": 0.000000001
                    }



    key1 = conversions[key1]
    key2 = conversions[key2]

    n = n * (key1 / key2)

    return n

def find_car():
    return "In the driveway {0}".format(getpass.getuser())

def omnianswer():
    return "42"

def how_r_u():
    return "I am doing well {0}".format(getpass.getuser())

def who_r_u():
    return "My name is PyTona"

def shut_down():
    return "I am afraid I cannot do that right now {0}".format(getpass.getuser())

def get_factorial(num):
    num = int(num)
    num = math.factorial(num)
    return num

def get_power(x,y):
    x = int(x)
    y = int(y)

    magic_result_of_POW = math.pow(x,y)
    magic_result_of_POW = int(magic_result_of_POW)
    return magic_result_of_POW

def get_root(da_number):
    da_number = int(da_number)
    da_number = math.sqrt(da_number)
    return da_number

def d_to_r(deg):
    deg = math.radians(deg)
    deg = int(deg)
    return deg

def r_to_d(rad):
    rad = math.degrees(rad)
    rad = int(rad)
    return rad






    
    
