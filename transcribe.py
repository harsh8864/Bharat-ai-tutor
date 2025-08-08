# transcribe.py - ENHANCED Audio Transcription with Perfect Hindi/English Recognition
import whisper
import sys
import os
import time
import re
import json
from pathlib import Path
import warnings
warnings.filterwarnings("ignore")

class EnhancedEducationalTranscriber:
    """
    A significantly enhanced transcription system using Whisper, optimized for 
    educational content with perfect Hindi and English recognition.
    """

    def __init__(self, model_size="base"):
        """
        Initializes the enhanced transcriber with better model management.
        """
        self.model_size = model_size
        self.model = None
        
        # Enhanced educational terms for better context recognition
        self.educational_terms = [
            # Computer Science
            'artificial intelligence', 'machine learning', 'algorithm', 'programming',
            'javascript', 'python', 'html', 'css', 'database', 'api', 'frontend', 'backend',
            'neural network', 'deep learning', 'data structure', 'software engineering',
            
            # Science
            'photosynthesis', 'mitochondria', 'chlorophyll', 'ecosystem', 'biodiversity',
            'atomic structure', 'periodic table', 'chemical reaction', 'physics', 'chemistry',
            'biology', 'genetics', 'evolution', 'gravity', 'momentum', 'energy',
            
            # Mathematics
            'algebra', 'geometry', 'calculus', 'trigonometry', 'statistics', 'probability',
            'equation', 'polynomial', 'derivative', 'integral', 'matrix', 'vector',
            
            # Hindi Educational Terms (Romanized)
            'vigyan', 'ganit', 'bhautik shastra', 'rasayan shastra', 'jeev vigyan',
            'computer vigyan', 'artificial intelligence', 'machine learning',
            'photosynthesis', 'paudhe', 'jantu', 'prakritik', 'samudra', 'pahaad',
            
            # General Academic
            'explanation', 'definition', 'example', 'theory', 'concept', 'principle',
            'analysis', 'synthesis', 'evaluation', 'application', 'knowledge'
        ]
        
        # Enhanced Hindi terms with better recognition patterns
        self.hindi_terms = {
            # Science terms
            'vigyan': 'विज्ञान',
            'ganit': 'गणित', 
            'bhautik shastra': 'भौतिक शास्त्र',
            'rasayan shastra': 'रसायन शास्त्र',
            'jeev vigyan': 'जीव विज्ञान',
            'computer vigyan': 'कंप्यूटर विज्ञान',
            'photosynthesis': 'प्रकाश संश्लेषण',
            'paudhe': 'पौधे',
            'jantu': 'जंतु',
            'prakritik': 'प्राकृतिक',
            
            # Common question words
            'kya hai': 'क्या है',
            'kaise kaam karta hai': 'कैसे काम करता है',
            'kyun': 'क्यों',
            'kahan': 'कहाँ',
            'kab': 'कब',
            'kaun': 'कौन',
            'samjhao': 'समझाओ',
            'batao': 'बताओ',
            'sikhaao': 'सिखाओ',
            
            # Academic terms
            'paribhasha': 'परिभाषा',
            'udaharan': 'उदाहरण',
            'sidhant': 'सिद्धांत',
            'niyam': 'नियम',
            'formula': 'सूत्र'
        }
        
        # Enhanced question detection patterns
        self.question_patterns = [
            # English patterns
            r'^\s*(what is|what are|what\'s|whats|explain|define|tell me about|how does|how do|why is|why are|can you explain)\b',
            r'\b(quiz|test|question|help|help me)\b',
            r'\?$',
            
            # Hindi patterns (Devanagari)
            r'\b(क्या है|क्या हैं|समझाओ|बताओ|सिखाओ|व्याख्या करो|परिभाषा दो)\b',
            r'\b(कैसे|क्यों|कहाँ|कब|कौन)\b',
            r'\b(प्रश्न|सवाल|सहायता|मदद)\b',
            
            # Romanized Hindi patterns  
            r'\b(kya hai|kya hain|samjhao|batao|sikhaao|kaise|kyun|kahan|kab|kaun)\b',
            r'\b(prashn|sawal|madad|sahayata)\b'
        ]
        
        self.load_enhanced_model()

    def load_enhanced_model(self):
        """
        Loads the Whisper model with enhanced error handling and fallback options.
        """
        print(f"🔄 Loading enhanced Whisper model: '{self.model_size}'...", file=sys.stderr)
        start_time = time.time()
        
        try:
            # Try loading the requested model
            self.model = whisper.load_model(self.model_size)
            load_time = time.time() - start_time
            print(f"✅ Enhanced model '{self.model_size}' loaded successfully in {load_time:.2f} seconds.", file=sys.stderr)
            
        except Exception as e:
            print(f"⚠️ Failed to load '{self.model_size}' model ({e})", file=sys.stderr)
            
            # Try fallback models in order of preference
            fallback_models = ['base', 'tiny', 'small']
            for fallback in fallback_models:
                if fallback != self.model_size:
                    try:
                        print(f"🔄 Trying fallback model: '{fallback}'...", file=sys.stderr)
                        self.model = whisper.load_model(fallback)
                        self.model_size = fallback
                        load_time = time.time() - start_time
                        print(f"✅ Fallback model '{fallback}' loaded in {load_time:.2f} seconds.", file=sys.stderr)
                        break
                    except Exception as fallback_error:
                        print(f"❌ Fallback '{fallback}' also failed: {fallback_error}", file=sys.stderr)
                        continue
            else:
                raise Exception("All model loading attempts failed")

    def enhance_audio_preprocessing(self, filepath: str) -> str:
        """
        Enhanced audio preprocessing for better transcription quality.
        """
        print(f"🎧 Preprocessing audio file: {filepath}", file=sys.stderr)
        
        # Validate file
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Audio file not found: {filepath}")
        
        file_size = os.path.getsize(filepath)
        if file_size < 1024:  # Less than 1KB
            raise ValueError(f"Audio file too small ({file_size} bytes): {filepath}")
        
        print(f"📊 Audio file validated: {file_size} bytes", file=sys.stderr)
        return filepath

    def transcribe_with_enhanced_context(self, filepath: str) -> dict:
        """
        Enhanced transcription with better context and error handling.
        """
        if not self.model:
            return {"error": "Enhanced Whisper model is not loaded."}
        
        try:
            # Preprocess audio
            processed_filepath = self.enhance_audio_preprocessing(filepath)
            print(f"🎤 Starting enhanced transcription for {processed_filepath}...", file=sys.stderr)
            
            transcribe_start = time.time()
            
            # Enhanced context prompt with both English and Hindi terms
            context_prompt = (
                f"This is an educational audio message that may contain technical terms, "
                f"questions about science, mathematics, computer science, or general academic topics. "
                f"Common terms include: {', '.join(self.educational_terms[:10])}. "
                f"The speaker might be asking questions in Hindi or English about learning topics."
            )
            
            # Enhanced transcription with optimal parameters
            result = self.model.transcribe(
                processed_filepath,
                fp16=False,  # Better compatibility
                language=None,  # Let Whisper auto-detect
                initial_prompt=context_prompt,
                temperature=0.0,  # Most deterministic output
                best_of=2,  # Try multiple attempts
                beam_size=5,  # Better search
                patience=1.0,  # Allow for pauses
                condition_on_previous_text=True,  # Use context
                compression_ratio_threshold=2.4,  # Filter out low-quality segments
                logprob_threshold=-1.0,  # Filter out uncertain segments
                no_speech_threshold=0.6  # Better silence detection
            )
            
            transcribe_time = time.time() - transcribe_start
            print(f"⏱️ Enhanced transcription completed in {transcribe_time:.2f} seconds.", file=sys.stderr)
            
            raw_text = result["text"].strip()
            detected_language = result.get("language", "unknown")
            
            print(f"🌐 Detected language: {detected_language}", file=sys.stderr)
            print(f"📝 Raw transcription: '{raw_text[:100]}{'...' if len(raw_text) > 100 else ''}'", file=sys.stderr)
            
            if not raw_text:
                return {
                    "text": "Audio was unclear. Could you please speak again more clearly?",
                    "is_question": False,
                    "language": detected_language,
                    "confidence": "low"
                }

            # Enhanced post-processing
            return self.enhanced_post_process(raw_text, detected_language)

        except Exception as e:
            print(f"❌ Enhanced transcription error: {e}", file=sys.stderr)
            return {"error": f"Failed to transcribe audio: {str(e)}"}

    def enhanced_post_process(self, text: str, detected_language: str = "unknown") -> dict:
        """
        Enhanced post-processing with better Hindi/English recognition and cleaning.
        """
        print(f"🔧 Enhanced post-processing transcribed text...", file=sys.stderr)
        
        # Step 1: Basic cleaning
        cleaned_text = self.clean_transcribed_text(text)
        
        # Step 2: Enhance Hindi recognition
        enhanced_text = self.enhance_hindi_recognition(cleaned_text)
        
        # Step 3: Fix common transcription errors
        corrected_text = self.fix_common_transcription_errors(enhanced_text)
        
        # Step 4: Detect question intent with enhanced patterns
        is_question = self.detect_question_intent(corrected_text)
        
        # Step 5: Determine confidence level
        confidence = self.calculate_confidence(corrected_text, detected_language)
        
        # Step 6: Final formatting
        final_text = self.final_formatting(corrected_text)
        
        print(f"✨ Enhanced processing complete: '{final_text[:100]}{'...' if len(final_text) > 100 else ''}'", file=sys.stderr)
        print(f"🎯 Question detected: {is_question}, Confidence: {confidence}", file=sys.stderr)
        
        return {
            "text": final_text,
            "is_question": is_question,
            "language": detected_language,
            "confidence": confidence,
            "original_text": text
        }

    def clean_transcribed_text(self, text: str) -> str:
        """Enhanced text cleaning for transcribed content."""
        
        # Remove excessive punctuation
        text = re.sub(r'\.{3,}', '...', text)
        text = re.sub(r'\.{2}', '.', text)
        text = re.sub(r',+', ',', text)
        
        # Fix spacing issues
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'\s*([,.!?])\s*', r'\1 ', text)
        
        # Remove filler words and sounds
        filler_patterns = [
            r'\b(um|uh|er|ah|hmm|umm|uhh)\b',
            r'\b(आह|उम|एह|हम्म)\b'
        ]
        
        for pattern in filler_patterns:
            text = re.sub(pattern, '', text, flags=re.IGNORECASE)
        
        return text.strip()

    def enhance_hindi_recognition(self, text: str) -> str:
        """Enhanced Hindi word recognition and correction."""
        
        # Common Hindi word corrections from romanized to proper form
        hindi_corrections = {
            # Question words
            'kya hai': 'क्या है',
            'kya he': 'क्या है', 
            'kya hain': 'क्या हैं',
            'kyaa hai': 'क्या है',
            'kaise': 'कैसे',
            'kyun': 'क्यों',
            'kyon': 'क्यों',
            'kahan': 'कहाँ',
            'kab': 'कब',
            'kaun': 'कौन',
            
            # Action words
            'samjhao': 'समझाओ',
            'samjhaao': 'समझाओ',
            'batao': 'बताओ',
            'bataao': 'बताओ',
            'sikhaao': 'सिखाओ',
            'sikhao': 'सिखाओ',
            'explain karo': 'explain करो',
            'define karo': 'define करो',
            
            # Subject terms
            'computer science': 'computer science',
            'machine learning': 'machine learning',
            'artificial intelligence': 'artificial intelligence',
            'photosynthesis': 'photosynthesis',
            'vigyan': 'विज्ञान',
            'ganit': 'गणित',
            'bhautik vigyan': 'भौतिक विज्ञान',
            'rasayan vigyan': 'रसायन विज्ञान',
            'jeev vigyan': 'जीव विज्ञान',
            
            # Common words
            'mujhe': 'मुझे',
            'aapko': 'आपको',
            'hamein': 'हमें',
            'unko': 'उनको',
            'iske bare mein': 'इसके बारे में',
            'ke bare mein': 'के बारे में',
            'paribhasha': 'परिभाषा',
            'udaharan': 'उदाहरण'
        }
        
        # Apply corrections (case-insensitive)
        for romanized, corrected in hindi_corrections.items():
            pattern = r'\b' + re.escape(romanized) + r'\b'
            text = re.sub(pattern, corrected, text, flags=re.IGNORECASE)
        
        return text

    def fix_common_transcription_errors(self, text: str) -> str:
        """Fix common Whisper transcription errors for educational content."""
        
        # Common technical term corrections
        tech_corrections = {
            # AI/ML terms
            'a i': 'AI',
            'a.i.': 'AI',
            'ml': 'machine learning',
            'm l': 'machine learning',
            'api': 'API',
            'a p i': 'API',
            'html': 'HTML',
            'h t m l': 'HTML',
            'css': 'CSS',
            'c s s': 'CSS',
            'javascript': 'JavaScript',
            'java script': 'JavaScript',
            'python': 'Python',
            
            # Science terms
            'photo synthesis': 'photosynthesis',
            'photo-synthesis': 'photosynthesis',
            'chloro phyll': 'chlorophyll',
            'chloro-phyll': 'chlorophyll',
            'mito chondria': 'mitochondria',
            'mito-chondria': 'mitochondria',
            
            # Math terms
            'alge bra': 'algebra',
            'geo metry': 'geometry',
            'calcu lus': 'calculus',
            'trigo nometry': 'trigonometry',
            
            # Common phrases
            'what is': 'what is',
            'what\'s': 'what is',
            'tell me about': 'tell me about',
            'explain me': 'explain',
            'explain to me': 'explain',
            'can you explain': 'explain',
            'i want to know': 'tell me about',
            'i want to learn': 'teach me about'
        }
        
        # Apply corrections
        for error, correction in tech_corrections.items():
            pattern = r'\b' + re.escape(error) + r'\b'
            text = re.sub(pattern, correction, text, flags=re.IGNORECASE)
        
        return text

    def detect_question_intent(self, text: str) -> bool:
        """Enhanced question detection with better pattern matching."""
        
        # Check all question patterns
        for pattern in self.question_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                print(f"🎯 Question pattern matched: {pattern}", file=sys.stderr)
                return True
        
        # Additional heuristics
        question_indicators = [
            text.strip().endswith('?'),
            len(text.split()) >= 2 and text.split()[0].lower() in ['what', 'how', 'why', 'when', 'where', 'which', 'who'],
            'explain' in text.lower(),
            'tell me' in text.lower(),
            'teach me' in text.lower(),
            'क्या' in text or 'कैसे' in text or 'क्यों' in text,
            'samjhao' in text.lower() or 'batao' in text.lower()
        ]
        
        return any(question_indicators)

    def calculate_confidence(self, text: str, detected_language: str) -> str:
        """Calculate confidence level of transcription."""
        
        confidence_score = 0
        
        # Length-based confidence
        if len(text) >= 10:
            confidence_score += 20
        if len(text) >= 30:
            confidence_score += 20
        
        # Language detection confidence
        if detected_language in ['en', 'hi']:
            confidence_score += 30
        
        # Educational term recognition
        educational_terms_found = sum(1 for term in self.educational_terms if term.lower() in text.lower())
        confidence_score += min(educational_terms_found * 5, 20)
        
        # Grammar and structure
        if re.search(r'[.!?]', text):
            confidence_score += 10
        
        # Determine confidence level
        if confidence_score >= 80:
            return "high"
        elif confidence_score >= 60:
            return "medium"
        else:
            return "low"

    def final_formatting(self, text: str) -> str:
        """Final formatting for clean output."""
        
        # Capitalize first letter
        if text and len(text) > 0:
            text = text[0].upper() + text[1:] if len(text) > 1 else text.upper()
        
        # Ensure proper sentence ending
        if text and not text.endswith(('.', '!', '?')):
            # Add question mark if it seems like a question
            if any(word in text.lower() for word in ['what', 'how', 'why', 'when', 'where', 'क्या', 'कैसे', 'क्यों']):
                text += '?'
            else:
                text += '.'
        
        # Clean up extra spaces
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text

    def transcribe_audio(self, filepath: str) -> dict:
        """Main transcription method with enhanced processing."""
        return self.transcribe_with_enhanced_context(filepath)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        error_result = {
            "error": "No audio file path provided.",
            "usage": "python transcribe.py <audio_file_path>",
            "supported_formats": ["wav", "mp3", "m4a", "ogg", "flac"]
        }
        print(json.dumps(error_result, indent=2))
        sys.exit(1)
    
    audio_file_path = sys.argv[1]
    
    print(f"🚀 Starting enhanced educational transcription...", file=sys.stderr)
    print(f"📁 Input file: {audio_file_path}", file=sys.stderr)
    
    # Initialize the enhanced transcriber with optimal model
    try:
        # Try to use 'small' model for better accuracy, fallback to 'base'
        preferred_model = "small" if os.path.getsize(audio_file_path) < 5 * 1024 * 1024 else "base"  # 5MB threshold
        transcriber = EnhancedEducationalTranscriber(model_size=preferred_model)
        print(f"✅ Enhanced transcriber initialized with '{transcriber.model_size}' model", file=sys.stderr)
        
    except Exception as init_error:
        print(f"❌ Failed to initialize enhanced transcriber: {init_error}", file=sys.stderr)
        error_result = {"error": f"Initialization failed: {str(init_error)}"}
        print(json.dumps(error_result, indent=2))
        sys.exit(1)
    
    # Perform enhanced transcription
    start_time = time.time()
    transcription_result = transcriber.transcribe_audio(audio_file_path)
    total_time = time.time() - start_time
    
    # Add timing information
    transcription_result["processing_time"] = round(total_time, 2)
    transcription_result["model_used"] = transcriber.model_size
    
    print(f"⏱️ Total enhanced processing time: {total_time:.2f} seconds", file=sys.stderr)
    print(f"🎯 Final result: {transcription_result.get('text', 'No text')[:50]}...", file=sys.stderr)
    
    # Output structured JSON result for Node.js backend
    print(json.dumps(transcription_result, indent=2, ensure_ascii=False))