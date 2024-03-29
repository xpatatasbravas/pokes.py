from .pokemon import Pokemon
from .movement import Movement

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = [None] * 6
        self.inbattlefieldpokemon = None
        
    def set_pokemon(self, index, pokemon: Pokemon):
        
        """Sets a pokemon in a certain position in a Trainer team.
        
        Args:
            self: Instance of Trainer
            index(int): Position at which the pokemon must be entered
            pokemon: Pokemon that we want to introduce
            
        Comments:
        
        """
        
        if 0 <= index <= len(self.pokemons):
            if self.pokemons[index] != None:
                print(f"Are you sure you want to change {self.pokemons[index].name} for {pokemon.name}?.")
                while user_response not in ["Y", "N"]:
                    user_response = input("Type 'Y' if you are sure or 'N' to cancel")
                    if user_response == "Y":
                        pass
                    else:
                        break
                
            self.pokemons[index] = pokemon
        
        else:
            print(f"The index {index} is not valid. Please introduce a number between 0 and {len(self.pokemons)}")
            
    def get_pokemon(self, index):
        if 0 <= index <= len(self.pokemons):
            return self.pokemons[index]
        
        else:
            print(f"The index {index} is not valid. Please select a number between 0 and 5.")
            
    def has_active_pokemon(self):
        return any(pokemon is not None and pokemon.is_alive() for pokemon in self.pokemons)
    
    def set_battlefield_pokemon(self, pokemon: Pokemon):
        self.inbattlefieldpokemon = pokemon
        print(f"{self.name}'s pokemon is now {pokemon.name}.")
            
    def select_target(self, own_pokemon, enemy_pokemon):
        while True:
            print("Choose a target for the movement:")
            print(f"1. Own pokemon: {own_pokemon.name}")
            print(f"2. Enemy pokemon: {enemy_pokemon.name}")
            chosen_pokemon_number = input("Your choice: ")
            if chosen_pokemon_number == "1":
                return own_pokemon
            elif chosen_pokemon_number == "2":
                return enemy_pokemon
            else:
                print("Your choice is not correct.")
    
    def select_movement(self, pokemon: Pokemon) -> Movement:
        
        """Displays the possible movements and asks the user to input an integer to select the movement he wants his pokemon to use

        Returns:
            Movement: The movement that the user selected
            
        Comments:
            - The user input must be between 1 and 4
            - The corresponding movement must be different from None
            - Will display a message to the user to inform which movement was selected.
        """
        
        print("Select a valid movement that your pokemon will use this turn:")
        
        pokemon.print_pokemon_movements()
        
        chosen_movement_number = pokemon.enter_valid_movement_selection()
        chosen_movement =  pokemon.movements[chosen_movement_number]

        return chosen_movement
                