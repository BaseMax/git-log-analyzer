# Git Log Analyzer

**Git Log Analyzer** is a Python-based tool that helps analyze and visualize commit patterns, contributor statistics, and repository activity in Git repositories. It provides insights into the commit frequency, contributor contributions, and overall repository activity over time. The tool generates reports and visualizations to better understand the development history of a repository.

## Features

- **Commit Activity Analysis**: Visualize commit patterns over time.
- **Contributor Statistics**: Track the number of commits per contributor, as well as their first and last commits.
- **Repository Activity**: Generate activity reports based on commit frequency by date.
- **Visualizations**: Commit activity and contributor statistics plots using `matplotlib` and `seaborn`.
- **Reports**: Generate HTML and text-based reports summarizing key repository stats.

## Requirements

To run this project, you'll need to install the following Python dependencies:

- `matplotlib`
- `seaborn`
- `pandas`
- `numpy`
- `GitPython`

You can install the required dependencies by running:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Analyzer

To use Git Log Analyzer, run the main.py script from the command line. Provide the path to the Git repository you want to analyze as an argument.

```bash
python main.py <path_to_repo>
```

This will analyze the Git repository's commit log, calculate statistics, generate visualizations, and create summary reports.

### Testing

```bash
C:\Users\ALI\Projects\git-log-analyzer>python main.py .
Matplotlib is building the font cache; this may take a moment.
Git Log Analysis Complete!
```

### Output

The following files will be generated:

- **Commit Activity Plot:** A line plot of commit frequency over time, saved as visualizations/commit_activity.png.
- **Contributor Stats Plot:** A bar chart of commits per contributor, saved as visualizations/contributor_stats.png.
- **Summary Report:** An HTML file containing the summary of commit activity, saved as reports/summary_report.html.
- **Contributor Stats Report:** A text file summarizing contributor statistics, saved as reports/stats_report.txt.

### License

MIT License

Copyright (c) 2025 Max Base
