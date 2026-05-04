# SOC 1 engagement letter (AT-C §320)

For Service Organization Control 1 (SOC 1) examinations on
controls relevant to user entities' ICFR.

## Required elements

- [ ] Service organization name and system description scope.
- [ ] Report type: Type 1 (point-in-time) or Type 2 (period of
      operating effectiveness).
- [ ] Reporting period (Type 2: typically 6 or 12 months).
- [ ] Subservice organization treatment: carve-out or inclusive.
- [ ] CUEC identification process (complementary user-entity
      controls).
- [ ] Control objectives definition responsibility (service
      organization management).
- [ ] Independence affirmation.
- [ ] Use restriction language.

## Template

> **SOC 1 EXAMINATION ENGAGEMENT LETTER**
>
> [DATE]
>
> [SERVICE ORGANIZATION NAME / ADDRESS]
> Attention: [CIO / VP CONTROLS / CFO]
>
> Thank you for engaging [FIRM NAME] to perform an examination
> on controls at the service organization relevant to user
> entities' internal control over financial reporting.
>
> **Report type**
>
> We will issue a SOC 1 [Type 1 / Type 2] report. [Type 1: as of
> [POINT IN TIME]; design-only.] [Type 2: covering the period
> [START] through [END]; design and operating effectiveness.]
>
> **System description**
>
> Management's description of the service organization's system
> will cover [SCOPE — services delivered, processes, classes of
> transactions, relevant procedures, controls, monitoring].
>
> **Standard**
>
> Our engagement is performed in accordance with AT-C §320,
> "Reporting on an Examination of Controls at a Service
> Organization Relevant to User Entities' Internal Control over
> Financial Reporting." Our procedures will provide reasonable
> assurance.
>
> **Subservice organizations**
>
> Subservice organizations identified: [LIST e.g., AWS,
> Salesforce, payroll-processing firm].
>
> Subservice treatment: [CARVE-OUT — description excludes
> subservice controls / INCLUSIVE — description includes
> subservice controls; subservice provides assertion and
> auditor's report].
>
> [If carve-out:] Complementary subservice organization controls
> (CSOCs) at the subservice will be identified.
>
> **Complementary user entity controls (CUECs)**
>
> Management's description will identify CUECs (controls at
> user entities assumed to be in operation) necessary to achieve
> the control objectives.
>
> **Control objectives**
>
> Management is responsible for defining the control objectives
> reflecting the service organization's impact on user-entity
> ICFR. Vague control objectives (e.g., "transactions are
> processed accurately") are insufficient; objectives must tie
> to specific user-entity F/S assertions.
>
> **Management responsibilities**
>
> Service organization management is responsible for:
> - The description of the system.
> - The control objectives.
> - The design of controls.
> - [Type 2 only: operating effectiveness of controls.]
> - Providing access to records, information, and personnel.
> - Written representations at the date of the report.
>
> **Independence**
>
> We are independent of the service organization in accordance
> with the AICPA Code of Professional Conduct.
>
> **Restrictions on use**
>
> The SOC 1 report's use is restricted to:
> - Management of the service organization.
> - User entities of the service organization's system.
> - Auditors of user entities.
>
> **Form of report**
>
> The report will include management's assertion, our opinion on
> the description and on design (Type 1) or design + operating
> effectiveness (Type 2), and the testing details for relevant
> controls (Type 2).
>
> **Fees, termination, other terms**
>
> [SEE COMMON-CLAUSES TEMPLATE]
>
> **Indemnification limitation (attest)**
>
> Indemnification provisions favoring the firm for the firm's
> own acts are not included on this attest engagement
> (AICPA Ethics Interpretation §1.400.205).
>
> Please sign to indicate your agreement.
>
> [FIRM NAME / SIGNATURE]
>
> Acknowledged: [SERVICE ORG / DATE]

## Practitioner notes

- SOC 1 vs SOC 2: SOC 1 = ICFR-relevant controls; SOC 2 = Trust
  Services Criteria. Choose the right report type based on
  user-entity needs.
- Subservice treatment: carve-out is standard for hyperscaler
  cloud (AWS, Azure, GCP) and enterprise SaaS (Salesforce,
  Workday); inclusive method requires subservice cooperation.
- CUEC identification: critical for user-entity auditors to
  understand what they need to test at user entities.
- Control objectives must reflect service organization's impact
  on user-entity F/S (e.g., for a payroll processor, control
  objectives might address the accuracy and completeness of
  payroll calculations, withholding, deposits).
- Type 2 reports are more common; Type 1 typically issued only
  for first-year service organizations or when periods don't
  align.

## Authority

- AT-C §320 (SOC 1 examination): cite as `AICPA_SSAE`,
  `binding_on_member`.
- AT-C §105, §205 (common concepts, examinations): supporting.
- AICPA SOC for Service Organizations practice aid: practice_aid.
