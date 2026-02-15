# Week 12: Mini Project - Game Character System
# Run: python3 week12-oop-advanced/03_game_characters.py

from typing import List
from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class for game characters"""
    
    def __init__(self, name: str, health: int, attack_power: int):
        self._name = name
        self._max_health = health
        self._health = health
        self._attack_power = attack_power
        self._is_alive = True
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def health(self) -> int:
        return self._health
    
    @property
    def max_health(self) -> int:
        return self._max_health
    
    @property
    def attack_power(self) -> int:
        return self._attack_power
    
    @property
    def is_alive(self) -> bool:
        return self._is_alive
    
    @property
    def health_percentage(self) -> float:
        """Calculate health as percentage"""
        return (self._health / self._max_health) * 100
    
    def take_damage(self, damage: int) -> None:
        """Reduce health by damage amount"""
        self._health -= damage
        if self._health <= 0:
            self._health = 0
            self._is_alive = False
            print(f"💀 {self._name} has been defeated!")
        else:
            print(f"❤️  {self._name} took {damage} damage. Health: {self._health}/{self._max_health}")
    
    def heal(self, amount: int) -> None:
        """Restore health"""
        if not self._is_alive:
            print(f"{self._name} cannot be healed (defeated)")
            return
        
        old_health = self._health
        self._health = min(self._health + amount, self._max_health)
        actual_heal = self._health - old_health
        print(f"💚 {self._name} healed {actual_heal} HP. Health: {self._health}/{self._max_health}")
    
    @abstractmethod
    def special_ability(self) -> str:
        """Each character type has unique special ability"""
        pass
    
    def __str__(self) -> str:
        status = "Alive" if self._is_alive else "Defeated"
        return f"{self._name} ({self.__class__.__name__}) - HP: {self._health}/{self._max_health} - {status}"
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self._name}', {self._health}, {self._attack_power})"


class Warrior(Character):
    """Warrior class with high health and defense"""
    
    def __init__(self, name: str):
        super().__init__(name, health=150, attack_power=20)
        self._armor = 10
    
    @property
    def armor(self) -> int:
        return self._armor
    
    def take_damage(self, damage: int) -> None:
        """Warriors reduce damage with armor"""
        reduced_damage = max(1, damage - self._armor)
        print(f"🛡️  {self._name}'s armor reduced damage by {damage - reduced_damage}")
        super().take_damage(reduced_damage)
    
    def special_ability(self) -> str:
        """Warrior's special: Shield Bash"""
        return f"⚔️  {self._name} uses Shield Bash! Deals {self._attack_power * 2} damage and stuns enemy!"


class Mage(Character):
    """Mage class with magic and mana"""
    
    def __init__(self, name: str):
        super().__init__(name, health=80, attack_power=30)
        self._mana = 100
        self._max_mana = 100
    
    @property
    def mana(self) -> int:
        return self._mana
    
    @property
    def max_mana(self) -> int:
        return self._max_mana
    
    def cast_spell(self, mana_cost: int) -> bool:
        """Cast spell if enough mana"""
        if self._mana >= mana_cost:
            self._mana -= mana_cost
            print(f"✨ {self._name} casts spell! Mana: {self._mana}/{self._max_mana}")
            return True
        else:
            print(f"❌ {self._name} doesn't have enough mana!")
            return False
    
    def restore_mana(self, amount: int) -> None:
        """Restore mana"""
        self._mana = min(self._mana + amount, self._max_mana)
        print(f"💙 {self._name} restored {amount} mana. Mana: {self._mana}/{self._max_mana}")
    
    def special_ability(self) -> str:
        """Mage's special: Fireball"""
        if self.cast_spell(30):
            return f"🔥 {self._name} casts Fireball! Deals {self._attack_power * 3} damage!"
        return f"{self._name} failed to cast (not enough mana)"


class Rogue(Character):
    """Rogue class with high damage and critical hits"""
    
    def __init__(self, name: str):
        super().__init__(name, health=100, attack_power=25)
        self._crit_chance = 0.3  # 30% critical hit chance
    
    @property
    def crit_chance(self) -> float:
        return self._crit_chance
    
    def special_ability(self) -> str:
        """Rogue's special: Backstab"""
        return f"🗡️  {self._name} uses Backstab! Deals {self._attack_power * 4} damage!"


class Party:
    """Manages a party of characters"""
    
    def __init__(self, name: str):
        self.name = name
        self.members: List[Character] = []
    
    def add_member(self, character: Character) -> None:
        """Add character to party"""
        self.members.append(character)
        print(f"➕ {character.name} joined {self.name}!")
    
    def remove_member(self, character: Character) -> None:
        """Remove character from party"""
        if character in self.members:
            self.members.remove(character)
            print(f"➖ {character.name} left {self.name}")
    
    def show_status(self) -> None:
        """Display all party members"""
        print(f"\n{'='*50}")
        print(f"Party: {self.name}")
        print(f"{'='*50}")
        for member in self.members:
            print(f"  {member}")
            if isinstance(member, Mage):
                print(f"    Mana: {member.mana}/{member.max_mana}")
            elif isinstance(member, Warrior):
                print(f"    Armor: {member.armor}")
        print(f"{'='*50}")
    
    def alive_members(self) -> List[Character]:
        """Return list of alive members"""
        return [m for m in self.members if m.is_alive]
    
    def __len__(self) -> int:
        return len(self.members)


# Demo the game system
def main():
    print("🎮 Welcome to the Character Battle System!\n")
    
    # Create characters
    warrior = Warrior("Thorin")
    mage = Mage("Gandalf")
    rogue = Rogue("Legolas")
    
    # Create party
    party = Party("Fellowship")
    party.add_member(warrior)
    party.add_member(mage)
    party.add_member(rogue)
    
    party.show_status()
    
    # Battle simulation
    print("\n⚔️  Battle begins!\n")
    
    # Warrior takes damage
    warrior.take_damage(30)
    warrior.take_damage(40)
    
    # Mage casts spells
    print(f"\n{mage.special_ability()}")
    mage.cast_spell(20)
    mage.restore_mana(50)
    
    # Rogue uses special
    print(f"\n{rogue.special_ability()}")
    
    # Healing
    print()
    warrior.heal(50)
    mage.heal(20)
    
    # More damage
    print()
    rogue.take_damage(80)
    rogue.take_damage(30)  # This will defeat the rogue
    
    party.show_status()
    
    print(f"\n✅ Alive members: {len(party.alive_members())}/{len(party)}")


if __name__ == "__main__":
    main()


# TODO: Add an Archer class with ranged attacks
# TODO: Implement a battle system where characters fight each other
# TODO: Add experience points and leveling system
# TODO: Create equipment system (weapons, armor)
# TODO: Add status effects (poison, stun, buff)
