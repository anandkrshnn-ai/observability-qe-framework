# Observability-QE Framework - Measuring Quality at Scale

**Mastering Quality through Data — DORA Metrics, SLO-as-Code, and Automated Quality Gates.**

This repository provides a comprehensive framework for implementing **Observability-Driven Quality Engineering**. It includes dashboard templates, metric calculation scripts, and SLO-as-Code definitions to turn raw data into actionable quality insights.

Used by QE Architects to move from "feeling" that quality is good to "proving" it with data.

![MIT License](https://img.shields.io/badge/license-MIT-green)
![Observability](https://img.shields.io/badge/Observability-Driven-blue)
![DORA](https://img.shields.io/badge/DORA-Metrics-orange)

## Core Capabilities

### 📊 **DORA Metrics Center**
Automated calculation of the four key metrics:
- **Deployment Frequency:** How often do we ship to prod?
- **Lead Time for Changes:** How fast does code go from commit to prod?
- **Change Failure Rate:** What percentage of deployments cause issues?
- **Failed Service Restoration Time (MTTR):** How fast do we recover?

### 🎯 **SLO-as-Code**
Define Service Level Objectives (SLOs) and Service Level Indicators (SLIs) in code using Terraform or Sloth.
- **Availability SLOs:** 99.9% uptime validation.
- **Latency SLOs:** P95 < 500ms validation.
- **Quality SLOs:** Defect escape rate < 1%.

### 📉 **Visual Quality Dashboards**
Ready-to-import dashboard templates for:
- **Grafana:** Multi-source quality trends.
- **AWS CloudWatch:** Lambda and RDS health.
- **Azure Monitor:** AKS and App Service quality.

## What's Inside

- **[Metrics Exporter](metrics-exporter/)** — Python tools to fetch data from GitHub/GitLab.
- **[SLO-as-Code](slo-as-code/)** — Terraform and Sloth templates.
- **[Dashboard Templates](dashboards/)** — JSON definitions for major observability platforms.
- **[Methodology](docs/01-observability-driven-qe.md)** — The strategy behind Observability-Driven QE.

## Getting Started

1.  **Configure Exporter:** Set your GitHub token in `metrics-exporter/config.yml`.
2.  **Calculate DORA:** Run `python metrics-exporter/dora_metrics_calculator.py`.
3.  **Import Dashboards:** Load the JSON files in `dashboards/grafana/` to your Grafana instance.

## 🔗 Related Repositories
- [gcp-qe-architecture](https://github.com/anandkrshnn-ai/gcp-qe-architecture)
- [aws-qe-architecture](https://github.com/anandkrshnn-ai/aws-qe-architecture)
- [azure-qe-architecture](https://github.com/anandkrshnn-ai/azure-qe-architecture)
- [ai-powered-qe](https://github.com/anandkrshnn-ai/ai-powered-qe)

---

**You can't improve what you don't measure. Start measuring quality today.**
