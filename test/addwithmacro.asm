	%macro addit 2
	mov eax,%1
	mov ebx,%2
	add eax,ebx
	%endmacro
	section .data
	msg db "Addition is %d"
  section .text
	global main
  extern printf
main:
	addit 10,10000
	push eax
  push msg
  call printf
  add esp,8

