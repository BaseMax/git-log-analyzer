import sys
from git_log_analyzer.git_repo import GitRepo
from git_log_analyzer.log_parser import LogParser
from git_log_analyzer.stats import Stats
from git_log_analyzer.visualizations import generate_commit_activity_plot, generate_contributor_stats_plot

def main(repo_path):
    git_repo = GitRepo(repo_path)
    
    raw_logs = git_repo.get_git_logs()

    parser = LogParser(raw_logs)
    commits = parser.parse_commits()

    stats = Stats(commits)
    contributor_stats = stats.get_contributor_stats()
    commit_activity = stats.get_commit_activity()

    generate_commit_activity_plot(commit_activity)
    generate_contributor_stats_plot(contributor_stats)

    stats.generate_stats_report(contributor_stats)
    stats.generate_summary_report(commit_activity)

    print("Git Log Analysis Complete!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_repo>")
        sys.exit(1)
    
    repo_path = sys.argv[1]
    main(repo_path)
