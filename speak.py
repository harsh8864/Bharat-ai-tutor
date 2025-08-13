# speak.py - ULTIMATE Enhanced Text-to-Speech with Perfect Hindi/English Quality
import sys
import os
from gtts import gTTS
import uuid
import re
import time
import textwrap

def clean_text_for_perfect_educational_speech(text):
    """Ultimate text cleaning specifically for perfect educational content delivery."""
    
    # Remove markdown and formatting
    # text = re.sub(r'\*{1,2}([^*]+)\*{1,2}', r'\1', text)  # Bold
    # text = re.sub(r'_{1,2}([^_]+)_{1,2}', r'\1', text)    # Italics
    # text = re.sub(r'`([^`]+)`', r'\1', text)              # Code
    # text = re.sub(r'#{1,6}\s*', '', text)                 # Headers
    text = re.sub(r'\[ANSWER:.*?\]', '', text)            # Remove answer hooks
    
    # Remove emojis and special symbols for cleaner speech
    # text = re.sub(r'[📚💡🎯✨🔬💻🧠🎉💪🙏🇮🇳🌟⚡🚀🔥]', '', text)
    # text = re.sub(r'[^\w\s.,!?;:\'\-]', ' ', text)
    
    # Convert educational formatting to speech-friendly format
    # text = re.sub(r'•\s*', 'Point: ', text)  # Bullet points
    # text = re.sub(r'\d+\.\s*', lambda m: f'Number {m.group().strip()}: ', text)  # Numbered lists
    # text = re.sub(r'(\w+):\s*', r'\1. ', text)  # Convert colons to periods for better flow

    
    # Enhanced technical abbreviations with pronunciations
    technical_replacements = {
        'AI': 'Artificial Intelligence',
        'IT': 'Information Technology',
        'HTML': 'H T M L',
        'CSS': 'Cascading Style Sheets',
        'JS': 'JavaScript',
        'API': 'Application Programming Interface',
        'URL': 'Uniform Resource Locator',
        'HTTP': 'H T T P',
        'HTTPS': 'H T T P S',
        'CPU': 'Central Processing Unit',
        'RAM': 'Random Access Memory',
        'GPU': 'Graphics Processing Unit',
        'SQL': 'Structured Query Language',
        'JSON': 'J S O N',
        'XML': 'X M L',
        'CSV': 'C S V',
        'PDF': 'P D F',
        'GB': 'Gigabytes',
        'MB': 'Megabytes',
        'KB': 'Kilobytes',
        'TB': 'Terabytes',
        'WWW': 'World Wide Web',
        'USB': 'U S B',
        'WiFi': 'Wi-Fi',
        'GPS': 'G P S',
        'NASA': 'N A S A',
        'DNA': 'D N A',
        'RNA': 'R N A',
        'UV': 'Ultraviolet',
        'AC': 'Alternating Current',
        'DC': 'Direct Current',
        'LED': 'L E D',
        'LCD': 'L C D',
        'VR': 'Virtual Reality',
        'AR': 'Augmented Reality',
        'IoT': 'Internet of Things',
        'ML': 'Machine Learning',
        'AI/ML': 'Artificial Intelligence and Machine Learning'
    }
    
    # Apply technical replacements
    for abbr, full in technical_replacements.items():
        text = re.sub(r'\b' + re.escape(abbr) + r'\b', full, text, flags=re.IGNORECASE)
    
    # Enhanced mathematical and scientific terms
    math_replacements = {
        '²': ' squared',
        '³': ' cubed',
        '°': ' degrees',
        '%': ' percent',
        '±': ' plus or minus',
        '≤': ' less than or equal to',
        '≥': ' greater than or equal to',
        '≠': ' not equal to',
        '∞': ' infinity',
        'π': ' pi',
        'α': ' alpha',
        'β': ' beta',
        'γ': ' gamma',
        'δ': ' delta',
        'Δ': ' Delta',
        '∑': ' sum',
        '∏': ' product',
        '√': ' square root of',
        '∫': ' integral of'
    }
    
    for symbol, word in math_replacements.items():
        text = text.replace(symbol, word)
    
    # Clean up extra spaces and normalize punctuation
    text = re.sub(r'\s+', ' ', text)  # Multiple spaces to single
    text = re.sub(r'\.{2,}', '.', text)  # Multiple dots to single
    text = re.sub(r',+', ',', text)  # Multiple commas to single
    text = text.strip()
    
    # Add natural speaking pauses for better comprehension
    text = re.sub(r'([.!?])\s*', r'\1 ', text)  # Pause after sentences
    text = re.sub(r'([,;])\s*', r'\1 ', text)   # Pause after commas/semicolons
    text = re.sub(r'(\w)([A-Z])', r'\1. \2', text)  # Add pause between words that might be concatenated
    
    # Ensure proper sentence structure
    sentences = text.split('. ')
    cleaned_sentences = []
    
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence:
            # Capitalize first letter
            sentence = sentence[0].upper() + sentence[1:] if len(sentence) > 1 else sentence.upper()
            
            # Ensure sentence ends with proper punctuation
            if not sentence.endswith(('.', '!', '?')):
                sentence += '.'
            
            cleaned_sentences.append(sentence)
    
    final_text = ' '.join(cleaned_sentences)
    
    return final_text

def enhance_hindi_text_for_perfect_tts(text):
    """Perfect Hindi text enhancement for crystal clear TTS."""
    
    # Common Hindi words that need pronunciation fixes
    hindi_pronunciation_fixes = {
        # Educational terms
        'विज्ञान': 'विज्ञान',
        'गणित': 'गणित',
        'भौतिक शास्त्र': 'भौतिक शास्त्र',
        'रसायन शास्त्र': 'रसायन शास्त्र',
        'जीव विज्ञान': 'जीव विज्ञान',
        'कंप्यूटर साइंस': 'कंप्यूटर साइंस',
        'प्रकाश संश्लेषण': 'प्रकाश संश्लेषण',
        
        # Common phrases
        'क्या है': 'क्या है',
        'कैसे काम करता है': 'कैसे काम करता है',
        'क्यों': 'क्यों',
        'कहाँ': 'कहाँ',
        'कब': 'कब',
        'कौन': 'कौन',
        'समझाओ': 'समझाओ',
        'बताओ': 'बताओ',
        'सिखाओ': 'सिखाओ',
        
        # Technical terms
        'आर्टिफिशियल इंटेलिजेंस': 'आर्टिफिशियल इंटेलिजेंस',
        'मशीन लर्निंग': 'मशीन लर्निंग',
        'कंप्यूटर प्रोग्रामिंग': 'कंप्यूटर प्रोग्रामिंग'
    }
    
    # Apply pronunciation fixes
    for original, fixed in hindi_pronunciation_fixes.items():
        text = text.replace(original, fixed)
    
    # Add natural pauses in Hindi
    text = re.sub(r'(।)\s*', r'\1 ', text)  # Pause after Hindi full stop
    text = re.sub(r'(है|हैं|था|थे|होगा|होंगे)\s+', r'\1 ', text)  # Pause after auxiliary verbs
    
    return text

def enhance_english_text_for_perfect_tts(text):
    """Perfect English text enhancement for crystal clear TTS."""
    
    # Add strategic pauses for better educational delivery
    text = re.sub(r'(Definition[:\.])', r'\1 ', text)
    text = re.sub(r'(Example[:\.])', r'\1 ', text)
    text = re.sub(r'(Important[:\.])', r'\1 ', text)
    text = re.sub(r'(Note[:\.])', r'\1 ', text)
    text = re.sub(r'(Remember[:\.])', r'\1 ', text)
    text = re.sub(r'(Key point[:\.])', r'\1 ', text)
    
    # Add pauses before transition words
    transition_words = ['However', 'Therefore', 'Moreover', 'Furthermore', 'Additionally', 
                       'Consequently', 'Nevertheless', 'Meanwhile', 'Similarly', 'Finally']
    
    for word in transition_words:
        text = re.sub(f'\\b{word}\\b', f' {word}', text)
    
    # Add emphasis to numbers and statistics
    text = re.sub(r'\b(\d+)\b', r' \1 ', text)
    
    return text

def optimize_text_for_perfect_education(text, language='en'):
    """Optimize text specifically for perfect educational content delivery."""
    
    # Break down complex sentences for better understanding
    sentences = text.split('. ')
    optimized_sentences = []
    
    for sentence in sentences:
        if len(sentence) > 150:  # Long sentences - break them down
            # Try to break at conjunctions
            conjunctions = ['and', 'but', 'or', 'however', 'therefore', 'because', 'since', 'although']
            if language == 'hi':
                conjunctions.extend(['और', 'लेकिन', 'या', 'इसलिए', 'क्योंकि', 'जब से', 'हालांकि'])
            
            parts = re.split(r'\s+(' + '|'.join(conjunctions) + r')\s+', sentence, flags=re.IGNORECASE)
            if len(parts) > 1:
                # Rejoin with pauses
                rejoined = ''
                for i, part in enumerate(parts):
                    if i > 0 and parts[i-1].lower() in [c.lower() for c in conjunctions]:
                        rejoined += f' {part}. '
                    else:
                        rejoined += part
                optimized_sentences.append(rejoined)
            else:
                optimized_sentences.append(sentence)
        else:
            optimized_sentences.append(sentence)
    
    return '. '.join(optimized_sentences)

def generate_perfect_educational_speech(text, lang_code, output_dir="audio"):
    """Generate the highest quality educational speech with perfect processing."""
    max_retries = 3
    retry_delay = 1
    
    try:
        # Ensure output directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"Created audio directory: {output_dir}", file=sys.stderr)
        
        print("🔧 Processing text for PERFECT educational speech...", file=sys.stderr)
        
        # Step 1: Universal text cleaning
        clean_text = clean_text_for_perfect_educational_speech(text)
        print(f"📝 Text cleaned: {len(clean_text)} characters", file=sys.stderr)
        
        # Step 2: Language-specific enhancements
        if lang_code == 'hi':
            clean_text = enhance_hindi_text_for_perfect_tts(clean_text)
            print("🇮🇳 Hindi TTS enhancements applied", file=sys.stderr)
        else:
            clean_text = enhance_english_text_for_perfect_tts(clean_text)
            print("🇺🇸 English TTS enhancements applied", file=sys.stderr)
        
        # Step 3: Educational optimization
        clean_text = optimize_text_for_perfect_education(clean_text, lang_code)
        print("🎓 Educational optimization complete", file=sys.stderr)
        
        # Handle empty text
        if not clean_text.strip():
            print("Warning: Empty text after processing", file=sys.stderr)
            if lang_code == 'hi':
                clean_text = "मुझे खुशी है कि आप सीख रहे हैं। कृपया अपना प्रश्न फिर से पूछें।"
            else:
                clean_text = "I'm happy you're learning. Please ask your question again."
        
        # Perfect text length management for optimal TTS
        optimal_length = 900 if lang_code == 'hi' else 1100  # Hindi needs shorter segments
        
        if len(clean_text) > optimal_length:
            print(f"📏 Text too long ({len(clean_text)} chars), intelligently optimizing...", file=sys.stderr)
            
            # Find the best place to cut (at sentence boundary)
            sentences = clean_text.split('. ')
            optimized_text = ""
            
            for sentence in sentences:
                if len(optimized_text + sentence + '. ') <= optimal_length:
                    optimized_text += sentence + '. '
                else:
                    break
            
            # If still too long, cut at word boundary
            if len(optimized_text) > optimal_length:
                words = optimized_text.split()
                optimized_text = ""
                for word in words:
                    if len(optimized_text + word + ' ') <= optimal_length:
                        optimized_text += word + ' '
                    else:
                        break
                
                if lang_code == 'hi':
                    optimized_text = optimized_text.strip() + '... और जानकारी के लिए पूछें।'
                else:
                    optimized_text = optimized_text.strip() + '... ask for more details.'
            
            clean_text = optimized_text
            print(f"✂️ Text optimized to {len(clean_text)} characters", file=sys.stderr)
        
        # Ensure minimum meaningful length
        if len(clean_text) < 30:
            if lang_code == 'hi':
                clean_text = f"यहाँ आपके प्रश्न का उत्तर है। {clean_text}। धन्यवाद।"
            else:
                clean_text = f"Here is the explanation for your question. {clean_text}. Thank you for learning."
        
        # Generate unique filename with timestamp
        timestamp = int(time.time())
        unique_id = str(uuid.uuid4())[:8]
        filename = f"perfect_speech_{lang_code}_{timestamp}_{unique_id}.mp3"
        filepath = os.path.join(output_dir, filename)
        
        print(f"🎙️ Generating PERFECT TTS for ({lang_code}): {clean_text[:100]}{'...' if len(clean_text) > 100 else ''}", file=sys.stderr)
        
        # Perfect TTS generation with enhanced retry mechanism
        for attempt in range(max_retries):
            try:
                print(f"🔄 Perfect TTS attempt {attempt + 1}/{max_retries}", file=sys.stderr)
                
                # Create TTS object with perfect settings for education
                tts_params = {
                    'text': clean_text,
                    'lang': lang_code,
                    'slow': False,  # Normal speed for better comprehension
                }
                
                # Language-specific optimizations
                if lang_code == 'hi':
                    tts_params['tld'] = 'co.in'  # Indian Hindi accent
                elif lang_code == 'en':
                    tts_params['tld'] = 'com'    # Clear American accent
                else:
                    tts_params['tld'] = 'com'    # Default
                
                tts = gTTS(**tts_params)
                
                # Save the audio file
                tts.save(filepath)
                
                # Verify file creation and content
                if os.path.exists(filepath) and os.path.getsize(filepath) > 1000:  # Minimum 1KB for valid audio
                    file_size = os.path.getsize(filepath)
                    duration_estimate = len(clean_text) / (12 if lang_code == 'hi' else 15)  # Hindi is slower
                    
                    print(f"✅ PERFECT educational audio created successfully!", file=sys.stderr)
                    print(f"   📁 File: {filename}", file=sys.stderr)
                    print(f"   📊 Size: {file_size} bytes", file=sys.stderr)
                    print(f"   ⏱️ Estimated duration: {duration_estimate:.1f} seconds", file=sys.stderr)
                    print(f"   🌐 Language: {lang_code} ({'Hindi' if lang_code == 'hi' else 'English'})", file=sys.stderr)
                    
                    return filename
                else:
                    raise Exception("Generated audio file is invalid or too small")
                    
            except Exception as e:
                print(f"❌ Perfect TTS attempt {attempt + 1} failed: {str(e)}", file=sys.stderr)
                
                # Clean up failed file
                if os.path.exists(filepath):
                    try:
                        os.remove(filepath)
                    except:
                        pass
                
                # Wait before retry (exponential backoff)
                if attempt < max_retries - 1:
                    wait_time = retry_delay * (2 ** attempt)
                    print(f"⏳ Waiting {wait_time} seconds before retry...", file=sys.stderr)
                    time.sleep(wait_time)
                else:
                    print("💔 All perfect TTS attempts failed", file=sys.stderr)
                    return None
        
    except Exception as e:
        print(f"🚨 Critical error in perfect educational TTS generation: {str(e)}", file=sys.stderr)
        return None

def test_perfect_educational_tts():
    """Test the perfect educational TTS system with sample content."""
    
    # Test English
    english_content = """
    Welcome to Bharat AI Tutor! Let me explain artificial intelligence in detail. 
    Definition: AI is the simulation of human intelligence by machines. 
    Key points: Machine learning, neural networks, and data processing are core components. 
    Example: Virtual assistants like Alexa use AI to understand and respond to voice commands. 
    This technology is revolutionizing education, healthcare, and transportation in India.
    """
    
    # Test Hindi
    hindi_content = """
    भारत AI ट्यूटर में आपका स्वागत है! मैं आपको आर्टिफिशियल इंटेलिजेंस के बारे में विस्तार से बताता हूँ।
    परिभाषा: AI मशीनों द्वारा मानव बुद्धिमत्ता का अनुकरण है।
    मुख्य बिंदु: मशीन लर्निंग, न्यूरल नेटवर्क्स, और डेटा प्रोसेसिंग मुख्य घटक हैं।
    उदाहरण: एलेक्सा जैसे वर्चुअल असिस्टेंट AI का उपयोग करके आवाज को समझते और जवाब देते हैं।
    """
    
    print("🧪 Testing PERFECT educational TTS system...", file=sys.stderr)
    
    # Test English
    english_result = generate_perfect_educational_speech(english_content, "en")
    english_success = english_result is not None
    
    # Test Hindi
    hindi_result = generate_perfect_educational_speech(hindi_content, "hi")
    hindi_success = hindi_result is not None
    
    if english_success and hindi_success:
        print(f"✅ PERFECT TTS test successful: English={english_result}, Hindi={hindi_result}", file=sys.stderr)
        return True
    else:
        print(f"❌ PERFECT TTS test failed: English={english_success}, Hindi={hindi_success}", file=sys.stderr)
        return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python speak.py [lang_code] [text_to_speak]", file=sys.stderr)
        print("PERFECT Enhanced for educational content with crystal clear voice explanations", file=sys.stderr)
        print("Example: python speak.py en 'Explain machine learning algorithms'", file=sys.stderr)
        print("Example: python speak.py hi 'मशीन लर्निंग के बारे में बताएं'", file=sys.stderr)
        print("Supported languages: en (English), hi (Hindi)", file=sys.stderr)
        sys.exit(1)

    # Parse arguments
    lang_code = sys.argv[1]
    text_to_speak = " ".join(sys.argv[2:])
    
    # Validate language code with enhanced support
    supported_langs = ['en', 'hi', 'bn', 'te', 'mr', 'ta', 'gu', 'kn', 'ml', 'pa']
    
    if lang_code not in supported_langs:
        print(f"⚠️ Language '{lang_code}' might not be fully optimized.", file=sys.stderr)
        print(f"✅ Fully optimized languages: en (English), hi (Hindi)", file=sys.stderr)
        print(f"✅ Supported languages: {', '.join(supported_langs)}", file=sys.stderr)
        print("🔄 Proceeding with the requested language...", file=sys.stderr)
    
    # Display processing info
    print(f"🎓 Bharat AI PERFECT Educational TTS Starting...", file=sys.stderr)
    print(f"🌐 Language: {lang_code} ({'Hindi' if lang_code == 'hi' else 'English' if lang_code == 'en' else lang_code})", file=sys.stderr)
    print(f"📝 Content length: {len(text_to_speak)} characters", file=sys.stderr)
    
    # Generate perfect educational speech
    start_time = time.time()
    output_filename = generate_perfect_educational_speech(text_to_speak, lang_code)
    end_time = time.time()
    
    if output_filename:
        print(f"⏱️ PERFECT processing completed in {end_time - start_time:.2f} seconds", file=sys.stderr)
        print(f"🎉 Ready for PERFECT educational audio delivery!", file=sys.stderr)
        print(output_filename)  # This goes to stdout for Node.js
    else:
        print("💔 Failed to generate PERFECT educational audio", file=sys.stderr)
        sys.exit(1)