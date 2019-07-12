#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'array\\.ipynb_checkpoints'))
	print(os.getcwd())
except:
	pass


# ---------------------------------------------------------------
# Challenge
# Given a string, find the length of the longest substring
# without repeating characters.

# Examples:
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3.
# ---------------------------------------------------------------
# Algorithm

# In summary : Form all posible sub_strings from original string, then return length of longest sub_string

# - start from 1st character, form as long as posible sub string

#             - Add first character to sub string
#             - Add second character to sub string if second character not exist in sub string
#             ...
#             - Repeate until got a character which already exist inside sub string or 
    
    
# - start from 2nd character, form as long as posible sub string

#             - Add first character to sub string
#             - Add second character to sub string if second character not exist in sub string
#             ...
#             - Repeate until got a character which already exist inside sub string


# ....


# - start from final character, form as long as posible sub string
#             - Add first character to sub string
#             - Add second character to sub string if second character not exist in sub string
#             ...
#             - Repeate until got a character which already exist inside sub string
# ---------------------------------------------------------------



