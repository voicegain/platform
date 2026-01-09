---
title: "Voicegain — GDPR Compliance Form (SaaS Provider)"
subtitle: "Edge Deployment (Europe)"
company: "Resolvity, Inc. (dba Voicegain)"
product: "Voicegain Speech-to-Text (STT) Platform"
completed_by: "Jacek Jarmulak, CTO"
date_completed: "2025-12-10"
review_cycle: "Annual"
---

# Voicegain — GDPR Compliance Form (SaaS Provider)  
## Edge Deployment (Europe)

**Company:** Resolvity, Inc. (dba Voicegain)  
**Product / Service:** Voicegain Speech-to-Text (STT) Platform  
**Completed by:** Jacek Jarmulak, CTO  
**Date completed:** Dec 10, 2025  
**Review cycle:** Annual  

> **Scope:** This form applies specifically to the **Voicegain Edge deployment hosted in Google Cloud Platform (GCP) Europe**, including the local Voicegain Portal for the EU deployment.

---

## Quick Compliance Snapshot

| Area | Summary |
|------|---------|
| **Data categories** | Customer Account Data (names/emails/contract info) + transient End‑User audio/transcripts |
| **Processing role** | **Controller** for Customer Account Data; **Processor** for End‑User data |
| **Retention** | End‑User transcripts removed immediately after transcription; logs retained 30 days |
| **Subprocessors** | Google Cloud Platform (GKE, Firestore, Cloud Logging) |
| **EU transfers** | **None** — data stays within selected EU region |
| **DPO / DPIA** | Not required (low footprint, transient processing) |
| **Security posture** | SOC2 + PCI‑DSS aligned, encryption, RBAC, MFA, monitoring |

---

## Table of Contents
1. [Company Information](#1-company-information)  
2. [Summary of Personal Data Processed](#2-summary-of-personal-data-processed)  
3. [Purposes & Legal Basis for Processing](#3-purposes--legal-basis-for-processing)  
4. [Transparency & User Information](#4-transparency--user-information)  
5. [Data Subject Rights Handling](#5-data-subject-rights-handling)  
6. [Data Minimization & Retention](#6-data-minimization--retention)  
7. [Security Measures](#7-security-measures)  
8. [Processors & Subprocessors](#8-processors--subprocessors)  
9. [International Data Transfers](#9-international-data-transfers)  
10. [Data Protection Officer (DPO)](#10-data-protection-officer-dpo)  
11. [Records of Processing Activities (ROPA)](#11-records-of-processing-activities-ropa)  
12. [Data Protection by Design & Default](#12-data-protection-by-design--default)  
13. [Data Breach Response](#13-data-breach-response)  
14. [DPIA (Data Protection Impact Assessment)](#14-dpia-data-protection-impact-assessment)  
15. [Additional Compliance Notes](#15-additional-compliance-notes)

---

## 1. Company Information

**Regulatory basis:** GDPR Articles 5 and 24 require organizations to demonstrate accountability and clearly identify responsibility for data protection matters.

- **Company Name:** Resolvity, Inc. (dba Voicegain)  
- **Service / Product Name:** Voicegain Speech-to-Text (STT) Platform  
- **Date Completed:** Dec 10th, 2025  
- **Completed By / Role:** Jacek Jarmulak, CTO  
- **Review Cycle:** Annually  
- **Notes:** Applies to Voicegain Edge deployment in Google GCP Europe.

---

## 2. Summary of Personal Data Processed

**Regulatory basis:** GDPR Article 30 requires documenting what personal data is processed, from whom, and for what purposes.

### Categories of personal data
1. **Customer Account Data (direct collection)**  
   - Contractual information  
   - Names and emails of Customer employee Users  

2. **End‑User Audio and Transcript Data (customer-provided)**  
   - Audio streams and resulting transcripts  
   - May incidentally include personal information (e.g., names, phone numbers)

### Sources
- **Customer Account Data:** entered directly into the Voicegain Console  
- **End‑User Data:** audio recordings supplied by Customers (typically customer support calls)

### Data subjects
- Customer employee Users  
- End users whose speech is processed by a Customer using the Voicegain STT Platform

**Operational note:** End‑User Data is **transient** and is automatically removed after transcription.

---

## 3. Purposes & Legal Basis for Processing

**Regulatory basis:** GDPR Article 6 requires each purpose of processing to have a lawful basis.

Voicegain acts as:
- **Controller** for Customer Account Data  
- **Processor** for End‑User audio/transcripts

### Purposes
- **Customer Account Data:** access management, user identification, billing and operational functions  
- **End‑User Data:** generate speech‑to‑text transcripts requested by the Customer

### Legal basis
- **Customer Account Data:** Performance of Contract  
- **End‑User Data:** Consent obtained by the Customer (e.g., call recording consent)

---

## 4. Transparency & User Information

**Regulatory basis:** GDPR Articles 12–14 require clear, accessible information about how personal data is processed.

- **Privacy notice available:** Yes  
- **Privacy Notice URL:** https://github.com/voicegain/platform/blob/master/PRIVACY.md  

**Note:** The privacy notice covers the broader Voicegain platform and may include items not specific to EU Edge deployments.

---

## 5. Data Subject Rights Handling

**Regulatory basis:** GDPR Articles 15–22 grant individuals data subject rights.

As a processor for End‑User Data, Voicegain supports Customer handling of these rights.

- **Access:** Submitted via Customer; Voicegain assists as needed. End‑User data does not persist.  
- **Rectification:** Customer request; account data may be updated. End‑User data does not remain after processing.  
- **Erasure:** End‑User data is transient. Customer Account data deletable upon account closure.  
- **Restriction:** Managed by Customer; Voicegain follows Customer instructions.  
- **Portability:** End‑User data does not persist; Customer data exportable on request.  
- **Objection:** Managed by Customer.  
- **Automated Decision‑Making:** Not applicable (transcription only).

---

## 6. Data Minimization & Retention

**Regulatory basis:** GDPR Article 5(1)(c) (minimization) and 5(1)(e) (storage limitation).

### Minimization
- Only required Customer Account data is collected.  
- End‑User data is processed transiently and discarded.

### Retention
- **Customer Account Data:** retained for account duration.  
- **End‑User Data:** removed immediately after transcription.  
- **Logs:** retained 30 days; Customers may export logs externally.

### Deletion
- Transcripts deleted automatically (typically within seconds).  
- Transcripts are memory‑only unless explicitly configured otherwise by the Customer.

---

## 7. Security Measures

**Regulatory basis:** GDPR Article 32 requires appropriate technical and organizational measures.

### Technical controls
- Encryption at rest and in transit  
- RBAC + MFA  
- TLS  
- Network isolation  
- Monitoring and alerting  
- Container security  
- Alignment with PCI‑DSS practices

### Organizational controls
- SOC2 + PCI‑DSS compliance posture  
- Access control policies  
- Employee security training  
- Least‑privilege enforcement  
- Incident response procedures

---

## 8. Processors & Subprocessors

**Regulatory basis:** GDPR Article 28 requires oversight and agreements for subprocessors.

### Subprocessors
**Google Cloud Platform (GCP)** provides:
- **GKE** (compute)  
- **Firestore** (storage)  
- **Cloud Logging** (monitoring/logging)  

Regions are selected by the Customer.

### DPAs
GCP provides a GDPR‑compliant Data Processing Agreement.

---

## 9. International Data Transfers

**Regulatory basis:** GDPR Articles 44–49 restrict transfers outside the EU/EEA.

- End‑User Data does not leave the selected EU region.  
- The local Voicegain Portal for EU deployment keeps Customer employee data within the EU.

**Transfer mechanisms:** Not required for EU‑only deployments.

---

## 10. Data Protection Officer (DPO)

**Regulatory basis:** GDPR Article 37.

- **DPO required:** No  
- **Rationale:** Low GDPR footprint; processing is transient and not large‑scale sensitive data.

---

## 11. Records of Processing Activities (ROPA)

**Regulatory basis:** GDPR Article 30.

- **ROPA maintained:** No  
- **Rationale:** Voicegain qualifies for the exemption (<250 employees + low‑risk transient processing).

---

## 12. Data Protection by Design & Default

**Regulatory basis:** GDPR Article 25.

Voicegain implements:
- SOC2 + PCI‑DSS controls  
- Transient processing architecture (no transcript persistence by default)  
- EU region isolation  
- Security‑first engineering practices  
- Protections for both Customer Account and End‑User data

---

## 13. Data Breach Response

**Regulatory basis:** GDPR Articles 33–34.

### Detection
SOC2/PCI‑aligned monitoring, alerting, and escalation.

### Notification
Affected Customers notified **within 72 hours**, typically within several hours.

---

## 14. DPIA (Data Protection Impact Assessment)

**Regulatory basis:** GDPR Art. 35.

- **DPIA required:** No  
- **Rationale:** End‑User data processing is transient, does not persist after transcription, and does not involve large‑scale sensitive data.

**Outcome:** Not applicable.

---

## 15. Additional Compliance Notes

*(No additional notes provided.)*
