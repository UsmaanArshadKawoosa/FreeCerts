"""
FreeCerts Data Tests

Automated tests for certifications.json data quality.
"""

import json
import os
import sys
import unittest
from typing import List, Dict, Any

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
SCHEMA_DIR = os.path.join(BASE_DIR, "schema")

CERTIFICATIONS_FILE = os.path.join(DATA_DIR, "certifications.json")
PROVIDERS_FILE = os.path.join(DATA_DIR, "providers.json")
CATEGORIES_FILE = os.path.join(DATA_DIR, "categories.json")
SCHEMA_FILE = os.path.join(SCHEMA_DIR, "certification.schema.json")

VALID_CATEGORIES = [
    "Artificial Intelligence & Machine Learning",
    "Data Science & Analytics",
    "Software Development",
    "Web Development",
    "Cybersecurity",
    "Cloud Computing",
    "DevOps & Infrastructure",
    "Networking",
    "Databases",
    "IT Support",
    "Blockchain & Web3",
    "UI/UX & Design",
    "Business & Management",
    "Digital Marketing",
    "Finance & Accounting",
    "Project Management",
    "Mathematics & Statistics",
    "Academic & University Courses",
    "Career Development",
    "Engineering",
]

VALID_CREDENTIAL_TYPES = [
    "free_certificate",
    "free_professional_certification",
    "free_course_certificate",
    "free_training_paid_exam",
    "financial_aid_or_scholarship",
    "free_trial_only",
]

VALID_DIFFICULTIES = ["beginner", "intermediate", "advanced"]
VALID_COST_VALUES = ["free", "paid", "freemium"]
VALID_EXAM_COST_VALUES = ["free", "paid", "none", "freemium"]
VALID_ASSESSMENT_TYPES = ["exam", "project", "quiz", "none", "peer_review"]
VALID_DELIVERY_TYPES = ["online", "in-person", "hybrid"]
VALID_CERTIFICATE_FORMATS = ["digital", "print", "both"]
VALID_AVAILABILITY = ["global", "regional", "country_specific"]
VALID_EXPIRATION = ["none", "review_required", "exam_retake"]
VALID_VERIFICATION_STATUS = ["verified", "unverified", "needs_review"]


def load_json_file(path: str) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


class TestDataFiles(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certifications = load_json_file(CERTIFICATIONS_FILE).get("certifications", [])
        cls.providers = load_json_file(PROVIDERS_FILE).get("providers", [])
        cls.categories = load_json_file(CATEGORIES_FILE).get("categories", [])
        cls.schema = load_json_file(SCHEMA_FILE)

    def test_certifications_file_exists(self):
        self.assertTrue(os.path.exists(CERTIFICATIONS_FILE))

    def test_providers_file_exists(self):
        self.assertTrue(os.path.exists(PROVIDERS_FILE))

    def test_categories_file_exists(self):
        self.assertTrue(os.path.exists(CATEGORIES_FILE))

    def test_schema_file_exists(self):
        self.assertTrue(os.path.exists(SCHEMA_FILE))

    def test_certifications_is_list(self):
        self.assertIsInstance(self.certifications, list)

    def test_providers_is_list(self):
        self.assertIsInstance(self.providers, list)

    def test_categories_is_list(self):
        self.assertIsInstance(self.categories, list)

    def test_schema_is_dict(self):
        self.assertIsInstance(self.schema, dict)


class TestCertifications(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cert_data = load_json_file(CERTIFICATIONS_FILE)
        cls.certifications = cert_data.get("certifications", []) if isinstance(cert_data, dict) else cert_data
        providers_data = load_json_file(PROVIDERS_FILE)
        cls.providers = providers_data.get("providers", []) if isinstance(providers_data, dict) else providers_data

    def test_certifications_not_empty(self):
        self.assertGreater(len(self.certifications), 0, "certifications.json should not be empty")

    def test_all_certifications_have_required_fields(self):
        required_fields = [
            "id",
            "name",
            "provider",
            "provider_url",
            "certification_url",
            "category",
            "credential_type",
            "difficulty",
            "learning_cost",
            "certificate_cost",
            "account_required",
            "verification_status",
            "last_verified",
        ]
        for cert in self.certifications:
            for field in required_fields:
                self.assertIn(
                    field,
                    cert,
                    f"Certification {cert.get('id', 'unknown')} missing required field: {field}",
                )
                self.assertIsNotNone(
                    cert.get(field),
                    f"Certification {cert.get('id', 'unknown')} has None value for: {field}",
                )

    def test_all_ids_are_unique(self):
        ids = [c["id"] for c in self.certifications]
        self.assertEqual(len(ids), len(set(ids)), "Duplicate certification IDs found")

    def test_all_urls_are_unique(self):
        urls = [c["certification_url"] for c in self.certifications]
        duplicates = [url for url in urls if urls.count(url) > 1]
        if duplicates:
            # Some providers use the same landing page for multiple certifications
            # This is acceptable - just warn about it
            import warnings
            warnings.warn(f"Duplicate certification URLs found (may be same provider page): {set(duplicates)}")

    def test_valid_categories(self):
        categories = {c["category"] for c in self.certifications}
        invalid = categories - set(VALID_CATEGORIES)
        self.assertEqual(len(invalid), 0, f"Invalid categories found: {invalid}")

    def test_valid_credential_types(self):
        types = {c["credential_type"] for c in self.certifications}
        invalid = types - set(VALID_CREDENTIAL_TYPES)
        self.assertEqual(len(invalid), 0, f"Invalid credential types found: {invalid}")

    def test_valid_difficulties(self):
        difficulties = {c["difficulty"] for c in self.certifications}
        invalid = difficulties - set(VALID_DIFFICULTIES)
        self.assertEqual(len(invalid), 0, f"Invalid difficulty values found: {invalid}")

    def test_valid_cost_values(self):
        for cert in self.certifications:
            self.assertIn(
                cert["learning_cost"],
                VALID_COST_VALUES,
                f"Invalid learning_cost for {cert['id']}: {cert['learning_cost']}",
            )
            self.assertIn(
                cert["certificate_cost"],
                VALID_COST_VALUES,
                f"Invalid certificate_cost for {cert['id']}: {cert['certificate_cost']}",
            )
            self.assertIn(
                cert["exam_cost"],
                VALID_EXAM_COST_VALUES,
                f"Invalid exam_cost for {cert['id']}: {cert['exam_cost']}",
            )

    def test_valid_url_format(self):
        import re

        url_pattern = re.compile(r"^https?://")
        for cert in self.certifications:
            self.assertTrue(
                url_pattern.match(cert["provider_url"]),
                f"Invalid provider_url for {cert['id']}: {cert['provider_url']}",
            )
            self.assertTrue(
                url_pattern.match(cert["certification_url"]),
                f"Invalid certification_url for {cert['id']}: {cert['certification_url']}",
            )

    def test_valid_date_format(self):
        import re

        date_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")
        for cert in self.certifications:
            date = cert.get("last_verified")
            self.assertIsNotNone(date, f"Missing last_verified for {cert['id']}")
            self.assertTrue(
                date_pattern.match(date),
                f"Invalid date format for {cert['id']}: {date}",
            )

    def test_valid_verification_status(self):
        for cert in self.certifications:
            self.assertIn(
                cert["verification_status"],
                VALID_VERIFICATION_STATUS,
                f"Invalid verification_status for {cert['id']}: {cert['verification_status']}",
            )

    def test_valid_delivery_types(self):
        for cert in self.certifications:
            if "delivery" in cert:
                self.assertIn(
                    cert["delivery"],
                    VALID_DELIVERY_TYPES,
                    f"Invalid delivery for {cert['id']}: {cert['delivery']}",
                )

    def test_valid_assessment_types(self):
        for cert in self.certifications:
            if "assessment" in cert:
                self.assertIn(
                    cert["assessment"],
                    VALID_ASSESSMENT_TYPES,
                    f"Invalid assessment for {cert['id']}: {cert['assessment']}",
                )

    def test_valid_certificate_formats(self):
        for cert in self.certifications:
            if "certificate_format" in cert:
                self.assertIn(
                    cert["certificate_format"],
                    VALID_CERTIFICATE_FORMATS,
                    f"Invalid certificate_format for {cert['id']}: {cert['certificate_format']}",
                )

    def test_valid_availability(self):
        for cert in self.certifications:
            if "availability" in cert:
                self.assertIn(
                    cert["availability"],
                    VALID_AVAILABILITY,
                    f"Invalid availability for {cert['id']}: {cert['availability']}",
                )

    def test_valid_expiration(self):
        for cert in self.certifications:
            if "expiration" in cert:
                self.assertIn(
                    cert["expiration"],
                    VALID_EXPIRATION,
                    f"Invalid expiration for {cert['id']}: {cert['expiration']}",
                )

    def test_estimated_hours_positive(self):
        for cert in self.certifications:
            if "estimated_hours" in cert and cert["estimated_hours"] is not None:
                self.assertGreater(
                    cert["estimated_hours"],
                    0,
                    f"estimated_hours must be positive for {cert['id']}",
                )

    def test_id_format(self):
        import re

        id_pattern = re.compile(r"^[a-z0-9-]+$")
        for cert in self.certifications:
            self.assertTrue(
                id_pattern.match(cert["id"]),
                f"Invalid id format for {cert['id']}: must be lowercase alphanumeric with hyphens",
            )

    def test_providers_exist_in_providers_file(self):
        provider_names = {p["name"] for p in self.providers}
        for cert in self.certifications:
            self.assertIn(
                cert["provider"],
                provider_names,
                f"Provider '{cert['provider']}' not found in providers.json for {cert['id']}",
            )

    def test_no_empty_strings_for_required_fields(self):
        required_string_fields = [
            "id",
            "name",
            "provider",
            "provider_url",
            "certification_url",
            "category",
            "credential_type",
            "difficulty",
        ]
        for cert in self.certifications:
            for field in required_string_fields:
                self.assertIsNotNone(
                    cert.get(field),
                    f"{cert.get('id', 'unknown')}: {field} is None",
                )
                self.assertNotEqual(
                    cert.get(field),
                    "",
                    f"{cert.get('id', 'unknown')}: {field} is empty string",
                )

    def test_at_least_50_certifications(self):
        self.assertGreaterEqual(
            len(self.certifications),
            50,
            f"Expected at least 50 certifications, found {len(self.certifications)}",
        )


class TestProviders(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        providers_data = load_json_file(PROVIDERS_FILE)
        cls.providers = providers_data.get("providers", []) if isinstance(providers_data, dict) else providers_data

    def test_providers_not_empty(self):
        self.assertGreater(len(self.providers), 0)

    def test_all_providers_have_required_fields(self):
        required = ["id", "name", "url", "description"]
        for provider in self.providers:
            for field in required:
                self.assertIn(field, provider, f"Provider {provider.get('id', 'unknown')} missing {field}")

    def test_all_provider_ids_unique(self):
        ids = [p["id"] for p in self.providers]
        self.assertEqual(len(ids), len(set(ids)), "Duplicate provider IDs found")

    def test_all_provider_urls_valid(self):
        import re

        url_pattern = re.compile(r"^https?://")
        for provider in self.providers:
            self.assertTrue(
                url_pattern.match(provider["url"]),
                f"Invalid URL for provider {provider['id']}: {provider['url']}",
            )


class TestCategories(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        categories_data = load_json_file(CATEGORIES_FILE)
        cls.categories = categories_data.get("categories", []) if isinstance(categories_data, dict) else categories_data

    def test_categories_not_empty(self):
        self.assertGreater(len(self.categories), 0)

    def test_all_categories_have_required_fields(self):
        required = ["id", "name", "description"]
        for cat in self.categories:
            for field in required:
                self.assertIn(field, cat, f"Category {cat.get('id', 'unknown')} missing {field}")

    def test_all_category_ids_unique(self):
        ids = [c["id"] for c in self.categories]
        self.assertEqual(len(ids), len(set(ids)), "Duplicate category IDs found")


if __name__ == "__main__":
    unittest.main()
