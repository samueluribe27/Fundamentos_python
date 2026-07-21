full_dot = '●'
empty_dot = '○'

def create_character(name, strong, intelligence, charisma):
    if not isinstance(name, str):
        return 'The character name should be a string'
    if name == '':
        return 'The character should have a name'
    if len(name) > 10:
        return 'The character name is too long'
    if " " in name:
        return "The character name should not contain spaces"
    if not isinstance(strong, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return 'All stats should be integers'
    if strong <1 or intelligence <1 or charisma < 1:
        return 'All stats should be no less than 1'
    if strong > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'
    if (strong + intelligence + charisma) != 7:
        return 'The character should start with 7 points'
    else:
        return f'{name}\nSTR ' + ('●' * strong + '○' * (10-strong))+'\nINT ' + ('●' * intelligence + '○' * (10-intelligence))+'\nCHA ' + ('●' * charisma + '○' * (10-charisma))


