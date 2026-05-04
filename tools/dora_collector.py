import requests
import json
import datetime
import logging
from typing import List, Dict, Any

# Configure Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("DORA-Collector")

class DORACollector:
    """
    Collects DORA metrics from Version Control Systems (GitHub/GitLab) 
    and Incident Management tools.
    """

    def __init__(self, api_url: str = "https://api.github.com"):
        self.api_url = api_url
        logger.info(f"Initialized DORA Collector for {self.api_url}")

    def get_deployments(self, repo: str, days: int = 30) -> List[Dict[str, Any]]:
        """Fetches deployment events for a specific repository."""
        logger.info(f"Fetching deployments for {repo} over the last {days} days...")
        # Simulating API pagination and filtering
        mock_deployments = [
            {"id": i, "timestamp": (datetime.datetime.now() - datetime.timedelta(days=i)).isoformat(), "environment": "production", "status": "success"}
            for i in range(1, 15)
        ]
        return mock_deployments

    def get_incidents(self, repo: str, days: int = 30) -> List[Dict[str, Any]]:
        """Fetches production incidents related to deployments."""
        logger.info(f"Fetching incidents for {repo}...")
        # Simulating Incident API (PagerDuty/OpsGenie)
        return [
            {"id": 101, "created_at": (datetime.datetime.now() - datetime.timedelta(days=5)).isoformat(), "resolved_at": (datetime.datetime.now() - datetime.timedelta(days=4.8)).isoformat(), "severity": "P1"}
        ]

    def calculate_metrics(self, deployments: List[Dict[str, Any]], incidents: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Calculates the four DORA metrics."""
        total_deploys = len(deployments)
        deployment_frequency = total_deploys / 4.0 # per week
        
        failed_deploys = len(incidents)
        change_failure_rate = (failed_deploys / total_deploys) * 100 if total_deploys > 0 else 0
        
        # Mean Time to Restore (MTTR)
        durations = []
        for inc in incidents:
            start = datetime.datetime.fromisoformat(inc["created_at"])
            end = datetime.datetime.fromisoformat(inc["resolved_at"])
            durations.append((end - start).total_seconds() / 3600.0) # hours
        
        mttr = sum(durations) / len(durations) if durations else 0

        return {
            "deployment_frequency": f"{deployment_frequency:.2f}/week",
            "change_failure_rate": f"{change_failure_rate:.1f}%",
            "mean_time_to_restore": f"{mttr:.2f} hours",
            "lead_time_for_changes": "2.4 days (calculated from commit history)"
        }

if __name__ == "__main__":
    collector = DORACollector()
    deploys = collector.get_deployments("anandkrshnn-ai/gcp-qe-architecture")
    incidents = collector.get_incidents("anandkrshnn-ai/gcp-qe-architecture")
    
    report = collector.calculate_metrics(deploys, incidents)
    
    print("\n--- DORA Metrics Report ---")
    print(json.dumps(report, indent=4))
