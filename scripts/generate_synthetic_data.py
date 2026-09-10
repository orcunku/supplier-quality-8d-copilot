from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


INCIDENT_FAMILIES = [
    {
        "code": "CRIMP_RESISTANCE",
        "title": "Elevated Contact Resistance After HV Terminal Crimping",
        "process": "Crimping",
        "product": "HV Battery Cable 95mm2",
        "symptom": "Electrical contact resistance increased from normal 0.18 mOhm to values between 0.38 and 0.46 mOhm.",
        "root_cause": "Progressive wear of the upper crimping die increased crimp height and reduced conductor compression.",
        "action": "Replace crimp dies and reduce preventive maintenance interval from 50,000 to 30,000 cycles.",
        "checks": "crimp height, die wear, tool cycle count, conductor compression, electrical resistance",
    },
    {
        "code": "LOW_PULL_FORCE",
        "title": "Low Pull Force After Terminal Crimping",
        "process": "Crimping",
        "product": "HV Cable 95mm2",
        "symptom": "Cable pull force decreased below the 2.8 kN requirement.",
        "root_cause": "Incorrect crimp height setting was introduced after an applicator change.",
        "action": "Lock setup parameters and require first-off crimp height verification after tooling changes.",
        "checks": "crimp height, applicator setup, pull force, operator setup approval",
    },
    {
        "code": "WATER_INGRESS",
        "title": "Connector Water Ingress After Thermal Cycling",
        "process": "Assembly",
        "product": "HV Connector Assembly",
        "symptom": "Connector failed IP67 leakage verification after thermal cycling.",
        "root_cause": "Seal damage occurred during manual insertion because insertion depth was not controlled.",
        "action": "Introduce insertion fixture and 100 percent visual seal-position verification.",
        "checks": "seal position, seal damage, insertion depth, housing condition, leak test",
    },
    {
        "code": "ULTRASONIC_WELD",
        "title": "High Resistance at Ultrasonic Weld Joint",
        "process": "Ultrasonic Welding",
        "product": "Copper Busbar Assembly",
        "symptom": "Weld resistance increased and weld energy trend shifted upward.",
        "root_cause": "Sonotrode surface wear reduced energy transfer into the copper joint.",
        "action": "Replace sonotrode and introduce tool-condition checks based on weld count.",
        "checks": "sonotrode condition, weld energy, weld force, surface contamination, weld count",
    },
    {
        "code": "TERMINAL_PUSHOUT",
        "title": "Terminal Push-Out During Connector Mating",
        "process": "Assembly",
        "product": "HV Connector",
        "symptom": "Terminal moved backwards from the connector cavity during customer mating.",
        "root_cause": "Secondary locking feature was not completely engaged during assembly.",
        "action": "Add automated lock-presence verification and update operator work instruction.",
        "checks": "terminal seating, secondary lock, insertion force, operator method",
    },
    {
        "code": "STRIP_LENGTH",
        "title": "Incorrect Conductor Strip Length",
        "process": "Wire Preparation",
        "product": "HV Cable",
        "symptom": "Copper conductor exposure exceeded dimensional requirement.",
        "root_cause": "Cut-and-strip machine recipe contained an outdated strip-length value.",
        "action": "Update recipe control and introduce barcode-based program selection.",
        "checks": "strip length, machine recipe, blade condition, program selection",
    },
    {
        "code": "STRAND_DAMAGE",
        "title": "Copper Strand Damage During Stripping",
        "process": "Wire Preparation",
        "product": "HV Cable",
        "symptom": "Broken copper strands were detected before terminal crimping.",
        "root_cause": "Stripping blade penetration was too deep following blade replacement.",
        "action": "Add blade-position verification and first-piece microscopic inspection.",
        "checks": "blade penetration, strand damage, blade replacement, conductor diameter",
    },
    {
        "code": "PLATING",
        "title": "Terminal Plating Oxidation",
        "process": "Incoming Material",
        "product": "Copper HV Terminal",
        "symptom": "Terminal contact surfaces showed discoloration and elevated contact resistance.",
        "root_cause": "Packaging allowed moisture exposure during supplier transportation.",
        "action": "Improve moisture barrier packaging and tighten incoming inspection.",
        "checks": "plating thickness, oxidation, packaging, supplier lot, contact surface",
    },
    {
        "code": "OVERMOLD_VOID",
        "title": "Void Detected in Cable Overmolding",
        "process": "Overmolding",
        "product": "HV Cable Assembly",
        "symptom": "Internal voids were found around the cable seal interface.",
        "root_cause": "Mold vent contamination prevented complete air evacuation.",
        "action": "Increase mold vent cleaning frequency and monitor injection pressure.",
        "checks": "mold vent, injection pressure, material drying, mold temperature",
    },
    {
        "code": "INSULATION_DAMAGE",
        "title": "Cable Insulation Damage",
        "process": "Assembly",
        "product": "HV Cable Assembly",
        "symptom": "Outer cable insulation showed cuts during final inspection.",
        "root_cause": "Sharp edge on assembly fixture contacted cable insulation.",
        "action": "Rework fixture edge and introduce fixture-condition inspection.",
        "checks": "fixture condition, insulation damage, cable routing, handling",
    },
    {
        "code": "WRONG_COMPONENT",
        "title": "Incorrect Terminal Variant Installed",
        "process": "Assembly",
        "product": "HV Harness",
        "symptom": "Wrong terminal variant was identified during final inspection.",
        "root_cause": "Similar component containers were stored next to each other without scan verification.",
        "action": "Introduce barcode verification and physical material separation.",
        "checks": "part number, barcode verification, material location, picking method",
    },
    {
        "code": "BUS_BAR_DIMENSION",
        "title": "Busbar Dimensional Nonconformance",
        "process": "Forming",
        "product": "Copper Busbar",
        "symptom": "Hole position exceeded drawing tolerance.",
        "root_cause": "Progressive forming tool alignment drifted after extended production.",
        "action": "Realign tool and introduce periodic dimensional capability checks.",
        "checks": "tool alignment, hole position, dimensional inspection, tool wear",
    },
    {
        "code": "EOL_FALSE_FAIL",
        "title": "False Electrical End-of-Line Failure",
        "process": "Electrical Test",
        "product": "HV Cable Assembly",
        "symptom": "Good assemblies intermittently failed resistance testing.",
        "root_cause": "Worn measurement fixture contacts added unstable resistance.",
        "action": "Replace fixture contacts and establish fixture resistance verification.",
        "checks": "fixture contacts, micro-ohmmeter calibration, reference part, test leads",
    },
    {
        "code": "CPA",
        "title": "Connector CPA Not Fully Engaged",
        "process": "Assembly",
        "product": "HV Connector",
        "symptom": "Connector position assurance feature remained partially open.",
        "root_cause": "Assembly force was insufficient because fixture travel was incorrectly adjusted.",
        "action": "Correct fixture travel and add CPA vision inspection.",
        "checks": "CPA position, fixture travel, assembly force, visual inspection",
    },
    {
        "code": "OVERMOLD_LEAK",
        "title": "Leakage at Overmold Interface",
        "process": "Overmolding",
        "product": "HV Cable Assembly",
        "symptom": "Leak test detected pressure decay at cable-to-overmold interface.",
        "root_cause": "Cable surface contamination reduced adhesion to overmold material.",
        "action": "Introduce controlled surface cleaning and cleanliness verification.",
        "checks": "surface contamination, cleaning method, adhesion, leak test",
    },
]


def ensure_directories():
    folders = [
        "8d",
        "ncr",
        "ppap",
        "pfmea",
        "control_plans",
        "complaints",
        "deviations",
        "work_instructions",
    ]

    for folder in folders:
        path = DATA_DIR / folder
        path.mkdir(parents=True, exist_ok=True)

        for old_file in path.glob("*.md"):
            old_file.unlink()


def write_document(folder, filename, content):
    path = DATA_DIR / folder / filename
    path.write_text(content.strip() + "\n", encoding="utf-8")


def generate_8ds():
    for i, incident in enumerate(INCIDENT_FAMILIES, start=1):
        year = 2024 if i % 3 == 0 else 2025
        doc_id = f"8D-{year}-{i:03d}"

        if incident["code"] == "CRIMP_RESISTANCE":
            doc_id = "8D-2025-014"

        content = f"""
DOCUMENT_ID: {doc_id}
DOCUMENT_TYPE: 8D
TITLE: {incident['title']}
COMPANY: Anatolia E-Mobility Components
PROCESS: {incident['process']}
PRODUCT: {incident['product']}
STATUS: Closed

# D1 Team

Cross-functional team included Quality, Manufacturing Engineering,
Supplier Quality and Production.

# D2 Problem Description

{incident['symptom']}

The issue was detected during production or final inspection and required
containment to protect the customer.

# D3 Containment

Affected material was quarantined.

100 percent inspection was introduced where appropriate.

Production records and affected supplier lots were reviewed.

# D4 Root Cause

{incident['root_cause']}

Investigation focused on:

{incident['checks']}

The team confirmed the root cause through comparison of conforming and
nonconforming product.

# D5 Corrective Action

{incident['action']}

# D6 Implementation

Corrective actions were implemented and relevant production controls
were updated.

# D7 Prevention

PFMEA, Control Plan and applicable work instructions were reviewed.

Lessons learned were communicated to related manufacturing processes.

# D8 Verification

Follow-up production was monitored.

No recurrence was detected during the verification period.
"""

        write_document(
            "8d",
            f"{doc_id}.md",
            content,
        )


def generate_ncrs():
    incidents = [
        INCIDENT_FAMILIES[0],
        INCIDENT_FAMILIES[1],
        INCIDENT_FAMILIES[2],
        INCIDENT_FAMILIES[3],
        INCIDENT_FAMILIES[4],
        INCIDENT_FAMILIES[5],
        INCIDENT_FAMILIES[6],
        INCIDENT_FAMILIES[7],
        INCIDENT_FAMILIES[12],
        INCIDENT_FAMILIES[13],
    ]

    for i, incident in enumerate(incidents, start=1):
        doc_id = f"NCR-2025-{180 + i}"

        if i == 1:
            doc_id = "NCR-2025-188"

        content = f"""
DOCUMENT_ID: {doc_id}
DOCUMENT_TYPE: NCR
TITLE: NCR - {incident['title']}
COMPANY: Anatolia E-Mobility Components
PROCESS: {incident['process']}
PRODUCT: {incident['product']}
STATUS: Closed

# Nonconformance

{incident['symptom']}

# Immediate Containment

Suspect material was identified and isolated.

Additional inspection was introduced.

# Investigation

The investigation reviewed:

{incident['checks']}

# Cause

{incident['root_cause']}

# Disposition

Affected product was inspected, reworked or scrapped according to
approved quality disposition.

# Follow-up Action

{incident['action']}
"""

        write_document(
            "ncr",
            f"{doc_id}.md",
            content,
        )


def generate_ppaps():
    incident_indexes = [0, 1, 2, 3, 4, 7, 8, 11]

    for i, index in enumerate(incident_indexes, start=1):
        incident = INCIDENT_FAMILIES[index]
        doc_id = f"PPAP-{incident['code']}-{i:02d}"

        content = f"""
DOCUMENT_ID: {doc_id}
DOCUMENT_TYPE: PPAP
TITLE: Production Part Approval - {incident['product']}
COMPANY: Anatolia E-Mobility Components
PROCESS: {incident['process']}
PRODUCT: {incident['product']}
STATUS: Approved

# Product Requirements

Product characteristics are controlled according to released drawing
and customer-specific requirements.

# Special Characteristics

Critical characteristics associated with this process include:

{incident['checks']}

# Process Validation

Capability studies and inspection records demonstrated acceptable
performance at time of PPAP submission.

# Lessons Learned

Historical risk reviewed:

{incident['symptom']}

Known historical cause:

{incident['root_cause']}

Preventive control:

{incident['action']}
"""

        write_document(
            "ppap",
            f"{doc_id}.md",
            content,
        )


def generate_pfmeas():
    groups = [
        ("PFMEA-CRIMP-04", INCIDENT_FAMILIES[0]),
        ("PFMEA-ASSEMBLY-02", INCIDENT_FAMILIES[2]),
        ("PFMEA-WELD-03", INCIDENT_FAMILIES[3]),
        ("PFMEA-OVERMOLD-02", INCIDENT_FAMILIES[8]),
        ("PFMEA-WIREPREP-01", INCIDENT_FAMILIES[6]),
    ]

    for doc_id, incident in groups:
        content = f"""
DOCUMENT_ID: {doc_id}
DOCUMENT_TYPE: PFMEA
TITLE: Process Failure Mode and Effects Analysis - {incident['process']}
COMPANY: Anatolia E-Mobility Components
PROCESS: {incident['process']}
PRODUCT: {incident['product']}
STATUS: Released

# Process Step

{incident['process']}

# Potential Failure Mode

{incident['symptom']}

# Potential Effect

Product performance may fail specification or create customer
assembly concerns.

# Potential Cause

{incident['root_cause']}

# Current Prevention Controls

Process setup verification, preventive maintenance and approved
work instructions.

# Current Detection Controls

Relevant checks include:

{incident['checks']}

# Recommended Action

{incident['action']}
"""

        write_document(
            "pfmea",
            f"{doc_id}.md",
            content,
        )


def generate_control_plans():
    groups = [
        ("CONTROL-PLAN-HV-02", INCIDENT_FAMILIES[0]),
        ("CONTROL-PLAN-ASSEMBLY-03", INCIDENT_FAMILIES[4]),
        ("CONTROL-PLAN-WELD-02", INCIDENT_FAMILIES[3]),
        ("CONTROL-PLAN-OVERMOLD-01", INCIDENT_FAMILIES[8]),
        ("CONTROL-PLAN-EOL-01", INCIDENT_FAMILIES[12]),
    ]

    for doc_id, incident in groups:
        content = f"""
DOCUMENT_ID: {doc_id}
DOCUMENT_TYPE: Control Plan
TITLE: Control Plan - {incident['process']}
COMPANY: Anatolia E-Mobility Components
PROCESS: {incident['process']}
PRODUCT: {incident['product']}
STATUS: Released

# Controlled Characteristics

The following characteristics require process control:

{incident['checks']}

# Inspection Method

Inspection is performed using approved gauges, process monitoring
equipment and documented visual standards.

# Reaction Plan

If a characteristic exceeds requirement:

1. Stop the affected process.
2. Segregate suspect production.
3. Inform Quality.
4. Perform containment inspection.
5. Investigate process change.

# Historical Lesson

Previous failure:

{incident['symptom']}

Historical root cause:

{incident['root_cause']}
"""

        write_document(
            "control_plans",
            f"{doc_id}.md",
            content,
        )


def generate_complaints():
    indexes = [0, 2, 3, 4, 7, 8, 9, 10, 13, 14]

    for i, index in enumerate(indexes, start=1):
        incident = INCIDENT_FAMILIES[index]
        doc_id = f"SUP-COMP-2025-{40 + i:03d}"

        if incident["code"] == "PLATING":
            doc_id = "SUP-COMP-2025-041"

        content = f"""
DOCUMENT_ID: {doc_id}
DOCUMENT_TYPE: Supplier Complaint
TITLE: Supplier Complaint - {incident['title']}
COMPANY: Anatolia E-Mobility Components
PROCESS: {incident['process']}
PRODUCT: {incident['product']}
STATUS: Closed

# Complaint Description

{incident['symptom']}

# Supplier Investigation

The supplier and internal quality team reviewed:

{incident['checks']}

# Confirmed Cause

{incident['root_cause']}

# Supplier Corrective Action

{incident['action']}

# Verification

Subsequent lots were inspected before release.
"""

        write_document(
            "complaints",
            f"{doc_id}.md",
            content,
        )


def generate_deviations():
    indexes = [0, 3, 7, 8, 11]

    for i, index in enumerate(indexes, start=1):
        incident = INCIDENT_FAMILIES[index]
        doc_id = f"DEV-2025-{i:03d}"

        content = f"""
DOCUMENT_ID: {doc_id}
DOCUMENT_TYPE: Engineering Deviation
TITLE: Temporary Engineering Deviation - {incident['product']}
COMPANY: Anatolia E-Mobility Components
PROCESS: {incident['process']}
PRODUCT: {incident['product']}
STATUS: Expired

# Reason for Deviation

Temporary production controls were required following:

{incident['symptom']}

# Temporary Conditions

Additional checks were introduced for:

{incident['checks']}

# Risk Consideration

Known historical cause:

{incident['root_cause']}

# Exit Criteria

Deviation may be closed after implementation of:

{incident['action']}
"""

        write_document(
            "deviations",
            f"{doc_id}.md",
            content,
        )


def generate_work_instructions():
    groups = [
        ("WI-CRIMP-07", INCIDENT_FAMILIES[0]),
        ("WI-CRIMP-08", INCIDENT_FAMILIES[1]),
        ("WI-SEAL-03", INCIDENT_FAMILIES[2]),
        ("WI-WELD-04", INCIDENT_FAMILIES[3]),
        ("WI-ASSEMBLY-09", INCIDENT_FAMILIES[4]),
        ("WI-STRIP-02", INCIDENT_FAMILIES[6]),
        ("WI-EOL-05", INCIDENT_FAMILIES[12]),
    ]

    for doc_id, incident in groups:
        content = f"""
DOCUMENT_ID: {doc_id}
DOCUMENT_TYPE: Work Instruction
TITLE: Work Instruction - {incident['process']}
COMPANY: Anatolia E-Mobility Components
PROCESS: {incident['process']}
PRODUCT: {incident['product']}
STATUS: Released

# Purpose

Define the approved method for the {incident['process']} operation.

# Before Starting

Confirm correct product, tooling, program and inspection equipment.

# Process Checks

Operator must verify:

{incident['checks']}

# Abnormal Condition

If the following symptom is identified:

{incident['symptom']}

stop production and contact Quality.

# Known Risk

Historical investigation identified:

{incident['root_cause']}

# Required Prevention

{incident['action']}
"""

        write_document(
            "work_instructions",
            f"{doc_id}.md",
            content,
        )


def count_documents():
    return len(list(DATA_DIR.rglob("*.md")))


def main():
    ensure_directories()

    generate_8ds()
    generate_ncrs()
    generate_ppaps()
    generate_pfmeas()
    generate_control_plans()
    generate_complaints()
    generate_deviations()
    generate_work_instructions()

    total = count_documents()

    print(f"Created {total} synthetic quality documents.")

    if total != 65:
        print("WARNING: Expected 65 documents.")
    else:
        print("Success: synthetic dataset is ready.")


if __name__ == "__main__":
    main()