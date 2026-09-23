async def run(ctx, inputs):
    leads = inputs["leads"]

    inactive_leads = []

    for lead in leads:
        inactive_leads.append({
            "name": lead["name"],
            "last_contact": lead["last_contact"],
            "notes": lead["notes"]
        })

    lines = [
        "# Lead Reactivation Plan",
        "",
        f"Total leads: {len(inactive_leads)}",
        ""
    ]

    for index, lead in enumerate(inactive_leads, start=1):
        lines.extend([
            f"## Lead {index}: {lead['name']}",
            f"- Last contact: {lead['last_contact']}",
            f"- Notes: {lead['notes']}",
            "- Recommended action: Send a personalized reactivation message based on the previous interaction.",
            ""
        ])

    return {
        "path": "reports/LEAD_REACTIVATION.md",
        "content": "\n".join(lines)
    }