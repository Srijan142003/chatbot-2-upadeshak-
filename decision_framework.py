"""
PHASE 2b: DECISION FRAMEWORK
=============================
Structure responses using authentic Dharmic logic:
- Inner Dharma (Antar-Dharma): Self-understanding, fear removal, clarity
- Outer Dharma (Bahya-Dharma): Practical action, responsibility, timing
- Integration: How they work together
"""

from typing import Dict, List
from dataclasses import dataclass

# ── DECISION FRAMEWORK ──────────────────────────────────────────────────────────

@dataclass
class DharmaStep:
    title: str
    explanation: str
    action: str
    verses: List[str]

@dataclass
class DharmaFramework:
    inner_dharma: List[DharmaStep]
    outer_dharma: List[DharmaStep]
    integration: str
    decision_path: List[str]


# ── FRAMEWORK TEMPLATES BY SCENARIO ─────────────────────────────────────────────

FRAMEWORKS = {
    "career_decision": {
        "name": "Career & Life Path Decision",
        "description": "Choosing between safe path vs passionate calling",
        "inner_dharma": [
            DharmaStep(
                title="Understand Your Nature (Svabhava)",
                explanation="Your true nature (guna, svabhava) is the foundation of dharma. Finding it is not optional - it's essential.",
                action="Reflect: What activities make you lose track of time? What problems naturally interest you?",
                verses=["BG-18.48", "BG-4.13", "BG-15.11"]
            ),
            DharmaStep(
                title="Remove Fear & Conditioning",
                explanation="Distinguish between authentic fear (real danger) and false fear (societal expectations, parents' disappointment).",
                action="Journal: Which fears are YOURS? Which are INHERITED from family expectations?",
                verses=["BG-2.3", "BG-18.30", "BG-2.40"]
            ),
            DharmaStep(
                title="Clarify: Passion vs Escape",
                explanation="Are you drawn to startup because it's YOUR dharma, or are you running FROM placement?",
                action="Test: Would you do this work even if it failed? Even if no one praised it?",
                verses=["BG-3.35", "BG-17.26", "BG-4.22"]
            ),
        ],
        "outer_dharma": [
            DharmaStep(
                title="Test Your Path Practically",
                explanation="Don't quit based on enthusiasm alone. Validate your calling through real-world testing.",
                action="Begin startup as side project while employed. Work on it for 6-12 months.",
                verses=["BG-3.8", "BG-18.48", "BG-2.47"]
            ),
            DharmaStep(
                title="Maintain Family Responsibility",
                explanation="Dharma is not selfish. You have duties to those who raised you.",
                action="Have open conversation with parents. Show them you've thought this through.",
                verses=["BG-3.11", "BG-18.41", "VN-13"]
            ),
            DharmaStep(
                title="Decide with Data, Not Just Passion",
                explanation="After testing, decide based on evidence: Is it working? Do you still want it?",
                action="Set clear milestones: revenue, product, user feedback. THEN transition.",
                verses=["BG-2.47", "BG-4.18", "BG-18.17"]
            ),
        ],
        "integration": """
Your dharma honors BOTH:
- BG 3.35: Follow your own path (try the startup)
- BG 18.41: Fulfill your responsibilities (respect family, be cautious)
- BG 2.47: Act without attachment to outcome (test without desperation)

Middle path: Take placement → Build startup parallel → Transition when ready
This way you honor your nature AND your duties. This is the warrior's path.
        """,
        "decision_path": [
            "Week 1: Self-reflection (what's YOUR truth vs inherited expectations?)",
            "Week 2-3: Family conversation (open, honest, no ultimatums)",
            "Month 1: Take placement OR start preparation phase",
            "Month 1-6: Build startup as side project (test your calling)",
            "Month 6: Review - Do you STILL want this?",
            "Month 6+: If yes, plan transition. If no, you now know."
        ]
    },
    
    "family_conflict": {
        "name": "Conflict: Personal Goals vs Family Expectations",
        "description": "When your dharma differs from family's expectations",
        "inner_dharma": [
            DharmaStep(
                title="Understand Your True Dharma",
                explanation="Your dharma is based on YOUR nature, not others' plans.",
                action="Meditation: What do you ACTUALLY want to do?",
                verses=["BG-3.35", "BG-18.48", "BG-4.13"]
            ),
            DharmaStep(
                title="Release Guilt",
                explanation="Following your dharma is not betrayal - it's honoring your soul.",
                action="Understand: Your parents' happiness is not YOUR responsibility.",
                verses=["BG-2.55", "BG-5.20", "BG-18.30"]
            ),
        ],
        "outer_dharma": [
            DharmaStep(
                title="Communicate with Compassion",
                explanation="Speak truth with love. Parents fear loss - address their fears.",
                action="Share your thinking: values, plans, how you'll stay safe.",
                verses=["BG-3.1", "BG-4.9", "BG-18.70"]
            ),
            DharmaStep(
                title="Take Responsibility",
                explanation="Show you're not rebelling - you're being thoughtful.",
                action="Have backup plan, financial plan, timeline for decisions.",
                verses=["BG-2.47", "BG-18.41", "BG-4.18"]
            ),
        ],
        "integration": """
Dharma is not rebellion. Show you can:
- Honor their values while following your path
- Be responsible and thoughtful
- Keep them informed, not ignored
This is how you love your family WHILE being true to yourself.
        """,
        "decision_path": [
            "Step 1: Get clear on YOUR dharma",
            "Step 2: Understand their fears (not just demands)",
            "Step 3: Propose plan that addresses their concerns",
            "Step 4: Show responsibility through action",
            "Step 5: Give time (change takes time)",
        ]
    },
    
    "fear_based": {
        "name": "Paralyzed by Fear",
        "description": "Fear of failure, judgment, or unknown",
        "inner_dharma": [
            DharmaStep(
                title="Name the Fear",
                explanation="What specifically are you afraid of? Be precise.",
                action="Write it down. Is it REAL or assumed?",
                verses=["BG-2.7", "BG-18.30", "BG-2.55"]
            ),
            DharmaStep(
                title="Understand Karma Yoga",
                explanation="You cannot control results. You can only control effort.",
                action="Accept: If you try and fail, that's still dharma. If you don't try, that's not.",
                verses=["BG-2.47", "BG-2.56", "BG-4.17"]
            ),
        ],
        "outer_dharma": [
            DharmaStep(
                title="Take Imperfect Action",
                explanation="You'll never feel 100% ready. Ready is a myth.",
                action="Do the next small thing. Then the next.",
                verses=["BG-3.8", "BG-18.48", "BG-2.40"]
            ),
        ],
        "integration": """
Fear is normal. Action despite fear is dharma.
- Feel the fear (don't deny it)
- Understand you can handle the consequence
- Act anyway with detachment to outcome
This is courage.
        """,
        "decision_path": [
            "Identify the specific fear",
            "Ask: What's the WORST that could happen?",
            "Ask: Could I survive/handle that?",
            "Answer: Yes, you could",
            "Therefore: Take action despite fear",
        ]
    }
}


def get_framework(scenario: str) -> Dict:
    """Get the decision framework for a scenario"""
    return FRAMEWORKS.get(scenario, None)


def format_framework_for_response(framework: DharmaFramework) -> str:
    """Format framework for LLM response"""
    lines = []
    
    lines.append("## INNER DHARMA — Understand Yourself")
    lines.append("(Foundation: Know what YOU truly want)")
    for i, step in enumerate(framework.inner_dharma, 1):
        lines.append(f"\n**Step {i}: {step.title}**")
        lines.append(step.explanation)
        lines.append(f"→ Action: {step.action}")
        lines.append(f"→ Supporting verses: {', '.join(step.verses)}")
    
    lines.append("\n\n## OUTER DHARMA — Take Responsibility")
    lines.append("(Application: How you move forward practically)")
    for i, step in enumerate(framework.outer_dharma, 1):
        lines.append(f"\n**Step {i}: {step.title}**")
        lines.append(step.explanation)
        lines.append(f"→ Action: {step.action}")
        lines.append(f"→ Supporting verses: {', '.join(step.verses)}")
    
    lines.append("\n\n## INTEGRATION — The Dharmic Path")
    lines.append(framework.integration)
    
    lines.append("\n\n## YOUR DECISION PATH")
    for i, step in enumerate(framework.decision_path, 1):
        lines.append(f"\n**{i}. {step}**")
    
    return "\n".join(lines)


# ── TEST ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("DECISION FRAMEWORKS TEST")
    print("=" * 70)
    
    framework_dict = FRAMEWORKS["career_decision"]
    print(f"\n{framework_dict['name']}")
    print(f"Description: {framework_dict['description']}")
    
    framework = DharmaFramework(
        inner_dharma=framework_dict["inner_dharma"],
        outer_dharma=framework_dict["outer_dharma"],
        integration=framework_dict["integration"],
        decision_path=framework_dict["decision_path"]
    )
    
    print("\n" + format_framework_for_response(framework))
