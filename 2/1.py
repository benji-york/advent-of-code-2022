import fileinput

outcome = dict(
    # First player plays Rock.
    AX = 3, AY = 6, AZ = 0,
    # First player plays Paper.
    BX = 0, BY = 3, BZ = 6,
    # First player plays Scissors.
    CX = 6, CY = 0, CZ = 3)

bonus = dict(X = 1, Y = 2, Z = 3)

score = 0
for line in fileinput.FileInput():
    assert line[1] == ' '
    play, response = line.split()
    score += outcome[play + response]
    score += bonus[response]

print(score)
