#Edward Bowyer - November 6 2021
#Workout Opimization Program - Values should be tweaked as necessary.
##Gain is muscle gain, divided by body sections 
##Fatigue is immediate tiredness
##Soreness is post workout tiredness
#Description of variables and contstraints
#G = gain
#F = fatigue
#S = soreness
#U = Upper
#L = Legs
#A = Abs
#RPush = russian pushup
#Pull = pullup
#Bsquat = bulgarian squat
#squat = regular weighted squat
#Vup = vup
#LazyV = lazy vup

from cvxpy import *
from cvxpy.expressions import variable
from numpy import string_

#ABs function
def ABS():
    Vup = Variable()
    LazyV = Variable()
    G_Vup =  10;
    G_LazyV =  8;
    F_Vup =  8;
    F_LazyV =  7;
    S_Vup =  12;
    S_LazyV =  10;
    G_A = Vup*G_Vup+G_LazyV*LazyV;
    constr_A = [130 >= S_Vup*Vup+S_LazyV*LazyV, 100 >= F_Vup*Vup+F_LazyV*LazyV, Vup >= 0, LazyV >= 0];
    obj_A = Maximize(G_A)
    prob_A = Problem(obj_A,constr_A)
    opt_val_A = prob_A.solve()
    print(opt_val_A)
    solution = G_A.value 
    print(Vup.value, LazyV.value)
    return solution

#Upper body function
def Upper():
    Pull = Variable()
    Rpush = Variable()
    G_Rpush =  10;
    G_Pull =  12;
    F_Pull =  10;
    F_Rpush = 9;
    S_Pull =  12;
    S_Rpush =  11;
    G_U = Pull*G_Pull+G_Rpush*Rpush;
    constr_U = [130 >= S_Pull*Pull+S_Rpush*Rpush, 100 >= F_Pull*Pull+F_Rpush*Rpush, Pull >=0,Rpush>=0];
    obj_U = Maximize(G_U)
    prob_U = Problem(obj_U,constr_U)
    opt_val_U = prob_U.solve()
    print(opt_val_U)
    solution = G_U.value 
    print(Pull.value, Rpush.value)
    return solution    

#Legs function
def L():
    squat = Variable()
    Bsquat = Variable()
    G_squat =  10;
    G_Bsquat =  12;
    F_squat =  9;
    F_Bsquat =  12;
    S_squat =  8;
    S_Bsquat =  14;
    G_L = squat*G_squat+G_Bsquat*Bsquat;
    constr_L = [200 >= squat*S_squat+S_Bsquat*Bsquat, 125 >= squat*F_squat+F_Bsquat*Bsquat, squat >= 0, Bsquat >= 0];
    obj_L = Maximize(G_L)
    prob_L = Problem(obj_L,constr_L)
    opt_val_L = prob_L.solve()
    print(opt_val_L)
    solution = G_L.value 
    print(squat.value, Bsquat.value)
    return solution

#Main
def Main():
    print("Welcome to my wack workout optimization...\n")
    choice = str;
    while choice != "A" or "U" or "L":
            choice = input("Chose what to optimize (A,U,L):\n")
            if choice == "A":
                ABS()    
                break
            elif choice == "U":
                Upper()
                break
            elif choice == "L":
                L()
                break
    
Main()