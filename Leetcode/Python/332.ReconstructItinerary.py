class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        reconstruction = []
        startingLegs = []
        for leg in tickets:
            if leg[0] == 'JFK':
                startingLegs.append(leg)

        reconstruction.append(sorted(startingLegs)[0][0])
        reconstruction.append(sorted(startingLegs)[0][1])
        return reconstruction


s = Solution()
print('Itinerary: ', s.findItinerary(
    [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
print('Itinerary: ', s.findItinerary([["JFK", "SFO"], [
      "JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
