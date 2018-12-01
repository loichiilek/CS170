import solver
import output_scorer

total_medium = 0
total_large = 0

for i in range(5):
    solver.main()
    score_1, msg_1 = output_scorer.score_output('./all_inputs/medium/medium', './outputs/medium/medium.out')
    score_2, msg_2 = output_scorer.score_output('./all_inputs/large/large', './outputs/large/large.out')

    print(msg_1)
    print(msg_2)

    total_medium += score_1
    total_large += score_2

print("Average medium: " + str(total_medium / 5))
print("Average large: " + str(total_large / 5))
