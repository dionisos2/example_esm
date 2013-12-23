#!/bin/python
# Albert:vert Béatrice:rouge Claude:violet Denis:bleu Emilie:jaune

from people import create_people
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

distribution = Distribution(distribution_dict_1, create_people())
distribution_tmp = Distribution(distribution_dict_2, create_people())

while(distribution_tmp > distribution):
    distribution = copy.deepcopy(distribution_tmp)
    for citizen in distribution_tmp:
        if(citizen != "Claude"):
            distribution_tmp[citizen]["Rbois"] += 0.1
            distribution_tmp[citizen]["Cbois"] += 1

print(distribution)
print("\n")
print(distribution.well_being_by_activity())
