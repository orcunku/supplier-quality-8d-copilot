INVESTIGATION_LIBRARY = {
    "Machine": [
        {
            "title": "Inspect tooling condition",
            "keywords": [
                "tool wear",
                "tooling",
                "die wear",
                "sonotrode",
                "fixture",
                "applicator",
            ],
            "checks": [
                "Inspect current tooling condition",
                "Check tooling cycle count",
                "Review preventive maintenance history",
                "Compare tooling against wear limits",
            ],
        },
        {
            "title": "Verify machine setup",
            "keywords": [
                "machine",
                "setup",
                "alignment",
                "fixture travel",
            ],
            "checks": [
                "Verify machine setup parameters",
                "Review latest approved setup",
                "Check machine alignment",
                "Review recent setup changes",
            ],
        },
    ],

    "Material": [
        {
            "title": "Verify incoming material",
            "keywords": [
                "supplier",
                "lot",
                "plating",
                "oxidation",
                "material",
                "contamination",
            ],
            "checks": [
                "Confirm supplier lot traceability",
                "Inspect incoming material condition",
                "Compare with previous conforming lot",
                "Review supplier inspection records",
            ],
        },
        {
            "title": "Inspect conductor or component condition",
            "keywords": [
                "strand",
                "conductor",
                "terminal",
                "seal",
                "surface",
            ],
            "checks": [
                "Inspect component for visible damage",
                "Check dimensions against specification",
                "Check contact or sealing surfaces",
                "Compare suspect and good components",
            ],
        },
    ],

    "Method": [
        {
            "title": "Verify process parameters",
            "keywords": [
                "crimp height",
                "insertion",
                "recipe",
                "method",
                "process",
                "cleaning",
            ],
            "checks": [
                "Compare current settings with specification",
                "Review last process change",
                "Check first-off approval record",
                "Verify work instruction was followed",
            ],
        },
    ],

    "Measurement": [
        {
            "title": "Verify the measurement system",
            "keywords": [
                "measurement",
                "resistance",
                "calibration",
                "gauge",
                "test",
                "inspection",
            ],
            "checks": [
                "Check calibration status",
                "Verify measurement fixture condition",
                "Test a known reference part",
                "Review Gauge R&R if available",
            ],
        },
    ],

    "Man": [
        {
            "title": "Review operator and setup history",
            "keywords": [
                "operator",
                "manual",
                "training",
                "setup",
                "work instruction",
            ],
            "checks": [
                "Confirm operator training status",
                "Review setup authorization",
                "Review shift and operator records",
                "Check whether the method was followed",
            ],
        },
    ],
}


def build_evidence_text(search_results):
    text_parts = []

    for result in search_results:

        text_parts.append(
            result["title"]
        )

        for match in result[
            "matches"
        ]:

            text_parts.append(
                match["text"]
            )

    return " ".join(
        text_parts
    ).lower()


def build_investigation_plan(
    search_results,
):
    evidence_text = build_evidence_text(
        search_results
    )

    plan = []

    for category, items in (
        INVESTIGATION_LIBRARY.items()
    ):

        for item in items:

            matches = []

            for keyword in item[
                "keywords"
            ]:

                if keyword.lower() in evidence_text:
                    matches.append(
                        keyword
                    )

            if matches:

                evidence_ids = []

                for result in (
                    search_results
                ):

                    result_text = " ".join(
                        match["text"]
                        for match in result[
                            "matches"
                        ]
                    ).lower()

                    if any(
                        keyword.lower()
                        in result_text
                        for keyword
                        in item[
                            "keywords"
                        ]
                    ):

                        evidence_ids.append(
                            result[
                                "document_id"
                            ]
                        )

                priority = "MEDIUM"

                if len(matches) >= 2:
                    priority = "HIGH"

                plan.append(
                    {
                        "category": category,
                        "title": item[
                            "title"
                        ],
                        "priority": priority,
                        "checks": item[
                            "checks"
                        ],
                        "evidence": list(
                            dict.fromkeys(
                                evidence_ids
                            )
                        )[:4],
                    }
                )

    if not plan:
        plan.append(
            {
                "category": "General",
                "title": (
                    "Perform structured "
                    "5M investigation"
                ),
                "priority": "MEDIUM",
                "checks": [
                    "Review Machine factors",
                    "Review Material factors",
                    "Review Method factors",
                    "Review Measurement factors",
                    "Review Man factors",
                ],
                "evidence": [
                    result[
                        "document_id"
                    ]
                    for result
                    in search_results[:3]
                ],
            }
        )

    priority_order = {
        "HIGH": 0,
        "MEDIUM": 1,
        "LOW": 2,
    }

    plan.sort(
        key=lambda item: priority_order[
            item["priority"]
        ]
    )

    return plan