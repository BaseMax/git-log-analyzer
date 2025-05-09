import subprocess

class GitRepo:
    def __init__(self, repo_path):
        self.repo_path = repo_path

    def get_git_logs(self):
        try:
            result = subprocess.run(
                ["git", "-C", self.repo_path, "log", "--pretty=format:%H|%an|%ad|%s"],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.splitlines()
        except subprocess.CalledProcessError as e:
            print(f"Error fetching git logs: {e}")
            return []
