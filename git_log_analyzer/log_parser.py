from datetime import datetime

class LogParser:
    def __init__(self, logs):
        self.logs = logs

    def parse_commits(self):
        commits = []
        for log in self.logs:
            hash, author, date, message = log.split('|')
            date = datetime.strptime(date, "%a %b %d %H:%M:%S %Y %z")
            commits.append({
                "hash": hash,
                "author": author,
                "date": date,
                "message": message
            })
        return commits
