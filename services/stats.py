import math

def poisson_probability(lmbda: float, k: int) -> float:
    """Calcule la probabilité d'un événement selon la loi de Poisson."""
    return (math.exp(-lmbda) * (lmbda ** k)) / math.factorial(k)

def calculate_match_probabilities(home_expected: float, away_expected: float, max_goals: int = 5):
    """Calcule les probabilités de victoire domicile, nul, extérieur."""
    home_win = 0.0
    draw = 0.0
    away_win = 0.0

    for h in range(max_goals + 1):
        for a in range(max_goals + 1):
            p = poisson_probability(home_expected, h) * poisson_probability(away_expected, a)
            if h > a:
                home_win += p
            elif h == a:
                draw += p
            else:
                away_win += p

    return {
        "home_win": round(home_win * 100, 2),
        "draw": round(draw * 100, 2),
        "away_win": round(away_win * 100, 2)
    }

