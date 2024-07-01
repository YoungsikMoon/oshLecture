import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', dest="MyName")
parser.add_argument('-o', dest="MyOld")
args = parser.parse_args()

print(args.MyName)
print(args.MyOld)