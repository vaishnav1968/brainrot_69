from flask import Flask, request, jsonify
from flask_cors import CORS 
import string

slang_dict = {
    "rizz": "charm ",
    "rizzler":"person with flirting ability",
    "rizzed":"charmed",
    "gyatt": "ass",
    "sigma": "lone wolf",
    "alpha": "a powerful and dominant",
    "jojo siwa": "a goddess or their mother",
    "moggers": "good looking",
    "skibidi": "chaotic ",
    "💜": "(notting)",
    "demure": "not very cute or mindful",
    "erm…ackshually": "the thing is",
    "cope": "deal with it",
    "af": "as fuck",
    "asf": "as fuck",
    "aura": "energy",
    "based": "agree with ",
    "basic": "mainstream products",
    "bde": "big dick energy",
    "bestie": "best friend",
    "bet": " it’s on",
    "bbl": "brazilian butt lift",
    "blud": " bro",
    "boujee": " luxurious",
    "bop": "excessively flirty",
    "bruh": "disappointed",
    "bussin": "excellent ",
    "cap": "lie",
    "clapback": "swift and witty response",
    "cook": "do it",
    "cooked":"done for",
    "cooking": "performing well",
    "ded": "extremely humorous ",
    "delusionship": "imaginary relationship",
    "delulu": "delusional",
    "drip": "trendy fashion",
    "fire": "impressive",
    "fina": "I’m going to",
    "fam": " friends",
    "gagged": "at a loss for words",
    "ghost": "ending communication without warning",
    "ghosted":"ignored",
    "girlboss": "female in a male-dominated field",
    "glaze": "over-praise",
    "glazing":"over-hyping",
    "glow up": "improvement in appearance",
    "glow down": "decline in appearance",
    "goat": "greatest of all time",
    "gucci": "fashionable",
    "ick": "sudden disgust ",
    "iykyk": "if you know, you know",
    "jit": "insult against inexperienced",
    "karen": "obnoxious  woman",
    "lit": "remarkable",
    "looksmaxing": "trying to look good",
    "mewing": "improving jawline",
    "mid": "average",
    "mogging": "more attractive than",
    "mogged": "getting disrespected",
    "npc": "awkward person",
    "nyaa": "evoking cuteness",
    "ohio": "strange",
    "sheesh": "surprising",
    "sksksk": "laughter",
    "slaying": "doing well",
    "sus": "suspicious",
    "tweaking": "acting strange",
    "valid": "socially acceptable",
    "uwu": "appearing cute",
    "w": "win",
    "l": "loss",
    "yap": "talk too much "
}

phrase_rules = {
    "npc rizz":"awkward flirting",
    "big yikes": "embarrassing",
    "fanum tax": "your friend taking 20% of your food",
    "has l rizz":"is bad  at flirting",
    "ipad kid": "a kid who spends most of their time staring at a screen",
    "has w rizz":"is good at flirting",
    "certified rizzologist":"master at flirting",
    "rizz machine":"smooth flirting",
     "main character": "center of attention",
    "got fannum taxed":"food eaten without permission",
    "kaicenat rizz":"chaotic charm",
    "caught in 4k": "caught with evidence",
    "skibidi toilet rizz":"flirting in absurd way",
    "was skibidi":"was cool",
    "so skibidi":"dumb",
    "hits different": "something feels better",
    "you didn’t thank beyonce": "a reminder to thank ",
    "pick me": "seeking validation",
    "vibe check": "checking personality or attitude",
    "red flag": "toxic characteristics",
    "green flag": "good person or positive traits",
    "skibidi rizz":"dumb charm",
    "you bet":"absolutly",
    "baby gronk": "eleven years old, greatest athlete",
    "big back": "overweight",
    "sussy baka": "suspicious idiot",
    "skill issue": "lack of ability",
    "touch grass": "go outside",
    "was a bop":"good song",
    "capping":"lying",
    "fit check": "checking an outfit",
    "so ick":"so disgusting",
    "no cap": "not lying",
    "unspoken Rizz":"effortless charm",
    "god-tier rizz":"top-notch charm",
    "was ick":"was disgusted",
    "was lit":"was amazing",
    "so ded":"was laughing",
    "understood the assignment": "got what to be done",
    "was ghosted":"was suddenly ignored",
    "sigma move":"independent move",
    "sigma energy":"self-relaince",
    "watch me cook": "am going to do incredible",
    "bussin food": "delicious food",   
    "rizzing up": "flirting with",     
    "mogging others": "looking superior to others", 
    "cooking up a storm": "doing something impressive",  
    "lit party": "amazing party",
    "a big back": "is fat"
}




def translate_slang(sentence, slang_dict, phrase_rules):
 
    for phrase, translation in phrase_rules.items():
        if phrase in sentence.lower():  
            sentence = sentence.lower().replace(phrase, translation)

    
    words = sentence.split()
    translated_words = []

    for word in words:
        # Remove punctuation for dictionary lookup
        cleaned_word = word.lower().strip(string.punctuation)

        
        translated_word = slang_dict.get(cleaned_word, word) 

     
        if word[-1] in string.punctuation:
            translated_word += word[-1]

        translated_words.append(translated_word)

    return ' '.join(translated_words)



app = Flask(__name__)
CORS(app) 
@app.route('/translate', methods=['POST','OPTIONS'])
def translate():
    if request.method == 'OPTIONS':
        # Handle CORS preflight request
        response = jsonify({"message": "OK"})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response

    if request.method == 'POST':
        try:
            data = request.get_json()  # Get JSON from the request body
            text = data.get('text', '')

            # Call the translation function
            translated_text = translate_slang(text)

            # Send the translation as a response
            return jsonify({'translation': translated_text})

        except Exception as e:
            return jsonify({'error': str(e)}), 400
    
# Run the app
if __name__ == "__main__":
    app.run(debug=True)
