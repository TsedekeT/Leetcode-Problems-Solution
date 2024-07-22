class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(range(1, n + 1))
        winner = 0
        while len(friends) > 1:
            # Calculate the index of the friend to be eliminated
            winner = (winner + k - 1) % len(friends)
            friends.pop(winner)
        return friends[0] 
