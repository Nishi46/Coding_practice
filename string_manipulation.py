f1 = open('/Users/nishi/Downloads/97_problematic_resources-orig', 'r')
f2 = open('/Users/nishi/Downloads/problematic_resources', 'w')
for line in f1:
    if 'ra76ad9f4200504501' in line:
        l1 = line.replace('"ra76ad9f4200504501",', '')
        l2 = l1.replace('"ra76ad9f4200504501"', '')
        l3 = l2.replace("ra76ad9f4200504501", '')
        l4 = l3.replace(r'\"\",', '')
        f2.write(l4)
    else:
        f2.write(line)
f1.close()
f2.close()

#       f2.write(line.replace('"ra76ad9f4200504501",', ''))
#   elif '"ra76ad9f4200504501"' in line:
#       f2.write(line.replace('"ra76ad9f4200504501"', ''))
#   elif 'ra76ad9f4200504501' in line:
#       l1 = line.replace("ra76ad9f4200504501", '')
#        l2 = l1.replace(r'\"\",', '')
#       f2.write(l2)
