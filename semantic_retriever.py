"""
PHASE 2: INTENT DETECTION + SEMANTIC RETRIEVAL
===============================================
Smart verse selection based on philosophical intent, not keywords.
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Tuple
from verse_canonicalizer import load_canonical_verses, CanonicalVerse
from verse_taxonomy import VERSE_CATEGORIES, build_verse_to_categories

# ── INTENT DETECTION ───────────────────────────────────────────────────────────

class IntentDetector:
    """Detect what type of spiritual/life question this is"""
    
    # Question type patterns
    DECISION_PATTERNS = [
        r"should i", r"what should", r"should i take", r"which option",
        r"choose.*between", r"path.*take", r"pursue", r"follow",
        r"career", r"startup", r"job", r"opportunity"
    ]
    
    EMOTIONAL_PATTERNS = [
        r"confused", r"lost", r"scared", r"afraid", r"worried",
        r"anxious", r"sad", r"depressed", r"struggling", r"hurt",
        r"disappointed", r"ashamed", r"embarrassed"
    ]
    
    FAMILY_PATTERNS = [
        r"parent", r"mother", r"father", r"family", r"relative",
        r"expectation", r"pressure", r"disappoint", r"responsibility",
        r"obligation", r"duty.*family"
    ]
    
    SPIRITUAL_PATTERNS = [
        r"dharma", r"karma", r"truth", r"meaning", r"purpose",
        r"soul", r"god", r"spiritual", r"enlighten", r"liberation",
        r"consciousness", r"inner peace"
    ]
    
    RELATIONSHIP_PATTERNS = [
        r"friendship", r"love", r"relationship", r"conflict",
        r"trust", r"betrayal", r"forgive", r"communication"
    ]
    
    def detect(self, query: str) -> Dict[str, float]:
        """
        Detect question intent.
        Returns scores for each intent type.
        """
        query_lower = query.lower()
        scores = {
            "decision": self._score_patterns(query_lower, self.DECISION_PATTERNS),
            "emotional": self._score_patterns(query_lower, self.EMOTIONAL_PATTERNS),
            "family": self._score_patterns(query_lower, self.FAMILY_PATTERNS),
            "spiritual": self._score_patterns(query_lower, self.SPIRITUAL_PATTERNS),
            "relationship": self._score_patterns(query_lower, self.RELATIONSHIP_PATTERNS),
        }
        return scores
    
    def _score_patterns(self, text: str, patterns: List[str]) -> float:
        """Score how many patterns match"""
        matches = sum(1 for p in patterns if re.search(p, text))
        return matches / len(patterns) if patterns else 0
    
    def get_primary_intent(self, query: str) -> str:
        """Get the primary intent (highest score)"""
        scores = self.detect(query)
        return max(scores.items(), key=lambda x: x[1])[0]
    
    def get_category_for_intent(self, intent: str) -> List[str]:
        """Map intent to verse categories"""
        intent_to_categories = {
            "decision": ["decision_making", "own_dharma", "duty_clarity"],
            "emotional": ["confusion_clarity", "fear_removal", "inner_strength"],
            "family": ["family_duty", "responsibility", "duty_clarity"],
            "spiritual": ["purpose_meaning", "inner_strength", "authentic_passion"],
            "relationship": ["family_duty", "leadership"],
        }
        return intent_to_categories.get(intent, ["own_dharma", "duty_clarity"])


# ── SEMANTIC VERSE RETRIEVER ───────────────────────────────────────────────────

class SemanticRetriever:
    """
    Retrieve verses using semantic intent matching, not keyword matching.
    Steps:
    1. Detect intent from query
    2. Get category for intent
    3. Prioritize verses from category
    4. Rank by relevance
    5. Verify authenticity
    """
    
    def __init__(self):
        self.canonical_verses = load_canonical_verses()
        self.verse_to_categories = build_verse_to_categories()
        self.intent_detector = IntentDetector()
    
    def retrieve(self, query: str, top_k: int = 6) -> List[CanonicalVerse]:
        """Semantically retrieve top verses for query"""
        
        # Step 1: Detect intent
        intent = self.intent_detector.get_primary_intent(query)
        print(f"  Intent detected: {intent}")
        
        # Step 2: Get relevant categories
        categories = self.intent_detector.get_category_for_intent(intent)
        print(f"  Relevant categories: {categories}")
        
        # Step 3: Get all verses in relevant categories
        candidate_verses = []
        for category in categories:
            if category in VERSE_CATEGORIES:
                verse_ids = VERSE_CATEGORIES[category]["verses"]
                priority = VERSE_CATEGORIES[category]["priority"]
                priority_score = {"CRITICAL": 3, "HIGH": 2, "MEDIUM": 1}.get(priority, 1)
                
                for verse_id in verse_ids:
                    if verse_id in self.canonical_verses:
                        candidate_verses.append((
                            self.canonical_verses[verse_id],
                            priority_score,
                            category
                        ))
        
        # Step 4: Sort by priority (critical first)
        candidate_verses.sort(key=lambda x: x[1], reverse=True)
        
        # Step 5: Return top K with source verification
        result = []
        for verse, priority, category in candidate_verses[:top_k]:
            if verse.verify():  # Verify authenticity
                result.append(verse)
        
        print(f"  Retrieved {len(result)} authentic verses")
        return result


# ── TEST ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("🔍 SEMANTIC RETRIEVAL TEST")
    print("=" * 60)
    
    retriever = SemanticRetriever()
    
    # Test case: Career dilemma
    query = """
    Namaste… I'm really confused right now. Everyone around me is preparing 
    for placements, and I also got an opportunity in a decent company. But 
    honestly, I don't feel excited about it. I want to try something of my 
    own, maybe a startup… but I'm scared of failing and disappointing my 
    parents. What should I do?
    """
    
    print(f"\n📝 Query: {query[:100]}...")
    print("\n🔄 Retrieving verses:")
    verses = retriever.retrieve(query, top_k=6)
    
    print(f"\n✅ Retrieved {len(verses)} verses:")
    for i, verse in enumerate(verses, 1):
        print(f"\n{i}. {verse.verse_id} ({verse.source})")
        print(f"   {verse.reference}")
        print(f"   Teaching: {verse.translation[:100]}...")
        print(f"   Verified: {verse.verify()}")
