# characters = "Bste!hetsi ogEAxpelrt x "
# document = "AlgoExpert is the Best!"

characters = '&*&you^a%^&8766 _=-09     docanCMakemthisdocument'
document = 'Can you make this document &'


def generateDocument(characters, document) -> bool:
    chars = {}
    for char in characters:
        if char not in chars:
            chars[char] = 0
        chars[char] += 1
    for char in document:
        if char not in chars or chars[char] == 0:
            return False
        chars[char] -= 1
    return True


print(generateDocument(characters, document))
