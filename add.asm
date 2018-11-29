section .data
  a dd 10003
  b dd 100000
  str1 db "Addition is %d"
section .bss
  as resb 23
  as1 resb 2
section .text
  global main
  extern printf
main:
  mov ecx,dword[a]
  mov eax,dword[b]
  add ecx,eax
  mov eax,ecx
  push eax
  push str1
  call printf
  add esp,8
