import genanki
from download_audio_files import get_audio_file_path

# Define the deck
deck = genanki.Deck(
    deck_id=1234567890, 
    name="MoeKani"
)

# Define the model for the flashcards
model = genanki.Model(
    model_id=1234567891, 
    name="Moekani Model",
    fields=[
        {"name": "ID"},
        {"name": "Type"},
        {"name": "Radical"},
        {"name": "Radical_Image"},
        {"name": "Radical_Name"},
        {"name": "Radical_Mnemonic"},
        {"name": "Radical_Alternative"},
        {"name": "Kanji"},
        {"name": "Kanji_Meaning"},
        {"name": "Reading_On"},
        {"name": "Reading_Kun"},
        {"name": "Radicals"},
        {"name": "Radical_Names"},
        {"name": "Kanji_Mnemonic"},
        {"name": "Kanji_Mnemonic_Bonus"},
        {"name": "Vocab"},
        {"name": "Meaning"},
        {"name": "Part_Of_Speech"},
        {"name": "Reading"},
        {"name": "Audio"},
        {"name": "Context1_en"},
        {"name": "Context1_jp"},
        {"name": "Context2_en"},
        {"name": "Context2_jp"},
        {"name": "Context3_en"},
        {"name": "Context3_jp"},
        {"name": "Meaning_Exp"},
        {"name": "Reading_Exp"},
        {"name": "Expression"}, 
        {"name": "Reading"}, 
        {"name": "Meaning"}, 
        {"name": "Audio"}, 
        {"name": "Audio on Front"}
    ],
    templates=[
        {
            "name": "Card",
            "qfmt": """
                {{#Radical}}
                    <div class="radical"><br>{{Radical}}<br><br></div>
                {{/Radical}}
                {{#Kanji}}
                    <div class="kanji"><br>{{Kanji}}<br><br></div>
                {{/Kanji}}
                {{#Vocab}}
                    <div class="vocab"><br>{{Vocab}}<br><br></div>
                {{/Vocab}}
                {{#Expression}}
                    <div class="tag">
                        基本{{#Tags}}｜{{/Tags}}{{Tags}}
                    </div>

                    {{^Audio on Front}}
                        <div class="japanese">
                            {{furigana:Expression}}
                        </div>
                    {{/Audio on Front}}

                    {{#Audio on Front}}{{^Audio}}
                        <div class="japanese">
                            {{furigana:Expression}}
                        </div>
                    {{/Audio}}{{/Audio on Front}}

                    {{#Audio on Front}}
                        {{Audio}}
                    {{/Audio on Front}}
                {{/Expression}}
            """,
            "afmt": """
                {{#Radical}}
                    <div class="radical"><br>{{Radical}}<br><br></div><br>
                    <span class="title"><font color="#4188F1"><b>{{Radical_Name}}</b></font></span><p>
                    <span class="text"><b><u>Mnemonic</u></b></span><br>
                    <span class="text">{{Radical_Mnemonic}}</span><p>
                    {{#Radical_Alternative}}
                    <span class="text"><b><u>Alternative</u></b></span><br>
                    <span class="hiragana">{{Radical_Alternative}}</span><br>
                    {{/Radical_Alternative}}
                {{/Radical}}

                {{#Kanji}}
                    <div class="kanji"><br>{{Kanji}}<br><br></div><br>
                    <span class="title"><font color="#EB417D"><b>{{Kanji_Meaning}}</b></font></span><p>
                    <span class="text"><b>On'yomi: </b></span>
                    <span class="hiragana">{{Reading_On}}</font></span><br>
                    <span class="text"><b>Kun'yomi: </b></span>
                    <span class="hiragana">{{Reading_Kun}}</font></span><p>
                    <span class="text"><b>Radicals: </b></span>
                    <span class="text">{{Radical_Names}}</span><p>

                    <span class="text"><b><u>Mnemonic</u></b></span><br>
                    <span class="text">{{Kanji_Mnemonic}}</span><p>
                    <span class="text">Hint: {{Kanji_Mnemonic_Bonus}}</span><p>
                {{/Kanji}}
                
                {{#Vocab}}
                    <div class="vocab"><br>{{Vocab}}<br><br></div>
                    <span class="title"><font color="#833EA8"><b>{{Meaning}}</b></font></span><p>
                    <span class="hiragana">{{Reading}}</font></span><br>
                    {{Audio}}<p>
                    <span class="text"><b><u>Part of Speech</u></b></span><br>
                    <span class="text2">{{Part_Of_Speech}}</span><p>
                    <span class="text"><u><b>Meaning Explanation</b></u></span><br>
                    <span class="text">{{Meaning_Exp}}</span><p>
                    <span class="text"><b><u>Reading Explanation</u></b></span><br>
                    <span class="text">{{Reading_Exp}}</span><p>
                    <span class="text"><b><u>Context Sentences</u></b></span><br>
                    <span class="context">{{Context1_jp}}</span><br>
                    <span class="text">{{Context1_en}}</span><p>
                    <span class="context">{{Context2_jp}}</span><br>
                    <span class="text">{{Context2_en}}</span><p>
                    <span class="context">{{Context3_jp}}</span><br>
                    <span class="text">{{Context3_en}}</span><p>
                {{/Vocab}}

                {{#Expression}}
                    <div class="tag">
                        基本{{#Tags}}｜{{/Tags}}{{Tags}}
                    </div>

                    {{^Audio on Front}}
                        <div class="japanese">
                            {{furigana:Expression}}
                        </div>
                    {{/Audio on Front}}

                    {{#Audio on Front}}{{^Audio}}
                        <div class="japanese">
                            {{furigana:Expression}}
                        </div>
                    {{/Audio}}{{/Audio on Front}}

                    {{#Audio on Front}}
                        {{Audio}}
                    {{/Audio on Front}}
                    {{FrontSide}}
                    <hr id=answer>

                    {{#Reading}}
                        <div class="japanese">
                            {{furigana:Reading}}
                        </div>
                    {{/Reading}}
                    <div class="meaning">
                        {{furigana:Meaning}}
                    </div>

                    {{^Audio on Front}}
                        {{Audio}}
                    {{/Audio on Front}}
                {{/Expression}}
            """
        }
    ],
    css=""".card {
    font-family: "Segoe UI", "Roboto", sans-serif;
    font-size: 16px;
    text-align: center;
    color: #969696;
}

.radical {
    font-family: "Meiryo", "Hiragino Kaku Gothic ProN", "Noto Sans JP", sans-serif;
    font-size: 70px;
    color: #FFFFFF;
    line-height: 100px;
    background-color: #4188F1;
}

.kanji {
    font-family: "Meiryo", "Hiragino Kaku Gothic ProN", "Noto Sans JP", sans-serif;
    font-size: 70px;
    color: #FFFFFF;
    line-height: 100px;
    background-color: #EB417D;
}

.vocab {
    font-family: "Meiryo", "Hiragino Kaku Gothic ProN", "Noto Sans JP", sans-serif;
    font-size: 40px;
    color: #FFFFFF;
    line-height: 100px;
    background-color: #833EA8;
}

.hiragana {
    font-family: "Meiryo", "Hiragino Kaku Gothic ProN", "Noto Sans JP", sans-serif;
    font-size: 20px;
}

.title {
    font-family: "Segoe UI", "Roboto", sans-serif;
    font-size: 26px;
}

.text {
    font-family: "Segoe UI", "Roboto", sans-serif;
}

.text2 {
    font-family: "Segoe UI", "Roboto", sans-serif;
    font-size: 13px;
}

@font-face { font-family: Noto Sans JP; src: url('_NotoSansJP-Regular.otf'); }

radical {
    font-weight: bold;
    color: #4188F1;
}

kanji {
    font-weight: bold;
    color: #EB417D;
}

vocab {
    font-weight: bold;
    color: #833EA8;
}

@font-face {
font-family: "IPAexGothic";
src: url("_ipaexg.ttf") ;
}

.card {
 //font-family:"IPAexGothic", IPAex Gothic;
 font-size: 22px;
 background-color:#FFFAF0;
 text-align: left;
 color:#333;
}

.tag {
  color:#585858; 
  font-size: 20px
}

.japanese {
  font-size: 35px;
}
.meaning {
  margin-top: 36px;
  font-size: 22px;
}

b {
  font-family: "IPAexGothic";
  color:#000;
}"""
)

def get_component_radicals(wanikani_data, wanikani_item):
    radicals = []
    radical_names = []
    for radical_id in wanikani_item['data']['component_subject_ids']:
        radical_data = next((x for x in wanikani_data if x['id'] == radical_id), None)
        if radical_data:
            radicals.append(radical_data['data']['characters'])
            radical_names.append(get_card_meaning(radical_data))
    return [', '.join(radicals), ', '.join(radical_names)]

def get_card_meaning(wanikani_item):
    return wanikani_item['data']['meanings'][0]['meaning']

def get_fields_mapping(wanikani_data, wanikani_item):
    match wanikani_item['object']:
        case 'radical':
            return {
                "Type": 'radical',
                "Radical": wanikani_item['data']['characters'],
                "Radical_Name": wanikani_item['data']['meanings'][0]['meaning'],
                "Radical_Mnemonic": wanikani_item['data']['meaning_mnemonic'],
            }
        case 'kanji':
            return {
                "Type": 'kanji',                
                "Kanji": wanikani_item['data']['slug'],
                "Kanji_Meaning": wanikani_item['data']['meanings'][0]['meaning'],
                "Reading_On": ", ".join([x['reading'] for x in wanikani_item['data']['readings'] if x['type'] == "onyomi"]),
                "Reading_Kun": ", ".join([x['reading'] for x in wanikani_item['data']['readings'] if x['type'] == "kunyomi"]),  
                "Radicals": get_component_radicals(wanikani_data, wanikani_item)[0],
                "Radical_Names": get_component_radicals(wanikani_data, wanikani_item)[1],
                "Kanji_Mnemonic": wanikani_item['data']['meaning_mnemonic'],
                "Kanji_Mnemonic_Bonus": wanikani_item['data']['meaning_hint'] or '',
            }
        case 'vocabulary':
            return {
                "Type": 'vocab',
                "Vocab": wanikani_item['data']['characters'],
                "Meaning": wanikani_item['data']['meanings'][0]['meaning'],
                "Part_Of_Speech": ', '.join(wanikani_item['data']['parts_of_speech']),
                "Reading": wanikani_item['data']['readings'][0]['reading'],  
                "Context1_en": wanikani_item['data']['context_sentences'][0]['en'],
                "Context1_jp": wanikani_item['data']['context_sentences'][0]['ja'],
                "Context2_en": wanikani_item['data']['context_sentences'][1]['en'] if len(wanikani_item['data']['context_sentences']) > 1 else '',
                "Context2_jp": wanikani_item['data']['context_sentences'][1]['ja'] if len(wanikani_item['data']['context_sentences']) > 1 else '',
                "Context3_en": wanikani_item['data']['context_sentences'][2]['en'] if len(wanikani_item['data']['context_sentences']) > 2 else '',
                "Context3_jp": wanikani_item['data']['context_sentences'][2]['ja'] if len(wanikani_item['data']['context_sentences']) > 2 else '',
                "Meaning_Exp": wanikani_item['data']['meaning_mnemonic'],
                "Reading_Exp": wanikani_item['data']['reading_mnemonic'],
                "Audio": f"[sound:{get_audio_file_path(wanikani_item['id'])}]"
            }
        case _:
            return "Error! Object not recognised"


# def map_to_fields(wanikani_data, wanikani_item):
#     # fields_mapping = get_fields_mapping(wanikani_data, wanikani_item)
#     fields = []
#     for field in model.fields:
#         fields.append(fields_mapping.get(field['name'], ''))
    
#     return fields