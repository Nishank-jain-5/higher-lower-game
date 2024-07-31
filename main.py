from game_data import data
import random
import art

compare_a = random.choice(data)

def get_random():
    againt_b = random.choice(data)

    while compare_a == againt_b:
        againt_b = random.choice(data)

    return againt_b


againt_b = get_random()

def joining(comparing_dict):
    joined_string = ""
    ans_list = []
    for i in comparing_dict:
        if i=="follower_count":
            ans_list.append(comparing_dict[i])
            continue
        else:
            joined_string += comparing_dict[i] 
        
        joined_string += ", "
    ans_list.append(joined_string)

    return ans_list

list_A = joining(compare_a)
list_B = joining(againt_b)

current_score = 0
game_run = True

print(art.logo)

while game_run:
    print("----------------------------------------------------------------------------------------\n")
    print(f"Compare A: {list_A[1]}")
    print(art.vs)
    print(f"Againt B: {list_B[1]}\n")
    user = input("\nWho has more follower? Type 'A' or 'B': ").lower()

    if user=="a":
        if list_A[0] > list_B[0]:
            current_score += 1
            print(f"\nyou're right! current score: {current_score}.")
            againt_b = get_random()
            list_B = joining(againt_b)
        else:
            game_run = False
            print("\n----------------------------------------------------------------------------------------")
            print(f"\nSorry that's wrong. Final score is: {current_score}.")
    
    elif user == "b":
        if list_B[0] > list_A[0]:
            list_A = list_B
            current_score += 1
            print(f"\nyou're right! current score: {current_score}.")
            againt_b = get_random()
            list_B = joining(againt_b)
        else:
            game_run = False
            print("\n----------------------------------------------------------------------------------------")
            print(f"\nSorry that's wrong. Final score is: {current_score}.")
    
    else:
        game_run = False
        print("----------------------------------------------------------------------------------------\n")
        print(f"Oops you press wrong key. Final score is: {current_score}.\n")

    