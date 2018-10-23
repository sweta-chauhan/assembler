
%macro write 2
        mov eax,1
        mov ebx,4
        mov ecx,%1
        mov edx,%2
        int 80h
%endmacro

%macro write1 1
        mov eax,1
        mov ebx,4
        mov ecx,%1
        int 80h
%endmacro


%macro write2 1
        mov eax,1
        mov ebx,4
        mov ecx,%1
        int 80h
%endmacro


%macro write3 1
        mov eax,1
        mov ebx,4
        mov ecx,%1
        int 80h
%endmacro


section .data
        str1 db "hello",10,0
        len1 equ $ - str1
section .text
        global main
main:
        write str1,len1

