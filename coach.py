import numpy as np
import copy

positions = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
roster = []
names_of_positions = {1:'rover',2:'catcher',3:'1st base',4:'2nd base',5:'3rd base',6:'shortstop',7:'leftfield',8:'centerfield',9:'rightfield'}

def new_player():
    print '\nADDING SOFTBALL PLAYER\n'
    person = raw_input('    Player Name: ')
    roster.append(person)
    
    print '\nCHOOSE A FEW POSITIONS'
    print '   1. rover'
    print '   2. catcher'
    print '   3. 1st base'
    print '   4. 2nd base'
    print '   5. 3rd base'
    print '   6. shortstop'
    print '   7. leftfield'
    print '   8. centerfield'
    print '   9. rightfield'
    print '   10. Anywhere...'
    pos = eval(raw_input('\n    Positions: '))
    
    if pos == 10:
        pos = np.arange(1,10)

    if type(pos) == int:
        positions[pos].append(person)
    else:    
        for p in list(pos):
            positions[p].append(person)
            
            
def inning():
    sitting = np.random.choice(roster,replace=False,size=len(roster)-9)
    unassigned = roster[:]
    fielders = copy.deepcopy(positions)

    for sit in sitting:
        unassigned.remove(sit)
        for p in np.arange(1,10):
            if sit in fielders[p]:
                fielders[p].remove(sit)
                
    takefield = {}
    
    for p in np.arange(1,10):

        if len(fielders[p]) == 1:
            f = fielders[p][0]
            takefield[p] = f
            for i in np.arange(p,10):
                if f in fielders[i]:
                    fielders[i].remove(f)
            unassigned.remove(f)
            
        elif len(fielders[p]) > 1:
            f = np.random.choice(fielders[p])
            takefield[p] = f
            for i in np.arange(p,10):
                if f in fielders[i]:
                    fielders[i].remove(f)
            unassigned.remove(f)
            
        else:
            takefield[p] = 'NEED VOLUNTEER'
            
    print '\nSITTING: '
    for sit in sitting: print sit
            
    print '\nTAKE THE FIELD!\n'#,takefield
    for p in np.arange(1,10):
        print takefield[p],':\t', names_of_positions[p]

    print '\nUNASSIGNED: '
    for un in unassigned: print un


#-------------------------------------------
#for testing inning function
#roster = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
#positions = {1: ['a', 'b', 'c', 'j', 'k', 'l'], 2: ['a', 'b', 'c', 'd', 'k', 'l'], 3: ['a', 'b', 'c', 'd', 'e', 'l'], 4: ['a', 'b', 'd', 'e', 'f', 'l'], 5: ['a', 'b', 'e', 'f', 'g', 'l', 'm', 'n'], 6: ['a', 'b', 'f', 'g', 'h', 'l', 'm', 'n'], 7: ['a', 'b', 'g', 'h', 'i', 'l'], 8: ['a', 'b', 'h', 'i', 'j', 'l'], 9: ['a', 'b', 'i', 'j', 'k', 'l']}
    
