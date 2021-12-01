"""
Strategy:
- 3 disks
  Move largest disk to the 3rd rod
  Move top 2 disks to the 2nd rod
  - To move top 2 disks to rod 2:
    move top disk (smallest) to rod 3
    move middle disk to rod 2
    move smallest disk to rod 2

Assumptions:
  1 <= start <= 3
  1 <= end <= 3
  start != end
  n >= 1

  1 -> 3 means Move the top disk from rod a to rod b

2^(n - 1) steps are required to solve for n disks
"""

def move_towers(n_rods, start, destination):
  if n_rods <= 0:
    print("I can't calculate it yet")
  elif n_rods == 1:
    print_move(start, destination)
  else:
    other_rod = 6 - (start + destination)
    move_towers(n_rods - 1, start, other_rod)
    print_move(start, destination)
    move_towers(n_rods - 1, other_rod, destination)

def print_move(start, destination):
  print(f"{start} -> {destination}")

move_towers(3, 1, 3)
# move_towers(200, 1, 3)
# Credits to https://youtu.be/rf6uf3jNjbo