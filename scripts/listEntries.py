import sys

whatToDList = sys.argv[0]

contentToFile=""

for ns in AdminConfig.list( whatToDList ).splitlines() :
    print ns
