from enum import Enum
import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from datasets.pokemon import Pokemon
    
    
class TargetType(Enum):
    OWN = 1
    ENEMY = 2
    CHOOSE = 3
    
class EffectCategory(Enum):
    PRIORITY = 1
    STATCHANGE = 2
    STATUSEFFECT = 3
    HEAL = 4
    DAMAGE = 5
    
class StatusType(Enum):
    PARALYZE = 1
    POISON = 2
    BURN = 3
    ICE = 4
    SLEEP = 5
    
    
class Effect:
    def __init__(self, user: "Pokemon", enemy: "Pokemon", category: EffectCategory, probability: float):
        self.user = user
        self.enemy = enemy
        self.category = category
        self.probability = probability
        
    def connected(self) -> bool:
        """
        Decides if a effect connected or failed
        
        Args:
            self(Effect): The Effect instance
            
        Returns:
            bool
            True if connected
            False if failed

        """    

        threshold = random.random()
        return threshold < self.probability / 100
    

        

        
class StatChangeEffect(Effect):
    
    def __init__(self, user, enemy, stat, magnitude, probability: float, target: TargetType):
        super().__init__(user, enemy, EffectCategory.STATCHANGE, probability)
        self.stat = stat
        self.magnitude = magnitude
        self.target = target
        
    def get_target(self) -> "Pokemon":
        if self.target == TargetType.OWN:
            self.target == self.user
            
        elif self.target == TargetType.ENEMY:
            self.target == self.enemy
            
        elif self.target == TargetType.CHOOSE:
            chosen_target = 0
            while chosen_target not in [1, 2]:
                print("Please select a valid target: ")
                print(f"1. {self.user.name}")
                print(f"2. {self.enemy.name}")
                try:
                    chosen_target = int(input("Your choice: "))
                    
                except:
                    print("Invalid selection. Please try again.")
                    
            if chosen_target == 1:
                self.target = self.user
            
            else:
                self.target = self.enemy
        

        
class StatusEffect(Effect):
    def __init__(self, status_type: StatusType, probability: float, target: TargetType):
        super().__init__(EffectCategory.STATUSEFFECT, probability)
        self.status_type = status_type
        self.target = target
        
class PriorityEffect(Effect):
    def __init__(self):
        super().__init__(pokemons.Pikachu, pokemons.Raichu, EffectCategory.PRIORITY, probability=100)


#Examples of each effect category        
x = PriorityEffect()
y = StatChangeEffect("attack", 1, 40, TargetType.CHOOSE)
y.get_target()
