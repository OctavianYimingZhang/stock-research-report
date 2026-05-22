#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


REQUIRED_REFERENCES = [
    "references/business-model-framework.md",
    "references/valuation-framework.md",
    "references/short-seller-risk-framework.md",
    "references/technical-analysis-framework.md",
    "references/report-style-patterns.md",
    "references/external-inspirations-and-license-notes.md",
]

REQUIRED_SECTIONS = [
    "Company Overview",
    "Business Model Logic",
    "Operations, Customers, And Orders",
    "Financials, Assets, And Debt",
    "Valuation",
    "Short-Seller Risk",
    "Technical Analysis",
    "Risk Factors",
    "Trade Plan",
]

FORBIDDEN_SKILL_PATTERNS = [
    r"Launch ALL FOUR",
    r"Agent 1",
    r"Agent 2",
    r"Agent 3",
    r"Agent 4",
    r"sub-skills required",
    r"Skill tool with skill",
    r"four specialized analysis skills in parallel",
    r"must be installed",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def read(path: str) -> str:
    target = ROOT / path
    if not target.exists():
        fail(f"missing file: {path}")
    return target.read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> dict[str, object]:
    if not text.startswith("---\n"):
        fail("SKILL.md missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        fail("SKILL.md frontmatter is not closed")
    raw = text[4:end]
    try:
        import yaml  # type: ignore

        data = yaml.safe_load(raw)
    except Exception:
        data = {}
        current_key = None
        for line in raw.splitlines():
            if not line.strip():
                continue
            if re.match(r"^[A-Za-z_-]+:", line):
                key, value = line.split(":", 1)
                data[key.strip()] = value.strip()
                current_key = key.strip()
            elif current_key and line.startswith("  "):
                data[current_key] = str(data.get(current_key, "")) + "\n" + line.strip()
    if not isinstance(data, dict):
        fail("SKILL.md frontmatter did not parse to a mapping")
    return data


def validate_skill() -> None:
    skill = read("SKILL.md")
    meta = parse_frontmatter(skill)
    if meta.get("name") != "stock-research-report":
        fail("SKILL.md frontmatter name must be stock-research-report")
    if "Self-contained" not in str(meta.get("description", "")):
        fail("SKILL.md description must identify the self-contained architecture")

    for ref in REQUIRED_REFERENCES:
        if ref not in skill:
            fail(f"SKILL.md does not reference {ref}")
        if not (ROOT / ref).exists():
            fail(f"referenced file does not exist: {ref}")

    for section in REQUIRED_SECTIONS:
        if section not in skill:
            fail(f"SKILL.md missing required report section: {section}")

    for pattern in FORBIDDEN_SKILL_PATTERNS:
        if re.search(pattern, skill, re.IGNORECASE):
            fail(f"SKILL.md still contains old orchestration pattern: {pattern}")

    permissive_average_patterns = [
        r"use\s+(a\s+)?probability-weighted",
        r"allow probability-weighting",
        r"use method averaging",
    ]
    for pattern in permissive_average_patterns:
        if re.search(pattern, skill, re.IGNORECASE):
            fail("SKILL.md appears to allow probability-weighted or averaged valuation targets")


def validate_readme() -> None:
    readme = read("README.md")
    for ref in REQUIRED_REFERENCES:
        if ref not in readme:
            fail(f"README.md does not reference {ref}")
    if "no longer depends at runtime" not in readme:
        fail("README.md must state that old standalone Skill dependencies were removed")


def load_yaml(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    try:
        import yaml  # type: ignore

        data = yaml.safe_load(text)
        if not isinstance(data, dict):
            fail(f"{path} did not parse to a mapping")
        return data
    except ImportError:
        data: dict[str, object] = {}
        for line in text.splitlines():
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            if re.match(r"^[A-Za-z0-9_-]+:", line):
                key, value = line.split(":", 1)
                data[key.strip()] = value.strip()
        return data


def validate_evals() -> None:
    case_dir = ROOT / "evals" / "cases"
    if not case_dir.exists():
        fail("missing evals/cases")
    cases = sorted(case_dir.glob("*.yaml"))
    if len(cases) < 7:
        fail("expected at least 7 eval case YAML files")
    seen_archetypes = set()
    for case in cases:
        data = load_yaml(case)
        for key in ["id", "archetype", "expected_primary_valuation"]:
            if key not in data:
                fail(f"{case} missing required key: {key}")
        seen_archetypes.add(str(data["archetype"]))
        text = case.read_text(encoding="utf-8")
        for section in REQUIRED_SECTIONS:
            if section not in text:
                fail(f"{case} missing required section assertion: {section}")
        for check in [
            "one_primary_valuation_method",
            "short_seller_grade",
        ]:
            if check not in text:
                fail(f"{case} missing required check: {check}")
    expected = {
        "semiconductor_cyclical",
        "early_commercialization_frontier",
        "resource_policy",
        "specialty_semiconductor_growth",
        "semiconductor_equipment_growth",
        "advanced_packaging_asset_intensive",
        "policy_linked_manufacturing",
    }
    missing = expected - seen_archetypes
    if missing:
        fail(f"eval coverage missing archetypes: {sorted(missing)}")


def validate_references() -> None:
    for ref in REQUIRED_REFERENCES:
        text = read(ref)
        if len(text.strip()) < 500:
            fail(f"{ref} is unexpectedly short")
    refs = {p.name for p in (ROOT / "references").glob("*")}
    expected = {Path(p).name for p in REQUIRED_REFERENCES}
    stale = refs - expected
    if stale:
        fail(f"unexpected stale reference files: {sorted(stale)}")


def validate_english_only_repo_text() -> None:
    checked_roots = [
        ROOT / "SKILL.md",
        ROOT / "README.md",
        ROOT / "references",
        ROOT / "evals",
        ROOT / "scripts",
        ROOT / ".github",
    ]
    files: list[Path] = []
    for root in checked_roots:
        if root.is_file():
            files.append(root)
        else:
            files.extend(p for p in root.rglob("*") if p.is_file())
    for path in files:
        text = path.read_text(encoding="utf-8")
        if re.search(r"[\u4e00-\u9fff]", text):
            rel = path.relative_to(ROOT)
            fail(f"{rel} contains non-English CJK text")


def main() -> None:
    validate_skill()
    validate_readme()
    validate_references()
    validate_evals()
    validate_english_only_repo_text()
    print("OK: validation passed")


if __name__ == "__main__":
    main()
