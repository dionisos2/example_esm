# Albert:vert Béatrice:rouge Claude:violet Denis:bleu Emilie:jaune
import copy
import decimal
import operator
from utils import *

class Distribution_factory:
    def __init__(self, people, transitions):
        self.people = people
        self.transitions = transitions
        Distribution_factory.verify_people(people, transitions)

    @staticmethod
    def verify_people(people, transition):
        for citizen in people:
            citizen_activities = people[citizen].keys()
            transition_activities = transition.transitions["induced"].keys()
            if (citizen_activities != transition_activities):
                raise ValueError("citizen " + citizen + " do not have correct activities:" + str(citizen_activities) + " should be " + str(transition_activities))

    def create_distribution(self, distribution_dict):
        return Distribution(distribution_dict, self.people, self.transitions)

class Distribution:
    def __init__(self, distribution_dict, people, transitions):
        self.distribution_dict = distribution_dict
        self.people = people
        self.transitions = transitions
        Distribution_factory.verify_people(people, transitions)

    def validity_on_transitions(self):
        result = True
        activities_sum = {}


        for citizen in self.distribution_dict:
            for economic_activity in self.distribution_dict[citizen]:
                if(economic_activity in activities_sum):
                    activities_sum[economic_activity] += self.distribution_dict[citizen][economic_activity]
                else:
                    activities_sum[economic_activity] = self.distribution_dict[citizen][economic_activity]

        for transition in self.transitions["check"]:
            transition_ok = self.transitions["check"][transition](activities_sum)
            if(not transition_ok):
                print(transition + " is not good.\n")
            result = result and transition_ok

        if(not result):
            print(activities_sum)

        return result

    def criterion_of_social_stability(self, show = False):
        if (not self.validity_on_transitions()):
            return False

        result = True
        for citizen in self.distribution_dict:
            social_stability = self.social_stability_with(citizen, show)
            result = result and social_stability
            if((show)and(not social_stability)):
                print("problem with " + citizen)

        return result

    def remove_self_production(self, citizen):
        # remove the consumption than the citizen auto-produce, and the linked production, the result is than we keep only what the citizen produce for other, and what he consume from other productions
        for production_activity in self[citizen]:
            if(self.transitions.is_production(production_activity)):
                production_quantity = self[citizen][production_activity]
                (consumption_activity, consumption_induced_quantity) = self.transitions["induced"][production_activity](production_quantity)
                consumption_quantity = self[citizen][consumption_activity]
                (plop, production_induced_quantity) = self.transitions["induced"][consumption_activity](consumption_quantity)


                if(production_quantity >= production_induced_quantity):
                    production_quantity -= production_induced_quantity
                    consumption_quantity = 0
                else:
                    consumption_quantity -= consumption_induced_quantity
                    production_quantity = 0

                self[citizen][production_activity] = production_quantity
                self[citizen][consumption_activity] = consumption_quantity



    def social_stability_with(self, citizen, show = False):
        if(show):
            print("-"*10 + citizen + "-"*10)

        distribution_with_activities = copy.deepcopy(self)
        del distribution_with_activities[citizen]

        distribution_without_activities = copy.deepcopy(self)
        distribution_without_activities.remove_self_production(citizen)

        for activity in distribution_without_activities[citizen]:
            distribution_without_activities.remove_induced_activities(citizen, activity)

        del distribution_without_activities[citizen]

        if(show):
            print(distribution_with_activities)
            print(distribution_without_activities)
            print(distribution_with_activities >= distribution_without_activities)
        return distribution_with_activities >= distribution_without_activities

    def remove_induced_activities(self, concerned_citizen, activity):
        # maximize the resulted distribution

        quantity = self[concerned_citizen][activity]
        (induced_activity, induced_quantity) = self.transitions["induced"][activity](quantity)


        while((induced_quantity > 0)and(not approx_equal(induced_quantity, 0))):
            well_being_by_citizen = self.well_being_by_citizen()
            if(self.transitions.is_production(activity)):
                sorted_well_beings = sorted(well_being_by_citizen.items(), key=operator.itemgetter(1), reverse=True)
            else:
                sorted_well_beings = sorted(well_being_by_citizen.items(), key=operator.itemgetter(1))


            for (citizen, well_being) in sorted_well_beings:
                if(citizen != concerned_citizen):
                   if(self.distribution_dict[citizen][induced_activity] > 0.01):
                       self.distribution_dict[citizen][induced_activity] -= 0.01
                       induced_quantity -= 0.01
                       break
                   else:
                       if(self.distribution_dict[citizen][induced_activity] > 0):
                           induced_quantity -= self.distribution_dict[citizen][induced_activity]
                           self.distribution_dict[citizen][induced_activity] = 0


    def well_being_by_activity(self):
        distribution_result = {}

        for citizen in self.distribution_dict:
            distribution_result[citizen] = {}
            for economic_activity in self.distribution_dict[citizen]:
                satisfaction = self.people[citizen][economic_activity]["satisfaction_function"](self.distribution_dict[citizen][economic_activity])

                distribution_result[citizen][economic_activity] = satisfaction

        return distribution_result


    def well_being_by_citizen(self):
        result = {}
        well_being_by_activity = self.well_being_by_activity()

        for citizen in well_being_by_activity:
            result[citizen] = round(sum([activity for activity in well_being_by_activity[citizen].values()]), 3)

        return result

    def __gt__(self, distribution):
        distribution_1 = list(self.well_being_by_citizen().values())
        distribution_2 = list(distribution.well_being_by_citizen().values())
        distribution_1.sort()
        distribution_2.sort()

        for a,b in zip(distribution_1, distribution_2):
            if(a != b):
                return (a > b)

        return False

    def number_of_citizens(self):
        return len(self.distribution_dict)

    def __eq__(self, distribution):
        distribution_1 = list(self.well_being_by_citizen().values())
        distribution_2 = list(distribution.well_being_by_citizen().values())
        distribution_1.sort()
        distribution_2.sort()

        return distribution_1 == distribution_2

    def __len__(self):
        return len(self.distribution_dict)

    def __ge__(self, distribution):
        return ((self == distribution) or (self > distribution))

    def __str__(self):
        result = "Distribution:\n"
        result += str(self.distribution_dict) + "\n\n"
        result += "Satisfaction des citoyens:\n"
        result += str(self.well_being_by_citizen()) + "\n"
        result += "Validité des transitions: " + str(self.validity_on_transitions()) + "\n"
        result += "Critère de stabilité sociale: " + str(self.criterion_of_social_stability()) + "\n"
        return result

    def __getitem__(self, key):
        return self.distribution_dict[key]

    def __setitem__(self, key, value):
        self.distribution_dict[key] = value

    def __delitem__(self, key):
        del self.distribution_dict[key]

    def  __iter__(self):
        for citizen in self.distribution_dict:
            yield citizen
