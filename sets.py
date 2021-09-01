# no duplicates,orderded

myset = {1, 2, 3, 4, 5, 4, 5, 5}
myset2 = {2, 3, 5}
print(myset)

# mutable
myset.add(5)
myset.remove(4)
# no errror here
myset.discard(5)
myset.pop()
# iteerate
for i in myset:
    print(i)


if 1 in myset:
    print('yes')
# union

# combines two sets without duplications
u = myset.union(myset2)

# intersection takes elements found in the both two sets
i = myset.intersection(myset2)

# the diffrence of two sets return s all the elements found in the first set but not found in the second set

diff = myset.difference(myset2)

# symmetric_diffrence returns all the elements rfrom set a and b but not the elements found in bothe the sets


symmetrci_diff = myset.symmetric_difference(myset2)

# modify the sets
myset.update(myset2)
# intersection update =>update the sets by keeping only the elements found in both sets.
myset.intersection_update(myset2)

# diff_update=>update the set by removing the elements found in another set
myset.difference_update(myset2)
# symm_diff_update=> does not update elements found in both
