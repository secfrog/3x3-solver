import kociemba
import ast

def solve():
    with open('assets/config/CubeState.txt', 'r') as cube:
        cf = cube.read()
        
    lines = cf.strip().splitlines()
    k = []

    for line in lines:
        try:
            # Convert the line into a Python list using ast.literal_eval()
            parsed_list = ast.literal_eval(line.strip())
            # Append the parsed list to the master list
            k.append(parsed_list)
        except (ValueError, SyntaxError) as e:
            # If there's an error parsing the line, print it for debugging
            print(f"Error parsing line: {line}\n{e}")

    print(k)

    '''
    solved k belike
    k = [   
            [['U1', 'U2', 'U3'], ['U4', 'U5', 'U6'], ['U7', 'U8', 'U9']], 
            [['R1', 'R2', 'R3'], ['R4', 'R5', 'R6'], ['R7', 'R8', 'R9']], 
            [['F1', 'F2', 'F3'], ['F4', 'F5', 'F6'], ['F7', 'F8', 'F9']], 
            [['D1', 'D2', 'D3'], ['D4', 'D5', 'D6'], ['D7', 'D8', 'D9']], 
            [['L1', 'L2', 'L3'], ['L4', 'L5', 'L6'], ['L7', 'L8', 'L9']], 
            [['B1', 'B2', 'B3'], ['B4', 'B5', 'B6'], ['B7', 'B8', 'B9']],
        ]
    '''
    color_mapping = {
        'yellow':'U',
        'blue':'R',
        'orange':'F',
        'white':'D',
        'green':'L',
        'red':'B',
    }
    print(color_mapping.get('blue'))

    kociemba_problem = ''
    try:
        for z in range(6):
            for y in range(3):
                for x in range(3):
                    p = k[z][y][x]
                    p = color_mapping.get(p)
                    kociemba_problem += p
    except:
        print('check cube and try again')

    print(kociemba_problem)
    print(len(kociemba_problem))

    try:
        solution = kociemba.solve(kociemba_problem)
        print(solution)
    except:
        print('probably cubestring is invalid')
