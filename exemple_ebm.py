#!/bin/python
# Albert:vert Béatrice:rouge Claude:violet Denis:bleu Emilie:jaune

from people import create_people, create_people_2
from transition import create_transitions, create_transitions_2
from distribution import Distribution, Distribution_factory
from distribution_finder import Distribution_finder
from esm_tools import *
import copy

distribution_factory = Distribution_factory(create_people_2(), create_transitions_2())

distribution_finder = Distribution_finder(distribution_factory)


d_1 = {'Albert': {'Rpomme':5, 'Cpomme':0, 'Rpoire':0, 'Cpoire':5},
       'Béatrice':{'Rpomme':0, 'Cpomme':5, 'Rpoire':5, 'Cpoire':0}}

distribution = distribution_factory.create_distribution(d_1)

print(distribution.criterion_of_social_stability())
print(distribution.validity_on_transitions())
input()
distribution = distribution_finder.optimize(distribution)
print(distribution.criterion_of_social_stability(True))
print(distribution)
print(distribution.validity_on_transitions())
print(distribution.criterion_of_social_stability())
view_auto_productions(distribution)

# distribution = good_random_distribution(distribution_finder)
# view_auto_productions(distribution)
# print(distribution)
# print(distribution.validity_on_transitions())
# print(distribution.criterion_of_social_stability())

# print(distribution_finder.distribution_1)
