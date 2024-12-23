from extract_moe_cards import extract_moe_cards
from deck_structure import deck, model, get_fields_mapping
from download_audio_files import download_wanikani_audio_files
import requests
import re
import genanki
import csv
import json

def get_wanikani_data():
    data = []
    for n in range(4,5):
        # url = 'https://api.wanikani.com/v2/subjects?page_after_id=' + str(1000 * n)
        url = 'https://api.wanikani.com/v2/subjects'
        api_token = 'f5f31e87-1905-4cf8-9b16-d4736d8de55a'
        headers = {'Authorization': 'Bearer ' + api_token}

        params = {
            # 'page_after_id': 1000 * n,
            # 'ids': '1,3,48,468,488,489,1000,1001,1002,1003,3500,3501,3502'
            # 'levels': '1'
        }

        response = requests.get(url, headers = headers, params = params)
        json_string = response.text
        parsed_json = json.loads(json_string)
        data += parsed_json["data"]
    return data

wanikani_data = get_wanikani_data()
# print(json.dumps(wanikani_data[17], indent=4))
print(json.dumps(wanikani_data, indent=4))

audio_files = download_wanikani_audio_files(wanikani_data)

# Get moe way deck 
# print(moe_cards)

# Add Wanikani cards to deck

wanikani_mapped_data = []
for item in wanikani_data:
    wanikani_mapped_data.append(get_fields_mapping(wanikani_data, item))



moe_cards = extract_moe_cards()



# # Find the kanji in moe deck
def find_kanji(expression):
    kanji_pattern = re.compile(r'[\u4E00-\u9FFF]')
    return kanji_pattern.findall(expression)

# # Find the kanji combos in moe deck
def find_kanji_combos(expression):
        kanji_pattern = re.compile(r'[\u4E00-\u9FFF]+')
        kanji_matches = kanji_pattern.findall(expression)
        return list(set(kanji_matches))

# we wanna do for wanikani card in deck because the moe stays in the same order
# 
wanikani_vocab_cards = list(filter(lambda card: card['Type'] == 'vocab', wanikani_mapped_data))
wanikani_kanji_cards = list(filter(lambda card: card['Type'] == 'kanji', wanikani_mapped_data))
wanikani_radical_cards = list(filter(lambda card: card['Type'] == 'radical', wanikani_mapped_data))

# VOCAB 
def trim_kana(phrase):
    return re.sub(r'^[\u3040-\u30FFー〜]+|[\u3040-\u30FFー〜]+$', '', phrase)

for wanikani_card in wanikani_vocab_cards:
    wanikani_card['Moe_Index'] = len(moe_cards) + 100

    trimmed_vocab = trim_kana(wanikani_card['Vocab'])

    for moe_card_index, moe_card in enumerate(moe_cards):
        # Use regex to ensure trimmed_vocab is surrounded only by kana (within moe card), not kanji (and thus likely part of a larger word)
        pattern = fr'(?:[^\u4E00-\u9FFF]|^){re.escape(trimmed_vocab)}(?:[^\u4E00-\u9FFF]|$)'
        if re.search(pattern, moe_card['Expression']):
            wanikani_card['Moe_Index'] = moe_card_index
            break

# KANJI 

moe_cards_kanji = []
for card in moe_cards:
    kanji_in_card = find_kanji(card['Expression'])
    moe_cards_kanji.append(kanji_in_card)

for wanikani_card in wanikani_kanji_cards:
    wanikani_card['Moe_Index'] = len(moe_cards) + 100

    for moe_card_index, moe_card_kanji in enumerate(moe_cards_kanji):
        if wanikani_card['Kanji'] in moe_card_kanji:
            wanikani_card['Moe_Index'] = moe_card_index
            break

# RADICALS
wanikani_kanji_cards.sort(key=lambda card: card['Moe_Index'])

for radical_card in wanikani_radical_cards:
    earliest_kanji_containing_radical = next((kanji for kanji in wanikani_kanji_cards if radical_card['Radical'] in kanji['Radicals']), None)
    if earliest_kanji_containing_radical:
        radical_card['Moe_Index'] = earliest_kanji_containing_radical['Moe_Index']
    else:
        radical_card['Moe_Index'] = len(moe_cards) + 100


def create_card_and_add_to_deck(card, sort_index):
    fields = []
    for field in model.fields:
        fields.append(card.get(field['name'], ''))

    note = genanki.Note(
        model = model,
        fields = fields,
        guid = str(sort_index)
    )
    deck.add_note(note)


# Make deck in order 
# first radicals, then kanji, then vocab, then moe
# for item in wanikani_mapped_data:
sort_index = 0
for index, moe_card in enumerate(moe_cards):
    moe_card_radicals = filter(lambda card: card['Moe_Index'] == index, wanikani_radical_cards)
    for radical_card in moe_card_radicals:
        create_card_and_add_to_deck(radical_card, sort_index)
        sort_index += 1

    moe_card_kanji = filter(lambda card: card['Moe_Index'] == index, wanikani_kanji_cards)
    for kanji_card in moe_card_kanji:
        create_card_and_add_to_deck(kanji_card, sort_index)
        sort_index += 1

    moe_card_vocab = filter(lambda card: card['Moe_Index'] == index, wanikani_vocab_cards)
    for vocab_card in moe_card_vocab:
        create_card_and_add_to_deck(vocab_card, sort_index)
        sort_index += 1
    
    create_card_and_add_to_deck(moe_card, sort_index)
    sort_index += 1


package = genanki.Package(deck)
package.media_files = audio_files


# order the kanji by moe sort order
# for each kanji, find the radicals it contains
# for each radical, find next (kanji) where radical in kanji.radicals
# add radical to kanjis
# 



    # If wanikani vocab word not found in moe deck, assign it a high sort number
    # if wanikani_card[-2] == '':
    #     wanikani_card[-2] = len(wanikani_vocab_cards)
    # Delete the id etc fields (which are not anki card fields)
    # del wanikani_card[:3]
  
# for card in moe_cards:
#     # Find vocab
#     kanji_combos_in_card = find_kanji_combos(card['Expression'])
#     foreach

#     # Find kanji
#     kanji_in_card = find_kanji(card['Expression'])

#     # Find radicals
#     vocab_in_card?

#     # 
#     # vocab_in_card = find
#         # Use regex to ensure trimmed_vocab is surrounded only by kana, not kanji (and thus likely part of a larger word)
#         pattern = fr'(?:[^\u4E00-\u9FFF]|^){re.escape(trimmed_vocab)}(?:[^\u4E00-\u9FFF]|$)'
#         if re.search(pattern, moe_card['Expression']):
#             wanikani_card[-2] = moe_card_index
#             break



# Save the deck to an .apkg file
apkg_file_path = '/Users/libbyrear/Downloads/MoeKani.apkg'
package.write_to_file(apkg_file_path)


