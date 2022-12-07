import fileinput

# Meanings for each symbol in the file.
rock = 'A'
paper = 'B'
scissors = 'C'

lose = 'X'
draw = 'Y'
win = 'Z'

# The first player's action and the desired outcome map to our choice.
choice = {
    rock + lose: scissors,
    rock + draw: rock,
    rock + win: paper,
    paper + lose: rock,
    paper + draw: paper,
    paper + win: scissors,
    scissors + lose: paper,
    scissors + draw: scissors,
    scissors + win: rock,
}

outcome = {lose: 0, draw: 3, win: 6}
bonus = {rock: 1, paper: 2, scissors: 3}

score = 0
for line in fileinput.FileInput():
    assert line[1] == ' ', 'unexpected formatting'
    first_play, desired_outcome = line.split()
    second_play = choice[first_play + desired_outcome]
    score += outcome[desired_outcome]
    score += bonus[second_play]

print(score)



