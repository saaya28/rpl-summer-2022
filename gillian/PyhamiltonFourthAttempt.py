#########################Fourth Assembly with pipette volume edits and hso file splitting edits########################################

from liquidhandling import SoloSoft, SoftLinx
from liquidhandling import Plate_96_Corning_3635_ClearUVAssay

'''
This code makes the required hso files that will be called in 
next section
The code for this is divided into 3 sections:
- making the dilution plate
- transferring cells into the final assay
- transferring nutrients from dilution plate to final assay plate
'''

#declaring variables used throughout protocol
assay = "Position4"
cells = "Position5"
tips = "Position3"
dilution = "Position6"
stock = "Position1"
dispenseHeight = 2
aspirateHeight = 2
syringeSpeed = 50
cells_volume = 80

plate_list= [
        "Empty",
        "Empty",
        "TipBox.50uL.Axygen-EV-50-R-S.tealbox",
        "Plate.96.Corning-3635.ClearUVAssay", 
        "Empty",
        "Plate.96.Corning-3635.ClearUVAssay",
        "Plate.96.Corning-3635.ClearUVAssay", #actually liquid waste,
        "Empty",
   ]


#making dilution plate
############################M9 media into dilution plate#############################
rows = ["A", "B", "C", "D", "E", "F", "G", "H"]

'''Phosphorus columns (stock is 10X)
Rows 1-2 should have no media
Rows 3-4 should have 600 uL media
Rows 5-6 should have 900 uL media
Rows 7-8 should have 1050 uL media

'''

#run this hso twice#
soloSoft = SoloSoft(
    filename = "dilution_P_M9_1.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(position=tips, num_tips=2)

for j in range(1,4):
    for row in rows[2::2]:
        for i in range(1,3):
            x = [1, 1.5, 1.75]
            transfer_volume = 100 * x[rows[2::2].index(row)] 
            soloSoft.aspirate(
                position = stock,
                aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, i+6, transfer_volume),
                aspirate_shift = [0, 0, 2],
                ##aspirate_height = aspirateHeight,
                syringe_speed = syringeSpeed,        
                )    
            soloSoft.dispense(
                position = dilution,
                dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, i, transfer_volume),
                dispense_shift = [0, 0, 2],
                ##dispense_height = dispenseHeight,
                syringe_speed = syringeSpeed,
                )

soloSoft.shuckTip()

soloSoft.savePipeline()

'''Carbon columns
C1 cells should have no media
C2 cells should have 600 ul media
C3 cells should have 900 uL media
C4 cells should have 1050 uL media
'''

#C2#
soloSoft = SoloSoft(
    filename = "dilution_C_M9_1.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(position=tips, num_tips=1)

for j in range(1,5):
    for row in rows[1::2]:
        for i in range(3,5):
            transfer_volume = 150
            soloSoft.aspirate(
                position = stock,    
                aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, i+6, transfer_volume),
                aspirate_shift = [0, 0, 2],
               # #aspirate_height = aspirateHeight,
                syringe_speed = syringeSpeed,        
                )    
            soloSoft.dispense(
                position = dilution,
                dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, i, transfer_volume),
                dispense_shift = [0, 0, 2],
               # #dispense_height = dispenseHeight,
                syringe_speed = syringeSpeed,
                )

soloSoft.shuckTip()

soloSoft.savePipeline()

#C3#
soloSoft = SoloSoft(
    filename = "dilution_C_M9_2.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(position=tips, num_tips=1)

for j in range(1,6):
    for row in rows[::2]:
        for i in range(5,7):
            transfer_volume = 180
            soloSoft.aspirate(
                position = stock,    
                aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, i+6, transfer_volume),
                aspirate_shift = [0, 0, 2],
                #aspirate_height = aspirateHeight,
                syringe_speed = syringeSpeed,        
                )    
            soloSoft.dispense(
                position = dilution,
                dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, i, transfer_volume),
                dispense_shift = [0, 0, 2],
                ##dispense_height = dispenseHeight,
                syringe_speed = syringeSpeed,
                )

soloSoft.shuckTip()

soloSoft.savePipeline()

#C4#
soloSoft = SoloSoft(
    filename = "dilution_C_M9_3.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(position=tips, num_tips=1)

for j in range(1,7):
    for row in rows[1::2]:
        for i in range(5,7):
            transfer_volume = 175
            soloSoft.aspirate(
                position = stock,    
                aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, i+6, transfer_volume),
                aspirate_shift = [0, 0, 2],
                #aspirate_height = aspirateHeight,
                syringe_speed = syringeSpeed,        
                )    
            soloSoft.dispense(
                position = dilution,
                dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, i, transfer_volume),
                dispense_shift = [0, 0, 2],
                #dispense_height = dispenseHeight,
                syringe_speed = syringeSpeed,
                )

soloSoft.shuckTip()

soloSoft.savePipeline()

'''Nitrogen columns
column 7 should have no media
column 8 should have 600 uL media
column 9 should have 900 uL media
column 10 should have 1050 uL media
column 11 should have 1125 uL media
'''

soloSoft = SoloSoft(
    filename = "dilution_N_M9_1.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(tips)

#N2#
for j in range(1,5):
    transfer_volume = 150
    soloSoft.aspirate(
        position = stock,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(8, transfer_volume),
        aspirate_shift = [0, 0, 2],
        #  #aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,        
        )
    soloSoft.dispense(
        position = dilution,
        dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(8, transfer_volume),
        dispense_shift = [0, 0, 2],
        #  #dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        )

#N3#
for j in range(1,6):
    transfer_volume = 180
    soloSoft.aspirate(
        position = stock,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(9, transfer_volume),
        aspirate_shift = [0, 0, 2],
        #  #aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,        
        )
    soloSoft.dispense(
        position = dilution,
        dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(9, transfer_volume),
        dispense_shift = [0, 0, 2],
        #  #dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        )

soloSoft.shuckTip()

soloSoft.savePipeline()

soloSoft = SoloSoft(
    filename = "dilution_N_M9_2.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(tips)

#N4#
for j in range(1,7):
    transfer_volume = 175
    soloSoft.aspirate(
        position = stock,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(10, transfer_volume),
        aspirate_shift = [0, 0, 2],
        #  #aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,        
        )
    soloSoft.dispense(
        position = dilution,
        dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(10, transfer_volume),
        dispense_shift = [0, 0, 2],
        #  #dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        )

#N5#
for j in range(1,10):
    transfer_volume = 125
    soloSoft.aspirate(
        position = stock,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(11, transfer_volume),
        aspirate_shift = [0, 0, 2],
        #  #aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,        
        )
    soloSoft.dispense(
        position = dilution,
        dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(11, transfer_volume),
        dispense_shift = [0, 0, 2],
        #  #dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        )

soloSoft.shuckTip()

soloSoft.savePipeline()

############################Treatments into dilution plate#############################
rows = ["A", "B", "C", "D", "E", "F", "G", "H"]

#Phosphorus
#P1 at 10X, P2 at 5X, P3 at 2.5X, P4 at 1.25X
soloSoft = SoloSoft(
    filename = "dilution_P_treatment_1.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(position=tips, num_tips=2)

transfer_volume = 150

#for P4#
for i in range(1,3):
    soloSoft.aspirate(
        position = stock,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell('G', 5, transfer_volume),
        aspirate_shift = [0, 0, 2],
        #aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,        
        )    
    soloSoft.dispense(
        position = dilution,
        dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell('G', i, transfer_volume),
        dispense_shift = [0, 0, 2],
        #dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        )

#for P3#
for j in range(1,3):
    for i in range(1,3):
        soloSoft.aspirate(
            position = stock,
            aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell('E', 5, transfer_volume),
            aspirate_shift = [0, 0, 2],
            #aspirate_height = aspirateHeight,
            syringe_speed = syringeSpeed,        
            )    
        soloSoft.dispense(
            position = dilution,
            dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell('E', i, transfer_volume),
            dispense_shift = [0, 0, 2],
            #dispense_height = dispenseHeight,
            syringe_speed = syringeSpeed,
            )

#for P2#
for j in range(1,5):
    for i in range(1,3):
        soloSoft.aspirate(
            position = stock,
            aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell('C', 5, transfer_volume),
            aspirate_shift = [0, 0, 2],
            #aspirate_height = aspirateHeight,
            syringe_speed = syringeSpeed,        
            )    
        soloSoft.dispense(
            position = dilution,
            dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell('C', i, transfer_volume),
            dispense_shift = [0, 0, 2],
            #dispense_height = dispenseHeight,
            syringe_speed = syringeSpeed,
            )

soloSoft.shuckTip()

soloSoft.savePipeline()

soloSoft = SoloSoft(
    filename = "dilution_P_treatment_2.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(position=tips, num_tips=2)

transfer_volume = 150

#for P1#
for j in range(1,9):
    for i in range(1,3):
        soloSoft.aspirate(
            position = stock,
            aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell('A', 5, transfer_volume),
            aspirate_shift = [0, 0, 2],
            #aspirate_height = aspirateHeight,
            syringe_speed = syringeSpeed,        
            )    
        soloSoft.dispense(
            position = dilution,
            dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell('A', i, transfer_volume),
            dispense_shift = [0, 0, 2],
            #dispense_height = dispenseHeight,
            syringe_speed = syringeSpeed,
            )

soloSoft.shuckTip()

soloSoft.savePipeline()

#Carbon
soloSoft = SoloSoft(
    filename = "dilution_C_treatment_1.hso",
    plateList = plate_list,
    )

soloSoft.getTip(position=tips, num_tips=1)

#prepping C4 cells (1.25X)#
for row in rows[1::2]:
    for i in range(5,7):
        transfer_volume = 150
        soloSoft.aspirate(
            position = stock,    
            aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, 1, transfer_volume),
            aspirate_shift = [0, 0, 2],
            #aspirate_height = aspirateHeight,
            syringe_speed = syringeSpeed,        
            )    
        soloSoft.dispense(
            position = dilution,
            dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, i, transfer_volume),
            dispense_shift = [0, 0, 2],
            #dispense_height = dispenseHeight,
            syringe_speed = syringeSpeed,
            )

#prepping C3 cells (2.5X)
for j in range(1,3):
    for row in rows[::2]:
        for i in range(5,7):
            transfer_volume = 150
            soloSoft.aspirate(
                position = stock,    
                aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, 1, transfer_volume),
                aspirate_shift = [0, 0, 2],
                #aspirate_height = aspirateHeight,
                syringe_speed = syringeSpeed,        
                )    
            soloSoft.dispense(
                position = dilution,
                dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, i, transfer_volume),
                dispense_shift = [0, 0, 2],
                #dispense_height = dispenseHeight,
                syringe_speed = syringeSpeed,
                )

soloSoft.shuckTip()

soloSoft.savePipeline()

#prepping C2 cells (5X)
soloSoft = SoloSoft(
    filename = "dilution_C_treatment_2.hso",
    plateList = plate_list,
    )

soloSoft.getTip(position=tips, num_tips=1)

for j in range(1,5):
    for row in rows[1::2]:
        for i in range(3,5):
            transfer_volume = 150
            soloSoft.aspirate(
                position = stock,    
                aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, 1, transfer_volume),
                aspirate_shift = [0, 0, 2],
                #aspirate_height = aspirateHeight,
                syringe_speed = syringeSpeed,        
                )    
            soloSoft.dispense(
                position = dilution,
                dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, i, transfer_volume),
                dispense_shift = [0, 0, 2],
                #dispense_height = dispenseHeight,
                syringe_speed = syringeSpeed,
                )

soloSoft.shuckTip()

soloSoft.savePipeline()

soloSoft = SoloSoft(
    filename = "dilution_C_treatment_3.hso",
    plateList = plate_list,
    )

soloSoft.getTip(position=tips, num_tips=1)

#prepping C1 cells (10X)
for j in range(1,5):
    for row in rows[::2]:
        for i in range(3,5):
            transfer_volume = 150
            soloSoft.aspirate(
                position = stock,    
                aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, 1, transfer_volume),
                aspirate_shift = [0, 0, 2],
             #   #aspirate_height = aspirateHeight,
                syringe_speed = syringeSpeed,        
                )    
            soloSoft.dispense(
                position = dilution,
                dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, i, transfer_volume),
                dispense_shift = [0, 0, 2],
            #    #dispense_height = dispenseHeight,
                syringe_speed = syringeSpeed,
                )

soloSoft.shuckTip()

soloSoft.savePipeline()

soloSoft = SoloSoft(
    filename = "dilution_C_treatment_3.2.hso",
    plateList = plate_list,
    )

soloSoft.getTip(position=tips, num_tips=1)

#prepping C1 cells part 2 (10X)
for j in range(1,5):
    for row in rows[::2]:
        for i in range(3,5):
            transfer_volume = 150
            soloSoft.aspirate(
                position = stock,    
                aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, 1, transfer_volume),
                aspirate_shift = [0, 0, 2],
             #   #aspirate_height = aspirateHeight,
                syringe_speed = syringeSpeed,        
                )    
            soloSoft.dispense(
                position = dilution,
                dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setCell(row, i, transfer_volume),
                dispense_shift = [0, 0, 2],
            #    #dispense_height = dispenseHeight,
                syringe_speed = syringeSpeed,
                )

soloSoft.shuckTip()

soloSoft.savePipeline()

#Nitrogen
#N1 should be 20X (1200 uL),N2 should be 10X (600 uL), N3 should be 5X (300 uL), N4 should be 2.5X (150 uL), N5 should be 1.25X (75 uL)

soloSoft = SoloSoft(
    filename = "dilution_N_treatment_1.hso",
    plateList = plate_list,
    ) 

transfer_volume = 150

soloSoft.getTip(tips) 
#### N5#####
# #75 uL#
soloSoft.aspirate(
    position = stock,
    aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(3, transfer_volume*0.5),
    aspirate_shift = [0, 0, 2],
    aspirate_height = aspirateHeight,
    syringe_speed = syringeSpeed,
    ) 

soloSoft.dispense(
    position = assay,
    dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(11, transfer_volume*0.5),
    dispense_shift = [0, 0, 2],
    dispense_height = dispenseHeight,
    syringe_speed = syringeSpeed,
    )

### N4###
#150 uL#
soloSoft.aspirate(
    position = stock,
    aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(3, transfer_volume),
    aspirate_shift = [0, 0, 2],
    aspirate_height = aspirateHeight,
    syringe_speed = syringeSpeed,        
    )

soloSoft.dispense(
    position = dilution,
    dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(10, transfer_volume),
    dispense_shift = [0, 0, 2],
    dispense_height = dispenseHeight,
    syringe_speed = syringeSpeed,
    )

###N3####
for j in range(1,3):
    soloSoft.aspirate(
        position = stock,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(3, transfer_volume),
        aspirate_shift = [0, 0, 2],
        aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,        
        )
    soloSoft.dispense(
        position = dilution,
        dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(9, transfer_volume),
        dispense_shift = [0, 0, 2],
        dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        )

soloSoft.shuckTip()

soloSoft.savePipeline() 

###N2####
soloSoft = SoloSoft(
    filename = "dilution_N_treatment_2.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(tips) 

for j in range(1,5):
    transfer_volume = 150
    soloSoft.aspirate(
        position = stock,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(3, transfer_volume),
        aspirate_shift = [0, 0, 2],
        aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,        
        )
    soloSoft.dispense(
        position = dilution,
        dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(8, transfer_volume),
        dispense_shift = [0, 0, 2],
        dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        )

soloSoft.shuckTip()

soloSoft.savePipeline()

######N1#######
soloSoft = SoloSoft(
    filename = "dilution_N_treatment_3.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(tips)

for j in range(1,9):
    transfer_volume = 150
    soloSoft.aspirate(
        position = stock,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(3, transfer_volume),
        aspirate_shift = [0, 0, 2],
        aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,        
        )
    soloSoft.dispense(
        position = dilution,
        dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(7, transfer_volume),
        dispense_shift = [0, 0, 2],
        dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        )

soloSoft.shuckTip()

soloSoft.savePipeline()

##############################making control#####################################
'''
The following code makes the control column on the dilution plate (control means 1x of every nutrient and no cells)
'''

soloSoft = SoloSoft(
    filename = "dilution_control.hso",
    plateList = plate_list,
    ) 

#M9#
soloSoft.getTip(tips)

for i in range(1,6):
    soloSoft.aspirate(
        position = stock,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(12, 180),
        aspirate_shift = [0, 0, 2],
        ##aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,
        )
    soloSoft.dispense(
        position = dilution,
        dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(12, 180),
        dispense_shift = [0, 0, 2],
        #dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        )

soloSoft.shuckTip()

#C#
c_control_volume = 120

soloSoft.getTip(tips)

soloSoft.aspirate(
    position = stock,
    aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(2, c_control_volume),
    aspirate_shift = [0, 0, 2],
    ##aspirate_height = aspirateHeight,
    syringe_speed = syringeSpeed,
    )
soloSoft.dispense(
    position = dilution,
    dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(12, c_control_volume),
    dispense_shift = [0, 0, 2],
    ##dispense_height = dispenseHeight,
    syringe_speed = syringeSpeed,
    )

soloSoft.shuckTip()

#P#
p_control_volume = 120

soloSoft.getTip(tips)

soloSoft.aspirate(
    position = stock,
    aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(6, p_control_volume),
    aspirate_shift = [0, 0, 2],
    #aspirate_height = aspirateHeight,
    syringe_speed = syringeSpeed,
    )
soloSoft.dispense(
    position = dilution,
    dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(12, p_control_volume),
    dispense_shift = [0, 0, 2],
    #dispense_height = dispenseHeight,
    syringe_speed = syringeSpeed,
    )

soloSoft.shuckTip()

#N#
n_control_volume = 60

soloSoft.getTip(tips)

soloSoft.aspirate(
    position = stock,
    aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(4, n_control_volume),
    aspirate_shift = [0, 0, 2],
    #aspirate_height = aspirateHeight,
    syringe_speed = syringeSpeed,
    )
soloSoft.dispense(
    position = dilution,
    dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(12, n_control_volume),
    dispense_shift = [0, 0, 2],
    #dispense_height = dispenseHeight,
    syringe_speed = syringeSpeed,
    )

soloSoft.shuckTip()

#############################cells to assay##########################
'''
The following code transfers cells to the final assay plate
'''

soloSoft = SoloSoft(
    filename = "cells_assay_1.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(tips)

for i in range(1,6):   
    soloSoft.aspirate(
        position = cells,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(i, cells_volume),
        aspirate_shift = [0, 0, 2],
        ##aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,
        )
    soloSoft.dispense(
        position = assay,
        dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(i, cells_volume),
        dispense_shift = [0, 0, 2],
        #dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        )

soloSoft.shuckTip()

soloSoft.savePipeline() 

soloSoft = SoloSoft(
    filename = "cells_assay_2.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(tips)

for i in range(7,12):   
    soloSoft.aspirate(
        position = cells,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(i, cells_volume),
        aspirate_shift = [0, 0, 2],
        ##aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,
        )
    soloSoft.dispense(
        position = assay,
        dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(i, cells_volume),
        dispense_shift = [0, 0, 2],
        #dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        )

soloSoft.shuckTip()

soloSoft.savePipeline() 

#dilution to assay
for j in range(1,3):
    soloSoft.getTip(tips)
    soloSoft.aspirate(
        position = dilution,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(12, 180),
        aspirate_shift = [0, 0, 2],
        #aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,
        )
    for i in [6,12]:
        soloSoft.dispense(
            position = assay,
            dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(i, 90),
            dispense_shift = [0, 0, 2],
            #dispense_height = dispenseHeight,
            syringe_speed = syringeSpeed,
            )
    soloSoft.shuckTip()

soloSoft.savePipeline()

################################################################

'''
The following code transfers nutrients to the final assay plate
'''

##############Dilution assay######## 
########Phosphorus########
#######Starting new SoloSoft for phosphorus on the assay plate#####

soloSoft = SoloSoft(
    filename = "dilution_assayP1.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(tips)

transfer_volume = 20

#for i in range(1,6):
for i in range(1,3):
    soloSoft.aspirate(
        position = dilution,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(1, transfer_volume*5),
        aspirate_shift = [0, 0, 2],
        #aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,
        ) 
    for i in range(1,6):
        #if i!= 6:
        soloSoft.dispense(
            position = assay,
            dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(i, transfer_volume),
            dispense_shift = [0, 0, 2],
            #dispense_height = dispenseHeight,
            syringe_speed = syringeSpeed,
            )

for i in range(1,3):
    soloSoft.aspirate(
        position = dilution,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(2, transfer_volume*5),
        aspirate_shift = [0, 0, 2],
        #aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,
        ) 
    for i in range(7,12):
        #if i!= 6:
        soloSoft.dispense(
            position = assay,
            dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(i, transfer_volume),
            dispense_shift = [0, 0, 2],
            #dispense_height = dispenseHeight,
            syringe_speed = syringeSpeed,
            )

soloSoft.savePipeline() 

##########Carbon####### 
#######Starting a new SoloSoft for carbon on the first half of the assay plate######
soloSoft = SoloSoft(
    filename = "dilution_assayC1.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(tips)

transfer_volume = 20 

for i in range(1,3):
    soloSoft.aspirate(
        position = dilution,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(3, transfer_volume*5),
        aspirate_shift = [0, 0, 2],
        #aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,
        ) 
    for i in reversed(range(1,6)):
        soloSoft.dispense(
            position = assay,
            dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(i, transfer_volume),
            dispense_shift = [0, 0, 2],
            #dispense_height = dispenseHeight,
            syringe_speed = syringeSpeed,
            )

soloSoft.shuckTip()

soloSoft.savePipeline() 

#######Starting a new SoloSoft for carbon on the second half of the assay plate######
soloSoft = SoloSoft(
    filename = "dilution_assayC2.hso",
    plateList = plate_list,
    ) 

soloSoft.getTip(tips)

transfer_volume = 20 

for i in range(1,3):
    soloSoft.aspirate(
        position = dilution,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(5, transfer_volume*5),
        aspirate_shift = [0, 0, 2],
        #aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,
        ) 
    for i in reversed(range(7,12)):
        soloSoft.dispense(
            position = assay,
            dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(i, transfer_volume),
            dispense_shift = [0, 0, 2],
            #dispense_height = dispenseHeight,
            syringe_speed = syringeSpeed,
            )

soloSoft.shuckTip()

soloSoft.savePipeline() 

#######Nitrogen############ 
#######Starting a new SoloSoft for nitrogen on the first half of the assay plate######

soloSoft = SoloSoft(
    filename = "dilution_assayN1.hso",
    plateList = plate_list,
    ) 

for i in reversed(range(1,6)):
    soloSoft.getTip(tips)
    transfer_volume = 40 
    soloSoft.aspirate(
        position = dilution,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(i+6, transfer_volume),
        aspirate_shift = [0, 0, 2],
        #aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,
        ) 
    soloSoft.dispense(
        position = assay,
        dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(i, transfer_volume),
        dispense_shift = [0, 0, 2],
        #dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        )
    soloSoft.shuckTip()

soloSoft.savePipeline() 

#######Starting a new SoloSoft for nitrogen on the second half of the assay plate######
soloSoft = SoloSoft(
    filename = "dilution_assayN2.hso",
    plateList = plate_list,
    ) 

for i in reversed(range(7,12)):
    soloSoft.getTip(tips)
    transfer_volume = 40 
    soloSoft.aspirate(
        position = dilution,
        aspirate_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(i, transfer_volume),
        aspirate_shift = [0, 0, 2],
        #aspirate_height = aspirateHeight,
        syringe_speed = syringeSpeed,
        ) 
    soloSoft.dispense(
        position = assay,
        dispense_volumes = Plate_96_Corning_3635_ClearUVAssay().setColumn(i, transfer_volume),
        dispense_shift = [0, 0, 2],
        #dispense_height = dispenseHeight,
        syringe_speed = syringeSpeed,
        )
    soloSoft.shuckTip()

soloSoft.savePipeline() 

##############################################################
'''
This is the Softlinx part of the code that entails the crane 
movements as well as the execution of the hso files
'''

softLinx = SoftLinx("Third_attempt", "Third_attempt.slvp") # display name, path to saves
softLinx.setPlates({"SoftLinx.PlateCrane.Stack5": "Plate_96_Corning_3635_ClearUVAssay", "SoftLinx.PlateCrane.Stack4":"TipBox.50uL.Axygen-EV-50-R-S.tealbox"})
#this is hwere you would softlinx run solo stuff, preparing diltuion stock (fill stuff in)###############
list_of_dilution = ["dilution_P_M9.hso","dilution_C_M9.hso","dilution_N_M9.hso","dilution_P_main.hso","dilution_C_main.hso","dilution_N_main.hso","dilution_control.hso"]
for c in list_of_dilution:
    softLinx.soloSoftRun(c)
softLinx.plateCraneMovePlate(["SoftLinx.PlateCrane.Stack5"],["SoftLinx.Solo.Position4"],poolID = 5)
softLinx.plateCraneRemoveLid(["SoftLinx.Solo.Position4"],["SoftLinx.PlateCrane.LidNest2"])
softLinx.plateCraneMovePlate(["SoftLinx.PlateCrane.Stack4"],["SoftLinx.Solo.Position3"],poolID = 4)
#prep the first assay plate###### 
list_of_final = ["dilution_assayP1.hso","cells_assay1.hso","cells_assay2.hso","dilution_assayC1.hso","dilution_assayC2.hso",
"dilution_assayN1.hso","dilution_assayN2.hso"]
for c in list_of_final:
    softLinx.soloSoftRun(c)
softLinx.plateCraneMovePlate(["SoftLinx.Solo.Position4"],["SoftLinx.Hidex.Nest"])
softLinx.plateCraneMoveCrane("SoftLinx.PlateCrane.Safe")
softLinx.hidexRun("pyhamilton")
softLinx.plateCraneMovePlate(["SoftLinx.Hidex.Nest"],["SoftLinx.Liconic.Nest"])
softLinx.plateCraneReplaceLid(["SoftLinx.PlateCrane.LidNest2"],["SoftLinx.Liconic.Nest"])
softLinx.liconicLoadIncubator(loadID=1)
