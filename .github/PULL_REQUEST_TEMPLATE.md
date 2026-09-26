# Pull Request Template

## Description

Please include a summary of the change and the motivation behind it.

## Type of Change

- [ ] Add new certification(s)
- [ ] Update existing certification(s)
- [ ] Deprecate/remove certification(s)
- [ ] Fix data errors or broken URLs
- [ ] Update documentation
- [ ] Update validation scripts or tests
- [ ] Other (please describe):

## Certifications Added/Modified

List any certifications added or modified in this PR:

- `certification-id`: Brief description of change

## Verification Checklist

- [ ] I have verified that the certification is genuinely free.
- [ ] I have confirmed the certificate/credential is free.
- [ ] I have checked that no credit card or paid subscription is required.
- [ ] I have provided the official provider and certification URLs.
- [ ] The entry follows the JSON schema (`schema/certification.schema.json`).
- [ ] The entry passes validation (`python scripts/validate_data.py`).
- [ ] The entry passes tests (`python -m pytest tests/`).
- [ ] I have reviewed the [CONTRIBUTING.md](CONTRIBUTING.md) guidelines.

## Screenshots (if applicable)

Add screenshots showing the free certification status (optional but helpful).

## Additional Notes

Add any other context or notes about the PR here.
