#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml  # type: ignore
except ImportError as exc:  # pragma: no cover - exercised by environment
    print(f"ERROR: PyYAML is required to validate contracts: {exc}", file=sys.stderr)
    sys.exit(1)


ROOT = Path(__file__).resolve().parents[1]
REPORT_SECTIONS_PATH = ROOT / "contracts" / "report_sections.yaml"
GATES_PATH = ROOT / "contracts" / "gates.yaml"
SETTINGS_SCHEMA_PATH = ROOT / "config" / "settings.schema.json"
ONBOARDING_PATH = ROOT / "config" / "onboarding.flow.yaml"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        fail(f"missing contract file: {path.relative_to(ROOT)}")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        fail(f"{path.relative_to(ROOT)} must contain a mapping")
    return data


def load_full_report_sections() -> list[str]:
    contract = load_yaml(REPORT_SECTIONS_PATH)
    views = contract.get("views")
    if not isinstance(views, dict):
        fail("report section contract missing views")
    full_report = views.get("full_report")
    if not isinstance(full_report, dict):
        fail("report section contract missing full_report view")
    sections = full_report.get("required_sections")
    if not isinstance(sections, list) or not all(isinstance(item, str) for item in sections):
        fail("full_report.required_sections must be a string list")
    return sections


def check_sections_in_docs(sections: list[str]) -> None:
    skill = read("SKILL.md")
    style = read("references/report-style-patterns.md")
    for section in sections:
        if section not in skill:
            fail(f"SKILL.md missing canonical section: {section}")
        if section not in style:
            fail(f"report-style-patterns.md missing canonical section: {section}")


def check_validator_uses_contract() -> None:
    validator = read("scripts/validate_report_output.py")
    if "contracts/report_sections.yaml" not in validator and "REPORT_SECTIONS_PATH" not in validator:
        fail("validate_report_output.py must read contracts/report_sections.yaml")


def check_no_obsolete_report_contracts() -> None:
    obsolete_patterns = [
        r"fixed nine-section report",
        r"default nine-section",
        r"ten-section",
        r"10-section",
    ]
    checked_files = [
        "SKILL.md",
        "README.md",
        "references/report-style-patterns.md",
        "references/scorecard-decision-framework.md",
        "references/technical-analysis-framework.md",
        "references/user-intake-settings-framework.md",
    ]
    for rel in checked_files:
        text = read(rel)
        for pattern in obsolete_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                fail(f"{rel} contains obsolete report-contract wording: {pattern}")
    technical = read("references/technical-analysis-framework.md")
    if "## Technical Analysis\n\n[One compact paragraph.]" in technical:
        fail("technical-analysis-framework.md still uses the obsolete final heading")


def check_onboarding_required_inputs() -> None:
    schema = json.loads(SETTINGS_SCHEMA_PATH.read_text(encoding="utf-8"))
    properties = schema.get("properties")
    if not isinstance(properties, dict):
        fail("settings schema missing properties")
    allowed_inputs = set(properties) | {"ticker_or_company_identifier"}
    data = load_yaml(ONBOARDING_PATH)
    required_inputs = data.get("required_inputs")
    if not isinstance(required_inputs, list):
        fail("onboarding flow missing required_inputs list")
    unsupported = sorted(str(item) for item in required_inputs if item not in allowed_inputs)
    if unsupported:
        fail(f"onboarding required_inputs are not schema-backed: {unsupported}")


def check_eval_cases_use_canonical_sections(sections: list[str]) -> None:
    case_dir = ROOT / "evals" / "cases"
    if not case_dir.exists():
        fail("missing evals/cases")
    canonical = set(sections)
    old_section_names = {"Company Overview", "Technical Analysis", "Trade Plan"}
    for path in sorted(case_dir.glob("*.yaml")):
        if path.name == "index.yaml":
            continue
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            fail(f"{path.relative_to(ROOT)} must contain a mapping")
        required_sections = data.get("required_sections")
        if not isinstance(required_sections, list):
            fail(f"{path.relative_to(ROOT)} missing required_sections")
        stale = sorted(str(item) for item in required_sections if item in old_section_names)
        if stale:
            fail(f"{path.relative_to(ROOT)} contains old section names: {stale}")
        unknown = sorted(str(item) for item in required_sections if item not in canonical)
        if unknown:
            fail(f"{path.relative_to(ROOT)} contains non-canonical sections: {unknown}")
        if path.stem[:2] in {"27", "28", "29", "30", "31"}:
            for field in ("must_include", "must_block"):
                values = data.get(field)
                if not isinstance(values, list) or not values or not all(isinstance(item, str) for item in values):
                    fail(f"{path.relative_to(ROOT)} missing {field} expected behavior list")


def main() -> None:
    if not GATES_PATH.exists():
        fail("missing contract file: contracts/gates.yaml")
    sections = load_full_report_sections()
    check_sections_in_docs(sections)
    check_validator_uses_contract()
    check_no_obsolete_report_contracts()
    check_onboarding_required_inputs()
    check_eval_cases_use_canonical_sections(sections)
    print("OK: contract validation passed")


if __name__ == "__main__":
    main()
