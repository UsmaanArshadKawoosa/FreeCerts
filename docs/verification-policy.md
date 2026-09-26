# Verification Policy

## Overview

This document describes the methodology used to verify and maintain the accuracy of certification entries in the FreeCerts repository.

## Verification Process

### Step 1: Source Identification

- Locate the **official** course or certification page on the provider's website.
- Do not rely on third-party aggregators, blog posts, or unverified sources.
- Record the exact URL where the certification is offered.

### Step 2: Cost Verification

Confirm the following:

- **Learning material is free**: All videos, readings, exercises, and labs are accessible without payment.
- **Certificate is free**: The digital certificate, badge, or credential itself does not require payment.
- **Exam is free**: If an exam is required, confirm that the exam attempt is free.

### Step 3: Access Requirements

Check whether the certification requires:

- Account creation (free account is acceptable)
- Credit card (must be **no** for genuinely free certifications)
- Paid subscription (must be **no**)
- Free trial that converts to paid (exclude from primary directory)

### Step 4: Assessment Type

Record the method of credential award:

- **Exam**: Proctored or unproctored exam
- **Project**: Completion of a project or portfolio
- **Quiz**: Knowledge check or multiple-choice assessment
- **Peer Review**: Assessment by peers or instructors
- **None**: Automatic upon completion

### Step 5: Eligibility & Restrictions

Note any:

- Geographic limitations (e.g., available only in certain countries)
- Age restrictions
- Prerequisites (prior courses, experience, or education)
- Time limits or expiration dates
- Institutional requirements (e.g., student status)

### Step 6: Evidence Collection

For each entry, collect:

- Screenshot of the certification page showing free status
- Link to terms of service or pricing page
- Date of verification
- Any relevant notes or caveats

### Step 7: Documentation

Record all findings in the certification entry:

- `verification_status`: `verified`, `unverified`, or `needs_review`
- `last_verified`: Date in `YYYY-MM-DD` format
- `notes`: Any limitations, restrictions, or important details
- `certification_url`: Direct link to the official page
- `provider_url`: Link to the provider's main website

## Verification Frequency

- **New entries**: Must be verified at the time of submission.
- **Existing entries**: Reviewed at least annually.
- **Random audits**: Community members and maintainers may audit entries at any time.
- **Deprecation**: Entries that become paid, unavailable, or unverifiable are marked as deprecated.

## Deprecation Policy

When a certification changes from free to paid:

1. The entry is marked as `verification_status: "needs_review"`.
2. A note is added explaining the change.
3. After a 30-day grace period, the entry is removed from the primary directory.
4. The Git history preserves the record of the change.

## Community Verification

Community members are encouraged to:

- Submit verification evidence via GitHub issues.
- Report outdated or incorrect entries.
- Participate in review discussions.
- Suggest new verified certifications.

All community submissions undergo the same verification process as maintainer-submitted entries.

## Transparency

- All verification evidence is documented in Git history.
- No hidden criteria or subjective judgments are used.
- Decisions can be challenged via GitHub issues.
