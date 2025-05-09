import pandas as pd

class Stats:
    def __init__(self, commits):
        self.commits = commits
        self.df = pd.DataFrame(commits)

    def get_contributor_stats(self):
        contributor_stats = self.df.groupby('author').agg(
            commits=('hash', 'count'),
            first_commit=('date', 'min'),
            last_commit=('date', 'max')
        ).reset_index()
        return contributor_stats

    def get_commit_activity(self):
        self.df['date'] = self.df['date'].dt.date
        activity = self.df.groupby('date').size().reset_index(name='commits')
        return activity

    def generate_stats_report(self, contributor_stats):
        with open("reports/stats_report.txt", "w") as file:
            for _, row in contributor_stats.iterrows():
                file.write(f"Contributor: {row['author']}, Commits: {row['commits']}, First Commit: {row['first_commit']}, Last Commit: {row['last_commit']}\n")

    def generate_summary_report(self, commit_activity):
        with open("reports/summary_report.html", "w") as file:
            file.write("<html><body><h1>Git Log Summary Report</h1><ul>")
            for _, row in commit_activity.iterrows():
                file.write(f"<li>Date: {row['date']}, Commits: {row['commits']}</li>")
            file.write("</ul></body></html>")
