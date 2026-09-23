import asyncio
import importlib.util
from pathlib import Path


WORKFLOW_FILE = (
    Path(__file__).parent.parent
    / "workflow_packages"
    / "growth.lead_reactivation"
    / "main.py"
)


def load_workflow():
    spec = importlib.util.spec_from_file_location(
        "lead_reactivation_main",
        WORKFLOW_FILE
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_lead_reactivation():
    workflow = load_workflow()

    inputs = {
        "project_id": "00000000-0000-0000-0000-000000000001",
        "leads": [
            {
                "name": "Alice",
                "last_contact": "2026-08-01",
                "notes": "Interested in the product but stopped responding."
            },
            {
                "name": "Bob",
                "last_contact": "2026-07-15",
                "notes": "Asked for pricing information."
            }
        ]
    }

    result = asyncio.run(workflow.run(None, inputs))

    assert result["path"] == "reports/LEAD_REACTIVATION.md"

    content = result["content"]

    assert "# Lead Reactivation Plan" in content
    assert "Total leads: 2" in content
    assert "Alice" in content
    assert "Bob" in content
    assert "Recommended action:" in content


def test_empty_leads():
    workflow = load_workflow()

    inputs = {
        "project_id": "00000000-0000-0000-0000-000000000001",
        "leads": []
    }

    result = asyncio.run(workflow.run(None, inputs))

    assert result["path"] == "reports/LEAD_REACTIVATION.md"
    assert "Total leads: 0" in result["content"]