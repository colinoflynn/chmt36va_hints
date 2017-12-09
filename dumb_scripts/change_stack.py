# Dumb Script: Searches for a given partnumber, and overrides the
#              m-stack number. This can be useful when you have the same
#              board with different build options, but don't want to
#              change ALL of a current mstack to another one.


#This will override the given part number with mstack number
mlist = {'C1':18, #HPF-C1
         'C2':1,
         'C3':19, #HPF-C2
         'C4':20, #HPF-C3
         'C5':22, #HPF-L2
         'C6':21, #HPF-L1
         'C7':1
         }


ofile = open("output.dpv", "w")
with open("input.dpv") as ifile:
    for line in ifile:

        #Check for component line
        if line.startswith("EComponent"):
            data = line.split(",")

            if data[11] in mlist.keys():
                data[4] = str(mlist[data[11]])

            line = ','.join(data)            
        
        ofile.write(line)

ofile.close()
