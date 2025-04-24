import random

lego_parts = [8980, 7323, 5343, 82700, 92232, 1203, 7319, 8903, 2328, 1279, 679, 589]

max(lego_parts)

print("🎲 Welcome to Dungeon Dice!")
name = input("What is your name, brave adventurer? ")

print(f"\nHello, {name}!")
difficulty = input("Choose your path: Easy or Hard? ").lower()

player_health = 10
enemy_health = 5 if difficulty == "easy" else 10

print("\n⚔️ Battle begins!\n")

while player_health > 0 and enemy_health > 0:
    input("Press Enter to roll your dice...")
    player_roll = random.randint(1, 6)
    enemy_roll = random.randint(1,6)

    print(f"\nYou rolled: {player_roll}")
    print(f"The enemy rolled: {enemy_roll}")

    if player_roll > enemy_roll:
        enemy_health -= 2
        print("💥 You hit the enemy!")
    elif player_roll < enemy_roll:
        player_health -= 2
        print("👿 The enemy strikes you!")
    else:
        print("🛡️ It's a tie. No damage.")

    print(f"\nYour HP: {player_health} | Enemy HP: {enemy_health}")
    print("-" * 30)

if player_health > 0:
    print(f"\n🏆 Victory, {name}! You survived the dungeon!")
else:
    print(f"\n💀 Game over, {name}. The dungeon has claimed you.")

