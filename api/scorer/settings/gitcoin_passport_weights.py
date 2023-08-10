"""Configuration for the gitcoin scorer"""

# Weight values for each stamp based on its perceived significance in assessing the unique humanity of the Passport holder
GITCOIN_PASSPORT_WEIGHTS = {
    "Brightid": "0.689",
    "CivicCaptchaPass": "1",
    "CivicLivenessPass": "2.25",
    "CivicUniquenessPass": "2.25",
    "Coinbase": "1.35",
    "CommunityStakingBronze": "1.27",
    "CommunityStakingGold": "1.27",
    "CommunityStakingSilver": "1.27",
    "Discord": "0.689",
    "Ens": "2.2",
    "EthGasProvider": "2.4",
    "EthGTEOneTxnProvider": "1.27",
    "ethPossessionsGte#1": "1.79",
    "ethPossessionsGte#10": "1.27",
    "ethPossessionsGte#32": "1.27",
    "Facebook": "0.689",
    "FacebookProfilePicture": "0.689",
    "FirstEthTxnProvider": "1.16",
    "GitcoinContributorStatistics#numGr14ContributionsGte#1": "1.41",
    "GitcoinContributorStatistics#numGrantsContributeToGte#1": "1.57",
    "GitcoinContributorStatistics#numGrantsContributeToGte#10": "2.30",
    "GitcoinContributorStatistics#numGrantsContributeToGte#100": "0.52",
    "GitcoinContributorStatistics#numGrantsContributeToGte#25": "1.48",
    "GitcoinContributorStatistics#numRoundsContributedToGte#1": "1.57",
    "GitcoinContributorStatistics#totalContributionAmountGte#10": "1.53",
    "GitcoinContributorStatistics#totalContributionAmountGte#100": "1.37",
    "GitcoinContributorStatistics#totalContributionAmountGte#1000": "1.18",
    "GitcoinGranteeStatistics#numGrantContributors#10": "0.71",
    "GitcoinGranteeStatistics#numGrantContributors#100": "0.73",
    "GitcoinGranteeStatistics#numGrantContributors#25": "0.61",
    "GitcoinGranteeStatistics#numGrantsInEcoAndCauseRound#1": "1.18",
    "GitcoinGranteeStatistics#numOwnedGrants#1": "1.10",
    "GitcoinGranteeStatistics#totalContributionAmount#100": "0.689",
    "GitcoinGranteeStatistics#totalContributionAmount#1000": "0.689",
    "GitcoinGranteeStatistics#totalContributionAmount#10000": "0.689",
    "githubAccountCreationGte#180": "1.21",
    "githubAccountCreationGte#365": "1.21",
    "githubAccountCreationGte#90": "1.21",
    "githubContributionActivityGte#120": "1.21",
    "githubContributionActivityGte#30": "1.21",
    "githubContributionActivityGte#60": "1.21",
    "GnosisSafe": "2.65",
    "Google": "2.25",
    "GuildAdmin": "0.689",
    "GuildMember": "0.689",
    "GuildPassportMember": "0.689",
    "HolonymGovIdProvider": "4",
    "Hypercerts": "0.689",
    "IdenaAge#10": "1.48",
    "IdenaAge#5": "1.48",
    "IdenaStake#100k": "1.41",
    "IdenaStake#10k": "1.16",
    "IdenaStake#1k": "0.9",
    "IdenaState#Human": "1.61",
    "IdenaState#Newbie": "0.51",
    "IdenaState#Verified": "1.35",
    "Lens": "2.45",
    "Linkedin": "2.45",
    "NFT": "0.69",
    "PHIActivityGold": "1.16",
    "PHIActivitySilver": "1.67",
    "Poh": "1.21",
    "SelfStakingBronze": "1.21",
    "SelfStakingGold": "1.21",
    "SelfStakingSilver": "1.21",
    "SnapshotProposalsProvider": "2.82",
    "SnapshotVotesProvider": "1.41",
    "twitterAccountAgeGte#180": "1.21",
    "twitterAccountAgeGte#365": "1.21",
    "twitterAccountAgeGte#730": "1.21",
    "twitterTweetDaysGte#30": "1.21",
    "twitterTweetDaysGte#60": "1.21",
    "twitterTweetDaysGte#120": "1.21",
    "ZkSync": "0.400",
    "ZkSyncEra": "0.400",
    "CyberProfilePremium": "1.21",
    "CyberProfilePaid": "1.21",
    "CyberProfileOrgMember": "1.21",
}


# The Boolean scorer deems Passport holders unique humans if they meet or exceed the below thresholdold
GITCOIN_PASSPORT_THRESHOLD = "20"
