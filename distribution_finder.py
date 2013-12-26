from distribution import Distribution, Distribution_factory
from utils import *
import copy
import random

class Distribution_finder:
    def __init__(self, distribution_factory):
        self.distribution_factory = distribution_factory
        self.transitions = self.distribution_factory.transitions
        self.people = self.distribution_factory.people
        self.create_exemples()
        self.min_value = 0
        self.max_value = 5
        self.stability_max = 500
        self.mute_speed = 0.5

    def mute(self, distribution):
        citizen = random.choice(list(distribution.distribution_dict.keys()))
        economic_activity = random.choice(list(distribution.distribution_dict[citizen].keys()))
        quantity = random.uniform(-self.mute_speed, self.mute_speed)
        if(quantity == 0):
            quantity = self.mute_speed

        (induced_activity, induced_quantity) = self.transitions["induced"][economic_activity](quantity)

        citizen_2 = random.choice(list(distribution.distribution_dict.keys()))
        muted_distribution = copy.deepcopy(distribution)
        muted_distribution[citizen][economic_activity] += quantity
        muted_distribution[citizen_2][induced_activity] += induced_quantity
        return muted_distribution

    def optimize(self, distribution):
        distribution = copy.deepcopy(distribution)
        stability = 0
        while(stability < self.stability_max):
            distribution_tmp = self.mute(distribution)
            if((distribution_tmp > distribution)and(distribution_tmp.criterion_of_social_stability())):
                print(stability)
                stability = 0
                distribution = distribution_tmp
            else:
                stability += 1

        return distribution

    def random_distribution(self):
        random_productions = self.random_productions()
        distribution_dict = copy.deepcopy(random_productions)
        possible_consumptions = self.get_possible_consumptions(random_productions)
        nbr_people = len(self.people)

        while(not approx_equal(sum(possible_consumptions.values()), 0)):
            for citizen in random_productions:
                for economic_activity in possible_consumptions:
                    quantity = random.uniform(0, possible_consumptions[economic_activity] * 2 / nbr_people)

                    if(not economic_activity in distribution_dict[citizen]):
                        distribution_dict[citizen][economic_activity] = 0

                    if(quantity > possible_consumptions[economic_activity]):
                        quantity = possible_consumptions[economic_activity]
                        possible_consumptions[economic_activity] = 0
                        distribution_dict[citizen][economic_activity] += quantity
                        break
                    else:
                        possible_consumptions[economic_activity] -= quantity
                        distribution_dict[citizen][economic_activity] += quantity

        distribution = self.distribution_factory.create_distribution(distribution_dict)
        return distribution

    def random_productions(self):
        economic_activities = self.transitions["economic_activities"]
        people = self.people
        productions_distribution = {}
        for citizen in people:
            productions_distribution[citizen] = {}
            for economic_activity in economic_activities:
                if(self.transitions.is_production(economic_activity)):
                    productions_distribution[citizen][economic_activity] = random.uniform(self.min_value, self.max_value)

        return productions_distribution


    def get_possible_consumptions(self, productions_distribution):
        possible_consumptions = {}
        for citizen in productions_distribution:
            for economic_activity in productions_distribution[citizen]:
                if(self.transitions.is_production(economic_activity)):
                    (induced_consumptions, induced_quantity) = self.transitions["induced"][economic_activity](productions_distribution[citizen][economic_activity])

                    if(induced_consumptions in possible_consumptions):
                        possible_consumptions[induced_consumptions] += induced_quantity
                    else:
                        possible_consumptions[induced_consumptions] = induced_quantity
        return possible_consumptions

    def create_exemples(self):
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

        distribution_dict_3 = {"Albert":{"Rbois":1, "Cbois":11, "Rtarte":0, "Ctarte":0},
                               "Béatrice":{"Rbois":1, "Cbois":10, "Rtarte":0, "Ctarte":0},
                               "Claude":{"Rbois":1, "Cbois":10, "Rtarte":0, "Ctarte":0},
                               "Denis":{"Rbois":1, "Cbois":10, "Rtarte":0, "Ctarte":0},
                               "Emilie":{"Rbois":1, "Cbois":10, "Rtarte":0, "Ctarte":0}}


        self.distribution_1 = self.distribution_factory.create_distribution(distribution_dict_1)
        self.distribution_2 = self.distribution_factory.create_distribution(distribution_dict_2)
        self.distribution_3 = self.distribution_factory.create_distribution(distribution_dict_3)


