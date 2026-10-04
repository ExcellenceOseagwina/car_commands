car_position = 0
moving = False
print("Type 'help' for a list of commands.")
# while commands != "quit": <--- can be used in place of while True
while True:
                 command = input("> ").lower()
                 if command == "start":
                                  if moving:
                                                   print("Car is already moving!")
                                  else:
                                                   moving = True
                                                   print("Car has started")
                 elif command == "help": 
                                  print('''
Start - To start game
Stop - To stop game
Quit - To exit game
                                        ''')
                 elif command == 'right':
                                  if not moving:
                                                   print("You need to start the car")
                                  else:
                                                   car_position += 1
                                                   print(f"Car moved right. Position: {car_position}")
                 elif command == "left":
                                  if not moving:
                                                   print("You need to start the car")
                                  else:
                                                   car_position -=1
                                                   print(f"Car moved left. Position: {car_position}")
                 elif command == "stop":
                                  if not moving:
                                                   print("Car has already stopped!")
                                  else:
                                                   moving = False
                                                   print("Car has stopped")
                                  print(f"Position: {car_position}")
                 elif command == "quit":
                                  print("Thank you for playing!")
                                  print(f"Position: {car_position}")
                                   
                                  break #<---- Should be removed if you are using while commands != "quit":
                 else:
                                  print(f"{command} is not recognised. Type 'help' to see the list of commands")