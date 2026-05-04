# SLO-as-Code Implementation using Terraform
# Defines the Service Level Objectives for the Multi-Cloud Architecture.

# 1. Availability SLO (Target: 99.9%)
resource "google_monitoring_slo" "api_availability" {
  name         = "projects/my-project/services/api-service/serviceLevelObjectives/availability-slo"
  display_name = "API Availability SLO - 99.9%"
  goal         = 0.999
  rolling_period_days = 30

  basic_sli {
    availability {
      enabled = true
    }
  }
}

# 2. Latency SLO (Target: 95% of requests < 500ms)
resource "google_monitoring_slo" "api_latency" {
  name         = "projects/my-project/services/api-service/serviceLevelObjectives/latency-slo"
  display_name = "API Latency SLO - P95 < 500ms"
  goal         = 0.95
  rolling_period_days = 30

  request_based_sli {
    distribution_cut {
      distribution_filter = "metric.type=\"serviceruntime.googleapis.com/api/request_latencies\" resource.type=\"api\""
      range {
        max = 500
      }
    }
  }
}

# 3. Alert Policy for SLO Breach (Burn Rate)
resource "google_monitoring_alert_policy" "slo_burn_alert" {
  display_name = "High SLO Burn Rate Alert"
  combiner     = "OR"
  conditions {
    display_name = "SLO Error Budget Burn Rate > 2x"
    condition_threshold {
      filter     = "select_slo_burn_rate(\"projects/my-project/services/api-service/serviceLevelObjectives/availability-slo\")"
      duration   = "3600s"
      comparison = "COMPARISON_GT"
      threshold_value = 2.0
    }
  }
  notification_channels = [var.notification_channel_id]
}
