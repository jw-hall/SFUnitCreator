import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'S&F Unit Creator'
        self.left = 500
        self.top = 500
        self.width = 320
        self.height = 100
        self.ancestry = ['Human']
        self.exp = ['Green']
        self.eq = ['Light']
        self.utype = ['Infantry']
        self.usize = ['1d4']
        self.name = ['Unit Name']
        print(self.ancestry)
        self.trait_name = [' ',' ',' ']
        self.trait_desc = [' ',' ',' ']
        self.stat_tot = [7]
        self.cost = [130]
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createGridLayout()
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        self.setWindowIcon(QIcon('MCDM2.png'))  
        self.show()
        
    def calc(self):
        trait_Amph_name = 'Amphibious'
        trait_Amph_desc = 'This unit does not suffer terrain penalties for fighting in water or on land.'

        trait_Bred_name = 'Bred for War'
        trait_Bred_desc = 'This unit cannot be diminished, and cannot have disadvantage on Morale checKs.'

        trait_Brut_name = 'Brutal'
        trait_Brut_desc = 'This unit inflicts 2 casualties on  a successful Power check.'

        trait_Cour_name = 'Courageous'
        trait_Cour_desc = 'Once per battle, this unit can choose to succeed on a Morale check it just failed.'

        trait_Eter_name = 'Eternal'
        trait_Eter_desc = 'This unit cannot be horrified, and it always succeeds on Morale checks to attack undead and fiends.'

        trait_Fren_name = 'Frenzy'
        trait_Fren_desc = 'If this unit diminishes an enemy unit, it immediately makes a free attack agains that unit.'

        trait_Horr_name = 'Horrify'
        trait_Horr_desc = 'If this unit inflicts a casualty on an enemy unit, that unit must make a DC 15 Morale check. Failure exhausts the unit.'

        trait_Mart_name = 'Martial'
        trait_Mart_desc = 'If this unit succeeds on a Power check and its size is greater than the defending unit, it inflicts 2 casualties.'

        trait_Mind_name = 'Mindless'
        trait_Mind_desc = 'This unit cannot fail Morale checks.'

        trait_Regen_name ='Regenerate'
        trait_Regen_desc = 'When this unit refreshes, increment its casualty die. This trait ceases to function if the unit suffers acasualty from battle magic.'

        trait_Rave_name = 'Ravenous'
        trait_Rave_desc = 'While any enemy unit is diminished, this unit can spend a round feeding on the corpses to increment their casualty die.'

        trait_Hurl_name = 'Hurl Rocks'
        trait_Hurl_desc = 'If this unit succeeds on an attack check, it inflicts 2 casualties. Against fortifications, it inflicts 1d6 casualties.'

        trait_Sava_name = 'Savage'
        trait_Sava_desc = 'This unit has advantage on the first attack check it makes each battle.'

        trait_Stal_name = 'Stalwart'
        trait_Stal_desc = 'Enemy battle magic has disadvantage on power checks against this unit.' 

        trait_Twis_name = 'Twisting Roots'
        trait_Twis_desc = 'As an action, this unit can sap the walls of a fortification. Siege units have advantage on Power checks against sapped fortifications.'

        trait_Unde_name = 'Undead'
        trait_Unde_desc = 'Green and regular troops must pass a Morale check to attack this unit. Each enemy unit need only do this once.'
        ancestry = self.ancestry[0]
        
        if ancestry == 'Human':
            stat_b = (2,0,0,0,1)
            trait = 50
            self.trait_name.clear()
            self.trait_name.insert(0, trait_Cour_name)
            self.trait_name.insert(1, '')
            self.trait_name.insert(2, '')
            print(self.trait_name)
            self.trait_desc.clear()
            self.trait_desc.insert(0, trait_Cour_desc)
            self.trait_desc.insert(1, '')
            self.trait_desc.insert(2, '')
        if ancestry == 'Bugbear':
            stat_b = (2,0,0,0,1)
            trait = 100
            self.trait_name.clear()
            self.trait_name.insert(0, trait_Mart_name)
            self.trait_name.insert(1, '')
            self.trait_name.insert(2, '')
            print(self.trait_name)
            self.trait_desc.clear()
            self.trait_desc.insert(0, trait_Mart_desc)
            self.trait_desc.insert(1, '')
            self.trait_desc.insert(2, '')
        if ancestry == 'Dragonborn':
            stat_b = (2,2,1,1,2)
            trait = 50
            self.trait_name.clear()
            self.trait_name.insert(0, trait_Cour_name)
            self.trait_name.insert(1, '')
            self.trait_name.insert(2, '')
            self.trait_desc.clear()
            self.trait_desc.insert(0, trait_Cour_desc)
            self.trait_desc.insert(1, '')
            self.trait_desc.insert(2, '')
        elif ancestry == 'Dwarf':
            stat_b = (3,1,1,1,2)
            trait = 50
            self.trait_name.clear()
            self.trait_name.insert(0, trait_Stal_name)
            self.trait_name.insert(1, '')
            self.trait_name.insert(2, '')
            self.trait_desc.clear()
            self.trait_desc.insert(0, trait_Stal_desc)
            self.trait_desc.insert(1, '')
            self.trait_desc.insert(2, '')
        elif ancestry == 'Elf':
            stat_b = (2,0,0,0,1)
            trait = 50
            self.trait_name.clear()
            self.trait_name.insert(0, trait_Eter_name)
            self.trait_name.insert(1, '')
            self.trait_name.insert(2, '')
            self.trait_desc.clear()
            self.trait_desc.insert(0, trait_Eter_desc)
            self.trait_desc.insert(1, '')
            self.trait_desc.insert(2, '')
        elif ancestry == 'Elf (Winged)':
            stat_b = (3,1,0,0,1)
            trait = 0
            self.trait_name.clear()
            self.trait_name.insert(0, trait_Eter_name)
            self.trait_name.insert(1, '')
            self.trait_name.insert(2, '')
            self.trait_desc.clear()
            self.trait_desc.insert(0, trait_Eter_desc)
            self.trait_desc.insert(1, '')
            self.trait_desc.insert(2, '')
        elif ancestry == 'Ghoul':
            stat_b = (-1,0,2,2,0)
            trait = 300
            self.trait_name.clear()
            self.trait_name.insert(0, trait_Unde_name)
            self.trait_name.insert(1, trait_Horr_name)
            self.trait_name.insert(2, trait_Rave_name)
            self.trait_desc.clear()
            self.trait_desc.insert(0, trait_Unde_desc)
            self.trait_desc.insert(1, trait_Horr_desc)
            self.trait_desc.insert(2, trait_Rave_desc)
        elif ancestry == 'Gnoll':
            stat_b = (2,0,0,0,1)
            trait = 50
            self.trait_name.clear()
            self.trait_name.insert(0, trait_Fren_name)
            self.trait_name.insert(1, '')
            self.trait_name.insert(2, '')
            self.trait_desc.clear()
            self.trait_desc.insert(0, trait_Fren_desc)
            self.trait_desc.insert(1, '')
            self.trait_desc.insert(2, '')
        elif ancestry == 'Gnome':
            stat_b = (1,-1,1,-1,1)
            trait = 0
        elif ancestry == 'Goblin':
            stat_b = (-1,-1,1,-1,0)
            trait = 0
        elif ancestry == 'Hobgoblin':
            stat_b = (2,0,0,0,1)
            trait = 100
            self.trait_name.clear()
            self.trait_name.insert(0, trait_Bred_name)
            self.trait_name.insert(1, trait_Mart_name)
            self.trait_name.insert(2, '')
            self.trait_desc.clear()
            self.trait_desc.insert(0, trait_Bred_desc)
            self.trait_desc.insert(1, trait_Mart_desc)
            self.trait_desc.insert(2, '')
        elif ancestry == 'Kobold':
            stat_b = (-1,-1,1,-1,-1)
            trait = 0
        elif ancestry == 'Lizardfolk':
            stat_b = (2,1,-1,1,1)
            trait = 50
            self.trait_name.clear()
            self.trait_name.insert(0, trait_Amph_name)
            self.trait_name.insert(1, '')
            self.trait_name.insert(2, '')
            self.trait_desc.clear()
            self.trait_desc.insert(0, trait_Amph_desc)
            self.trait_desc.insert(1, '')
            self.trait_desc.insert(2, '')
        elif ancestry == 'Ogre':
            stat_b = (0,2,0,2,1)
            trait = 200
            self.trait_name.clear()
            self.trait_name.insert(0, trait_Brut_name)
            self.trait_name.insert(1, '')
            self.trait_name.insert(2, '')
            self.trait_desc.clear()
            self.trait_desc.insert(0, trait_Brut_desc)
            self.trait_desc.insert(1, '')
            self.trait_desc.insert(2, '')
        elif ancestry == 'Orc':
            stat_b = (2,1,1,1,2)
            trait = 50
            self.trait_name.clear()
            self.trait_name.insert(0, trait_Sava_name)
            self.trait_name.insert(1, '')
            self.trait_name.insert(2, '')
            self.trait_desc.clear()
            self.trait_desc.insert(0, trait_Sava_desc)
            self.trait_desc.insert(1, '')
            self.trait_desc.insert(2, '')
        elif ancestry == 'Skeleton':
            stat_b = (-2,-1,1,1,1)
            trait = 150
            self.trait_name.clear()
            self.trait_name.insert(0, trait_Unde_name)
            self.trait_name.insert(1, trait_Mind_name)
            self.trait_name.insert(2, '')
            self.trait_desc.clear()
            self.trait_desc.insert(0, trait_Unde_desc)
            self.trait_desc.insert(1, trait_Mind_desc)
            self.trait_desc.insert(2, '')
            print(self.trait_name)
            print(self.trait_name[0])
            print(self.trait_name[1])
        elif ancestry == 'Treant':
            stat_b = (0,2,0,2,0)
            trait = 450
            self.trait_name.clear()
            self.trait_name.insert(0, trait_Twis_name)
            self.trait_name.insert(1, trait_Hurl_name)
            self.trait_name.insert(2, '')
            self.trait_desc.clear()
            self.trait_desc.insert(0, trait_Twis_desc)
            self.trait_desc.insert(1, trait_Hurl_desc)
            self.trait_desc.insert(2, '')
        elif ancestry == 'Troll':
            stat_b = (0,2,0,2,0)
            trait = 200
            self.trait_name.clear()
            self.trait_name.insert(0, trait_Regen_name)
            self.trait_name.insert(1, '')
            self.trait_name.insert(2, '')
            self.trait_desc.clear()
            self.trait_desc.insert(0, trait_Regen_desc)
            self.trait_desc.insert(1, '')
            self.trait_desc.insert(2, '')
        elif ancestry == 'Zombie':
            stat_b = (-2,0,2,2,2)
            trait = 150
            self.trait_name.clear()
            self.trait_name.insert(0, trait_Unde_name)
            self.trait_name.insert(1, trait_Mind_name)
            self.trait_name.insert(2, '')
            self.trait_desc.clear()
            self.trait_desc.insert(0, trait_Unde_desc)
            self.trait_desc.insert(1, trait_Mind_desc)
            self.trait_desc.insert(2, '')

        exp = self.exp[0]
        if exp == 'Green':
            stat_c = (0,0,0,0,0)
        elif exp == 'Regular':
            stat_c = (1,0,0,1,1)
        elif exp == 'Seasoned':
	        stat_c = (1,0,0,1,2)
        elif exp == 'Veteran':
	        stat_c = (1,0,0,1,3)
        elif exp == 'Elite':
	        stat_c = (1,0,0,1,4)
        elif exp == 'Super Elite':
	        stat_c = (1,0,0,1,5)

        eq = self.eq[0]
        if eq == 'Light':
	        stat_d = (0,1,1,0,0)
        elif eq == 'Medium':
            stat_d = (0,2,2,0,0)
        elif eq == 'Heavy':
            stat_d = (0,4,4,0,0)
        elif eq == 'Super-Heavy':
            stat_d = (0,6,6,0,0)

        utype = self.utype[0]
        if utype == 'Infantry':
            stat_e = (0,0,1,1,0)
            cost_mod = 1
        elif utype == 'Flying':
            stat_e = (0,0,0,0,3)
            cost_mod = 2
        elif utype == 'Archers':
            stat_e = (0,1,0,0,1)
            cost_mod = 1.75
        elif utype == 'Cavalry':
            stat_e = (1,1,0,0,2)
            cost_mod = 1.5
        elif utype == 'Levies':
            stat_e = (0,0,0,0,-1)
            cost_mod = 0.75
        elif utype == 'Siege Engine':
            stat_e = (1,1,0,1,0)
            cost_mod = 1.5

        size = self.usize[0]
        if size == '1d4':
           size_mod = 0.66
        if size == '1d6':
           size_mod = 1
        if size == '1d8':
           size_mod = 1.33
        if size == '1d10':
           size_mod = 1.66
        if size == '1d12':
           size_mod = 2
        if size == '1d20':
           size_mod = 2.33
        self.stat_tot.clear()   
        self.stat_tot.append ([sum(x) for x in zip(stat_b,stat_c,stat_d,stat_e)])
        print(self.stat_tot)
        print(self.stat_tot[0][0])
        self.cost.clear()
        costCalc = (int(round(((self.stat_tot[0][0] + self.stat_tot[0][2] + self.stat_tot [0][4]) + 2 * self.stat_tot[0][4]) * (cost_mod*size_mod*10) + 30 + trait, -1)))
        print(costCalc)
        self.cost.insert (0,costCalc)    
    def index_changed(self, i): # i is an int
        print(i)

    def ancestry_changed(self, s): # s is a str
        print(s)
        self.ancestry.clear()
        self.ancestry.insert(0, s)
        print(self.ancestry)
        
    def exp_changed(self, s): # s is a str
        print(s)
        self.exp.clear()
        self.exp.insert(0, s)
        print(self.exp)
    
    def eq_changed(self, s): # s is a str
        print(s)
        self.eq.clear()
        self.eq.insert(0, s)
        print(self.eq)
    
    def utype_changed(self, s): # s is a str
        print(s)
        self.utype.clear()
        self.utype.insert(0, s)
        print(self.utype)    
    
    def usize_changed(self, s): # s is a str
        print(s)
        self.usize.clear()
        self.usize.insert(0, s)
        print(self.usize)
    
    def name_changed(self, s): # s is a str
        print(s)
        self.name.clear()
        self.name.insert(0, s)
        print(self.name)    
    
    def Print(self):
        f = open(self.name[0] + '.txt', 'a')
        print(self.name[0] + '\n' + self.ancestry[0] + ' ' + self.exp[0] + ' ' + self.eq[0] + ' ' + self.utype[0] + '\n' 
              + 'Size: ' + self.usize[0] 
              + "\n" 'Attack: ' + '+' + str(self.stat_tot[0][0]) + "\n" 
              + 'Defense: ' + str(self.stat_tot[0][1]+10) + "\n" 
              + 'Power: ' + '+' + str(self.stat_tot[0][2]) + "\n" 
              + 'Toughness: '+ str(self.stat_tot[0][3]+10)+ "\n" 
              + 'Morale: ' + '+' + str(self.stat_tot[0][4])+ "\n" 
              + 'Cost: ' + str(self.cost) + " " + 'GP' + "\n" + "\n" 
              + self.trait_name[0] + "\n" + self.trait_desc[0] + "\n" + "\n"
              + self.trait_name[1] + "\n" + self.trait_desc[1] + "\n" + "\n"
              + self.trait_name[2] + "\n" + self.trait_desc[2], file=f)
        f.close()
            
    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("Grid")
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)
        
        widget = QComboBox()
        widget.addItems(["Human", "Bugbear", "Dragonborn","Dwarf","Elf","Elf (Winged)","Ghoul","Gnoll","Gnome","Goblin","Hobgoblin","Kobold","Lizardfolk","Ogre","Orc","Skeleton","Treant","Troll","Zombie"])
        widget.currentIndexChanged.connect( self.index_changed )
        widget.currentIndexChanged[str].connect(self.ancestry_changed)

        layout.addWidget(widget,0,0)
        
        widget = QComboBox()
        widget.addItems(["Green","Regular","Seasoned","Veteran","Elite","Super-Elite"])
        widget.currentIndexChanged.connect( self.index_changed )
        widget.currentIndexChanged[str].connect( self.exp_changed )
        layout.addWidget(widget,0,1)
        
        widget = QComboBox()
        widget.addItems(["Light","Medium","Heavy","Super-Heavy"])
        widget.currentIndexChanged.connect( self.index_changed )
        widget.currentIndexChanged[str].connect( self.eq_changed )
        layout.addWidget(widget,0,2)
        
        widget = QComboBox()
        widget.addItems(["Infantry","Flying","Archers","Cavalry","Levies","Siege Engine"])
        widget.currentIndexChanged.connect( self.index_changed )
        widget.currentIndexChanged[str].connect( self.utype_changed )
        layout.addWidget(widget,0,3)
        
        widget = QComboBox()
        widget.addItems(["1d4","1d6","1d8","1d10","1d12","1d20"])
        widget.currentIndexChanged.connect( self.index_changed )
        widget.currentIndexChanged[str].connect( self.usize_changed )
        layout.addWidget(widget,0,4)
  
        widget = QLineEdit()
        widget.textChanged[str].connect( self.name_changed )
        widget.textChanged[str].connect( self.calc )
        layout.addWidget(widget,1,0)
        
        button = QPushButton('Print')
        layout.addWidget(button)
        button.pressed.connect(self.Print)
        
        layout.addWidget(widget,1,1)
        
        self.horizontalGroupBox.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
