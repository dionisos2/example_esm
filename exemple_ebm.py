#!/bin/python
# Albert:vert Béatrice:rouge Claude:violet Denis:bleu Emilie:jaune

from people import create_people
from transition import create_transitions
from distribution import Distribution, Distribution_factory
from distribution_finder import Distribution_finder
import copy


distribution_factory = Distribution_factory(create_people(), create_transitions())

distribution_finder = Distribution_finder(distribution_factory)

print(distribution_finder.distribution_1)
print(distribution_finder.distribution_2)
print(distribution_finder.distribution_3)
