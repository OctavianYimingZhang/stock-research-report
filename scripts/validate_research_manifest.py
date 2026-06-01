#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_TOP_LEVEL = [
    "research_run",
    "article_thesis_maps",
    "thesis_path_replays",
    "alpha_discoveries",
    "technical_mechanism_primers",
    "mispricing_assessments",
    "company_control_point_assessments",
    "opportunity_archetypes",
    "demand_expansion_assessments",
    "scaling_difficulty_assessments",
    "scarcity_bottleneck_assessments",
    "commercialization_path_assessments",
    "operating_machines",
    "demand_proxy_maps",
    "asset_financing_platforms",
    "asset_financing_flywheels",
    "contracted_asset_value_waterfalls",
    "cash_generation_bridges",
    "management_metric_reconciliations",
    "financing_transactions",
    "financing_cadence_ledgers",
    "policy_monetization_maps",
    "source_documents",
    "source_snapshots",
    "source_partitions",
    "evidence_items",
    "claims",
    "conflict_resolutions",
    "data_gaps",
    "earnings_revision_bridges",
    "alpha_case_sets",
    "materiality_evidence_matrices",
    "valuation_cases",
    "equity_bridges",
    "profit_cash_flow_quality_analyses",
    "technical_setups",
    "falsification_patterns",
    "early_warning_dashboards",
    "position_sizing_rationales",
    "expectation_revision_assessments",
    "momentum_regime_assessments",
    "valuation_odds_assessments",
    "risk_filter_assessments",
    "decision_scorecards",
    "trade_plans",
    "catalyst_linked_trade_plans",
    "action_trigger_matrices",
    "short_seller_assessments",
    "report_sections",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def require_dict(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        fail(f"{label} must be an object")
    return value


def require_list(value: Any, label: str) -> list[Any]:
    if not isinstance(value, list):
        fail(f"{label} must be a list")
    return value


def ids(items: list[Any], label: str) -> set[str]:
    result: set[str] = set()
    for item in items:
        obj = require_dict(item, label)
        object_id = obj.get("id")
        if not isinstance(object_id, str) or not object_id:
            fail(f"{label} item missing id")
        if object_id in result:
            fail(f"{label} contains duplicate id: {object_id}")
        result.add(object_id)
    return result


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: validate_research_manifest.py <manifest.json>")
    path = Path(sys.argv[1])
    if not path.exists():
        fail(f"missing manifest file: {path}")
    manifest = json.loads(path.read_text(encoding="utf-8"))
    root = require_dict(manifest, "manifest")

    for key in REQUIRED_TOP_LEVEL:
        if key not in root:
            fail(f"manifest missing top-level key: {key}")

    run = require_dict(root["research_run"], "research_run")
    gate_results = require_list(run.get("gate_results"), "research_run.gate_results")
    allowed_gate_status = {"pass", "warn", "block", "fail", "not_applicable"}
    for result in gate_results:
        obj = require_dict(result, "gate result")
        if obj.get("status") not in allowed_gate_status:
            fail(f"unsupported gate status: {obj.get('status')}")

    source_document_ids = ids(require_list(root["source_documents"], "source_documents"), "source_documents")
    source_snapshot_ids = ids(require_list(root["source_snapshots"], "source_snapshots"), "source_snapshots")
    article_map_ids = ids(require_list(root["article_thesis_maps"], "article_thesis_maps"), "article_thesis_maps")
    thesis_path_ids = ids(require_list(root["thesis_path_replays"], "thesis_path_replays"), "thesis_path_replays")
    alpha_ids = ids(require_list(root["alpha_discoveries"], "alpha_discoveries"), "alpha_discoveries")
    mechanism_ids = ids(require_list(root["technical_mechanism_primers"], "technical_mechanism_primers"), "technical_mechanism_primers")
    mispricing_ids = ids(require_list(root["mispricing_assessments"], "mispricing_assessments"), "mispricing_assessments")
    control_point_ids = ids(require_list(root["company_control_point_assessments"], "company_control_point_assessments"), "company_control_point_assessments")
    opportunity_ids = ids(require_list(root["opportunity_archetypes"], "opportunity_archetypes"), "opportunity_archetypes")
    demand_ids = ids(require_list(root["demand_expansion_assessments"], "demand_expansion_assessments"), "demand_expansion_assessments")
    scaling_ids = ids(require_list(root["scaling_difficulty_assessments"], "scaling_difficulty_assessments"), "scaling_difficulty_assessments")
    scarcity_ids = ids(require_list(root["scarcity_bottleneck_assessments"], "scarcity_bottleneck_assessments"), "scarcity_bottleneck_assessments")
    commercialization_ids = ids(require_list(root["commercialization_path_assessments"], "commercialization_path_assessments"), "commercialization_path_assessments")
    operating_machine_ids = ids(require_list(root["operating_machines"], "operating_machines"), "operating_machines")
    demand_proxy_ids = ids(require_list(root["demand_proxy_maps"], "demand_proxy_maps"), "demand_proxy_maps")
    asset_financing_platform_ids = ids(require_list(root["asset_financing_platforms"], "asset_financing_platforms"), "asset_financing_platforms")
    asset_financing_flywheel_ids = ids(require_list(root["asset_financing_flywheels"], "asset_financing_flywheels"), "asset_financing_flywheels")
    asset_value_waterfall_ids = ids(require_list(root["contracted_asset_value_waterfalls"], "contracted_asset_value_waterfalls"), "contracted_asset_value_waterfalls")
    cash_generation_bridge_ids = ids(require_list(root["cash_generation_bridges"], "cash_generation_bridges"), "cash_generation_bridges")
    management_metric_ids = ids(require_list(root["management_metric_reconciliations"], "management_metric_reconciliations"), "management_metric_reconciliations")
    financing_transaction_ids = ids(require_list(root["financing_transactions"], "financing_transactions"), "financing_transactions")
    financing_cadence_ids = ids(require_list(root["financing_cadence_ledgers"], "financing_cadence_ledgers"), "financing_cadence_ledgers")
    policy_monetization_ids = ids(require_list(root["policy_monetization_maps"], "policy_monetization_maps"), "policy_monetization_maps")
    source_partition_ids = ids(require_list(root["source_partitions"], "source_partitions"), "source_partitions")
    evidence_ids = ids(require_list(root["evidence_items"], "evidence_items"), "evidence_items")
    claim_ids = ids(require_list(root["claims"], "claims"), "claims")
    conflict_resolution_ids = ids(require_list(root["conflict_resolutions"], "conflict_resolutions"), "conflict_resolutions")
    data_gap_ids = ids(require_list(root["data_gaps"], "data_gaps"), "data_gaps")
    revision_bridge_ids = ids(require_list(root["earnings_revision_bridges"], "earnings_revision_bridges"), "earnings_revision_bridges")
    alpha_case_ids = ids(require_list(root["alpha_case_sets"], "alpha_case_sets"), "alpha_case_sets")
    materiality_matrix_ids = ids(require_list(root["materiality_evidence_matrices"], "materiality_evidence_matrices"), "materiality_evidence_matrices")
    valuation_ids = ids(require_list(root["valuation_cases"], "valuation_cases"), "valuation_cases")
    equity_bridge_ids = ids(require_list(root["equity_bridges"], "equity_bridges"), "equity_bridges")
    profit_cash_ids = ids(require_list(root["profit_cash_flow_quality_analyses"], "profit_cash_flow_quality_analyses"), "profit_cash_flow_quality_analyses")
    technical_ids = ids(require_list(root["technical_setups"], "technical_setups"), "technical_setups")
    falsification_ids = ids(require_list(root["falsification_patterns"], "falsification_patterns"), "falsification_patterns")
    early_warning_ids = ids(require_list(root["early_warning_dashboards"], "early_warning_dashboards"), "early_warning_dashboards")
    position_size_ids = ids(require_list(root["position_sizing_rationales"], "position_sizing_rationales"), "position_sizing_rationales")
    expectation_ids = ids(require_list(root["expectation_revision_assessments"], "expectation_revision_assessments"), "expectation_revision_assessments")
    momentum_ids = ids(require_list(root["momentum_regime_assessments"], "momentum_regime_assessments"), "momentum_regime_assessments")
    valuation_odds_ids = ids(require_list(root["valuation_odds_assessments"], "valuation_odds_assessments"), "valuation_odds_assessments")
    risk_filter_ids = ids(require_list(root["risk_filter_assessments"], "risk_filter_assessments"), "risk_filter_assessments")
    decision_scorecard_ids = ids(require_list(root["decision_scorecards"], "decision_scorecards"), "decision_scorecards")
    trade_plan_ids = ids(require_list(root["trade_plans"], "trade_plans"), "trade_plans")
    catalyst_trade_plan_ids = ids(require_list(root["catalyst_linked_trade_plans"], "catalyst_linked_trade_plans"), "catalyst_linked_trade_plans")
    action_trigger_ids = ids(require_list(root["action_trigger_matrices"], "action_trigger_matrices"), "action_trigger_matrices")
    short_ids = ids(require_list(root["short_seller_assessments"], "short_seller_assessments"), "short_seller_assessments")

    for replay in require_list(root["thesis_path_replays"], "thesis_path_replays"):
        obj = require_dict(replay, "thesis path replay")
        if obj.get("article_thesis_map_id") not in article_map_ids:
            fail(f"thesis path replay {obj.get('id')} lacks article thesis map")

    for opportunity in require_list(root["opportunity_archetypes"], "opportunity_archetypes"):
        obj = require_dict(opportunity, "opportunity archetype")
        if obj.get("thesis_path_replay_id") not in thesis_path_ids:
            fail(f"opportunity archetype {obj.get('id')} lacks thesis path replay")
        if not obj.get("archetype"):
            fail(f"opportunity archetype {obj.get('id')} lacks archetype")

    for assessment in require_list(root["mispricing_assessments"], "mispricing_assessments"):
        obj = require_dict(assessment, "mispricing assessment")
        if obj.get("opportunity_archetype_id") not in opportunity_ids:
            fail(f"mispricing assessment {obj.get('id')} lacks opportunity archetype")
        if not obj.get("correct_denominator"):
            fail(f"mispricing assessment {obj.get('id')} lacks correct denominator")

    for assessment in require_list(root["company_control_point_assessments"], "company_control_point_assessments"):
        obj = require_dict(assessment, "company control point assessment")
        if obj.get("opportunity_archetype_id") not in opportunity_ids:
            fail(f"company control point {obj.get('id')} lacks opportunity archetype")
        if not obj.get("control_point_or_gap"):
            fail(f"company control point {obj.get('id')} lacks control point or gap")

    for discovery in require_list(root["alpha_discoveries"], "alpha_discoveries"):
        obj = require_dict(discovery, "alpha discovery")
        if obj.get("mispricing_assessment_id") not in mispricing_ids:
            fail(f"alpha discovery {obj.get('id')} lacks mispricing assessment")
        if obj.get("company_control_point_assessment_id") not in control_point_ids:
            fail(f"alpha discovery {obj.get('id')} lacks company control point assessment")
        if not obj.get("thesis_spine"):
            fail(f"alpha discovery {obj.get('id')} lacks thesis spine")
        if not obj.get("broken_thesis_signal"):
            fail(f"alpha discovery {obj.get('id')} lacks broken thesis signal")

    for primer in require_list(root["technical_mechanism_primers"], "technical_mechanism_primers"):
        obj = require_dict(primer, "technical mechanism primer")
        if obj.get("company_control_point_assessment_id") not in control_point_ids:
            fail(f"technical mechanism primer {obj.get('id')} lacks company control point assessment")
        if not obj.get("customer_pain_or_gap"):
            fail(f"technical mechanism primer {obj.get('id')} lacks customer pain or gap")

    for assessment_key, assessment_ids, label in [
        ("demand_expansion_assessments", demand_ids, "demand expansion assessment"),
        ("scaling_difficulty_assessments", scaling_ids, "scaling difficulty assessment"),
        ("scarcity_bottleneck_assessments", scarcity_ids, "scarcity bottleneck assessment"),
        ("commercialization_path_assessments", commercialization_ids, "commercialization path assessment"),
    ]:
        for assessment in require_list(root[assessment_key], assessment_key):
            obj = require_dict(assessment, label)
            if obj.get("opportunity_archetype_id") not in opportunity_ids:
                fail(f"{label} {obj.get('id')} lacks opportunity archetype")

    for machine in require_list(root["operating_machines"], "operating_machines"):
        obj = require_dict(machine, "operating machine")
        if obj.get("company_control_point_assessment_id") not in control_point_ids:
            fail(f"operating machine {obj.get('id')} lacks company control point assessment")
        if not obj.get("failure_signal_or_gap"):
            fail(f"operating machine {obj.get('id')} lacks failure signal or gap")

    for demand_proxy in require_list(root["demand_proxy_maps"], "demand_proxy_maps"):
        obj = require_dict(demand_proxy, "demand proxy map")
        if obj.get("commercialization_path_assessment_id") not in commercialization_ids:
            fail(f"demand proxy map {obj.get('id')} lacks commercialization path assessment")
        if not obj.get("valuation_usability"):
            fail(f"demand proxy map {obj.get('id')} lacks valuation usability")

    for platform in require_list(root["asset_financing_platforms"], "asset_financing_platforms"):
        obj = require_dict(platform, "asset financing platform")
        if obj.get("company_control_point_assessment_id") not in control_point_ids:
            fail(f"asset financing platform {obj.get('id')} lacks company control point assessment")
        if not obj.get("monetization_channels"):
            fail(f"asset financing platform {obj.get('id')} lacks monetization channels")

    for flywheel in require_list(root["asset_financing_flywheels"], "asset_financing_flywheels"):
        obj = require_dict(flywheel, "asset financing flywheel")
        if obj.get("asset_financing_platform_id") not in asset_financing_platform_ids:
            fail(f"asset financing flywheel {obj.get('id')} lacks platform")
        if not obj.get("equity_value_creation"):
            fail(f"asset financing flywheel {obj.get('id')} lacks equity value creation")

    for waterfall in require_list(root["contracted_asset_value_waterfalls"], "contracted_asset_value_waterfalls"):
        obj = require_dict(waterfall, "contracted asset value waterfall")
        if obj.get("asset_financing_platform_id") not in asset_financing_platform_ids:
            fail(f"contracted asset value waterfall {obj.get('id')} lacks platform")
        if obj.get("per_share_value_or_blocker") in (None, ""):
            fail(f"contracted asset value waterfall {obj.get('id')} lacks per-share value or blocker")

    for bridge in require_list(root["cash_generation_bridges"], "cash_generation_bridges"):
        obj = require_dict(bridge, "cash generation bridge")
        if obj.get("asset_financing_platform_id") not in asset_financing_platform_ids:
            fail(f"cash generation bridge {obj.get('id')} lacks platform")
        if not obj.get("recurring_or_timing_dependent"):
            fail(f"cash generation bridge {obj.get('id')} lacks recurring/timing classification")

    for reconciliation in require_list(root["management_metric_reconciliations"], "management_metric_reconciliations"):
        obj = require_dict(reconciliation, "management metric reconciliation")
        if not obj.get("metric_name"):
            fail(f"management metric reconciliation {obj.get('id')} lacks metric name")
        if not obj.get("valuation_use"):
            fail(f"management metric reconciliation {obj.get('id')} lacks valuation use")

    for transaction in require_list(root["financing_transactions"], "financing_transactions"):
        obj = require_dict(transaction, "financing transaction")
        if not obj.get("type") or not obj.get("recourse_status"):
            fail(f"financing transaction {obj.get('id')} lacks type or recourse status")

    for ledger in require_list(root["financing_cadence_ledgers"], "financing_cadence_ledgers"):
        obj = require_dict(ledger, "financing cadence ledger")
        linked_transactions = set(obj.get("financing_transaction_ids") or [])
        if linked_transactions - financing_transaction_ids:
            fail(f"financing cadence ledger {obj.get('id')} references unknown transaction")
        if not obj.get("upcoming_proof_events"):
            fail(f"financing cadence ledger {obj.get('id')} lacks upcoming proof events")

    for policy_map in require_list(root["policy_monetization_maps"], "policy_monetization_maps"):
        obj = require_dict(policy_map, "policy monetization map")
        if not obj.get("policy_name") or not obj.get("monetization_channel"):
            fail(f"policy monetization map {obj.get('id')} lacks policy name or channel")
        if not obj.get("valuation_use"):
            fail(f"policy monetization map {obj.get('id')} lacks valuation use")

    for snapshot in require_list(root["source_snapshots"], "source_snapshots"):
        obj = require_dict(snapshot, "source snapshot")
        if obj.get("source_document_id") not in source_document_ids:
            fail(f"source snapshot {obj.get('id')} lacks source document lineage")

    for partition in require_list(root["source_partitions"], "source_partitions"):
        obj = require_dict(partition, "source partition")
        if obj.get("source_snapshot_id") not in source_snapshot_ids:
            fail(f"source partition {obj.get('id')} lacks valid source_snapshot_id")

    for evidence in require_list(root["evidence_items"], "evidence_items"):
        obj = require_dict(evidence, "evidence item")
        if obj.get("source_snapshot_id") not in source_snapshot_ids:
            fail(f"evidence item {obj.get('id')} lacks source snapshot lineage")
        if obj.get("source_partition_id") not in source_partition_ids:
            fail(f"evidence item {obj.get('id')} lacks source partition lineage")

    for claim in require_list(root["claims"], "claims"):
        obj = require_dict(claim, "claim")
        linked_evidence = set(obj.get("evidence_ids") or [])
        linked_gaps = set(obj.get("data_gap_ids") or [])
        linked_conflict_resolution = obj.get("conflict_resolution_id")
        if obj.get("materiality") == "high" and not linked_evidence and not linked_gaps:
            fail(f"high-materiality claim {obj.get('id')} lacks evidence or data gap")
        if linked_evidence - evidence_ids:
            fail(f"claim {obj.get('id')} references unknown evidence")
        if linked_gaps - data_gap_ids:
            fail(f"claim {obj.get('id')} references unknown data gap")
        if linked_conflict_resolution and linked_conflict_resolution not in conflict_resolution_ids:
            fail(f"claim {obj.get('id')} references unknown conflict resolution")

    for matrix in require_list(root["materiality_evidence_matrices"], "materiality_evidence_matrices"):
        obj = require_dict(matrix, "materiality evidence matrix")
        linked_claims = set(obj.get("claim_ids") or [])
        if linked_claims - claim_ids:
            fail(f"materiality evidence matrix {obj.get('id')} references unknown claim")
        if not obj.get("low_evidence_high_materiality_items"):
            fail(f"materiality evidence matrix {obj.get('id')} lacks low-evidence high-materiality items")

    for bridge in require_list(root["equity_bridges"], "equity_bridges"):
        obj = require_dict(bridge, "equity bridge")
        if obj.get("valuation_case_id") not in valuation_ids:
            fail(f"equity bridge {obj.get('id')} references unknown valuation case")
        blocker = obj.get("blocker_reason_or_gap")
        target = obj.get("target_price_or_blocker")
        if blocker in (None, "", "none") and target in (None, "", "blocked"):
            fail(f"equity bridge {obj.get('id')} lacks target or blocker")

    for valuation in require_list(root["valuation_cases"], "valuation_cases"):
        obj = require_dict(valuation, "valuation case")
        if obj.get("equity_bridge_id") not in equity_bridge_ids:
            fail(f"valuation case {obj.get('id')} lacks equity bridge")

    for bridge in require_list(root["earnings_revision_bridges"], "earnings_revision_bridges"):
        obj = require_dict(bridge, "earnings revision bridge")
        if obj.get("alpha_discovery_id") not in alpha_ids:
            fail(f"earnings revision bridge {obj.get('id')} lacks alpha discovery")
        if obj.get("valuation_case_id") not in valuation_ids:
            fail(f"earnings revision bridge {obj.get('id')} lacks valuation case")
        if not obj.get("disconfirming_signal"):
            fail(f"earnings revision bridge {obj.get('id')} lacks disconfirming signal")

    for case_set in require_list(root["alpha_case_sets"], "alpha_case_sets"):
        obj = require_dict(case_set, "alpha case set")
        if obj.get("valuation_case_id") not in valuation_ids:
            fail(f"alpha case set {obj.get('id')} lacks valuation case")
        if obj.get("earnings_revision_bridge_id") not in revision_bridge_ids:
            fail(f"alpha case set {obj.get('id')} lacks earnings revision bridge")
        case_names = set(obj.get("cases") or [])
        required_cases = {"current_market_implied", "base_proof", "alpha", "broken"}
        if not required_cases.issubset(case_names):
            fail(f"alpha case set {obj.get('id')} lacks current/base/alpha/broken cases")

    for analysis in require_list(root["profit_cash_flow_quality_analyses"], "profit_cash_flow_quality_analyses"):
        obj = require_dict(analysis, "profit cash-flow quality analysis")
        if not obj.get("valuation_effect") or not obj.get("short_risk_effect"):
            fail(f"profit cash-flow analysis {obj.get('id')} lacks valuation or short-risk effect")

    for scorecard in require_list(root["decision_scorecards"], "decision_scorecards"):
        obj = require_dict(scorecard, "decision scorecard")
        if obj.get("expectation_revision_assessment_id") not in expectation_ids:
            fail(f"decision scorecard {obj.get('id')} lacks expectation revision assessment")
        if obj.get("momentum_regime_assessment_id") not in momentum_ids:
            fail(f"decision scorecard {obj.get('id')} lacks momentum regime assessment")
        if obj.get("valuation_odds_assessment_id") not in valuation_odds_ids:
            fail(f"decision scorecard {obj.get('id')} lacks valuation odds assessment")
        if obj.get("risk_filter_assessment_id") not in risk_filter_ids:
            fail(f"decision scorecard {obj.get('id')} lacks risk filter assessment")
        if obj.get("profit_cash_flow_quality_analysis_id") not in profit_cash_ids:
            fail(f"decision scorecard {obj.get('id')} lacks profit cash-flow quality analysis")
        if not obj.get("action_grade") or not obj.get("binding_cap_reason"):
            fail(f"decision scorecard {obj.get('id')} lacks action grade or binding cap reason")

    for setup in require_list(root["technical_setups"], "technical_setups"):
        obj = require_dict(setup, "technical setup")
        if obj.get("freshness_status") == "stale" and obj.get("drives_trade_plan") is True:
            fail(f"stale technical setup {obj.get('id')} drives trade plan")

    for dashboard in require_list(root["early_warning_dashboards"], "early_warning_dashboards"):
        obj = require_dict(dashboard, "early warning dashboard")
        if obj.get("falsification_pattern_id") not in falsification_ids:
            fail(f"early warning dashboard {obj.get('id')} lacks falsification pattern")
        if not obj.get("monitoring_variables"):
            fail(f"early warning dashboard {obj.get('id')} lacks monitoring variables")

    for plan in require_list(root["trade_plans"], "trade_plans"):
        obj = require_dict(plan, "trade plan")
        if obj.get("valuation_case_id") not in valuation_ids:
            fail(f"trade plan {obj.get('id')} references unknown valuation case")
        if obj.get("technical_setup_id") not in technical_ids:
            fail(f"trade plan {obj.get('id')} references unknown technical setup")
        if obj.get("short_seller_assessment_id") not in short_ids:
            fail(f"trade plan {obj.get('id')} references unknown short assessment")
        if obj.get("decision_scorecard_id") not in decision_scorecard_ids:
            fail(f"trade plan {obj.get('id')} references unknown decision scorecard")
        if obj.get("falsification_pattern_id") not in falsification_ids:
            fail(f"trade plan {obj.get('id')} references unknown falsification pattern")
        if obj.get("position_sizing_rationale_id") not in position_size_ids:
            fail(f"trade plan {obj.get('id')} references unknown position sizing rationale")

    for plan in require_list(root["catalyst_linked_trade_plans"], "catalyst_linked_trade_plans"):
        obj = require_dict(plan, "catalyst-linked trade plan")
        if obj.get("trade_plan_id") not in trade_plan_ids:
            fail(f"catalyst-linked trade plan {obj.get('id')} lacks trade plan")
        if obj.get("technical_setup_id") not in technical_ids:
            fail(f"catalyst-linked trade plan {obj.get('id')} lacks technical setup")
        if obj.get("early_warning_dashboard_id") not in early_warning_ids:
            fail(f"catalyst-linked trade plan {obj.get('id')} lacks early warning dashboard")
        if not obj.get("catalyst_or_proof_event"):
            fail(f"catalyst-linked trade plan {obj.get('id')} lacks catalyst or proof event")

    for matrix in require_list(root["action_trigger_matrices"], "action_trigger_matrices"):
        obj = require_dict(matrix, "action trigger matrix")
        if obj.get("trade_plan_id") not in trade_plan_ids:
            fail(f"action trigger matrix {obj.get('id')} lacks trade plan")
        for key in ["trigger_variables", "wait_conditions", "add_conditions", "trim_conditions", "stop_or_downgrade_conditions"]:
            if not obj.get(key):
                fail(f"action trigger matrix {obj.get('id')} lacks {key}")

    for assessment in require_list(root["short_seller_assessments"], "short_seller_assessments"):
        obj = require_dict(assessment, "short-seller assessment")
        if obj.get("grade") in {"C", "D", "F"} and not obj.get("valuation_or_size_effect"):
            fail(f"short-seller grade {obj.get('grade')} lacks valuation or size effect")

    for section in require_list(root["report_sections"], "report_sections"):
        obj = require_dict(section, "report section")
        cited_claims = set(obj.get("claim_ids") or [])
        if cited_claims - claim_ids:
            fail(f"report section {obj.get('section_name')} references unknown claim")

    print("OK: research manifest validation passed")


if __name__ == "__main__":
    main()
