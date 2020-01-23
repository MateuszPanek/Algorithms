def calculate_damage(your_type, opponent_type, attack, defense):
    """Calculates the damage caused by certain type of pokemon"""
    relation = ('fire grass', 'water fire', 'electric water', 'grass water')
    effectiveness = 1

    if f'{your_type} {opponent_type}' in relation:
        effectiveness = 2

    if f'{opponent_type} {your_type}' in relation or your_type == opponent_type:
        effectiveness = 0.5

    return 50 * (attack / defense) * effectiveness
