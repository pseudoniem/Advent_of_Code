AoC_input_test = '''\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''

AoC_input = '''\
Game 1: 1 green, 2 blue; 15 blue, 12 red, 2 green; 4 red, 6 blue; 10 blue, 8 red; 3 red, 12 blue; 1 green, 12 red, 8 blue
Game 2: 5 green, 2 red, 18 blue; 18 blue, 6 red, 9 green; 6 blue, 3 green; 6 green, 1 red, 9 blue; 19 blue, 2 green, 6 red
Game 3: 16 red, 10 green; 12 red, 6 blue, 9 green; 10 green, 5 blue; 10 green, 16 red; 5 red, 8 green, 8 blue
Game 4: 9 blue, 20 green; 1 red, 3 blue, 10 green; 7 blue, 18 green; 4 blue, 20 green; 8 blue, 1 green, 1 red; 1 green
Game 5: 3 green, 8 red; 1 blue, 10 red; 6 red, 4 green; 8 red, 1 blue, 3 green; 1 blue, 4 green, 3 red; 1 green, 1 blue, 4 red
Game 6: 7 green, 15 red, 11 blue; 2 red, 12 blue; 11 red, 11 green
Game 7: 14 green, 10 blue, 4 red; 3 red, 11 green, 14 blue; 1 red, 2 green, 11 blue; 9 green, 1 red; 6 red, 6 blue, 9 green
Game 8: 1 red, 6 green, 3 blue; 4 green; 4 red, 3 green, 1 blue; 2 red, 10 green, 3 blue; 2 green, 6 red, 3 blue
Game 9: 2 green, 8 red, 3 blue; 2 green, 4 blue, 2 red; 2 green, 5 blue, 2 red
Game 10: 9 green, 1 blue; 2 blue, 12 green, 3 red; 2 red, 3 blue, 1 green; 3 blue, 8 green; 4 blue, 4 red, 1 green; 5 green, 4 blue
Game 11: 5 red, 2 blue, 2 green; 3 blue, 2 green, 8 red; 6 red, 1 green
Game 12: 8 blue, 7 green; 2 green, 2 red, 7 blue; 4 green, 1 red, 20 blue; 5 green, 13 blue, 2 red
Game 13: 1 blue, 11 green, 13 red; 6 blue, 13 red, 19 green; 5 blue, 6 green, 6 red
Game 14: 12 blue, 1 red, 15 green; 16 green; 1 red, 18 blue, 15 green; 14 blue; 12 blue, 1 red, 8 green; 4 blue, 16 green
Game 15: 6 blue, 3 green; 1 red, 1 blue, 2 green; 3 green, 4 blue, 7 red
Game 16: 17 red, 14 green, 6 blue; 5 blue, 2 red; 1 blue, 11 red, 2 green; 13 green, 12 red
Game 17: 14 green, 4 red; 1 green, 5 blue, 15 red; 5 green, 14 red, 5 blue
Game 18: 8 blue, 2 green, 1 red; 12 blue, 1 green; 1 green, 1 red, 5 blue; 1 green, 1 red, 9 blue
Game 19: 1 red, 2 blue; 2 green, 5 red; 1 blue, 2 green, 11 red; 10 red; 4 green, 11 red
Game 20: 5 red, 11 green, 5 blue; 2 red, 5 blue, 7 green; 12 blue, 5 green, 10 red; 4 blue, 15 red, 10 green; 11 green, 12 blue, 7 red; 15 red, 12 blue, 5 green
Game 21: 5 blue, 6 green, 1 red; 18 blue, 13 green; 7 blue, 3 red; 9 blue, 2 red, 14 green
Game 22: 4 blue, 2 green, 19 red; 11 green, 5 blue, 17 red; 12 red, 4 blue, 13 green; 2 blue, 11 green; 1 blue, 19 red, 10 green; 8 blue, 2 green
Game 23: 12 green, 6 red; 1 blue, 1 red, 11 green; 1 blue, 3 red, 8 green; 4 green, 8 red
Game 24: 8 blue, 1 green, 6 red; 6 blue, 9 red; 8 red, 1 green, 1 blue
Game 25: 2 red, 4 blue, 1 green; 1 blue, 4 red, 2 green; 1 green, 5 blue, 1 red; 3 red, 2 blue
Game 26: 2 green, 10 blue, 5 red; 14 blue, 6 green, 12 red; 7 green, 2 red, 1 blue; 3 blue, 5 green, 3 red; 7 blue, 1 red, 3 green; 5 red, 2 green, 6 blue
Game 27: 8 blue, 2 red; 2 green, 8 blue, 6 red; 4 green, 2 red; 2 blue, 4 green, 7 red
Game 28: 8 green; 1 red, 9 blue, 10 green; 8 green, 9 blue, 2 red
Game 29: 5 red, 3 green, 2 blue; 12 red, 6 blue, 1 green; 6 red, 12 blue; 2 green, 4 blue, 5 red
Game 30: 9 red, 1 blue, 2 green; 13 green, 12 blue, 11 red; 11 red, 5 green, 9 blue; 4 blue, 12 green, 3 red; 10 red, 8 green; 2 red, 3 blue, 12 green
Game 31: 11 green, 5 red; 1 green, 4 red; 6 green, 9 red, 2 blue
Game 32: 6 blue, 3 red; 2 red, 11 blue, 4 green; 1 green, 4 red, 12 blue; 3 blue, 2 red
Game 33: 1 green, 7 red; 15 red, 15 green, 1 blue; 15 green, 3 red; 1 blue, 13 green, 6 red; 1 blue, 13 green, 20 red
Game 34: 3 red, 5 green, 1 blue; 13 green, 5 blue, 2 red; 3 red, 3 blue, 8 green; 3 blue, 1 red, 1 green; 4 blue, 3 red; 9 green, 3 red
Game 35: 6 blue, 8 green; 6 red, 9 blue, 12 green; 4 green, 3 blue; 5 red, 3 blue
Game 36: 17 green, 1 red, 1 blue; 1 red, 7 blue, 13 green; 6 blue, 5 green; 9 blue, 6 red, 5 green
Game 37: 2 green, 16 blue, 1 red; 3 red, 5 blue, 4 green; 3 green, 5 red, 2 blue
Game 38: 10 red, 3 blue, 1 green; 2 blue, 4 red; 7 red, 1 blue; 8 blue, 5 red, 11 green; 12 green, 4 blue, 8 red
Game 39: 3 blue, 3 green, 1 red; 5 green, 9 blue; 1 green, 6 blue; 5 blue, 7 green, 1 red; 9 blue, 1 green
Game 40: 1 blue, 2 red, 2 green; 2 green, 14 blue; 2 red, 6 blue; 13 blue; 2 green, 10 blue
Game 41: 1 red, 1 blue, 1 green; 11 green, 1 red; 4 green; 5 green; 1 blue, 1 red, 10 green
Game 42: 4 blue, 3 red, 2 green; 6 red, 1 blue, 6 green; 11 red, 7 blue, 3 green; 6 blue, 7 red, 1 green; 11 red, 1 green, 6 blue; 2 blue, 4 green, 10 red
Game 43: 3 red, 5 blue; 2 green, 4 red, 3 blue; 7 red, 10 blue, 13 green
Game 44: 13 green, 5 blue, 3 red; 1 green, 5 blue, 8 red; 11 green, 4 blue, 9 red; 5 blue, 7 green, 9 red
Game 45: 12 red, 9 blue, 5 green; 9 green, 3 red; 3 green, 11 blue, 15 red
Game 46: 5 blue, 2 green, 1 red; 1 blue, 3 red, 3 green; 2 green, 7 blue
Game 47: 8 red, 8 green, 5 blue; 12 blue, 8 green, 7 red; 5 red, 1 blue, 2 green; 1 red, 4 green, 6 blue; 1 red, 3 blue; 5 green, 1 red, 3 blue
Game 48: 3 blue, 2 red, 5 green; 4 green, 5 blue; 3 blue, 13 green, 5 red
Game 49: 4 red, 9 blue, 1 green; 12 red, 8 blue; 5 red, 2 blue, 1 green; 11 red, 2 green, 9 blue; 8 red, 9 blue, 3 green
Game 50: 3 blue, 2 red; 3 blue, 7 green; 4 red, 2 blue, 8 green; 7 green, 2 blue, 4 red; 3 red, 3 green; 6 green, 4 red, 2 blue
Game 51: 9 blue, 4 red, 2 green; 5 red, 3 green, 3 blue; 5 green, 10 blue, 5 red; 8 red, 11 blue, 5 green; 1 red, 3 blue, 7 green
Game 52: 1 blue, 9 red, 6 green; 8 red, 1 blue, 4 green; 13 green, 3 blue, 6 red; 3 green, 9 red; 3 blue, 12 green, 7 red
Game 53: 1 blue, 9 green; 1 red, 2 green; 7 green, 1 red
Game 54: 3 green, 3 blue, 9 red; 6 blue, 11 green, 1 red; 6 green, 1 red, 4 blue; 4 blue, 2 red, 13 green; 3 green, 1 red; 6 blue, 3 green, 8 red
Game 55: 1 blue, 6 green; 4 red, 5 green; 8 red, 12 green; 5 red, 1 blue, 7 green; 1 blue, 11 red, 3 green
Game 56: 1 green, 11 red, 1 blue; 2 green, 8 blue, 3 red; 5 blue, 6 red, 1 green
Game 57: 5 green, 3 red, 2 blue; 10 green, 12 blue, 16 red; 7 blue, 13 red, 11 green
Game 58: 5 green, 16 blue, 5 red; 9 blue, 2 green, 5 red; 5 blue, 3 red, 9 green
Game 59: 2 blue, 2 red; 7 blue, 3 green, 4 red; 2 green, 1 blue
Game 60: 12 red, 5 green, 1 blue; 2 blue, 12 red, 4 green; 16 red, 4 green, 2 blue
Game 61: 3 green, 1 blue, 6 red; 4 green, 1 blue, 8 red; 4 red, 1 blue, 1 green; 4 green, 13 red
Game 62: 2 red, 4 blue; 2 blue, 13 green, 8 red; 4 red, 9 green, 4 blue; 8 green, 3 red, 7 blue; 3 blue, 6 red, 3 green
Game 63: 1 green, 3 blue; 6 blue, 4 red, 3 green; 3 blue, 1 green, 1 red; 2 green, 2 blue, 3 red; 1 red, 2 blue; 5 red, 6 blue
Game 64: 7 red, 10 blue, 4 green; 1 green, 18 red, 2 blue; 7 blue, 2 green; 10 red, 1 green, 7 blue; 3 green, 5 blue, 11 red
Game 65: 11 red, 2 blue; 1 green, 2 blue, 1 red; 3 blue, 2 green, 3 red; 3 blue, 3 red, 7 green
Game 66: 3 red, 7 blue, 11 green; 10 blue, 4 green, 9 red; 11 blue, 11 red, 12 green; 8 red, 7 blue, 10 green; 5 red, 14 green, 3 blue
Game 67: 5 green, 1 red; 7 green, 4 blue; 3 red, 1 green, 3 blue
Game 68: 9 blue, 11 green, 10 red; 12 blue, 3 red, 3 green; 8 red, 7 green, 9 blue
Game 69: 1 green, 7 blue, 1 red; 1 red, 9 blue; 1 green, 2 red
Game 70: 9 green, 2 blue, 1 red; 1 red, 2 blue, 16 green; 13 green, 4 blue, 13 red; 8 red, 7 green, 6 blue; 12 green, 3 blue, 3 red
Game 71: 2 green, 4 red, 6 blue; 11 green, 6 blue, 2 red; 3 green, 1 blue, 5 red; 7 blue, 6 green
Game 72: 4 blue, 1 green; 4 blue; 1 green, 3 blue; 4 blue; 1 red, 4 blue; 3 blue
Game 73: 4 red, 1 green, 7 blue; 15 green, 4 blue, 17 red; 19 green, 3 blue, 11 red; 13 green, 5 blue, 1 red; 10 blue, 13 green, 17 red
Game 74: 9 green, 2 blue, 18 red; 5 red, 8 green; 3 green, 4 blue, 3 red; 5 green, 3 blue
Game 75: 1 red, 10 blue, 1 green; 2 red, 19 blue; 4 red, 10 blue; 3 red, 7 blue, 1 green; 2 red, 3 blue
Game 76: 4 green, 9 red, 7 blue; 8 green, 7 blue; 12 green, 9 red
Game 77: 1 red, 6 blue, 2 green; 8 red, 5 green, 4 blue; 4 blue, 2 red, 3 green
Game 78: 9 blue, 1 red, 8 green; 2 green, 9 blue; 2 green, 9 blue
Game 79: 4 blue, 4 green, 1 red; 4 blue, 4 red, 4 green; 4 green, 1 blue, 6 red; 6 green; 6 red
Game 80: 13 red, 8 blue; 2 green, 14 red, 13 blue; 7 red, 9 blue; 11 red, 18 blue; 2 blue, 3 red, 1 green
Game 81: 2 green, 9 red, 12 blue; 5 green, 5 red, 13 blue; 5 blue, 5 red; 2 red, 8 blue
Game 82: 6 red, 15 green; 1 blue, 15 red, 13 green; 6 green, 1 blue, 1 red; 5 red, 6 green, 1 blue
Game 83: 1 green; 1 blue, 1 green, 10 red; 7 red, 1 blue; 1 green, 11 red; 2 blue, 1 green, 3 red
Game 84: 17 green, 8 red; 1 blue, 14 green, 2 red; 6 red, 1 blue, 6 green; 4 red, 10 green, 1 blue; 2 red, 2 blue, 1 green; 4 blue, 5 green, 3 red
Game 85: 5 blue, 3 red; 1 blue, 1 green; 6 green, 1 blue, 1 red; 4 green, 2 blue, 7 red
Game 86: 7 red, 3 blue, 4 green; 1 blue, 13 red; 3 red, 3 blue, 6 green; 1 blue, 1 green, 17 red; 8 blue, 13 red, 4 green; 6 blue, 4 green, 17 red
Game 87: 10 red, 3 green, 4 blue; 12 green, 10 red, 3 blue; 2 green, 16 red; 16 red, 3 blue, 14 green; 14 green, 11 red, 1 blue; 9 red, 4 blue, 6 green
Game 88: 7 green, 4 red, 19 blue; 1 green, 5 red, 18 blue; 19 blue, 3 green, 6 red; 9 green, 14 blue, 5 red; 3 green, 5 red
Game 89: 4 red, 2 blue, 10 green; 6 blue, 5 red; 3 green, 4 blue, 1 red; 12 green, 2 red, 2 blue; 3 blue, 3 green, 3 red
Game 90: 1 green, 19 red, 1 blue; 7 blue, 4 green, 10 red; 6 blue, 3 green, 13 red
Game 91: 1 green, 9 blue; 7 green, 4 red, 3 blue; 6 green, 2 red, 8 blue; 1 red, 1 blue; 3 red, 2 green
Game 92: 18 red, 2 green, 2 blue; 6 blue, 4 red, 6 green; 3 blue, 10 red; 8 blue, 2 green, 7 red
Game 93: 13 blue, 3 green, 15 red; 14 red, 2 green, 7 blue; 1 blue, 4 green, 13 red; 19 red, 5 green
Game 94: 6 blue; 5 green, 8 blue; 1 red, 9 blue; 1 red, 8 blue; 5 green, 6 blue; 1 red
Game 95: 9 blue, 14 green; 2 green, 1 red, 1 blue; 1 red, 3 green, 2 blue; 6 green, 1 red; 1 red, 8 blue, 14 green; 1 green, 5 blue
Game 96: 7 blue, 17 green; 19 green, 3 red, 2 blue; 6 green, 2 red, 2 blue; 3 blue, 16 green; 3 red, 20 green; 4 green, 2 blue
Game 97: 1 green, 1 red, 1 blue; 4 red, 2 blue; 7 red; 6 red; 7 red
Game 98: 2 red, 15 green; 10 green, 1 red; 1 red, 11 blue, 11 green; 13 blue, 8 green, 2 red; 1 red, 12 green, 7 blue
Game 99: 14 red, 2 blue, 1 green; 3 green, 13 red, 9 blue; 9 red, 9 blue, 2 green; 13 red, 7 green, 5 blue; 5 blue, 3 green, 11 red
Game 100: 1 blue, 1 red, 1 green; 8 blue, 1 green; 1 green, 7 blue, 1 red; 1 green, 4 blue, 1 red; 1 green, 3 blue'''