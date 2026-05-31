# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        result = []
        for idx in range(len(pairs)):
            current_pair = pairs[idx]
            if idx == 0:
                result.append(pairs[:])
            elif current_pair.key >= pairs[idx-1].key:
                result.append(pairs[:])
            else:
                k = 1
                while pairs[idx-k+1].key < pairs[idx-k].key:
                    pairs[idx-k+1] = pairs[idx-k]
                    pairs[idx-k] = current_pair
                    k += 1
                    if idx-k < 0:
                        break
                result.append(pairs[:])
        return result
