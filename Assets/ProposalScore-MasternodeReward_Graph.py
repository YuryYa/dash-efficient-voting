import matplotlib.pyplot as plt

k = 15
m = 10
n = m + k

proposalScore = [0, 0.5, 1]
masternodeRewardYes = [0, 1, n/k]
masternodeRewardNo = [n/m, 1, 0]

plt.plot(proposalScore, masternodeRewardYes,
         color='#6aa84fff', label='Masternode voted «Yes»')
plt.plot(proposalScore, masternodeRewardNo,
         color='#db4437ff', label='Masternode voted «No»')

plt.xlabel('ProposalScore')
plt.ylabel('MasternodeReward')
plt.title('Example for k=%d, m=%d' % (k, m))
plt.legend()

plt.savefig('ProposalScore-MasternodeReward_Graph.svg')
