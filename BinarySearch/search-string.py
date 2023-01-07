from bisect import bisect_left, bisect_right
def count_by_range(array, left_value, right_value):
    left_index = bisect_left(array, left_value)
    right_index = bisect_right(array, right_value)
    print(array, left_value, right_value)
    return right_index - left_index

def solution(words, queries):
    arrays = [[] for _ in range(10001)]
    reversed_arrays = [[] for _ in range(10001)]
    for word in words:
        arrays[len(word)].append(word)
        reversed_arrays[len(word)].append(word[::-1])

    for i in range(10001):
        arrays[i].sort()
        reversed_arrays[i].sort()

    result = []
    for query in queries:
        if query[0] == "?":
            result.append(count_by_range(reversed_arrays[len(query)], query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z')))
        else:
            result.append(count_by_range(arrays[len(query)], query.replace('?','a'), query.replace('?','z')))

    return result

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"]))