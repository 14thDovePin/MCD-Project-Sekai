# Generate trails for gliding players.
execute at @a[nbt={FallFlying:1b, SelectedItem:{id:"minecraft:firework_rocket"}}] run particle minecraft:flame ~ ~ ~ .25 .25 .25 0 2 force
execute at @a[nbt={FallFlying:1b, SelectedItem:{id:"minecraft:firework_rocket"}}] run particle minecraft:soul_fire_flame ~ ~ ~ .25 .25 .25 0 2 force
execute at @a[nbt={FallFlying:1b, SelectedItem:{id:"minecraft:firework_rocket"}}] run particle minecraft:dragon_breath ~ ~ ~ .25 .25 .25 0 2 force

# For all players flying.
# @a[nbt={FallFlying:1b}]

# For all players flying, as well as holding
# a firework rocket on their offhand.
# @a[nbt={FallFlying:1b, Inventory:[{Slot:-106b, id:"minecraft:firework_rocket"}]}]

# For all players flying, as well as holding
# a firework rocket on their main hand.
# @a[nbt={FallFlying:1b, SelectedItem:{id:"minecraft:firework_rocket"}}]
