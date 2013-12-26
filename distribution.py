# Albert:vert Béatrice:rouge Claude:violet Denis:bleu Emilie:jaune
import copy

class Distribution_factory:
    def __init__(self, people, transitions):
        self.people = people
        self.transitions = transitions

    def create_distribution(self, distribution_dict):
        return Distribution(distribution_dict, self.people, self.transitions)

class Distribution:
    def __init__(self, distribution_dict, people, transitions):
        self.distribution_dict = distribution_dict
        self.people = people
        self.transitions = transitions

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

    def criterion_of_social_stability(self):
        result = True
        for citizen in self.distribution_dict:
            social_stability = self.social_stability_with(citizen)
            result = result and social_stability
            # if(not social_stability):
            #     print("problem with " + citizen)

        return result

    def social_stability_with(self, citizen):
        # print("--------------------" + citizen + "-"*20)
        distribution_with_activities = copy.deepcopy(self)
        del distribution_with_activities[citizen]

        distribution_without_activities = copy.deepcopy(self)
        del distribution_without_activities[citizen]

        for activity in self[citizen]:
            distribution_without_activities.remove_induced_activities(activity, self[citizen][activity])

        # print(distribution_with_activities)
        # print(distribution_without_activities)
        # print(distribution_with_activities >= distribution_without_activities)
        return distribution_with_activities >= distribution_without_activities

    def remove_induced_activities(self, activity, quantity):
        (induced_activity, induced_quantity) = self.transitions["induced"][activity](quantity)

        total_quantity = 0
        for citizen in self.distribution_dict:
            total_quantity += self[citizen][induced_activity]

        if(total_quantity != 0):
            percent = induced_quantity / total_quantity

            for citizen in self.distribution_dict:
                self.distribution_dict[citizen][induced_activity] *= (1 - percent)

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
            result[citizen] = sum([activity for activity in well_being_by_activity[citizen].values()])

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
