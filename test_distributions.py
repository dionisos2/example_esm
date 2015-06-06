#!/bin/python

from people import create_people, create_people_2
from transition import create_transitions, create_transitions_2
from distribution import Distribution, Distribution_factory
from distribution_finder import Distribution_finder
from esm_tools import *
import copy

distribution_factory = Distribution_factory(create_people_2(), create_transitions_2())


d1 = {'Béatrice': {'Ctarte': 1.9913932789899316, 'Cbois': 19.988216738039938, 'Rbois': 1.9988216738039943, 'Rtarte': 0.28448475414141866}, 'Denis': {'Ctarte': 2.02650670569229, 'Cbois': 20.06266659061805, 'Rbois': 2.0062666590618057, 'Rtarte': 0.2895009579560414}, 'Emilie': {'Ctarte': 6.56823966175799, 'Cbois': 22.4545501695684, 'Rbois': 2.2454550169568406, 'Rtarte': 0.9383199516797128}, 'Albert': {'Ctarte': 0.0470870580418421, 'Cbois': 10.257685772908665, 'Rbois': 1.0257685772908667, 'Rtarte': 0.006726722577405999}, 'Claude': {'Ctarte': 5.018266635339719, 'Cbois': 9.970866332064922, 'Rbois': 0.9970866332064924, 'Rtarte': 0.7168952336199598}}

d2 = {'Claude': {'Cbois': 43.40451256954468, 'Rbois': 1, 'Ctarte': 23.17164096961605, 'Rtarte': 2}, 'Denis': {'Cbois': 14.601391402819457, 'Rbois': 0.3089450187331072, 'Ctarte': 27.213341489914864, 'Rtarte': 2.6532640818433677}, 'Emilie': {'Cbois': 19.266902741563264, 'Rbois': 3.0885556121871134, 'Ctarte': 8.986221344994386, 'Rtarte': 0.5743582909693179}, 'Albert': {'Cbois': 19.102288828759562, 'Rbois': 0.606012204288125, 'Ctarte': 10.592782827661603, 'Rtarte': 2.6836400067914745}, 'Béatrice': {'Cbois': 5.251484505050204, 'Rbois': 1.7373940718052912, 'Ctarte': 12.664675469285983, 'Rtarte': 0.9888823955302989}}

d_1 = {'Albert': {'Rpomme':5, 'Cpomme':0, 'Rpoire':0, 'Cpoire':5},
       'Béatrice':{'Rpomme':0, 'Cpomme':5, 'Rpoire':5, 'Cpoire':0}}

distribution_3_people = {'Béatrice': {'Rpoire': 8.896617477560335, 'Cpoire': 0.9038545645214577, 'Rpomme': 0.01230325163291246, 'Cpomme': 7.497478599412243}, 'Albert': {'Rpoire': 0.034739717019565686, 'Cpoire': 9.995459138883245, 'Rpomme': 13.427574780487596, 'Cpomme': 0.4839997079845195}, 'Claude': {'Rpoire': 4.002438763151131, 'Cpoire': 2.034482254326328, 'Rpomme': 0.8909950007542887, 'Cpomme': 6.3493947254780325}}


distribution_2_people = {'Béatrice': {'Cpomme': 7.49909347048283, 'Rpomme': 0.0015290323533975192, 'Rpoire': 8.287495095234771, 'Cpoire': 0.7905242204397525}, 'Albert': {'Cpomme': 2.789786467581422, 'Rpomme': 10.28735090571086, 'Rpoire': 1.841252575381236, 'Cpoire': 9.338223450176253}}

# distribution_1 = distribution_factory.create_distribution(d1)
# distribution_2 = distribution_factory.create_distribution(d2)
distribution_1 = distribution_factory.create_distribution(d_1)

distribution_finder = Distribution_finder(distribution_factory)

random_distribution = good_random_distribution(distribution_finder)
# distribution_finder.optimize(distribution_1)
print(random_distribution)
print(random_distribution.well_being_by_activity())
view_auto_productions(random_distribution)

print(random_distribution.criterion_of_social_stability())
