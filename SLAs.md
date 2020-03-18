# Voicegain Cloud Platform Service Level Agreement (SLA)
Last modified: March 18, 2020 

During the Term of the agreement under which Voicegain has agreed to provide Voicegain Cloud Platform to Customer (as applicable, the "Agreement"), the Covered Service will provide a Monthly Uptime Percentage to Customer as follows (the "Service Level Objective" or "SLO"):

| Covered Service      | Monthly Uptime Percentage |
|----------------------|---------------------------|
| Web API              | >= 99.9%                  |
| Web API Preemptible | >= 99.0%                  |

If Voicegain does not meet the SLO, and if Customer meets its obligations under this SLA, Customer will be eligible to receive the Financial Credits described below. This SLA states Customer’s sole and exclusive remedy for any failure by Voicegain to meet the SLO. Capitalized terms used in this SLA, but not defined in this SLA, have the meaning stated in the Agreement. 

## Definitions
The following definitions apply to the SLA:

* **"Preemptible"** means the request was made to preemptible resources as indicated by "preemptible" parameter in the request being se to "true"
* **"Back-off Requirements"** means, when an error occurs, the Customer is responsible for waiting for a period of time before issuing another request. This means that after the first error, there is a minimum back-off interval of 1 second and for each consecutive error, the back-off interval increases exponentially up to 32 seconds.

* **"Covered Service"** means all Web APIs provided to customer as well as the Web Portal

* **"Downtime"** means more than a 2.5% Error Rate. Downtime is measured based on server side Error Rate.

* **"Downtime Period"** means a period of one or more consecutive minutes of Downtime. Partial minutes or Intermittent Downtime for a period of less than one minute will not be counted towards any Downtime Periods.

* **"Error Rate"** : means the number of Valid Requests that result in a response with HTTP Status 500 divided by the total number of Valid Requests during that period. Repeated identical requests do not count towards the Error Rate unless they conform to the Back-off Requirements. 

* **"Financial Credit"** means the following:

  |Covered Service     |Monthly Uptime Percentage	|Percentage of monthly bill for Covered Service which does not meet SLO that will be credited to future monthly bills of Customer|
  |--------------------|---------------------------|---------------------------------------|
  |Web API             |99% – < 99.9%	 |10% |
  |Web API             |95.0% – < 99.0%  |25% |
  |Web API             |< 95.0%	         |50% |
  |Web API Preemptible|95.0% – < 99.0%  |10% |
  |Web API Preemptible|90.0% – < 95.0%  |20% |
  |Web API Preemptible|< 90.0%	         |40% |

* **"Monthly Uptime Percentage"** means total number of minutes in a month, minus the number of minutes of Downtime suffered from all Downtime Periods in a month, divided by the total number of minutes in a month.

* **"Valid Requests"** are requests that conform to the Documentation, and that would normally result in a non-error response.

## Customer Must Request Financial Credit
In order to receive any of the Financial Credits described above, Customer must notify Voicegain technical support (via support portal) within 30 days from the time Customer becomes eligible to receive a Financial Credit. Customer must also provide Voicegain with identifying information (e.g., Account Name or ID) and the date and time those errors occurred. If Customer does not comply with these requirements, Customer will forfeit its right to receive a Financial Credit. If a dispute arises with respect to this SLA, Voicegain will make a determination in good faith based on its system logs, monitoring reports, configuration records, and other available information.

## Maximum Financial Credit
The total maximum number of Financial Credits to be issued by Voicegain to Customer for any and all Downtime Periods that occur in a single billing month will not exceed 50% of the amount due by Customer for the Covered Service for the applicable month.  Financial Credits will be made in the form of a monetary credit applied to future use of the Service and will be applied within 60 days after the Financial Credit was requested.

## SLA Exclusions
The SLA does not apply to any: (a) features designated Alpha or Beta (unless otherwise stated in the associated Documentation), (b) features excluded from the SLA (in the associated Documentation), or (c) errors: (i) caused by factors outside of Voicegain’s reasonable control; (ii) that resulted from Customer’s software or hardware or third party software or hardware, or both; (iii) that resulted from abuses or other behaviors that violate the Agreement; (iv) that resulted from quotas applied by the system or listed in the Admin Console; or (v) that resulted from Customer use of the Covered Service inconsistent with the Documentation, including but not limited to invalid request fields, unauthorized users, or inaccessible data.

## Indicative Connection Latencies
Connection Latencies, defined as roundtrip time for start of TLS handshake, are **not part of the SLA**, as they depend partially on Customer's network provider.
For indication, below we list the Connection Latencies to be expected given the current location of Voicegain services.
| From Region    | Expected Connection Latencies |
|----------------|-------------------------------|
| [US East Coast](https://updown.io/xa7t)  | <15ms                         |
| [US West Coast](https://updown.io/xa7t)  | 60-80ms                       |
| [Europe](https://updown.io/onvf)         | 80-125ms                      |
| [East Asia](https://updown.io/ntbh)      | 160-250ms                     |
| India          | 250-300ms                     |
