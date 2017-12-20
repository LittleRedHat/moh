def language2index(language):
    brief = language.split('-')
    if len(brief):
        brief = brief[0].lower()

    index_map = {
        'moh-en':['en','nl','pt','it','no','sv','fi','da','el','pl','is'],
        'moh-es':['es','sh','sk','sl','uk'],
        'moh-fr':['fr'],
        'moh-asia':['zh','ko','tr','ja','sq','th'],
        'moh-ru':['ru','ro','sr'],
        'moh-de':['de'],
        'moh-ar':['ar','he']
    }

    for index,value in index_map.items():
        if brief in value:
            return index
        
    return 'moh-en'

print language2index('ja')
