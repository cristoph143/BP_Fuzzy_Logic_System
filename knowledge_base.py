from dataBase import *


def infos():
    name = input('What is your name! ')
    age: int = int(input('What is your age? '))
    while age < 0 or age > 100:
        if age < 0:
            print('You input Lower than Zero!')
        if age > 100:
            print('You input Greater than 100')
        age: int = int(input('What is your age? '))
    gender = input('What is your gender ')
    while gender.lower():
        if gender == 'male' or gender == 'female':
            break
        else:
            print('Please Input Correct Gender! ' + str(gender))
            gender = input('What is your gender ')
    info = Personal_Info(name, age, gender)
    info.set_name(name)
    info.set_age(age)
    info.set_gender(gender)
    info.hello()
    print('name')
    for lst in info.info:
        print(lst)
    return info.info


def bp_info(lst):
    # Getting Input for Systolic
    systolic = int(input(lst + ', What is your systolic level? '))
    while systolic < 65 or systolic > 230:
        if systolic < 65:
            print(lst + ", You inputted below 65!")
        if systolic > 230:
            print(lst + ", You entered above 230!")
        systolic = int(input(lst + ', What is your systolic level? '))
    diastolic = int(input(lst + ', What is your diastolic level? '))
    while diastolic < 35 or diastolic > 135:
        if diastolic < 35:
            print(lst + ", You inputted below 35!")
        if diastolic > 135:
            print(lst + ", You entered above 135!")
        diastolic = int(input(lst + ', What is your diastolic level? '))
    bp = BP(systolic, diastolic)
    bp.set_systolic(systolic)
    bp.set_diastolic(diastolic)
    bp.status()
    for lst in bp.patient_info:
        print(lst)
    return bp.patient_info