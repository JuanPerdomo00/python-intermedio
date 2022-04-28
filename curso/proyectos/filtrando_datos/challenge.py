#!/usr/bin/env python3
from data import DATA

def main():
    all_python_devs = list(filter(lambda worker: worker['language'] == 'python', DATA))
    all_python_devs = list(map(lambda worker: worker['language'] == 'python', all_python_devs))

    all_platzi_workers = list(filter(lambda worker: worker['organization'] == 'Platzi', DATA))
    all_platzi_workers = list(map(lambda worker: worker['organization'] == 'Platzi', all_platzi_workers))

    '''
    adults = list(filter(lambda edad: edad['age'] >= 18, DATA)) 
    adults = list(map(lambda worker: worker['name'], adults)) 

    old_people = list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA))
    '''


    adults = [worker['name'] for worker in DATA if worker['age'] >= 18]

    old_people = [worker | {'old': worker['age'] > 70} for worker in DATA]

    for i in old_people:
        print(i)


if __name__ == '__main__':
    main()