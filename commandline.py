import argparse
parser=argparse.ArgumentParser(
    description="my math script"
)


#add positional/optional parameters
parser.add_argument('num1',help="number 1",type=float)
parser.add_argument('num2',help="number 2",type=float)
parser.add_argument('operation',help=" provide operator")
#parse the arguments
args=parser.parse_args()
print(args)
result=None
if args.operation=='+':
    result=args.num1+args.num2
print(result)
'''for optional parameters we add --num1 as the parameter also when executing we enter the num1 45'''