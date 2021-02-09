# https://www.codingame.com/ide/puzzle/chuck-norris
message = input()

byte_msg = bytearray(message, "utf8")

byte_list = [bin(byte) for byte in byte_msg]

byte_str = ""
for elem in byte_list:
    truncate_str = byte_list[byte_list.index(elem)][2:]
    while len(truncate_str) < 7:
        truncate_str = "0" + truncate_str
    byte_str += truncate_str

n = 0
unibin_str = ""
while n < len(byte_str):
    for elem in byte_str:
        if n == 0:
            unibin_str += "0 0" if elem == "1" else "00 0"
        else:
            if byte_str[n] != byte_str[n - 1]:
                unibin_str += " 0 0" if elem == "1" else " 00 0"
            else:
                unibin_str += "0"
        n += 1

print(unibin_str)
