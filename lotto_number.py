from random import choice


"""Will find a winning ticket from numbers given and how long it took the
computer to find a match"""

def winning_ticket(lotto_numbers):
    #creating an empty list to store the winning numbers
    winning_numbers = []

    #make sure not to have dups
    while len(winning_numbers) < 4:
        number = choice(lotto_numbers)
        while number not in winning_numbers:
            winning_numbers.append(number)
    return (winning_numbers)

#new definition for person's number
def my_ticket(lotto_numbers):
    #creating an empty list to store the winning numbers
    my_ticket = []

    #make sure not to have dups
    while len(my_ticket) < 4:
        number = choice(lotto_numbers)
        while number not in my_ticket:
            my_ticket.append(number)
    return (my_ticket)

#check if winning ticket and my ticket match
def matching_ticket(played_ticket,winning_ticket):
    for number in winning_ticket:
        if number not in played_ticket:
            return False
    #found a winning ticket
    return True

lotto_numbers = [1,2,3,4,5,6,7,8,9,'a', 'b', 'c','d','e']
winning_ticket = winning_ticket(lotto_numbers)


won = False
#stopping the system after a certain number of tries
max_tries = 10_000
count = 0

while not won:
    new_ticket = my_ticket(lotto_numbers)
    won = matching_ticket(new_ticket,winning_ticket)
    count += 1
    if count >= max_tries:
        break

if won:
    print(f'The winning numbers are {winning_ticket}.')
    print(f'Your ticket numbers are {new_ticket}.')
    print (f'It took {count} tries to get a winning ticket.')

else:
    print(f'The winning numbers were {winning_ticket}.')
    print(f'Your numbers were {new_ticket}.')
    print(f"The system tried {count} to get a winning ticket for you.")
