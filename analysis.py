import scipy.stats as stats

def perform_mann_whitney_test(df, column, group1, group2):
    """Perform Mann-Whitney U test for two groups."""
    group1_data = df[df[column] == group1]['count']
    group2_data = df[df[column] == group2]['count']
    statistic, p_value = stats.mannwhitneyu(group1_data, group2_data)
    return statistic, p_value

def perform_kruskal_wallis_test(df, column):
    """Perform Kruskal-Wallis H-test for multiple groups."""
    groups = [group for _, group in df.groupby(column)['count']]
    statistic, p_value = stats.kruskal(*groups)
    return statistic, p_value