# Voicegain Transcribe SaaS — Service Level Agreement (SLA)

## Version Information

| Item            | Details                  |
| --------------- | ------------------------ |
| Document Name   | Voicegain Transcribe SLA |
| Version         | 3.0                      |
| Effective Date  | Feb 1, 2026              |
| Owner           | Jacek Jarmulak, CTO      |
| Review Cycle    | Annual                   |

---

## 1. Purpose

This Service Level Agreement ("SLA") defines the support services, response targets, escalation procedures, and service commitments provided by **Resolvity, Inc DBA Voicegain** ("Provider") to its customers ("Customer") for the use of the **Voicegain Transcribe SaaS SLA**.

This SLA is intended to:

- Define support expectations clearly
- Establish measurable service commitments
- Improve transparency and accountability
- Ensure operational continuity for Customers

---

## 2. Scope

This SLA applies to:

- Production environments of Voicegain Transcribe SaaS Apps
- Incident response and resolution management
- Availability commitments
- Escalation management

This SLA does **not** apply to:

- Beta or preview features
- Failures to meet SLAs caused by Customer-provided device, connectivity, or infrastructure issues
- Third-party APIs/integrations outside Voicegain control
- Scheduled maintenance windows

---

## 3. Support Channels

| Channel                              | Availability                       | Purpose                       |
| ------------------------------------ | ---------------------------------- | ----------------------------- |
| Voicegain Freshdesk Support Portal   | 24x7                               | Ticket submission & tracking  |
| Email Support                        | 24x7                               | Standard support requests     |
| Live Phone Support                   | Weekdays — 8:00 AM – 6:00 PM CT    | Critical incidents            |
| Status Page                          | 24x7                               | Service health updates        |

### Contact Information

- **Support Email:** transcribe.support@voicegain.ai
- **Support Portal:** https://support.voicegain.ai/hc/en-us
- **Status Page:** https://console.voicegain.ai/login

---

## 4. Support Hours

| Support Tier              | Hours                                     |
| ------------------------- | ----------------------------------------- |
| Standard Support          | Monday–Friday, 8:00 AM – 6:00 PM CT       |
| Premium Support           | 24x7x365                                  |
| Critical Incident Support | 24x7x365                                  |

Provider-observed holidays are excluded unless otherwise stated in Customer agreements.

---

## 5. Incident Severity Levels

### Severity Definitions

| Severity          | Description                                                              | Examples                                                                                                                                                                              |
| ----------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **P1 – Critical** | Complete production outage or severe business impact with no workaround  | Voicegain Transcribe App and/or Desktop Recorder App and/or Mobile Apps unavailable, widespread login failure, data loss                                                              |
| **P2 – High**     | Major functionality impaired with significant business impact            | Failure to generate Summaries and Action Items; severely degraded Speaker Diarization or Transcription Accuracy affecting many users                                                  |
| **P3 – Medium**   | Partial functionality issue with workaround available                    | Reporting delays; Supervisor App / Administration Features that are not time-sensitive; isolated feature malfunction; requiring user to log in frequently; slightly delayed processing |
| **P4 – Low**      | General questions, cosmetic issues, enhancement requests                 | Dark mode not working                                                                                                                                                                 |

---

## 6. Response & Resolution Targets — Standard Support

### Initial Response Targets

| Severity      | Initial Response Time | Update Frequency |
| ------------- | --------------------- | ---------------- |
| P1 – Critical | 1 hour                | Every 2 hours    |
| P2 – High     | 4 hours               | Every 8 hours    |
| P3 – Medium   | Daily                 | Daily            |
| P4 – Low      | 5 Business Days       | As needed        |

### Target Resolution Goals

| Severity      | Target Resolution Time               |
| ------------- | ------------------------------------ |
| P1 – Critical | 8 hours                              |
| P2 – High     | 1 business day                       |
| P3 – Medium   | 3 business days                      |
| P4 – Low      | Best effort / roadmap prioritization |

### Notes

- Resolution targets are goals, not guarantees, unless otherwise specified in a Master Services Agreement (MSA).
- Complex issues requiring third-party involvement may extend timelines.

---

## 7. Service Availability Commitment

Provider commits to a monthly uptime availability of:

> **99.5% Transcribe App Monthly Uptime**

### Uptime Calculation

$$\text{Availability} = \frac{\text{Total Minutes} - \text{Downtime Minutes}}{\text{Total Minutes}} \times 100$$

Downtime is defined as the cumulative downtime from the following events. Each event is multiplied by the number of Users affected:

1. User is unable to log into any one of the Voicegain Transcribe web browser applications, the Voicegain Windows Offline Recorder App on the desktop (offline), or the Voicegain Transcribe Mobile Apps to initiate recording of an in-home visit.
2. User can log in to the Voicegain Transcribe App but is unable to record the in-home assessment.
3. When the User has consistent high-speed internet connectivity (bandwidth of at least 100 Mbps and packet loss < 0.5% for 30 minutes) and the transcript, summary, and action items are not generated within 15 minutes of audio being submitted to the Voicegain Transcribe backend (User clicks the "Stop" button on the record-live button).

Outages are measured in 5-minute intervals.

### Excluded Downtime

The following are excluded from uptime calculations:

- Scheduled maintenance
- Emergency maintenance
- Force majeure events
- DDoS attacks and cyberattacks
- Network outages and Internet service provider failures
- Customer network/configuration issues
- Third-party platform outages outside Voicegain control

---

## 8. Scheduled Maintenance

| Maintenance Type      | Notification Window                    |
| --------------------- | -------------------------------------- |
| Scheduled Maintenance | Minimum 72 hours notice                |
| Emergency Maintenance | As much notice as reasonably possible  |

Maintenance windows typically occur during off-peak hours and on the weekend.

---

## 9. Escalation Procedures

### Escalation Path

| Level                | Role                          | Responsibility                    |
| -------------------- | ----------------------------- | --------------------------------- |
| Level 1              | Support Engineer              | Initial triage & troubleshooting  |
| Level 2              | Senior Support / Engineering  | Advanced technical investigation  |
| Level 3              | CTO / Engineering Leader      | Platform-level remediation        |
| Executive Escalation | Customer Success Leadership   | Business-critical coordination    |

### Customer Escalation

Customers may escalate unresolved issues by:

1. Updating the support ticket
2. Contacting the Customer Success Manager
3. Requesting executive escalation for unresolved P1 incidents

---

## 10. Customer Responsibilities

Customers are expected to:

- Provide accurate issue details
- Designate authorized support contacts
- Maintain supported configurations
- Cooperate with troubleshooting efforts
- Promptly respond to Provider requests

Failure to meet these responsibilities may impact SLA performance.

---

## 11. Service Credits

If monthly uptime falls below the committed SLA threshold, eligible Customers may request service credits.

| Monthly Uptime  | Service Credit |
| --------------- | -------------- |
| 99.01 – 99.5%   | 10%            |
| 98.01 – 99.00%  | 15%            |
| 97.01 – 98.00%  | 20%            |
| 95.01 – 97.00%  | 25%            |
| Below 95%       | 33%            |

### Conditions

- Credits apply only upon written request within 30 days
- Credits apply to future invoices only
- Credits cannot exceed a cap of 33% of monthly subscription fees

---

## 12. Data Retention, Backup & Disaster Recovery

### 12.1 Data Retention Commitment

Provider shall retain Customer production data for the Medicaid-mandated minimum period of **ten (10) years**, unless:

- Customer requests earlier deletion in writing;
- Retention is prohibited by applicable law; or
- A separate written agreement supersedes this commitment.

#### Scope of Retained Data

Retained data may include:

- Transcripts, audio recordings, LLM-generated summaries, action items, and responses
- Metadata
- Audit logs
- Call / Transcription Session records
- Transaction history
- Configuration data
- System backups

Archived data may be stored in lower-cost storage tiers but shall remain recoverable within commercially reasonable timeframes.

### 12.2 Backup Policy

Provider maintains automated backup procedures designed to ensure business continuity and disaster recovery readiness.

#### Backup Standards

| Backup Type                | Frequency                    | Retention      |
| -------------------------- | ---------------------------- | -------------- |
| Incremental Backups        | Hourly                       | 35 Days        |
| Daily Snapshots            | Daily                        | 90 Days        |
| Monthly Archives           | Monthly                      | 10 Years       |
| Disaster Recovery Replicas | Continuous / Near Real-Time  | Per DR Policy  |

Backups are:

- Encrypted at rest and in transit
- Stored across geographically separate locations in the United States
- Periodically validated through restoration testing

### 12.3 Recovery Objectives

Provider maintains the following disaster recovery objectives for production systems:

| Metric                          | Commitment |
| ------------------------------- | ---------- |
| Recovery Point Objective (RPO)  | 2 Hours    |
| Recovery Time Objective (RTO)   | 4 Hours    |

#### Definitions

- **Recovery Point Objective (RPO):** Maximum tolerable amount of data loss measured in time.
- **Recovery Time Objective (RTO):** Target time to restore service after a declared disaster event.

These objectives apply to:

- Production environments
- Critical platform infrastructure
- Customer production data repositories

#### Exclusions

RPO/RTO commitments do not apply to:

- Customer-managed integrations
- Third-party service outages outside Provider control
- Non-production or sandbox environments
- Force majeure events

---

## 13. Premium Support Tiers

Provider offers multiple support tiers designed to align with Customer operational requirements and annual contract value ("ACV").

### 13.1 Premium Support Features

| Feature                          | Premium Support |
| -------------------------------- | --------------- |
| Availability                     | 24x7x365        |
| Named Support Contacts           | Included        |
| Priority Queue Routing           | Included        |
| Senior Support Engineers         | Included        |
| Technical Account Manager (TAM)  | Included        |
| Quarterly Service Reviews        | Included        |
| Escalation Management            | Included        |
| SLA Reporting                    | Included        |
| Onboarding Assistance            | Included        |
| API & Integration Guidance       | Included        |

### 13.2 Premium Support Response Targets

| Severity      | Response Time                   |
| ------------- | ------------------------------- |
| P1 – Critical | 15 Minutes (on Slack or Teams)  |
| P2 – High     | 30 Minutes (on Slack or Teams)  |
| P3 – Medium   | 2 Business Hours                |
| P4 – Low      | 8 Business Hours                |

---

## 14. High ACV Customer Success Commitments

For Customers exceeding agreed ACV thresholds, Voicegain may additionally provide:

- Dedicated Customer Success Manager
- Executive business reviews
- Customized onboarding plans
- Solution architecture consultation
- Usage optimization workshops
- Security & compliance reviews
- Joint incident retrospectives
- Product roadmap alignment sessions

Eligibility and scope are defined in applicable Order Forms or Master Services Agreements.

---

## 15. Disaster Recovery Testing

Provider performs periodic disaster recovery and backup restoration testing to validate operational readiness.

| Activity                          | Frequency  |
| --------------------------------- | ---------- |
| Restore Testing                   | Quarterly  |
| Full Disaster Recovery Simulation | Annually   |

Summary results may be shared with enterprise Customers upon request and subject to confidentiality obligations.

---

## 16. SLA Exclusions

This SLA does not apply to issues resulting from:

- Misuse of the platform
- Unsupported integrations
- Customer customizations
- Internet or ISP failures
- Force majeure events
- Customer infrastructure failures
