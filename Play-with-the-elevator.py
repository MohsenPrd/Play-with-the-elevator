# Define the calculation function ---
def calculate_floor(actions : str):
    result = 0
    for action in actions:
        if action == 'u':
          result += 1
        elif action == 'd':
          result -= 1
    return result


# Define the valdiation function for inputs ---
def validation(user_input):
    is_in = False
    while is_in == False:
        #check length of input ---
        while len(user_input) != 4:
            user_input = input('--*4* choices allowed: (u / d) ')

        #check chars of input ---
        for word in user_input:
            if word != 'u' and word != 'd':
                is_in = False
                user_input = input('Just (u / d) allowed: ')
                break
            else:
                is_in = True




# initialize floor number ---
floor_num = 0


# ** Saeed turn **
saeed_turn = input('--Saeed, its your turn: where you want to go? (u / d) ')

# validate saeed ---
validation(saeed_turn)

# calculate floor_num ---
floor_num += calculate_floor(saeed_turn)
print (floor_num)



# ** Hamid turn ** 
hamid_turn = input('--Hamid, its your turn: where you want to go? (u / d) ')

# validate hamid ---
validation(hamid_turn)


# ** check floor_num **
final_floor_num = floor_num + calculate_floor(hamid_turn)

while final_floor_num < -4:

    # set final_floor_num to first value (without the hamid choices)
    final_floor_num = floor_num

    hamid_turn = input('Cant go down anymore! : ')

    # validate hamid ---
    validation(hamid_turn)
    
    # add to final_floor_num
    final_floor_num += calculate_floor(hamid_turn)




# print final_floor_num
print ('final floor: ' ,final_floor_num)