def shout(word):
    return word.upper() + "!"

counts = {}
for w in ["sun", "moon", "sun"]:
    counts[w] = counts.get(w, 0) + 1

nums = [3, 1, 2]
print(counts)
print(shout("hello"))
print(sorted(nums)[0], len(nums))
