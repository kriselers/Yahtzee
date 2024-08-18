from typing import List

from rules import Rule
from hand import Hand

class Scoreboard:
    def __init__(self):
        self.rules = []
        self.points = []

    def register_rules(self, rule: List):
        self.rules.extend(rule)
        self.points = [0] * len(self.rules)

    def rule_count(self):
        return len(self.rules)

    def get_rule(self, row: int):
        return self.rules(row)

    def assign_points(self, rule: Rule, hand: Hand):
        row = self.rules.index(rule)
        if self.points[row] > 0:
            raise Exception("This rule has already been assigned points.")
        points = rule.points(hand)
        self.points[row] = points
        return points

    def total_points(self):
        return sum(self.points)

    def points_overview(self, hand: Hand = None):
        strs = []
        for idx, rule in enumerate(self.rules):
            points = self.points[idx]
            if hand is not None and points == 0 and rule.points(hand) > 0:
                strs.append(f"{idx + 1}. {rule.name()}: +{rule.points(hand)} points ***")
            else:
                strs.append(f"{idx + 1}. {rule.name()}: {self.points[idx]} points")
        return strs
