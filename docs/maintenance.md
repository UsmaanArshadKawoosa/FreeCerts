# Maintenance Policy

## Overview

This document describes how the FreeCerts repository is maintained, reviewed, and updated.

## Review Cycle

- **Continuous**: Entries are reviewed as issues are submitted.
- **Annual Review**: All entries are reviewed at least once per year.
- **Ad-hoc**: Maintainers may update entries when providers announce changes.

## Deprecation Process

When a certification is no longer free or available:

1. **Mark as needs_review**: Update `verification_status` to `needs_review`.
2. **Add note**: Explain the change in the `notes` field.
3. **Grace period**: Keep the entry for 30 days with a deprecation notice.
4. **Remove**: After the grace period, remove the entry from the primary directory.
5. **Archive**: The Git history preserves the record of the change.

## Community Involvement

- **Issue reporting**: Community members can report outdated entries via GitHub issues.
- **Verification**: Community members can submit verification evidence.
- **Review**: Community members may participate in PR reviews.
- **Moderation**: Maintainers moderate all submissions and issues.

## Data Quality Standards

All entries must meet these standards:

- **Verified**: Must have `verification_status: "verified"` and a recent `last_verified` date.
- **Accurate**: All fields must be truthful and up-to-date.
- **Complete**: All required fields must be present.
- **Valid**: Must pass JSON schema validation.
- **Unique**: No duplicate IDs or URLs.

## Automated Checks

GitHub Actions runs on every push and PR:

- JSON syntax validation
- JSON Schema compliance
- Unique ID and URL checks
- Valid category and credential-type values
- Valid date and URL formats
- Required field presence

## Manual Reviews

Maintainers perform periodic manual reviews:

- Verify that URLs are still accessible
- Confirm that certifications are still free
- Check for new certifications from known providers
- Review and resolve open issues

## Versioning

- The dataset follows semantic versioning.
- Breaking changes to the schema increment the major version.
- Additions to categories or credential types increment the minor version.
- Bug fixes and corrections increment the patch version.

## Changelog

Changes to the dataset are tracked in Git history. Significant changes are documented in release notes.

## Contact

For questions about maintenance or to report issues:

- Open a GitHub issue
- Tag maintainers in the issue
- Follow the contribution guidelines in CONTRIBUTING.md
