#!/bin/python
# Albert:vert Béatrice:rouge Claude:violet Denis:bleu Emilie:jaune

from people import create_people, create_people_2
from transition import create_transitions, create_transitions_2
from distribution import Distribution, Distribution_factory
from distribution_finder import Distribution_finder
from esm_tools import *
import copy

distribution_factory = Distribution_factory(create_people(), create_transitions())

distribution_finder = Distribution_finder(distribution_factory)

distribution = distribution_finder.distribution_zero()
distribution = distribution_finder.optimize(distribution)

print(distribution)
view_auto_productions(distribution)

