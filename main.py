from random import randint

def run(switch:bool):
    # Evil dict hack
    var = {
    'Door0':False,
    'Door1':False,
    'Door2':False,
    }
    var[f'Door{randint(0,2)}'] = True
    choice = f'Door{randint(0,2)}'
    while True:
        remove = f'Door{randint(0,2)}'
        if not var[remove] and remove != choice:
            break
    del var[remove]
    # Dumb switching algorithm
    if switch:
        for i in var:
            if i != choice:
                choice = i
    return var[choice]

def main():
    iterations = input(f"# of iterations to run for each >>> ")
    try:
        iterations = int(iterations)
    except:
        print("Please enter an integer!")
        return
    switched = []
    Nswitched = []
    for i in range(iterations):
        switched.append(run(True))
    switched = switched.count(True) / len(switched) * 100
    for i in range(iterations):
        Nswitched.append(run(False))
    Nswitched = Nswitched.count(True) / len(Nswitched) * 100
    print(f"When not switching doors, you win the car {Nswitched}% of the time.\n"
    f"When switching doors, you win the car {switched}% of the time.")
    # What the frick?!

if __name__ == "__main__":
    main()
