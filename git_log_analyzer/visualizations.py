import matplotlib.pyplot as plt
import seaborn as sns

def generate_commit_activity_plot(commit_activity):
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=commit_activity, x='date', y='commits')
    plt.title('Commit Activity Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Commits')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('visualizations/commit_activity.png')

def generate_contributor_stats_plot(contributor_stats):
    plt.figure(figsize=(10, 6))
    sns.barplot(data=contributor_stats, x='author', y='commits')
    plt.title('Contributors Commit Count')
    plt.xlabel('Contributor')
    plt.ylabel('Number of Commits')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('visualizations/contributor_stats.png')
