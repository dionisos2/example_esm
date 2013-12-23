# Albert:vert Béatrice:rouge Claude:violet Denis:bleu Emilie:jaune

class Distribution:
    def __init__(self, distribution_dict, people):
        self.distribution_dict = distribution_dict
        self.people = people

    def validity_on_transition(self):
        nbr_Rbois = 0
        nbr_Cbois = 0
        nbr_Rtarte = 0
        nbr_Ctarte = 0

        for citizen in self.distribution_dict:
            nbr_Rbois += self.distribution_dict[citizen]["Rbois"] * 10
            nbr_Cbois += self.distribution_dict[citizen]["Cbois"]
            nbr_Rtarte += self.distribution_dict[citizen]["Rtarte"]
            nbr_Ctarte += self.distribution_dict[citizen]["Ctarte"]

            ok_bois = (nbr_Rbois == nbr_Cbois)
            ok_tarte = (nbr_Rtarte * 7 == nbr_Ctarte)
            return ok_bois and ok_tarte

    def criterion_of_social_stability(self):
        return True

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

    def  __iter__(self):
        for citizen in self.distribution_dict:
            yield citizen
