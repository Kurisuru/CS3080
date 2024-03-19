'''
PROGRAMMER:..Christopher Colbert
USERNAME:....ccolbert
PROGRAM:.....hw02_01.py

DESCRIPTION: Takes in the input of a file name (Without extension). Open and read the given file, outputs the original file
input with some space and then the dissasembled machine instruction
'''
#setup comp instruction dictionaries
comp_0 = {"101010": "0","111111": "1","111010": "-1","001100": "D","110000": "A", "001101": "!D", "110001": "!A", "001111": "-D","110011": "-A",
          "011111": "D+1", "110111":"A+1","001110": "D-1","110010": "A-1", "000010": "D+A","010011": "D-A", "000111": "A-D","000000": "D&A","010101": "D|A"}
comp_1 = {"101010": "","111111": "","111010": "","001100": "","110000": "M", "001101": "", "110001": "!M", "001111": "","110011": "-M",
          "011111": "", "110111":"M+1","001110": "","110010": "M-1", "000010": "D+M","010011": "D-M", "000111": "M-D","000000": "D&M","010101": "D|M"}
dest = {"000": "", "001": "M","010": "D","011": "MD","100": "A","101": "AM","110": "AD","111": "AMD"}
jump = {"000": "","001": "JGT","010": "JEQ","011": "JGE","100": "JLT","101": "JNE","110": "JLE","111": "JMP"}

#obtain file name from user
print("DATA ENTRY")
file_name = (input("Enter file name (Without extension): "))
file_name = file_name + ".hack"


print("DISASSEMBLED OUTPUT")
with open(file_name, "r") as file:
    #for each line in file
    for line in file:
        #remove newline character from each line
        line = line.strip()
        #if first digit is 0, convert to decimal
        if line[0] == "0":
            output = "@" + str(int(line[1:], 2))
        #if first 3 digits are "111" 
        elif line[0:3] == "111":
            a = line[3]
            comp_bits = line[4:10]
            dest_bits = line[10:13]
            jump_bits = line[13:]
            
            comp_dict = comp_0 if line[3] == "0" else comp_1
            comp_mnemonic = comp_dict[comp_bits]
            dest_mnemonic = dest[dest_bits]
            jump_mnemonic = jump[jump_bits]
            
            #normal output: comp=dest;jump
            if dest_mnemonic and jump_mnemonic:
                output = dest_mnemonic + "=" + comp_mnemonic + ";" + jump_mnemonic
            #if jump is empty output: comp=dest
            elif dest_mnemonic:
                output = dest_mnemonic + "=" + comp_mnemonic
            #if dest is missing output: comp;jump
            elif jump_mnemonic:
                output = comp_mnemonic + ";" + jump_mnemonic
            #if dest and jump are missing output: comp
            else:
                output = comp_mnemonic
                
        print("%16s	%10s" % (line, output))
