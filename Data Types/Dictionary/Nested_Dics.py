

d = {
    'name' : {
        'mainName' : 'Bishnudev',
        'surName' : 'Khutia'
    },
    'roll' : {
        'collegeRoll' : 'CSE/20/020',
        'univerRoll' : 1070120026
    }
}

print(d['roll']['univerRoll'])

for k,v in d.items():
    print(k,v['surName'])