# Contributing to FreeCerts

Thank you for your interest in contributing to FreeCerts! This document provides guidelines and instructions for contributing.

## Code of Conduct

This project adheres to the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to uphold this code.

## How to Contribute

### Reporting Issues

- **Add a certification**: Use the [Add Certification](.github/ISSUE_TEMPLATE/add-certification.yml) issue form.
- **Report outdated information**: Use the [Report Outdated Entry](.github/ISSUE_TEMPLATE/report-outdated-entry.yml) issue form.

### Submitting Changes

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/my-new-certification`).
3. Make your changes following the guidelines below.
4. Run validation: `python scripts/validate_data.py`
5. Run tests: `python -m pytest tests/`
6. Commit your changes (`git commit -am 'Add certification: XYZ'`).
7. Push to the branch (`git push origin feature/my-new-certification`).
8. Open a Pull Request using the [PR template](.github/PULL_REQUEST_TEMPLATE.md).

## Certification Submission Guidelines

### Eligibility Requirements

Only submit certifications that meet ALL of the following criteria:

- The learning material is completely free (no paywalls, no paid tiers).
- The certificate, credential, or exam is free.
- No credit card is required to access or complete the certification.
- No paid subscription is required.
- The certification is from a reputable provider (university, technology company, recognized educational platform, or established nonprofit).
- The certification is not a limited free trial.

### Verification Checklist

Before submitting, verify the following:

- [ ] **Official Source**: The certification page is on the provider's official website.
- [ ] **Free Learning**: All course materials, videos, and exercises are accessible without payment.
- [ ] **Free Certificate**: The certificate or credential itself is free (not just a free trial).
- [ ] **No Credit Card**: Registration and completion do not require a credit card.
- [ ] **No Subscription**: The certification does not require a paid subscription.
- [ ] **Geographic Access**: The certification is accessible in your region (note any restrictions).
- [ ] **Assessment Type**: Clearly documented whether the credential requires an exam, project, quiz, or is automatic.
- [ ] **Certificate Format**: Confirm whether the credential is digital, printable, or both.
- [ ] **Expiration**: Check if the certificate or exam access expires.
- [ ] **Last Verified**: Record the date you verified the information.

### Data Format

All certifications must follow the JSON schema defined in [`schema/certification.schema.json`](schema/certification.schema.json).

Required fields:
- `id`: Unique slug (e.g., `provider-certification-name`)
- `name`: Full certification name
- `provider`: Provider name
- `provider_url`: Provider's official website
- `certification_url`: Direct URL to the certification page
- `category`: Must match one of the predefined categories
- `credential_type`: Must be one of the predefined credential types
- `difficulty`: `beginner`, `intermediate`, or `advanced`
- `learning_cost`: `free`, `paid`, or `freemium`
- `certificate_cost`: `free`, `paid`, or `freemium`
- `exam_cost`: `free`, `paid`, `none`, or `freemium`
- `account_required`: `true` or `false`
- `credit_card_required`: `true` or `false`
- `subscription_required`: `true` or `false`
- `verification_status`: `verified`, `unverified`, or `needs_review`
- `last_verified`: Date in `YYYY-MM-DD` format
- `notes`: Any relevant limitations or eligibility conditions

### Prohibited Submissions

Do NOT submit:

- Certifications that require a credit card for a "free trial" that automatically converts to a paid subscription.
- Affiliate links or referral links.
- Promotional content or spam.
- Fabricated or unverifiable certifications.
- Certifications where only the course is free but the certificate/exam is paid (use `free_training_paid_exam` if applicable, but these will not appear in the primary directory).
- Duplicate entries for the same certification.
- Expired or discontinued programs without noting their deprecated status.

## Pull Request Guidelines

### PR Title Format

Use a descriptive title:
- `Add certification: AWS Cloud Practitioner`
- `Update: freeCodeCamp Python Certification`
- `Fix: Corrected URL for HubSpot Inbound Certification`
- `Deprecate: Oracle Database SQL Certification (no longer free)`

### PR Description

Include the following in your PR description:

1. **Summary**: Brief description of the change.
2. **Certification Details**: Name, provider, URL, and category.
3. **Verification**: Date verified and method used.
4. **Testing**: Confirm the entry passes validation.
5. **Screenshots**: Optional screenshots of the certification page showing free status.

### Review Process

- All PRs are reviewed by maintainers.
- Maintainers may request changes or clarification.
- PRs that do not pass validation or do not meet contribution guidelines will be closed.
- Approved PRs are merged into the `main` branch.

## Validation

Before submitting, run the validation script:

```bash
python scripts/validate_data.py
```

This checks:
- JSON syntax and required fields
- JSON Schema compliance
- Unique IDs
- Valid category and credential-type values
- Valid difficulty values
- Correct date formats
- Valid HTTP/HTTPS URL syntax
- Duplicate certification URLs

## Questions?

Open an issue if you have questions about contributing or need clarification on any guidelines.
