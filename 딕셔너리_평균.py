score = {
    'python': 80,
    'django': 89,
    'web': 83
}

score["algorithm"] = 80
score["python"] = 85

print(sum(score.values())/len(score))