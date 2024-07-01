import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--msg", dest="massage")
parser.add_argument("-l", "--lr", dest="learningrate")
args = parser.parse_args()

print(args.massage)
print(args.learningrate)