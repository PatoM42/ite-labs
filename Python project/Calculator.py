import math

A = 3130; ## A = DBM0  (Day of Birth - Month - 0)
DB = 31;
M = 3;

Q = 0.098 * A
L = (DB + 18) * math.sqrt(A);

if L >= 2:
    Lmax = 2;

else:
    Lmax = L;


## trapezoidal thread - Tr
## Buttress thread - S 


def get_thread_type():

    if DB % 2 == 0:
        thread_type = "Tr"; ## trapezoidal thread
    else:
        thread_type = "S"; ## buttress thread

    return thread_type



def get_nut_height_factor():

    nut_height_factor = input("Enter the nut height factor(It can be from 1.5 to 2.5): ");

    if nut_height_factor < 1.5 or nut_height_factor > 2.5:

        print("Invalid input! Please enter a value between 1.5 and 2.5.");
        get_nut_height_factor();

    return nut_height_factor;



def get_thread_multiplicity():

    if M % 2 == 0:
        i = 1;

    else:
        i = 2;

    return i;


Steel_Young_Modulus = 2.06 * 10**5; ## MPa

z = h/P;

def get_height_factor(thread_type):

    if thread_type == "Tr":
    
        Height_Factor = 0.5; ## Height factor for trapezoidal thread

    elif thread_type == "S":
    
        Height_Factor = 0.75; ## Height factor for buttress thread

    return Height_Factor;

def mean_thread_pressure(): 
## z - number of threads along height h
## d_2 - mean diameter of the thread
## H_1 - height of the working thread

    p = Q/(z*pi*d_2*H_1);

    return p;





