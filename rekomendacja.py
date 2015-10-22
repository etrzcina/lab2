﻿#  Wzorowane na przykładzie Rona Zacharskiego

from math import sqrt

users = {"Ania": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bonia":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Celina": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dominika": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Ela": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Fruzia":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Gosia": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Hela": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }

def manhattan(rating1, rating2):
    """Oblicz odległość w metryce taksówkowej między dwoma  zbiorami ocen
       danymi w postaci: {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}
       Zwróć -1, gdy zbiory nie mają wspólnych elementów"""
    try:
        odl = 0
        p = 0
        for i in users[rating1]:
            if i in users[rating2]:
                odl += abs(users[rating1][i]-users[rating2][i])
                p = 1
        if p != 1:
            odl = -1
        return odl
    except KeyError:
        print u"Błędne dane."

def computeNearestNeighbor(username, users):
    """dla danego użytkownika username, zwróć ze słownika users nazwę użytkownika o najbliższych preferencjach"""
    nameOfNearestNeighbor = ""
    distances = []
    if username in users:
        for i in users:
            if i != username and manhattan(username,i) != -1:
                distances.append((manhattan(username, i),i))
        if distances != []:
            nameOfNearestNeighbor = sorted(distances)[0][1]
        return nameOfNearestNeighbor
    else:
        print u"Błędne dane."

def recommend(username, users):
    """Zwróć listę rekomendacji dla użytkownika"""
    # znajdź preferencje najbliższego sąsiada
    nearest = computeNearestNeighbor(username, users)
    recommendations = []
    # zarekomenduj użytkownikowi wykonawcę, którego jeszcze nie ocenił, a zrobił to jego najbliższy sąsiad
    try:
        print nearest
        if nearest !="":
            for i in users[nearest]:
                if i not in users[username]:
                    recommendations.append((i, users[nearest][i]))
            return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)
    except KeyError:
        pass
    
##przykłady
##print( recommend('Hela', users))
##print( recommend('Celina', users))
