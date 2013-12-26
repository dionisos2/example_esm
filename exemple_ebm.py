#!/bin/python
# Albert:vert Béatrice:rouge Claude:violet Denis:bleu Emilie:jaune

from people import create_people
from transition import create_transitions
from distribution import Distribution, Distribution_factory
from distribution_finder import Distribution_finder
import copy


distribution_factory = Distribution_factory(create_people(), create_transitions())

distribution_finder = Distribution_finder(distribution_factory)

random_distribution = distribution_finder.random_distribution()

distribution_1 = distribution_finder.distribution_1
print(distribution_1)
distribution_1 = distribution_finder.optimize(distribution_1)
print(distribution_1)
print(distribution_1.validity_on_transitions())
print(distribution_1.criterion_of_social_stability())

# for x in range(10000):
#     random_distribution_tmp = distribution_finder.random_distribution()
#     if((random_distribution_tmp > random_distribution)and(random_distribution_tmp.criterion_of_social_stability())):
#         random_distribution = random_distribution_tmp

# print(random_distribution)
# print(random_distribution.validity_on_transitions())
# print(random_distribution.criterion_of_social_stability())

# print(distribution_finder.distribution_1)
