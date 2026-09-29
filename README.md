# FreeCerts

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Verified Entries](https://img.shields.io/badge/verified-10-green.svg)
![Categories](https://img.shields.io/badge/categories-7-orange.svg)

A community-maintained, curated directory of genuinely free certifications, professional certificates, and certificate-awarding courses from reputable organizations, universities, technology companies, and educational platforms.

**Free and open source. No paid APIs, subscriptions, or proprietary dependencies.**

## Table of Contents

- [Quick Start](#quick-start)
- [Browse by Category](#browse-by-category)
- [Certification Table](#certification-table)
- [Credential Types](#credential-types)
- [Data Verification](#data-verification)
- [Contributing](#contributing)
- [Repository Structure](#repository-structure)

## Quick Start

FreeCerts is a data-first repository. All certifications are stored in [`data/certifications.json`](data/certifications.json) and validated against [`schema/certification.schema.json`](schema/certification.schema.json).

To browse:

1. Scroll down to the [Certification Table](#certification-table) below.
2. Use your browser's search (Ctrl+F / Cmd+F) to filter by provider, category, or keyword.
3. Check the "Credential Type" column to understand what kind of credential each entry offers.



## Certification Table

| Certification | Provider | Category | Level | Credential Type | Cost | Official Link |
|---------------|----------|----------|-------|-----------------|------|---------------|
| [MATLAB Onramp](https://matlabacademy.mathworks.com/en/details/matlab-onramp/gettingstarted) | MathWorks | Software Development | Beginner | `free_course_certificate` | Free | [Link](https://matlabacademy.mathworks.com/en/details/matlab-onramp/gettingstarted) |
| [Simulink Onramp](https://matlabacademy.mathworks.com/details/simulink-onramp/simulink) | MathWorks | Engineering | Beginner | `free_course_certificate` | Free | [Link](https://matlabacademy.mathworks.com/details/simulink-onramp/simulink) |
| [Simscape Battery Onramp](https://matlabacademy.mathworks.com/details/simscape-battery-onramp/orsb) | MathWorks | Engineering | Intermediate | `free_course_certificate` | Free | [Link](https://matlabacademy.mathworks.com/details/simscape-battery-onramp/orsb) |
| [Claude Academy](https://academy.claude.com/courses) | Anthropic | Artificial Intelligence & Machine Learning | Beginner | `free_course_certificate` | Free | [Link](https://academy.claude.com/courses) |
| [Cisco Networking Academy — Free Course Catalogue](https://www.netacad.com/catalogs/learn?category=course) | Cisco Networking Academy | Networking | Beginner | `free_course_certificate` | Free | [Link](https://www.netacad.com/catalogs/learn?category=course) |
| [EC-Council — Free Cybersecurity Courses for Beginners](https://www.eccouncil.org/cybersecurity-exchange/cyber-novice/free-cybersecurity-courses-beginners/) | EC-Council | Cybersecurity | Beginner | `free_course_certificate` | Free | [Link](https://www.eccouncil.org/cybersecurity-exchange/cyber-novice/free-cybersecurity-courses-beginners/) |
| [ScholarHat — Free Courses](https://www.scholarhat.com/free-course) | ScholarHat | Software Development | Beginner | `free_course_certificate` | Free | [Link](https://www.scholarhat.com/free-course) |
| [IBM SkillsBuild — Free Learning and Digital Credentials](https://skillsbuild.org/) | IBM SkillsBuild | Artificial Intelligence & Machine Learning | Beginner | `free_course_certificate` | Free | [Link](https://skillsbuild.org/) |
| [HP LIFE — Free Courses](https://www.life-global.org/) | HP LIFE | Business & Management | Beginner | `free_course_certificate` | Free | [Link](https://www.life-global.org/) |
| [Forage — Free Virtual Job Simulations](https://www.theforage.com/simulations) | Forage | Career Development | Beginner | `free_course_certificate` | Free | [Link](https://www.theforage.com/simulations) |

## Credential Types

| Type | Description |
|------|-------------|
| `free_certificate` | The course and certificate are completely free. |
| `free_professional_certification` | The certification and required assessment or exam are free. |
| `free_course_certificate` | A free educational course awards a certificate, but it is not necessarily an industry-recognized professional certification. |
| `free_training_paid_exam` | Training is free, but the certification examination costs money. **Not included in the primary directory.** |
| `financial_aid_or_scholarship` | Free access depends on financial aid or an application. **Kept separate from universally free options.** |
| `free_trial_only` | Access depends on a limited free trial. **Excluded from the genuinely free directory.** |

### Distinction Between Credentials

- **Professional Certification**: Industry-recognized credential awarded after passing a formal exam or assessment (e.g., Oracle Cloud Infrastructure Foundations, HubSpot certifications).
- **Course Completion Certificate**: Certificate awarded for completing a course, may not be industry-recognized (e.g., Kaggle Learn, freeCodeCamp).
- **Digital Badge**: Visual credential (often via Credly) representing a specific skill or achievement.
- **Attendance Certificate**: Certificate for participating in or completing a course, not necessarily assessing competency.

## Data Verification

Every entry in this repository follows a strict verification methodology:

1. **Official Source Verification**: We locate the official course or certification page on the provider's website.
2. **Cost Verification**: We confirm that both the learning material and the certificate/credential are free.
3. **Access Requirements**: We check whether account creation, subscription, credit card, or paid access is required.
4. **Assessment Type**: We record whether the credential is awarded automatically, after an assessment, or after an examination.
5. **Eligibility & Restrictions**: We note any geographic limitations, eligibility restrictions, or expiration dates.
6. **Date Stamping**: Every entry includes a `last_verified` date.
7. **Evidence**: Official enrollment or certification URLs are recorded for every entry.

**Unverified entries are marked with `verification_status: "unverified"` and may be moved to a separate section or excluded from the primary directory.**

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### Quick Contribution Checklist

- [ ] Verify the certification is genuinely free (no credit card, no subscription).
- [ ] Confirm the certificate or credential is free (not just the course).
- [ ] Provide the official provider URL.
- [ ] Check for geographic or eligibility restrictions.
- [ ] Record the verification date.
- [ ] Ensure the entry passes JSON schema validation.

### Reporting Issues

- **Add a certification**: Use the [Add Certification](.github/ISSUE_TEMPLATE/add-certification.yml) issue form.
- **Report outdated information**: Use the [Report Outdated Entry](.github/ISSUE_TEMPLATE/report-outdated-entry.yml) issue form.

## Repository Structure

```
FreeCerts/
├── README.md                      # This file
├── CONTRIBUTING.md                # Contribution guidelines
├── CODE_OF_CONDUCT.md             # Community standards
├── LICENSE                        # MIT License
├── SECURITY.md                    # Security policy
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── add-certification.yml
│   │   └── report-outdated-entry.yml
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
│       └── validate-data.yml
├── data/
│   ├── certifications.json        # Main dataset
│   ├── providers.json             # Provider information
│   └── categories.json            # Category taxonomy
├── schema/
│   └── certification.schema.json  # JSON Schema validation
├── scripts/
│   ├── validate_data.py           # Data validation script
│   └── check_links.py             # Link checker (optional)
├── docs/
│   ├── verification-policy.md     # Verification methodology
│   ├── certification-types.md     # Credential type definitions
│   └── maintenance.md             # Maintenance and review policy
└── tests/
    └── test_data.py               # Automated tests
```

## Data License

The data in this repository is licensed under the [MIT License](LICENSE).

## Maintenance Policy

- **Review Cycle**: Entries are reviewed at least annually.
- **Deprecation**: Entries that become paid, unavailable, or unverifiable are marked as deprecated and removed after a grace period.
- **Community Audits**: The community is encouraged to submit issues for outdated or incorrect entries.
- **Transparency**: All changes are tracked via Git history.

---

**Last Dataset Verification**: 2026-09-26
