from random import randint




def user_batting():
    user_total_runs=0
    user = 0
    comp = 10
    
    while (user!=comp):
        comp = randint(1,6)
        
        try:
            user = int(input('enter your choice:\n'))            
                        
            if (user<1 or user>6):
                 print('wrong choice!')
            elif (comp==user):
                print(f"COMPUTER CHOSE {comp}\nYOU CHOSE {user}\nYOUR TOTAL SCORE IS {user_total_runs}!\n")
                break
            else:
                user_total_runs= user_total_runs + user
                print(f"COMPUTER CHOSE {comp}\nYOU CHOSE {user}\nYOUR TOTAL SCORE IS {user_total_runs}!\n")
 
        except ValueError as x:
            print('VALUE ERROR')           
        except Exception as y:
            print('ERROR')
            
    print('YOU ARE OUT!\n\n')
    return int(user_total_runs)




def comp_batting():
    comp_total_runs = 0
    user = 0
    comp = 10
    
    while (user!=comp):
        comp = randint(1,6)
        
        try:
            user = int(input('enter your choice:\n'))
            
            if (user<1 or user>6):
                 print('wrong choice!')
            elif (comp==user):
                print(f"COMPUTER CHOSE {comp}\nYOU CHOSE {user}\nCOMPUTER'S TOTAL SCORE IS {comp_total_runs}!\n")
                break
            else:
                comp_total_runs= comp_total_runs + comp
                print(f"COMPUTER CHOSE {comp}\nYOU CHOSE {user}\nCOMPUTER'S TOTAL SCORE IS {comp_total_runs}!\n")
        
        except ValueError as x:
            print('VALUE ERROR')            
        except Exception as y:
            print('ERROR')
            
    print('COMPUTER IS OUT!\n') 
    return int(comp_total_runs) 
 



def cricket():
    print('Welcome to the Hand Cricket Game\n')
    print(f"RULES:\nYou can enter any no between 1 and 6\nIf your choice matches with Computer's, you're out!\nIf not, the number you chose is added to the total score!\n")
    print('Best of Luck!\n')
    
    try:
        start = int(input('Type 1 to begin the game:'))
        
        if (start == 1):
            print('THE GAME HAS STARTED\n')
            
            try:
                begin_toss = int(input('Type 0 to toss the coin!:'))            
                
                if (begin_toss == 0):
                    toss = randint(1,2)
                    
                    if (toss==1):
                        print('YOU BAT FIRST!\n')
                        user_total_runs=user_batting()
                        print('COMPUTER BATS NOW!\n')
                        comp_total_runs=comp_batting()
                    else:
                        print('COMPUTER BATS FIRST!\n')
                        comp_total_runs=comp_batting()
                        print('YOU BAT NOW!\n')
                        user_total_runs=user_batting()
                    
                    print(f'YOU SCORED {user_total_runs} runs!')
                    print(f'COMPUTER SCORED {comp_total_runs} runs!')
                    
                    if user_total_runs>comp_total_runs:
                        user_win_by = user_total_runs-comp_total_runs                
                        print(f'YOU WON BY {user_win_by} RUNS!')
                                
                    elif (comp_total_runs>user_total_runs):
                        comp_win_by= comp_total_runs-user_total_runs
                        print(f'COMPUTER WINS BY {comp_win_by} RUNS!')
                        print('Better luck next time!')
                    else:
                        print('MATCH TIED!')
                        
                else:
                    cricket()
                    
            except ValueError as x:
                cricket()
            except Exception as y:
                cricket()
                            
        else:
            cricket()
            
    except ValueError as x:
        cricket()        
    except Exception as y:
        cricket()
  



if __name__=="__main__":
    cricket()
