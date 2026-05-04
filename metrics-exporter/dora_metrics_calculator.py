import datetime
import random

def calculate_dora_metrics(repo_name):
    """
    Simulates fetching deployment and incident data from GitHub/GitLab
    to calculate DORA metrics.
    """
    print(f"--- DORA Metrics Calculator ---")
    print(f"Analyzing Repository: {repo_name}\n")
    
    # Mock Data Calculation
    deployment_frequency = random.randint(5, 20)  # Deployments per week
    lead_time_days = random.uniform(0.5, 3.0)     # Days from commit to prod
    change_failure_rate = random.uniform(1.0, 15.0) # Percentage
    mttr_hours = random.uniform(1.0, 8.0)         # Hours to restore
    
    # Rating Logic (Accelerate State of DevOps 2023)
    def get_rating(val, thresholds, reverse=False):
        if reverse:
            if val <= thresholds[0]: return "Elite"
            if val <= thresholds[1]: return "High"
            return "Medium"
        else:
            if val >= thresholds[0]: return "Elite"
            if val >= thresholds[1]: return "High"
            return "Medium"

    metrics = [
        {"name": "Deployment Frequency", "value": f"{deployment_frequency}/week", "rating": get_rating(deployment_frequency, [15, 7])},
        {"name": "Lead Time for Changes", "value": f"{lead_time_days:.1f} days", "rating": get_rating(lead_time_days, [1, 7], reverse=True)},
        {"name": "Change Failure Rate", "value": f"{change_failure_rate:.1f}%", "rating": get_rating(change_failure_rate, [5, 15], reverse=True)},
        {"name": "Time to Restore Service", "value": f"{mttr_hours:.1f} hours", "rating": get_rating(mttr_hours, [1, 24], reverse=True)},
    ]
    
    print("-" * 60)
    print(f"{'Metric':<25} | {'Value':<15} | {'Rating':<10}")
    print("-" * 60)
    for m in metrics:
        print(f"{m['name']:<25} | {m['value']:<15} | {m['rating']:<10}")
    print("-" * 60)
    
    return metrics

if __name__ == "__main__":
    calculate_dora_metrics("my-cloud-app")
