population = [int(n) for n in input().split(", ")]
minimum_wealth = int(input())

distribution = True
for ind, num in enumerate(population):
    if num < minimum_wealth:
        main_string = minimum_wealth - num
        max_number = max(population)
        index_max_num = population.index(max_number)
        check_number = max_number - main_string
        if check_number >= minimum_wealth:
            population[ind] = minimum_wealth
            population[index_max_num] = max_number - main_string
        else:
            distribution = False
            print("No equal distribution possible")
            break
    else:
        population[ind] = num

if distribution:
    print(population)