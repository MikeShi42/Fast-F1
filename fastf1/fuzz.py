def ratio(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)
    
    # Initialize the matrix
    dp = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]

    # Initialize the first row and first column
    for i in range(1, len_s1 + 1):
        dp[i][0] = i
    for j in range(1, len_s2 + 1):
        dp[0][j] = j

    # Fill the matrix
    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            if s1[i-1] == s2[j-1]:
                cost = 0
            else:
                cost = 2  # Substitution has a weight of 2
            
            dp[i][j] = min(dp[i-1][j] + 1,      # Deletion
                           dp[i][j-1] + 1,      # Insertion
                           dp[i-1][j-1] + cost) # Substitution

    # The Levenshtein distance with substitution weight 2
    levenshtein_dist = dp[len_s1][len_s2]
    
    # Normalized similarity
    max_len = max(len_s1, len_s2)
    if max_len == 0:
        return 100  # Both strings are empty
    normalized_similarity = 1 - (levenshtein_dist / (2 * max_len))
    
    return normalized_similarity * 100
