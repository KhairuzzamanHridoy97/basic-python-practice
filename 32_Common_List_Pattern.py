# print(list(range(1,10)))


# new_sentence = '! '.join(['hi','my','name','is','jojo'])
# print(new_sentence)


#------------------Exercise------------------

#fix this code so that it prints a sorted list of all of our friends (alphabetical). Scroll to see answer
# friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']
# new_friend = ['Stanley']
# friends.extend(new_friend)
# print(sorted(friends))
# print(friends.sort() + new_friend)





# Solution: (keep in mind there are multiple ways to do this, so your answer may vary. As long as it works that's all that matters!)
# friends.extend(new_friend)
# print(sorted(friends))

print(list(range(102))) 


#fix this code so that it prints a sorted list of all of our friends (alphabetical). Scroll to see answer
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

new_friend = ['Stanley']
friends.extend(new_friend)
print(friends)
print(sorted(friends))
