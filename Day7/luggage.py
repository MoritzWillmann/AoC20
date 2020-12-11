import re

def check1(ruledict, col):
    count = 0
    for rule in list(ruledict):
        if any(col in bag for bag in ruledict[rule]) and not any('flag' in bag for bag in ruledict[rule]):
            ruledict[rule].append('flag')
            count += 1 + check1(ruledict, rule)
    return count

def check2(ruledict, col):
    count = 0
    for bag in ruledict[col]:
        if bag != "no other":
            count += int(bag[0]) * (1 + check2(ruledict, bag[2:]))
    return count

def main():
    #pattern1 = re.compile(r'(.+)\sbags\scontain\s(.+)')
    #pattern2 = re.compile(r'(\d)\s([a-z\s]+)\sbags?[,\.]')
    ruledict = {}
    with open('Day7/input.txt', 'r') as ipnt:
        #ruledict = dict(pattern1.findall(ipnt.read()))
        #ruledict.update({k: dict([(value[1], int(value[0])) for value in pattern2.findall(v)]) for k, v in ruledict.items()})
        for line in ipnt:
            [outer, inner] = line.strip().split(' contain ')
            outer = outer.replace(' bags', '')
            inner = inner.strip('.').split(', ')
            ruledict[outer] =  [col.replace(' bags', '').replace(' bag', '') for col in inner]
    print('Containing Shiny Gold: {}, Contained in Shiny Gold: {}'.format(check1(ruledict, 'shiny gold'), check2(ruledict, 'shiny gold')))

if __name__ == "__main__":
    main()
