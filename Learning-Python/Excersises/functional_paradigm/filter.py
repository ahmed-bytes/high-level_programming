def over_average(score):
    return score > 50


scores = [73, 20, 65, 19, 76, 100, 88]

print(list(filter(over_average, scores)))
