# Set is a collection which is unordered, unchangeable*, and un-indexed.
# Set items are unchangeable, but you can remove items and add new items.
bri = set(['brazil', 'russia', 'india'])
if 'india' in bri:
    print("india belongs to bri")

if 'usa' in bri:
    print("usa does not belong to bri")

bric = bri.copy()
bric.add('china')
if bric.issuperset(bri):
    print("bric is superset of bri")

bri.remove('russia')
if bri & bric:
    print(bri & bric)

if bri.intersection(bric):
    print(bri.intersection(bric))
