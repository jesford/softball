import numpy as np
import copy

class Team:

    names_of_positions = {1:'rover',2:'catcher',3:'1st base',4:'2nd base',5:'3rd base',6:'shortstop',7:'leftfield',8:'centerfield',9:'rightfield'}
    
    def __init__(self):
        self.numPlayers = 0
        self.describe = 'This is a softball team.'
        self.positions = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
        self.roster = []

    def regulars(self):
        reg = {'Jes':[7,1],'Lee':[6],'Jason':[8,6],'Amanda':[2,3,4,5]}
        self.numPlayers += len(reg)
        for regPlayer in reg:
            self.roster.append(regPlayer)
            for p in reg[regPlayer]:
                self.positions[p].append(regPlayer)
        
    def add(self):
        self.numPlayers += 1
        
        print '\nADDING NEW SOFTBALL PLAYER'
        player = get_name()
        self.roster.append(player)
        
        pos = get_positions()
        
        if type(pos) == int:
            self.positions[pos].append(player)
        else:    
            for p in list(pos):
                self.positions[p].append(player)

    def remove(self):
        self.numPlayers -= 1
        
        print '\nREMOVING SOFTBALL PLAYER'
        player = get_name()
        self.roster.remove(player)

        for i in np.arange(1,10):
            if player in self.positions[i]:
                self.positions[i].remove(player)
        
    def inning(self):
        new_inning(self.roster,self.positions,self.names_of_positions)

                
def get_name():
    return raw_input('    Player Name: ')

def get_positions():
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
    p = eval(raw_input('\n    Positions: '))
    if p == 10:
        p = np.arange(1,10)
    return p
  

def new_inning(roster,positions,names):
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
        print takefield[p],':\t', names[p]

    print '\nUNASSIGNED: '
    for un in unassigned: print un

   
