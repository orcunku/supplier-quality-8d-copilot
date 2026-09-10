from pathlib import Path

import streamlit as st

from src.vector_store import load_index
from src.retrieval import search_documents
from src.investigation import (
    build_investigation_plan,
)


# ---------------------------------------------------------
# PATHS
# ---------------------------------------------------------

BASE_DIR = Path(
    __file__
).resolve().parent

INDEX_PATH = (
    BASE_DIR
    / "vector_db"
    / "quality.index"
)

METADATA_PATH = (
    BASE_DIR
    / "vector_db"
    / "metadata.json"
)


# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------

st.set_page_config(
    page_title=(
        "Supplier Quality 8D Copilot"
    ),
    page_icon="🔎",
    layout="wide",
)


# ---------------------------------------------------------
# CACHE VECTOR DATABASE
# ---------------------------------------------------------

@st.cache_resource
def get_vector_database():

    if not INDEX_PATH.exists():
        return None, None

    if not METADATA_PATH.exists():
        return None, None

    return load_index(
        INDEX_PATH,
        METADATA_PATH,
    )


index, chunks = get_vector_database()


# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------

if "results" not in st.session_state:
    st.session_state.results = []

if "problem" not in st.session_state:
    st.session_state.problem = ""

if "investigation_plan" not in (
    st.session_state
):
    st.session_state.investigation_plan = []


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

st.sidebar.title(
    "Supplier Quality 8D Copilot"
)

st.sidebar.caption(
    "Synthetic demonstration environment"
)

st.sidebar.divider()

document_types = st.sidebar.multiselect(
    "Document Types",
    [
        "8D",
        "NCR",
        "PPAP",
        "PFMEA",
        "Control Plan",
        "Supplier Complaint",
        "Engineering Deviation",
        "Work Instruction",
    ],
    default=[
        "8D",
        "NCR",
        "PFMEA",
        "Control Plan",
        "Supplier Complaint",
    ],
)

process_filter = st.sidebar.selectbox(
    "Process",
    [
        "All",
        "Crimping",
        "Assembly",
        "Ultrasonic Welding",
        "Wire Preparation",
        "Incoming Material",
        "Overmolding",
        "Electrical Test",
        "Forming",
    ],
)

number_results = st.sidebar.slider(
    "Maximum Results",
    min_value=3,
    max_value=10,
    value=5,
)

st.sidebar.divider()

st.sidebar.write(
    "**Demo company**"
)

st.sidebar.write(
    "Anatolia E-Mobility Components"
)

st.sidebar.caption(
    "All company names, incidents and "
    "documents are fictional."
)


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.title(
    "Supplier Quality 8D Copilot"
)

st.write(
    "Find similar historical quality "
    "failures and recover how they "
    "were previously investigated."
)


# ---------------------------------------------------------
# KPI CARDS
# ---------------------------------------------------------

col1, col2, col3, col4 = st.columns(
    4
)

with col1:
    st.metric(
        "Quality Documents",
        "65",
    )

with col2:
    st.metric(
        "Historical 8Ds",
        "15",
    )

with col3:
    st.metric(
        "NCRs",
        "10",
    )

with col4:
    vector_count = (
        index.ntotal
        if index is not None
        else 0
    )

    st.metric(
        "Indexed Evidence Chunks",
        vector_count,
    )


st.divider()


# ---------------------------------------------------------
# DATABASE CHECK
# ---------------------------------------------------------

if index is None:

    st.error(
        "Vector database not found."
    )

    st.code(
        "python scripts/generate_synthetic_data.py\n"
        "python scripts/build_index.py"
    )

    st.stop()


# ---------------------------------------------------------
# PROBLEM INPUT
# ---------------------------------------------------------

st.subheader(
    "Describe the New Quality Problem"
)

problem = st.text_area(
    "Problem",
    value=st.session_state.problem,
    height=140,
    placeholder=(
        "Example: HV cable terminal "
        "resistance increased from "
        "0.18 mOhm to 0.43 mOhm after "
        "crimping. Supplier lot B240817."
    ),
    label_visibility="collapsed",
)

search_button = st.button(
    "Find Similar Incidents",
    type="primary",
    use_container_width=True,
)


# ---------------------------------------------------------
# RUN SEARCH
# ---------------------------------------------------------

if search_button:

    if not problem.strip():

        st.warning(
            "Please describe the "
            "quality problem first."
        )

    else:

        with st.spinner(
            "Searching historical "
            "quality records..."
        ):

            results = search_documents(
                query=problem,
                index=index,
                chunks=chunks,
                max_documents=(
                    number_results
                ),
            )

        filtered_results = []

        for result in results:

            if (
                document_types
                and result[
                    "document_type"
                ]
                not in document_types
            ):
                continue

            if (
                process_filter != "All"
                and result[
                    "process"
                ]
                != process_filter
            ):
                continue

            filtered_results.append(
                result
            )

        st.session_state.results = (
            filtered_results
        )

        st.session_state.problem = (
            problem
        )

        st.session_state[
            "investigation_plan"
        ] = []


# ---------------------------------------------------------
# DISPLAY RESULTS
# ---------------------------------------------------------

results = st.session_state.results


if results:

    st.divider()

    st.success(
        f"{len(results)} similar "
        "historical records found."
    )

    st.subheader(
        "Similar Historical Incidents"
    )

    for rank, result in enumerate(
        results,
        start=1,
    ):

        with st.container(
            border=True
        ):

            score_col, content_col = (
                st.columns(
                    [1, 5]
                )
            )

            with score_col:

                st.metric(
                    "Historical Similarity",
                    (
                        f"{result['display_score']}%"
                    ),
                )

                st.caption(
                    f"Rank #{rank}"
                )

            with content_col:

                st.markdown(
                    f"### "
                    f"{result['document_id']}"
                )

                st.caption(
                    f"{result['document_type']} "
                    f"• {result['process']} "
                    f"• {result['product']}"
                )

                st.write(
                    f"**{result['title']}**"
                )

                st.markdown(
                    "**Most Relevant Evidence**"
                )

                for match in (
                    result["matches"][:2]
                ):

                    st.write(
                        f"**{match['section']}**"
                    )

                    st.write(
                        match["text"]
                    )

                with st.expander(
                    "View All Retrieved "
                    "Source Evidence"
                ):

                    for match in (
                        result["matches"]
                    ):

                        st.markdown(
                            f"#### "
                            f"{match['section']}"
                        )

                        st.write(
                            match["text"]
                        )

                        st.caption(
                            f"Source: "
                            f"{result['document_id']}"
                            f" — "
                            f"{match['section']}"
                        )

                        st.divider()


    # -----------------------------------------------------
    # INVESTIGATION PLAN
    # -----------------------------------------------------

    st.divider()

    st.subheader(
        "Quality Investigation Assistant"
    )

    st.write(
        "Generate an investigation checklist "
        "based on evidence retrieved from "
        "historical quality records."
    )

    investigate_button = st.button(
        "Generate Investigation Plan",
        use_container_width=True,
    )

    if investigate_button:

        plan = build_investigation_plan(
            results
        )

        st.session_state[
            "investigation_plan"
        ] = plan


# ---------------------------------------------------------
# SHOW INVESTIGATION PLAN
# ---------------------------------------------------------

plan = st.session_state[
    "investigation_plan"
]


if plan:

    st.divider()

    st.subheader(
        "Recommended Investigation"
    )

    high_priority = [
        item
        for item in plan
        if item["priority"] == "HIGH"
    ]

    if high_priority:

        st.error(
            "Historical evidence suggests "
            "starting with: "
            + high_priority[0]["title"]
        )

    categories = [
        "Machine",
        "Material",
        "Method",
        "Measurement",
        "Man",
        "General",
    ]

    available_categories = [
        category
        for category in categories
        if any(
            item["category"]
            == category
            for item in plan
        )
    ]

    tabs = st.tabs(
        available_categories
    )

    for tab, category in zip(
        tabs,
        available_categories,
    ):

        with tab:

            category_items = [
                item
                for item in plan
                if item[
                    "category"
                ]
                == category
            ]

            for item_index, item in (
                enumerate(
                    category_items
                )
            ):

                with st.container(
                    border=True
                ):

                    st.markdown(
                        f"### "
                        f"{item['title']}"
                    )

                    if (
                        item["priority"]
                        == "HIGH"
                    ):

                        st.error(
                            "Priority: HIGH"
                        )

                    else:

                        st.warning(
                            "Priority: MEDIUM"
                        )

                    st.markdown(
                        "**What to check**"
                    )

                    for (
                        check_index,
                        check,
                    ) in enumerate(
                        item["checks"]
                    ):

                        st.checkbox(
                            check,
                            key=(
                                f"{category}-"
                                f"{item_index}-"
                                f"{check_index}-"
                                f"{check}"
                            ),
                        )

                    st.markdown(
                        "**Evidence Sources**"
                    )

                    for evidence in (
                        item["evidence"]
                    ):

                        st.write(
                            f"• {evidence}"
                        )


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.divider()

st.caption(
    "Supplier Quality 8D Copilot provides "
    "evidence-based decision support. "
    "Final quality and engineering decisions "
    "remain with authorized personnel."
)

st.caption(
    "Demo environment. All organizations, "
    "document IDs, products and incidents "
    "are synthetic."
)