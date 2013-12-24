#!/bin/python
# Albert:vert Béatrice:rouge Claude:violet Denis:bleu Emilie:jaune

from people import create_people
from transition import create_transitions
from distribution import Distribution
import copy

distribution_dict_1 = {"Albert":{"Rbois":0.5, "Cbois":5, "Rtarte":0, "Ctarte":0},
                  "Béatrice":{"Rbois":0.5, "Cbois":5, "Rtarte":0, "Ctarte":0},
                  "Claude":{"Rbois":0.5, "Cbois":5, "Rtarte":0, "Ctarte":0},
                  "Denis":{"Rbois":0.5, "Cbois":5, "Rtarte":0, "Ctarte":0},
                  "Emilie":{"Rbois":0.5, "Cbois":5, "Rtarte":0, "Ctarte":0}}

distribution_dict_2 = {"Albert":{"Rbois":1, "Cbois":10, "Rtarte":0, "Ctarte":0},
                  "Béatrice":{"Rbois":1, "Cbois":10, "Rtarte":0, "Ctarte":0},
                  "Claude":{"Rbois":1, "Cbois":10, "Rtarte":0, "Ctarte":0},
                  "Denis":{"Rbois":1, "Cbois":10, "Rtarte":0, "Ctarte":0},
                  "Emilie":{"Rbois":1, "Cbois":10, "Rtarte":0, "Ctarte":0}}

distribution_dict_3 = {"Albert":{"Rbois":1, "Cbois":10, "Rtarte":0, "Ctarte":0},
                  "Béatrice":{"Rbois":1, "Cbois":10, "Rtarte":0, "Ctarte":0},
                  "Claude":{"Rbois":1, "Cbois":10, "Rtarte":0, "Ctarte":0},
                  "Denis":{"Rbois":1, "Cbois":10, "Rtarte":0, "Ctarte":0},
                  "Emilie":{"Rbois":1, "Cbois":10, "Rtarte":0, "Ctarte":0}}

distribution = Distribution(distribution_dict_1, create_people(), create_transitions())
distribution_tmp = Distribution(distribution_dict_2, create_people(), create_transitions())
distribution_3 = Distribution(distribution_dict_3, create_people(), create_transitions())

while(distribution_tmp > distribution):
    distribution = copy.deepcopy(distribution_tmp)
    for citizen in distribution_tmp:
        if(citizen != "Claude"):
            distribution_tmp[citizen]["Rbois"] += 0.1
        distribution_tmp[citizen]["Cbois"] += 1

print(distribution)
print(distribution.validity_on_transitions())
print(distribution.criterion_of_social_stability())
# print("\n")
# print(distribution.well_being_by_activity())
# print("\n")
print(distribution_3.criterion_of_social_stability())
