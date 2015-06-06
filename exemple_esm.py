#!/bin/python
# Albert:vert Béatrice:rouge Claude:violet Denis:bleu Emilie:jaune

from people import create_5_people, create_2_people, create_3_people
from transition import create_transitions, create_transitions_2
from distribution import Distribution, Distribution_factory
from distribution_finder import Distribution_finder
from esm_tools import *
import copy

distribution_factory = Distribution_factory(create_3_people(), create_transitions_2())

distribution_2_people = {'Béatrice': {'Cpomme': 7.49909347048283, 'Rpomme': 0.0015290323533975192, 'Rpoire': 8.287495095234771, 'Cpoire': 0.7905242204397525}, 'Albert': {'Cpomme': 2.789786467581422, 'Rpomme': 10.28735090571086, 'Rpoire': 1.841252575381236, 'Cpoire': 9.338223450176253}, 'Claude':{'Cpomme':0, 'Rpomme':0, "Cpoire":0, "Rpoire":0}}

distribution_finder = Distribution_finder(distribution_factory)

distribution_2_people = distribution_1 = distribution_factory.create_distribution(distribution_2_people)
# distribution = distribution_finder.distribution_zero()

distribution_2_people = distribution_finder.optimize(distribution_2_people)

print(distribution_2_people)
view_auto_productions(distribution_2_people)

