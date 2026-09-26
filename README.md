# FreeCerts

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Verified Entries](https://img.shields.io/badge/verified-50-green.svg)
![Categories](https://img.shields.io/badge/categories-20-orange.svg)

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

## Browse by Category

- [Artificial Intelligence & Machine Learning](#artificial-intelligence--machine-learning)
- [Data Science & Analytics](#data-science--analytics)
- [Software Development](#software-development)
- [Web Development](#web-development)
- [Cybersecurity](#cybersecurity)
- [Cloud Computing](#cloud-computing)
- [DevOps & Infrastructure](#devops--infrastructure)
- [Networking](#networking)
- [Databases](#databases)
- [IT Support](#it-support)
- [Business & Management](#business--management)
- [Digital Marketing](#digital-marketing)
- [Project Management](#project-management)
- [Academic & University Courses](#academic--university-courses)
- [Engineering](#engineering)

## Certification Table

| Certification | Provider | Category | Level | Credential Type | Cost | Official Link |
|---------------|----------|----------|-------|-----------------|------|---------------|
| [Responsive Web Design Certification](https://www.freecodecamp.org/learn/2025/responsive-web-design/) | freeCodeCamp | Web Development | Beginner | `free_certificate` | Free | [Link](https://www.freecodecamp.org/learn/2025/responsive-web-design/) |
| [JavaScript Algorithms and Data Structures](https://www.freecodecamp.org/learn/2025/javascript-algorithms-and-data-structures/) | freeCodeCamp | Software Development | Beginner | `free_certificate` | Free | [Link](https://www.freecodecamp.org/learn/2025/javascript-algorithms-and-data-structures/) |
| [Python Programming Certification](https://www.freecodecamp.org/learn/2025/python-programming/) | freeCodeCamp | Software Development | Beginner | `free_certificate` | Free | [Link](https://www.freecodecamp.org/learn/2025/python-programming/) |
| [Relational Databases Certification](https://www.freecodecamp.org/learn/2025/relational-databases/) | freeCodeCamp | Databases | Beginner | `free_certificate` | Free | [Link](https://www.freecodecamp.org/learn/2025/relational-databases/) |
| [Front End Libraries Certification](https://www.freecodecamp.org/learn/2025/front-end-libraries/) | freeCodeCamp | Web Development | Intermediate | `free_certificate` | Free | [Link](https://www.freecodecamp.org/learn/2025/front-end-libraries/) |
| [Back End Development and APIs Certification](https://www.freecodecamp.org/learn/2025/back-end-development-and-apis/) | freeCodeCamp | Web Development | Intermediate | `free_certificate` | Free | [Link](https://www.freecodecamp.org/learn/2025/back-end-development-and-apis/) |
| [Certified Full Stack Developer Certification](https://www.freecodecamp.org/learn/2025/) | freeCodeCamp | Web Development | Intermediate | `free_certificate` | Free | [Link](https://www.freecodecamp.org/learn/2025/) |
| [CS50x: Introduction to Computer Science](https://cs50.harvard.edu/x/2025/certificate/) | Harvard University | Academic & University Courses | Beginner | `free_certificate` | Free | [Link](https://cs50.harvard.edu/x/2025/certificate/) |
| [CS50's Introduction to AI with Python](https://cs50.harvard.edu/ai/) | Harvard University | Artificial Intelligence & Machine Learning | Intermediate | `free_certificate` | Free | [Link](https://cs50.harvard.edu/ai/) |
| [CS50's Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/) | Harvard University | Web Development | Intermediate | `free_certificate` | Free | [Link](https://cs50.harvard.edu/web/) |
| [CS50's Mobile App Development with React Native](https://cs50.harvard.edu/mobile/) | Harvard University | Software Development | Intermediate | `free_certificate` | Free | [Link](https://cs50.harvard.edu/mobile/) |
| [Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning) | Kaggle Learn | Artificial Intelligence & Machine Learning | Beginner | `free_course_certificate` | Free | [Link](https://www.kaggle.com/learn/intro-to-machine-learning) |
| [Python Programming Course](https://www.kaggle.com/learn/python) | Kaggle Learn | Software Development | Beginner | `free_course_certificate` | Free | [Link](https://www.kaggle.com/learn/python) |
| [Pandas for Data Analysis](https://www.kaggle.com/learn/pandas) | Kaggle Learn | Data Science & Analytics | Beginner | `free_course_certificate` | Free | [Link](https://www.kaggle.com/learn/pandas) |
| [Data Visualization Course](https://www.kaggle.com/learn/data-visualization) | Kaggle Learn | Data Science & Analytics | Beginner | `free_course_certificate` | Free | [Link](https://www.kaggle.com/learn/data-visualization) |
| [Intro to SQL](https://www.kaggle.com/learn/intro-to-sql) | Kaggle Learn | Databases | Beginner | `free_course_certificate` | Free | [Link](https://www.kaggle.com/learn/intro-to-sql) |
| [Intro to Deep Learning](https://www.kaggle.com/learn/intro-to-deep-learning) | Kaggle Learn | Artificial Intelligence & Machine Learning | Intermediate | `free_course_certificate` | Free | [Link](https://www.kaggle.com/learn/intro-to-deep-learning) |
| [Feature Engineering Course](https://www.kaggle.com/learn/feature-engineering) | Kaggle Learn | Artificial Intelligence & Machine Learning | Intermediate | `free_course_certificate` | Free | [Link](https://www.kaggle.com/learn/feature-engineering) |
| [Introduction to Cybersecurity](https://www.netacad.com/courses/introduction-to-cybersecurity) | Cisco Networking Academy | Cybersecurity | Beginner | `free_course_certificate` | Free | [Link](https://www.netacad.com/courses/introduction-to-cybersecurity) |
| [Python Essentials 1](https://www.netacad.com/courses/python-essentials-1) | Cisco Networking Academy | Software Development | Beginner | `free_course_certificate` | Free | [Link](https://www.netacad.com/courses/python-essentials-1) |
| [Python Essentials 2](https://www.netacad.com/courses/python-essentials-2) | Cisco Networking Academy | Software Development | Intermediate | `free_course_certificate` | Free | [Link](https://www.netacad.com/courses/python-essentials-2) |
| [Getting Started with Cisco Packet Tracer](https://www.netacad.com/courses/getting-started-with-cisco-packet-tracer) | Cisco Networking Academy | Networking | Beginner | `free_course_certificate` | Free | [Link](https://www.netacad.com/courses/getting-started-with-cisco-packet-tracer) |
| [Introduction to Data Science](https://www.netacad.com/courses/introduction-to-data-science) | Cisco Networking Academy | Data Science & Analytics | Beginner | `free_course_certificate` | Free | [Link](https://www.netacad.com/courses/introduction-to-data-science) |
| [CCNA: Introduction to Networks](https://www.netacad.com/courses/introduction-to-networking) | Cisco Networking Academy | Networking | Beginner | `free_course_certificate` | Free | [Link](https://www.netacad.com/courses/introduction-to-networking) |
| [Cybersecurity Basics](https://www.netacad.com/courses/cybersecurity-basics) | Cisco Networking Academy | Cybersecurity | Beginner | `free_course_certificate` | Free | [Link](https://www.netacad.com/courses/cybersecurity-basics) |
| [Cisco Networking Academy — Free Course Catalogue](https://www.netacad.com/catalogs/learn?category=course) | Cisco | Networking | Beginner | `free_course_certificate` | Free | [Link](https://www.netacad.com/catalogs/learn?category=course) |
| [EC-Council — Free Cybersecurity Courses for Beginners](https://www.eccouncil.org/cybersecurity-exchange/cyber-novice/free-cybersecurity-courses-beginners/) | EC-Council | Cybersecurity | Beginner | `free_course_certificate` | Free | [Link](https://www.eccouncil.org/cybersecurity-exchange/cyber-novice/free-cybersecurity-courses-beginners/) |
| [ScholarHat — Free Courses](https://www.scholarhat.com/free-course) | ScholarHat | Software Development | Beginner | `free_course_certificate` | Free | [Link](https://www.scholarhat.com/free-course) |
| [IBM SkillsBuild — Free Learning and Digital Credentials](https://skillsbuild.org/) | IBM SkillsBuild | Artificial Intelligence & Machine Learning | Beginner | `free_course_certificate` | Free | [Link](https://skillsbuild.org/) |
| [Inbound Certification](https://academy.hubspot.com/courses/inbound) | HubSpot Academy | Digital Marketing | Beginner | `free_professional_certification` | Free | [Link](https://academy.hubspot.com/courses/inbound) |
| [Content Marketing Certification](https://academy.hubspot.com/courses/content-marketing) | HubSpot Academy | Digital Marketing | Intermediate | `free_professional_certification` | Free | [Link](https://academy.hubspot.com/courses/content-marketing) |
| [Email Marketing Certification](https://academy.hubspot.com/courses/email-marketing) | HubSpot Academy | Digital Marketing | Intermediate | `free_professional_certification` | Free | [Link](https://academy.hubspot.com/courses/email-marketing) |
| [Digital Marketing Certification](https://academy.hubspot.com/courses/digital-marketing) | HubSpot Academy | Digital Marketing | Intermediate | `free_professional_certification` | Free | [Link](https://academy.hubspot.com/courses/digital-marketing) |
| [Social Media Marketing Certification](https://academy.hubspot.com/courses/social-media-marketing) | HubSpot Academy | Digital Marketing | Intermediate | `free_professional_certification` | Free | [Link](https://academy.hubspot.com/courses/social-media-marketing) |
| [Inbound Sales Certification](https://academy.hubspot.com/courses/inbound-sales) | HubSpot Academy | Business & Management | Beginner | `free_professional_certification` | Free | [Link](https://academy.hubspot.com/courses/inbound-sales) |
| [Salesforce Trailhead Superbadges](https://trailhead.salesforce.com/superbadges) | Salesforce Trailhead | Software Development | Intermediate | `free_course_certificate` | Free | [Link](https://trailhead.salesforce.com/superbadges) |
| [AI Fundamentals on Google Skills](https://www.skills.google/paths/ai-fundamentals) | Google Cloud Skills Boost | Artificial Intelligence & Machine Learning | Beginner | `free_course_certificate` | Free | [Link](https://www.skills.google/paths/ai-fundamentals) |
| [Data Analytics Certificate on Google Skills](https://www.skills.google/paths/data-analytics) | Google Cloud Skills Boost | Data Science & Analytics | Beginner | `free_course_certificate` | Free | [Link](https://www.skills.google/paths/data-analytics) |
| [Generative AI Fundamentals on Google Skills](https://www.skills.google/paths/generative-ai-fundamentals) | Google Cloud Skills Boost | Artificial Intelligence & Machine Learning | Beginner | `free_course_certificate` | Free | [Link](https://www.skills.google/paths/generative-ai-fundamentals) |
| [Cybersecurity Certificate on Google Skills](https://www.skills.google/paths/cybersecurity) | Google Cloud Skills Boost | Cybersecurity | Beginner | `free_course_certificate` | Free | [Link](https://www.skills.google/paths/cybersecurity) |
| [Agile Explorer Badge](https://skillsbuild.org/digital-credentials) | IBM SkillsBuild | Project Management | Beginner | `free_course_certificate` | Free | [Link](https://skillsbuild.org/digital-credentials) |
| [Digital Literacy Badge](https://skillsbuild.org/digital-credentials) | IBM SkillsBuild | IT Support | Beginner | `free_course_certificate` | Free | [Link](https://skillsbuild.org/digital-credentials) |
| [IT Support Technician Certificate](https://skillsbuild.org/learning-catalog) | IBM SkillsBuild | IT Support | Beginner | `free_course_certificate` | Free | [Link](https://skillsbuild.org/learning-catalog) |
| [Software Engineering for Web Developers Certificate](https://skillsbuild.org/learning-catalog) | IBM SkillsBuild | Web Development | Intermediate | `free_course_certificate` | Free | [Link](https://skillsbuild.org/learning-catalog) |
| [Cybersecurity Analyst Fundamentals](https://skillsbuild.org/learning-catalog) | IBM SkillsBuild | Cybersecurity | Intermediate | `free_course_certificate` | Free | [Link](https://skillsbuild.org/learning-catalog) |
| [Oracle Cloud Infrastructure Foundations Associate](https://mylearn.oracle.com/) | Oracle University | Cloud Computing | Beginner | `free_professional_certification` | Free | [Link](https://mylearn.oracle.com/) |
| [Oracle AI Foundations Associate](https://mylearn.oracle.com/) | Oracle University | Artificial Intelligence & Machine Learning | Beginner | `free_professional_certification` | Free | [Link](https://mylearn.oracle.com/) |
| [MongoDB Overview Skill Badge](https://learn.mongodb.com/courses/mongodb-overview) | MongoDB University | Databases | Beginner | `free_course_certificate` | Free | [Link](https://learn.mongodb.com/courses/mongodb-overview) |
| [AWS Cloud Practitioner Essentials](https://aws.amazon.com/training/digital/) | AWS Training | Cloud Computing | Beginner | `free_course_certificate` | Free | [Link](https://aws.amazon.com/training/digital/) |
| [AWS Technical Essentials](https://aws.amazon.com/training/course-descriptions/technical-essentials/) | AWS Training | Cloud Computing | Beginner | `free_course_certificate` | Free | [Link](https://aws.amazon.com/training/course-descriptions/technical-essentials/) |
| [AWS Machine Learning Foundations](https://aws.amazon.com/training/digital/) | AWS Training | Artificial Intelligence & Machine Learning | Intermediate | `free_course_certificate` | Free | [Link](https://aws.amazon.com/training/digital/) |
| [AWS Cloud Security Fundamentals](https://aws.amazon.com/training/digital/) | AWS Training | Cybersecurity | Intermediate | `free_course_certificate` | Free | [Link](https://aws.amazon.com/training/digital/) |
| [AWS Solutions Architect Introduction](https://aws.amazon.com/training/digital/) | AWS Training | Cloud Computing | Intermediate | `free_course_certificate` | Free | [Link](https://aws.amazon.com/training/digital/) |
| [Azure Fundamentals Learning Path](https://learn.microsoft.com/en-us/credentials/certifications/azure-fundamental/) | Microsoft Learn | Cloud Computing | Beginner | `free_course_certificate` | Free | [Link](https://learn.microsoft.com/en-us/credentials/certifications/azure-fundamental/) |
| [AI Fundamentals Learning Path](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-fundamental/) | Microsoft Learn | Artificial Intelligence & Machine Learning | Beginner | `free_course_certificate` | Free | [Link](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-fundamental/) |
| [AI Business Professional Learning Path](https://learn.microsoft.com/en-us/credentials/certifications/ai-business-professional/) | Microsoft Learn | Artificial Intelligence & Machine Learning | Intermediate | `free_course_certificate` | Free | [Link](https://learn.microsoft.com/en-us/credentials/certifications/ai-business-professional/) |
| [DevOps Fundamentals Learning Path](https://learn.microsoft.com/en-us/training/paths/devops-fundamentals/) | Microsoft Learn | DevOps & Infrastructure | Beginner | `free_course_certificate` | Free | [Link](https://learn.microsoft.com/en-us/training/paths/devops-fundamentals/) |
| [Security Fundamentals Learning Path](https://learn.microsoft.com/en-us/credentials/certifications/security-fundamentals/) | Microsoft Learn | Cybersecurity | Beginner | `free_course_certificate` | Free | [Link](https://learn.microsoft.com/en-us/credentials/certifications/security-fundamentals/) |
| [Data Fundamentals Learning Path](https://learn.microsoft.com/en-us/credentials/certifications/azure-data-fundamentals/) | Microsoft Learn | Data Science & Analytics | Beginner | `free_course_certificate` | Free | [Link](https://learn.microsoft.com/en-us/credentials/certifications/azure-data-fundamentals/) |
| [Power Platform Fundamentals](https://learn.microsoft.com/en-us/training/paths/power-plat-fundamentals/) | Microsoft Learn | Software Development | Beginner | `free_course_certificate` | Free | [Link](https://learn.microsoft.com/en-us/training/paths/power-plat-fundamentals/) |
| [GitHub Fundamentals Learning Path](https://learn.microsoft.com/en-us/training/paths/github-fundamentals/) | Microsoft Learn | Software Development | Beginner | `free_course_certificate` | Free | [Link](https://learn.microsoft.com/en-us/training/paths/github-fundamentals/) |
| [Fortinet Cybersecurity Fundamentals](https://www.fortinet.com/training/courses) | Fortinet Training Institute | Cybersecurity | Beginner | `free_course_certificate` | Free | [Link](https://www.fortinet.com/training/courses) |
| [Network Security Fundamentals](https://www.fortinet.com/training/courses) | Fortinet Training Institute | Cybersecurity | Beginner | `free_course_certificate` | Free | [Link](https://www.fortinet.com/training/courses) |
| [Introduction to Deep Learning](https://www.nvidia.com/en-us/deep-learning-ai/education/) | NVIDIA Deep Learning Institute | Artificial Intelligence & Machine Learning | Intermediate | `free_course_certificate` | Free | [Link](https://www.nvidia.com/en-us/deep-learning-ai/education/) |
| [What Is Artificial Intelligence?](https://www.nvidia.com/en-us/deep-learning-ai/education/) | NVIDIA Deep Learning Institute | Artificial Intelligence & Machine Learning | Beginner | `free_course_certificate` | Free | [Link](https://www.nvidia.com/en-us/deep-learning-ai/education/) |
| [Google Analytics 4 (GA4) Course](https://skillshop.exceedlms.com/student/path/417) | Google | Digital Marketing | Intermediate | `free_course_certificate` | Free | [Link](https://skillshop.exceedlms.com/student/path/417) |
| [AWS Developer Fundamentals](https://aws.amazon.com/training/digital/) | AWS Training | Software Development | Intermediate | `free_course_certificate` | Free | [Link](https://aws.amazon.com/training/digital/) |
| [AWS Data Analytics Fundamentals](https://aws.amazon.com/training/digital/) | AWS Training | Data Science & Analytics | Beginner | `free_course_certificate` | Free | [Link](https://aws.amazon.com/training/digital/) |
| [Introduction to Linux](https://www.redhat.com/en/services/training/rh124-red-hat-system-administration-i) | Red Hat Training | Software Development | Beginner | `free_course_certificate` | Free | [Link](https://www.redhat.com/en/services/training/rh124-red-hat-system-administration-i) |
| [MATLAB Onramp](https://matlabacademy.mathworks.com/en/details/matlab-onramp/gettingstarted) | MathWorks | Software Development | Beginner | `free_course_certificate` | Free | [Link](https://matlabacademy.mathworks.com/en/details/matlab-onramp/gettingstarted) |
| [Simulink Onramp](https://matlabacademy.mathworks.com/details/simulink-onramp/simulink) | MathWorks | Engineering | Beginner | `free_course_certificate` | Free | [Link](https://matlabacademy.mathworks.com/details/simulink-onramp/simulink) |
| [Simscape Battery Onramp](https://matlabacademy.mathworks.com/details/simscape-battery-onramp/orsb) | MathWorks | Engineering | Intermediate | `free_course_certificate` | Free | [Link](https://matlabacademy.mathworks.com/details/simscape-battery-onramp/orsb) |
| [Claude Academy](https://academy.claude.com/courses) | Anthropic | Artificial Intelligence & Machine Learning | Beginner | `free_course_certificate` | Free | [Link](https://academy.claude.com/courses) |
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
