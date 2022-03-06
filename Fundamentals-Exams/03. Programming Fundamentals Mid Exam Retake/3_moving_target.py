targets = [int(n) for n in input().split()]
command = input()


def shoot_target(index, power):
    if 0 <= index < len(targets):
        targets[index] -= power
        if targets[index] <= 0:
            del targets[index]


def add_target(index, value):
    if 0 <= index < len(targets):
        targets.insert(index, value)
    else:
        print("Invalid placement!")


def strike_target(index, radius):
    if all([index - radius >= 0, index + radius < len(targets)]):
        del targets[index - radius:index + radius + 1]
    else:
        print("Strike missed!")


while command != "End":
    command = command.split()
    type_command = command[0]
    index_target = int(command[1])
    power_value_radius = int(command[2])
    if type_command == "Shoot":
        shoot_target(index_target, power_value_radius)
    elif type_command == "Add":
        add_target(index_target, power_value_radius)
    elif type_command == "Strike":
        strike_target(index_target, power_value_radius)
    command = input()

print(*targets, sep="|")
