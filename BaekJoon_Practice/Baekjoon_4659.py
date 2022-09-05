import sys

if __name__ =='__main__' :

    alpha_list = ['a', 'e', 'i', 'o', 'u']
    while True :
        input_string = sys.stdin.readline().strip()
        if input_string == 'end' :
            break

        pre_word = ''
        consonant_count = 0
        vowel_count = 0
        chk_vowel = False
        success = True
        for ch in input_string :
            if ch in alpha_list :
                chk_vowel = True
                consonant_count = 0
                vowel_count = vowel_count + 1
            else :
                vowel_count = 0
                consonant_count = consonant_count + 1

            if consonant_count == 3 or vowel_count == 3:
                success = False
                break

            if ch == pre_word :
                if ch == 'e' or ch == 'o' :
                    continue
                else :
                    success = False
                    break
            else :
                pre_word = ch

        if chk_vowel == True and success == True :
            print('<%s> is acceptable.' % (input_string))
        else :
            print('<%s> is not acceptable.' % (input_string))