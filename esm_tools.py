def citizen_effects(distribution, citizen):
    effects = {}
    transitions = distribution.transitions

    for production in transitions.productions:
        induced = transitions["induced"][production](distribution[citizen][production])
        effects[production[1:]] = induced[1] - distribution[citizen][induced[0]]

    return effects

def good_random_distribution(distribution_finder):
    random_distribution = distribution_finder.random_distribution()
    for x in range(10000):
        print(x)
        random_distribution_tmp = distribution_finder.random_distribution()
        if(((random_distribution_tmp > random_distribution) or not(random_distribution.criterion_of_social_stability())) and (random_distribution_tmp.criterion_of_social_stability())):
            random_distribution = random_distribution_tmp
            print("NEW FIND !!")
            print(random_distribution)
            print(random_distribution.validity_on_transitions())
            print(random_distribution.criterion_of_social_stability())

    return random_distribution

def view_auto_productions(distribution):
    for citizen in distribution:
        print(citizen)
        print(citizen_effects(distribution, citizen))
