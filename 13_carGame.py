command=""
started = False
stopped = False



while True:
    command = input().lower()
    if command == 'start':
        if started:
            print(f"Car is Already Started")
        else:
            started = True
            print(f'Car Started')

    elif command == 'stop':
        if stopped == False :
            print(f'Car Stopped')
            stopped = True
        else:
            
            print(f"Car is already stopped")

    elif command == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to quit the game
        ''')
    elif command == "quit":
        break
    else:
        print(f"I don't understand ")