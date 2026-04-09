"""
PHASE 1b: VERSE CATEGORIZATION TAXONOMY
========================================
Map each authentic verse to philosophical categories.
Used for smart semantic selection, not keyword matching.
"""

import json
from pathlib import Path
from typing import Dict, List, Set

# ── VERSE CATEGORIES (Philosophical Intent) ────────────────────────────────────

VERSE_CATEGORIES = {
    # CORE DECISION-MAKING VERSES
    "own_dharma": {
        "name": "Own Dharma vs Borrowed Path",
        "description": "Follow your nature, not society's expectations",
        "verses": [
            "BG-3.35",      # Better to follow one's own dharma imperfectly
            "BG-18.48",     # Success in your nature, failure in another's
            "BG-4.13",      # Four-fold division of society by nature
            "BG-15.11",     # Understanding own nature
            "BG-2.31",      # Duty according to nature
        ],
        "priority": "CRITICAL"
    },
    
    "fear_removal": {
        "name": "Removing Fear & Doubt",
        "description": "Overcome paralysis and self-doubt",
        "verses": [
            "BG-2.3",       # Why do you lament?
            "BG-18.30",     # Fearlessness and mental clarity
            "BG-2.40",      # Lose no effort in the path
            "BG-4.10",      # Free from fear and anger
            "BG-15.5",      # Free from pride and delusion
        ],
        "priority": "HIGH"
    },
    
    "duty_clarity": {
        "name": "Understanding Dharma & Duty",
        "description": "What is right duty? Clarity on responsibilities",
        "verses": [
            "BG-2.47",      # Do your duty without attachment to result
            "BG-3.11",      # By yagna, nourish all beings
            "BG-18.41",     # Every person has duty based on nature",
            "BG-2.31",      # Duty of one's state of life",
            "BG-3.19",      # Work is worship",
        ],
        "priority": "HIGH"
    },
    
    "detachment": {
        "name": "Detachment from Outcome (Nishkama Karma)",
        "description": "Act without clinging to success or failure",
        "verses": [
            "BG-2.47",      # Right to perform duty, not to fruit
            "BG-2.56",      # Separate from ups and downs
            "BG-18.11",     # Cannot be destroyed by actions
            "BG-4.19",      # Freed from desire and aversion
            "BG-5.11",      # Renounce attachment to fruit
        ],
        "priority": "HIGH"
    },
    
    # EMOTIONAL/MENTAL CLARITY
    "confusion_clarity": {
        "name": "Overcoming Confusion & Indecision",
        "description": "From confusion to clarity",
        "verses": [
            "BG-2.7",       # I am confused, please guide me
            "BG-10.11",     # I shine with knowledge
            "BG-5.16",      # Knowledge dispels ignorance
            "BG-13.25",     # Understanding the supreme truth
            "CN-86",        # Wisdom in choosing path
        ],
        "priority": "HIGH"
    },
    
    "inner_strength": {
        "name": "Building Inner Strength & Courage",
        "description": "Cultivate confidence and resilience",
        "verses": [
            "BG-18.78",     # Where there is Krishna...
            "BG-10.12",     # You are the supreme power
            "BG-18.26",     # Fixed in resolve",
            "BG-2.40",      # No effort is wasted",
            "BG-4.9",       # Free from reaction, pure knowledge",
        ],
        "priority": "MEDIUM"
    },
    
    # RELATIONSHIPS & RESPONSIBILITIES
    "family_duty": {
        "name": "Family Duty & Responsibilities",
        "description": "Balancing personal goals with family obligations",
        "verses": [
            "BG-1.28-40",   # Arjuna's concern for family
            "BG-2.37",      # Arise and fight
            "BG-3.13",      # Those who eat without giving are sinners (obligation)",
            "BG-18.41",     # Duty of each station",
            "VN-13",        # Kings have duty to subjects",
        ],
        "priority": "HIGH"
    },
    
    "leadership": {
        "name": "Leadership & Responsibility",
        "description": "How to lead without ego",
        "verses": [
            "BG-3.21",      # Whatever great person does, others follow",
            "BG-18.1-2",    # Renounce action with attachment",
            "CN-1",         # Chanakya on wise counsel",
            "CN-32",        # Administrator's duty",
        ],
        "priority": "MEDIUM"
    },
    
    # PRACTICAL ACTION
    "action_path": {
        "name": "Taking Action & Next Steps",
        "description": "How to move forward practically",
        "verses": [
            "BG-3.8",       # Perform action and sacrifice",
            "BG-18.48",     # Strive with all your might",
            "BG-11.33",     # Kill the enemy, do your duty",
            "BG-2.47",      # Perform all duties",
            "CN-2",         # Chanakya on practical wisdom",
        ],
        "priority": "HIGH"
    },
    
    "decision_making": {
        "name": "Decision-Making Framework",
        "description": "How to choose between options",
        "verses": [
            "BG-3.35",      # Own dharma is better
            "BG-18.48",     # Choose your nature-aligned path",
            "BG-2.31",      # Duty according to station in life",
            "BG-4.13",      # Natural divisions of work",
            "CN-53",        # Wisdom in decisions",
        ],
        "priority": "CRITICAL"
    },
    
    # SUCCESS & FAILURE
    "success_mindset": {
        "name": "Success Without Ego",
        "description": "Achieve without attachment or arrogance",
        "verses": [
            "BG-18.24",     # Result of action centered on self
            "BG-18.17-19",  # Pure action with no attachment",
            "BG-2.48",      # Yoga is skill in action",
            "BG-5.23",      # Find peace within",
            "CN-86",        # Winning with dharma",
        ],
        "priority": "MEDIUM"
    },
    
    "failure_resilience": {
        "name": "Handling Failure & Setback",
        "description": "Balance, equanimity, learning from failure",
        "verses": [
            "BG-2.56",      # Separate from pairs of opposites",
            "BG-2.38",      # Look at pleasure and pain equal",
            "BG-5.20",      # Not shaken by loss",
            "BG-18.9",      # Performs action detached from fruit",
            "VN-48",        # Vidura on forgiveness and resilience",
        ],
        "priority": "MEDIUM"
    },
    
    # PASSION & MOTIVATION
    "authentic_passion": {
        "name": "Authentic Passion vs False Enthusiasm",
        "description": "Distinguishing true calling from impulse",
        "verses": [
            "BG-3.35",      # Own dharma imperfectly
            "BG-18.48",     # Based on your nature",
            "BG-17.26",     # Actions done for right reason",
            "BG-4.18",      # See action in all inaction, and action in all action",
            "CN-45",        # Wisdom and folly distinguished",
        ],
        "priority": "HIGH"
    },
    
    "purpose_meaning": {
        "name": "Finding Purpose & Meaning",
        "description": "What is my life for?",
        "verses": [
            "BG-3.19",      # Perform action without selfish motive",
            "BG-18.46",     # Worship the almighty through one's duty",
            "BG-4.24",      # Brahman is the offering",
            "BG-15.11",     # Light of self-knowledge",
            "CN-86",        # Purpose of life",
        ],
        "priority": "MEDIUM"
    },
}

# ── VERSE LOOKUP INDEX ─────────────────────────────────────────────────────────

def build_verse_to_categories() -> Dict[str, Set[str]]:
    """Build reverse index: verse_id → {categories}"""
    index = {}
    for category_name, category_data in VERSE_CATEGORIES.items():
        for verse_id in category_data.get("verses", []):
            if verse_id not in index:
                index[verse_id] = set()
            index[verse_id].add(category_name)
    return index


def get_critical_verses() -> List[str]:
    """Get all CRITICAL priority verses"""
    verses = []
    for cat_name, cat_data in VERSE_CATEGORIES.items():
        if cat_data.get("priority") == "CRITICAL":
            verses.extend(cat_data.get("verses", []))
    return list(set(verses))


def get_verses_by_priority(priority: str) -> List[str]:
    """Get all verses matching priority"""
    verses = []
    for cat_name, cat_data in VERSE_CATEGORIES.items():
        if cat_data.get("priority") == priority:
            verses.extend(cat_data.get("verses", []))
    return list(set(verses))


def get_categories_for_intent(intent: str) -> List[str]:
    """Get categories relevant to a specific intent"""
    relevant = []
    intent_lower = intent.lower()
    
    for cat_name, cat_data in VERSE_CATEGORIES.items():
        desc = cat_data.get("description", "").lower()
        if any(word in desc for word in intent_lower.split()):
            relevant.append(cat_name)
    
    return relevant


# ── SAVE TAXONOMY ──────────────────────────────────────────────────────────────

def save_taxonomy():
    """Save taxonomy for reference"""
    output = {
        "categories": VERSE_CATEGORIES,
        "verse_to_categories": build_verse_to_categories(),
        "critical_verses": get_critical_verses(),
        "summary": {
            "total_categories": len(VERSE_CATEGORIES),
            "total_verse_mappings": len(build_verse_to_categories()),
            "critical_count": len(get_critical_verses()),
        }
    }
    
    with open("VERSE_TAXONOMY.json", "w", encoding="utf-8") as f:
        output["verse_to_categories"] = {k: list(v) for k, v in output["verse_to_categories"].items()}
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    print("✅ Saved VERSE_TAXONOMY.json")


# ── TEST ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("📚 VERSE CATEGORIZATION TAXONOMY")
    print("=" * 60)
    
    print(f"\n✓ {len(VERSE_CATEGORIES)} philosophical categories")
    print(f"✓ {len(build_verse_to_categories())} verses mapped")
    
    print(f"\nCRITICAL verses (must use for decisions):")
    for v in get_critical_verses():
        print(f"  • {v}")
    
    print(f"\nCategory Sample:")
    for name, data in list(VERSE_CATEGORIES.items())[:3]:
        print(f"  [{data['priority']}] {data['name']}")
        print(f"       {data['description']}")
        print(f"       Verses: {', '.join(data['verses'][:3])}")
    
    save_taxonomy()
