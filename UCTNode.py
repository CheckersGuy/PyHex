import math
class UCTNode:
    def __init__(self):
        self.visits = 0
        self.value = 0
        self.children = []

    def get_best_child(self):
        return max(self.children, key=lambda x: x.visits)

        return 0

    def select(self):
        exp_constant = 1.0
        max_node = self.children[0]
        max_value = 0.0
        p_visits =1.0 if self.visits ==0 else self.visits
        for node in self.children:
            temp = 1.0 if node.visits == 0 else node.visits
            u_value = node.value / temp
            p_value = math.sqrt(math.log(p_visits) / temp)
            uct_value = u_value + exp_constant * p_value
            if uct_value > max_value:
                max_node = node

        return max_node

    def __str__(self):
        return "visits: {} value: {}".format(self.visits, self.value)
