#!/usr/bin/env python3
"""
FreeCerts Data Validator

Validates certifications.json against the JSON schema and performs
additional data quality checks.
"""

import json
import os
import sys
import re
from datetime import datetime
from typing import List, Dict, Any

try:
    import jsonschema
except ImportError:
    print("ERROR: jsonschema is not installed. Install with: pip install jsonschema")
    sys.exit(1)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
SCHEMA_DIR = os.path.join(BASE_DIR, "schema")

REQUIRED_FILES = {
    "certifications": os.path.join(DATA_DIR, "certifications.json"),
    "providers": os.path.join(DATA_DIR, "providers.json"),
    "categories": os.path.join(DATA_DIR, "categories.json"),
    "schema": os.path.join(SCHEMA_DIR, "certification.schema.json"),
}

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
VALID_COST_VALUES = ["free", "paid", "freemium", "none"]
VALID_EXAM_COST_VALUES = ["free", "paid", "none", "freemium"]
VALID_ASSESSMENT_TYPES = ["exam", "project", "quiz", "none", "peer_review"]
VALID_DELIVERY_TYPES = ["online", "in-person", "hybrid"]
VALID_CERTIFICATE_FORMATS = ["digital", "print", "both"]
VALID_AVAILABILITY = ["global", "regional", "country_specific"]
VALID_EXPIRATION = ["none", "review_required", "exam_retake"]
VALID_VERIFICATION_STATUS = ["verified", "unverified", "needs_review"]


class ValidationResult:
    def __init__(self):
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.info: List[str] = []

    def add_error(self, message: str):
        self.errors.append(f"ERROR: {message}")

    def add_warning(self, message: str):
        self.warnings.append(f"WARNING: {message}")

    def add_info(self, message: str):
        self.info.append(f"INFO: {message}")

    def is_valid(self) -> bool:
        return len(self.errors) == 0

    def print_report(self):
        for msg in self.info:
            print(msg)
        for msg in self.warnings:
            print(msg)
        for msg in self.errors:
            print(msg)
        if self.is_valid():
            print("\n[OK] Validation passed")
        else:
            print(f"\n[FAIL] Validation failed with {len(self.errors)} error(s)")


def load_json_file(path: str) -> Any:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Required file not found: {path}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in {path}: {e}")


def validate_schema(data: List[Dict], schema: Dict, result: ValidationResult):
    errors = []
    for i, entry in enumerate(data):
        try:
            jsonschema.validate(instance=entry, schema=schema)
        except jsonschema.ValidationError as e:
            errors.append(f"Entry {i} ({entry.get('id', 'unknown')}): {e.message}")
    if errors:
        result.add_error(f"Schema validation failed for {len(errors)} entries:")
        for err in errors[:10]:
            result.add_error(f"  {err}")
    else:
        result.add_info("[OK] JSON Schema validation passed for all entries")


def validate_categories(certifications: List[Dict], result: ValidationResult):
    categories = {c["category"] for c in certifications}
    invalid = categories - set(VALID_CATEGORIES)
    if invalid:
        result.add_error(f"Invalid categories found: {invalid}")
    else:
        result.add_info("[OK] All categories are valid")


def validate_credential_types(certifications: List[Dict], result: ValidationResult):
    types = {c["credential_type"] for c in certifications}
    invalid = types - set(VALID_CREDENTIAL_TYPES)
    if invalid:
        result.add_error(f"Invalid credential types found: {invalid}")
    else:
        result.add_info("[OK] All credential types are valid")


def validate_difficulties(certifications: List[Dict], result: ValidationResult):
    difficulties = {c["difficulty"] for c in certifications}
    invalid = difficulties - set(VALID_DIFFICULTIES)
    if invalid:
        result.add_error(f"Invalid difficulty values found: {invalid}")
    else:
        result.add_info("[OK] All difficulty values are valid")


def validate_dates(certifications: List[Dict], result: ValidationResult):
    date_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")
    invalid_dates = []
    for cert in certifications:
        date = cert.get("last_verified")
        if date and not date_pattern.match(date):
            invalid_dates.append(f"{cert['id']}: {date}")
    if invalid_dates:
        result.add_error(f"Invalid date formats: {invalid_dates}")
    else:
        result.add_info("[OK] All dates are in valid YYYY-MM-DD format")


def validate_urls(certifications: List[Dict], result: ValidationResult):
    url_pattern = re.compile(r"^https?://")
    invalid_urls = []
    for cert in certifications:
        for field in ["provider_url", "certification_url"]:
            url = cert.get(field)
            if url and not url_pattern.match(url):
                invalid_urls.append(f"{cert['id']}: {field} = {url}")
    if invalid_urls:
        result.add_error(f"Invalid URLs found: {invalid_urls}")
    else:
        result.add_info("[OK] All URLs are valid")


def validate_unique_ids(certifications: List[Dict], result: ValidationResult):
    ids = [c["id"] for c in certifications]
    duplicates = [id for id in ids if ids.count(id) > 1]
    if duplicates:
        result.add_error(f"Duplicate IDs found: {set(duplicates)}")
    else:
        result.add_info(f"[OK] All {len(ids)} IDs are unique")


def validate_unique_urls(certifications: List[Dict], result: ValidationResult):
    urls = [c["certification_url"] for c in certifications]
    duplicates = [url for url in urls if urls.count(url) > 1]
    if duplicates:
        result.add_warning(f"Duplicate certification URLs found: {set(duplicates)}")
    else:
        result.add_info("[OK] All certification URLs are unique")


def validate_costs(certifications: List[Dict], result: ValidationResult):
    inconsistent = []
    for cert in certifications:
        if cert.get("learning_cost") == "free":
            if cert.get("certificate_cost") not in ["free", "none"]:
                inconsistent.append(
                    f"{cert['id']}: learning_cost is free but certificate_cost is {cert.get('certificate_cost')}"
                )
    if inconsistent:
        result.add_warning(f"Potentially inconsistent cost entries: {inconsistent}")
    else:
        result.add_info("[OK] Cost classifications appear consistent")


def validate_required_fields(certifications: List[Dict], result: ValidationResult):
    required = [
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
    missing = []
    for cert in certifications:
        for field in required:
            if field not in cert or cert[field] is None or cert[field] == "":
                missing.append(f"{cert.get('id', 'unknown')}: missing {field}")
    if missing:
        result.add_error(f"Missing required fields: {missing}")
    else:
        result.add_info("✓ All required fields are present")


def validate_providers(certifications: List[Dict], providers: List[Dict], result: ValidationResult):
    provider_names = {p["name"] for p in providers}
    unknown = set()
    for cert in certifications:
        if cert.get("provider") not in provider_names:
            unknown.add(cert.get("provider"))
    if unknown:
        result.add_warning(f"Providers not in providers.json: {unknown}")
    else:
        result.add_info("[OK] All providers are defined in providers.json")


def validate_evidence_fields(certifications: List[Dict], result: ValidationResult):
    unverified_without_evidence = []
    for cert in certifications:
        if cert.get("verification_status") == "verified" and not cert.get("last_verified"):
            unverified_without_evidence.append(cert["id"])
    if unverified_without_evidence:
        result.add_warning(
            f"Verified entries without last_verified date: {unverified_without_evidence}"
        )
    else:
        result.add_info("[OK] Evidence fields look good")


def main():
    result = ValidationResult()
    print("FreeCerts Data Validator")
    print("=" * 50)
    print()

    try:
        schema_data = load_json_file(REQUIRED_FILES["schema"])
        certifications_data = load_json_file(REQUIRED_FILES["certifications"])
        providers_data = load_json_file(REQUIRED_FILES["providers"])
        categories_data = load_json_file(REQUIRED_FILES["categories"])
    except Exception as e:
        result.add_error(str(e))
        result.print_report()
        sys.exit(1)

    # Extract data from wrapper objects
    certifications = certifications_data.get("certifications", []) if isinstance(certifications_data, dict) else certifications_data
    providers = providers_data.get("providers", []) if isinstance(providers_data, dict) else providers_data
    categories = categories_data.get("categories", []) if isinstance(categories_data, dict) else categories_data

    result.add_info(f"Loaded {len(certifications)} certifications")
    result.add_info(f"Loaded {len(providers)} providers")
    result.add_info(f"Loaded {len(categories)} categories")
    print()

    validate_schema(certifications, schema_data, result)
    validate_unique_ids(certifications, result)
    validate_required_fields(certifications, result)
    validate_categories(certifications, result)
    validate_credential_types(certifications, result)
    validate_difficulties(certifications, result)
    validate_dates(certifications, result)
    validate_urls(certifications, result)
    validate_unique_urls(certifications, result)
    validate_costs(certifications, result)
    validate_providers(certifications, providers, result)
    validate_evidence_fields(certifications, result)

    print()
    result.print_report()

    if not result.is_valid():
        sys.exit(1)


if __name__ == "__main__":
    main()
