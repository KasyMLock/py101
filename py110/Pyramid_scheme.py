print("whats up user, we are gonna make a square pyramid with cubes...")



blocks_starting = input("How many cubes ya got? ").strip()
while blocks_starting.isdigit() == False:
    blocks_starting = input("please enter a digit: ").strip() 



levels_decending = 0
blocks_available = int(blocks_starting)



for level in range(1,1000):
    blocks_used = (level * level)
    if blocks_used > blocks_available:
        feet = (levels_decending * 1.5625) // 12
        inches = (levels_decending * 1.5625) % 12
    
        print(F"You can make {levels_decending} levels using {blocks_starting}"
              F" blocks with {blocks_available} remaining."
              F" The bottom level would be {level - 1} by {level - 1} equaling "
              F"{(level - 1) * (level - 1)} blocks."
              F" this would be roughly {feet}ft and {inches}inches tall in childrens blocks")
        break
    else:
        levels_decending += 1
        blocks_available -= blocks_used

    

