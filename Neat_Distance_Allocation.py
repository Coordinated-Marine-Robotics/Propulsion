Active_ASVs = [1,3,7,5,2]
ListDist = [[24,42,53,63,24],[25,86,43,52,42],[15,24,26,34,43],[16,76,32,74,52],[24,76,74,24,36]]
ASV_Dists = []
i=0
while i<len(Active_ASVs):
    ASV_Dists.append((Active_ASVs[i],ListDist[i]))
    i+=1print(ASV_Dists)
## ASV_Dists is a list of tuples with the ASV's name and list of distances from ## each position
## ASV_Dists[i] = (ASV_Name, [distance from each position])

## Minimising total time to get them all in position
## order in decending order of maximum distance
ASV_Dists_Dec_Max = sorted(ASV_Dists, key=lambda ASV:max(ASV[1]), reverse=True)

## assign each its minimum distance position
## make sure each position only has 1 ASV

## ASVPositions = List of ASV names in positional order
ASVPositions = ['x' for number in range(0, len(Active_ASVs))]for i in ASV_Dists_Dec_Max:
	minIndex = i[1].index(min(i[1]))
	while ASVPositions[minIndex] != 'x':
		i[1][minIndex] = max(i[1]) + 1
		minIndex = i[1].index(min(i[1]))
	if ASVPositions[minIndex] == 'x':
		ASVPositions[minIndex] = i[0]print(ASV_Dists)print(ASVPositions)