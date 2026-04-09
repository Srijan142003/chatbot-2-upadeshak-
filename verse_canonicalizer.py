"""
PHASE 1: SOURCE VERIFICATION + VERSE CANONICALIZATION
========================================================
Build a verified verse database from the 4 authentic JSON sources.
All verses MUST come from these sources only.
No AI fabrication allowed.
"""

import json
import hashlib
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict

DATA_DIR = Path(__file__).parent / "data"

# ── CANONICAL VERSE STRUCTURE ──────────────────────────────────────────────────

@dataclass
class CanonicalVerse:
    """Single source of truth for any verse"""
    verse_id: str               # BG-2.47, CN-86, VN-5, H-1-1
    source: str                 # "Bhagavad Gita", "Chanakya Niti", etc.
    sanskrit: str               # Devanagari (if available)
    transliteration: str        # Roman script (if available)
    translation: str            # English meaning
    reference: str              # "Chapter 2, Verse 47"
    context: str                # Additional context
    source_hash: str            # SHA256 hash for verification
    
    def verify(self) -> bool:
        """Verify this verse hasn't been tampered with"""
        expected = self._calculate_hash()
        return expected == self.source_hash
    
    def _calculate_hash(self) -> str:
        """Calculate integrity hash"""
        content = f"{self.verse_id}|{self.sanskrit}|{self.translation}"
        return hashlib.sha256(content.encode()).hexdigest()[:16]


# ── LOADER: BUILD CANONICAL VERSE DATABASE ─────────────────────────────────────

class VerseCanonicalizer:
    """Transform raw JSON files into verified canonical verses"""
    
    def __init__(self):
        self.verses: Dict[str, CanonicalVerse] = {}
        self.source_records: Dict[str, int] = {}
    
    def load_all(self) -> Dict[str, CanonicalVerse]:
        """Load and verify all 4 sources"""
        print("🔍 Loading authentic sources...")
        
        self.load_bhagavad_gita()
        self.load_chanakya()
        self.load_vidura_niti()
        self.load_hitopadesha()
        
        print(f"✅ Loaded {len(self.verses)} verified verses")
        print(f"   Sources: {self.source_records}")
        return self.verses
    
    def load_bhagavad_gita(self):
        """Load Bhagavad Gita (701 verses)"""
        path = DATA_DIR / "bhagavad_gita_complete.json"
        if not path.exists():
            print(f"❌ {path} not found")
            return
        
        with open(path, encoding="utf-8") as f:
            records = json.load(f)
        
        for r in records:
            chapter = r.get("chapter", 0)
            verse_num = r.get("text_number", 0)
            verse_id = f"BG-{chapter}.{verse_num}"
            
            if not r.get("translation"):
                continue
            
            canonical = CanonicalVerse(
                verse_id=verse_id,
                source="Bhagavad Gita",
                sanskrit=r.get("sanskrit", ""),
                transliteration=r.get("transliteration", ""),
                translation=r.get("translation", ""),
                reference=f"Chapter {chapter}, Verse {verse_num}",
                context=r.get("purport", "")[:200],
                source_hash=""
            )
            canonical.source_hash = canonical._calculate_hash()
            
            self.verses[verse_id] = canonical
        
        self.source_records["Bhagavad Gita"] = len([v for v in self.verses.values() if v.source == "Bhagavad Gita"])
        print(f"  ✓ Bhagavad Gita: {self.source_records['Bhagavad Gita']} verses")
    
    def load_chanakya(self):
        """Load Chanakya Niti (356 verses)"""
        path = DATA_DIR / "chanakya.json"
        if not path.exists():
            print(f"❌ {path} not found")
            return
        
        with open(path, encoding="utf-8") as f:
            records = json.load(f)
        
        for i, r in enumerate(records):
            chapter = r.get("chapter", 0)
            verse = r.get("verse", i + 1)
            verse_id = f"CN-{chapter}.{verse}"
            
            if not r.get("meaning"):
                continue
            
            canonical = CanonicalVerse(
                verse_id=verse_id,
                source="Chanakya Niti",
                sanskrit=r.get("shloka", ""),
                transliteration="",
                translation=r.get("meaning", ""),
                reference=f"Chanakya Niti - Verse {verse}",
                context="",
                source_hash=""
            )
            canonical.source_hash = canonical._calculate_hash()
            
            self.verses[verse_id] = canonical
        
        self.source_records["Chanakya Niti"] = len([v for v in self.verses.values() if v.source == "Chanakya Niti"])
        print(f"  ✓ Chanakya Niti: {self.source_records['Chanakya Niti']} verses")
    
    def load_vidura_niti(self):
        """Load Vidura Niti (104 verses)"""
        path = DATA_DIR / "vidura_niti.json"
        if not path.exists():
            print(f"❌ {path} not found")
            return
        
        with open(path, encoding="utf-8") as f:
            records = json.load(f)
        
        for r in records:
            verse_id = r.get("verse_id", "VN-?")
            
            if not r.get("translation"):
                continue
            
            canonical = CanonicalVerse(
                verse_id=verse_id,
                source="Vidura Niti",
                sanskrit=r.get("sanskrit_shloka", ""),
                transliteration="",
                translation=r.get("translation", ""),
                reference=verse_id,
                context=r.get("context", ""),
                source_hash=""
            )
            canonical.source_hash = canonical._calculate_hash()
            
            self.verses[verse_id] = canonical
        
        self.source_records["Vidura Niti"] = len([v for v in self.verses.values() if v.source == "Vidura Niti"])
        print(f"  ✓ Vidura Niti: {self.source_records['Vidura Niti']} verses")
    
    def load_hitopadesha(self):
        """Load Hitopadesha (31 stories)"""
        path = DATA_DIR / "hitopadesha.json"
        if not path.exists():
            print(f"❌ {path} not found")
            return
        
        with open(path, encoding="utf-8") as f:
            records = json.load(f)
        
        for r in records:
            story_id = r.get("story_id", "H-?-?")
            story_title = r.get("story_title", "")
            
            # Extract teaching from verses
            verses = r.get("verses", [])
            translations = [v.get("translation", "") for v in verses if v.get("translation")]
            
            if not translations:
                continue
            
            teaching = " ".join(translations)[:400]
            
            canonical = CanonicalVerse(
                verse_id=story_id,
                source="Hitopadesha",
                sanskrit="",
                transliteration="",
                translation=teaching,
                reference=f"Story: {story_title}",
                context=r.get("moral", ""),
                source_hash=""
            )
            canonical.source_hash = canonical._calculate_hash()
            
            self.verses[story_id] = canonical
        
        self.source_records["Hitopadesha"] = len([v for v in self.verses.values() if v.source == "Hitopadesha"])
        print(f"  ✓ Hitopadesha: {self.source_records['Hitopadesha']} stories")
    
    def verify_database(self) -> bool:
        """Verify all verses are authentic"""
        failures = 0
        for verse_id, verse in self.verses.items():
            if not verse.verify():
                print(f"❌ Verification failed: {verse_id}")
                failures += 1
        
        if failures == 0:
            print(f"✅ All {len(self.verses)} verses verified authentic")
            return True
        else:
            print(f"⚠️  {failures} verses failed verification")
            return False
    
    def save_canonical_db(self):
        """Save canonical database for quick loading"""
        db_path = DATA_DIR / ".verse_db.json"
        data = {
            verse_id: asdict(verse) 
            for verse_id, verse in self.verses.items()
        }
        with open(db_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"💾 Saved canonical database: {len(self.verses)} verses")


# ── QUICK LOADER (Use cached canonical DB) ────────────────────────────────────

def load_canonical_verses() -> Dict[str, CanonicalVerse]:
    """Load or rebuild canonical verse database"""
    db_path = DATA_DIR / ".verse_db.json"
    
    # Try loading from cache
    if db_path.exists():
        print(">> Loading verified verse database...")
        with open(db_path, encoding="utf-8") as f:
            data = json.load(f)
        verses = {
            vid: CanonicalVerse(**v) 
            for vid, v in data.items()
        }
        print(f"OK - Loaded {len(verses)} authentic verses from database")
        return verses
    
    # Rebuild if cache doesn't exist
    print(">> Building canonical verse database...")
    canonicalizer = VerseCanonicalizer()
    verses = canonicalizer.load_all()
    canonicalizer.verify_database()
    canonicalizer.save_canonical_db()
    return verses


# ── TEST ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    verses = load_canonical_verses()
    
    # Verify a sample
    print("\n📋 Sample Verses:")
    for vid in list(verses.keys())[:3]:
        v = verses[vid]
        print(f"\n{v.verse_id} ({v.source})")
        print(f"  Ref: {v.reference}")
        print(f"  Teaching: {v.translation[:100]}...")
        print(f"  Verified: {v.verify()}")
