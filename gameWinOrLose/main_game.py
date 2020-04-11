"""
WIN or LOSE (100 Marks)
A new fighting game has become popular. There are N number of villains with each having some strength. There are N players in the game with each having some energy. The energy is used to kill the villains. The villain can be killed only if the energy of the player is greater than the strength of the villain.
Maxi is playing the game and at a particular time wants to know if it is possible for him to win the game or not with the given set of energies and strengths of players and villains. Maxi wins the game if his players can kill all the villains with the allotted energy.
Input Format
The first line of input consist of number of test cases, T.
The first line of each test case consist of number of villains and player, N.
The second line of each test case consist of the N space separated strengths of Villains.
The third line of each test case consist of N space separated energy of players.

Constraints
1<= T <=10
1<= N <=1000
1<= strength , energy <=100000
Output Format
For each test case, Print WIN if all villains can be killed else print LOSE in separate lines.
Sample TestCase 1
Input
1
6
112 243 512 343 90 478
500 789 234 400 452 150
Output
WIN

Explanation
For the given test case, If we shuffle the players and villains, we can observe that all the villains can be killed by players.
As all the villains can be killed by the players, MAXI will WIN the game. Thus, the final output is WIN.

Sample TestCase 2
Input
2
6
10 20 50 100 500 400
30 20 60 70 90 490
5
10 20 30 40 50
40 50 60 70 80

Output
LOSE
WIN

"""

PLAYERS_KEY="players_villain"
STRENGTH_KEY="strength"
ENERGY_KEY="energy"
TEST_RESULT="case_result"
STRENGTH_SUM="total_strength"
ENERGY_SUM="total_energy"

def get_sum(lst_obj):
    sum=0
    for i in lst_obj:
        sum+=int(i)
    return sum

def enter_input(test_cases):
    input_data={}
    counter=0
    while(True):
        if int(test_cases)==counter: break
        counter+=1
        players=int(input("Enter Number of players: "))
        strengths=input("Enter Strengths separated by space: ")
        energies=input("Enter Energies separated by space: ")

        strengths_obj=strengths.split(' ')
        energies_obj=energies.split(' ')

        input_object={PLAYERS_KEY:0,STRENGTH_KEY:[],ENERGY_KEY:[],STRENGTH_SUM:0,ENERGY_SUM:0,TEST_RESULT:'LOSE'}
        input_object[PLAYERS_KEY]=players
        input_object[STRENGTH_KEY]=strengths_obj
        input_object[ENERGY_KEY]=energies_obj

        input_data.update({"test_case_"+counter.__str__():input_object})
        # print("test case",counter)
    # print("input_data",input_data)
    return input_data


def main_game():
    test_cases=int(input("enter line1: "))
    all_input=enter_input(test_cases)
    # executing for all test cases
    for i in range(test_cases):
        test_cases_object=all_input['test_case_'+(i+1).__str__()]

        test_cases_object[STRENGTH_SUM]=get_sum(test_cases_object[STRENGTH_KEY])
        test_cases_object[ENERGY_SUM]=get_sum(test_cases_object[ENERGY_KEY])

        if test_cases_object[ENERGY_SUM]>test_cases_object[STRENGTH_SUM]:
            test_cases_object[TEST_RESULT]="WIN"
        else:
            test_cases_object[TEST_RESULT]="LOSE"

        print(test_cases_object)
        print(test_cases_object[TEST_RESULT])
    return


if __name__ == '__main__':
    main_game()



