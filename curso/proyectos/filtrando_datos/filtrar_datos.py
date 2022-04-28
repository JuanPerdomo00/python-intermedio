#!/usr/bin/env python3
from data import DATA


def main():
    # todos los que les gusta python
    all_python_devs = [worker['name'] for worker in DATA if worker['language'] == 'python']
    all_platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']

    adults = list(filter(lambda edad: edad['age'] >= 18, DATA)) 
    adults = list(map(lambda worker: worker['name'], adults)) 

    old_people = list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA))
    
    for worker in old_people:
        print(worker)


if __name__ == '__main__':
    main()