# assembler
pass2 assembler
It is 32 bit intel assembler with few instruction support.
Instruction supported are:
{
	mov r32,r32
	mov r32,dword[symbol]
	mov r32,imm32
	add r32,imm32
	add r32,r32
	call printf
	push r32
	push data_label
}


To run this assembler
python3 assembler.py <input.asm file> <-L flag> <-U flag> <-S flag>
<input.i> file will be generated

flag are optional :-

<-L>
to see the literal table entry

<-U>
to see the undefined symbol

<-S>
to see the symbol table entry

<-l filename>
to create lst file
Note : lst file will be created only for without macro files

<filenam.o> file will be generated

python3 smaco.py <filename.o>
program will execute

program in test directory can be used to check it's working

