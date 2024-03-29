# Write a function to convert numbers to text numerals
NUM_WORD = {
  "1": 'one',
  "2": 'two',
  "3": 'three',
  "4": 'four',
  "5": 'five',
  "6": 'six',
  "7": 'seven',
  "8": 'eight',
  "9": 'nine',
  "10": 'ten',
  "11": 'eleven',
  "12": 'twelve',
  "13": 'thirteen',
  "14": 'fourteen',
  "15": 'fifteen',
  "16": 'sixteen',
  "17": 'seventeen',
  "18": 'eighteen',
  "19": 'nineteen',
  "20": 'twenty',
  "30": 'thirty',
  "40": 'forty',
  "50": 'fifty',
  "60": 'sixty',
  "70": 'seventy',
  "80": 'eighty',
  "90": 'ninety'
}
def text_numeral(num):
  """
  Returns the word form of numbers between 1-99. WILL BREAK IF GIVEN NUMBERS ABOVE 100
  Parameters:
  
  num: int
    Number to be converted
    
  Returns:
  
  text: str
    Converted Text
  """
  wordKeys = list(NUM_WORD.keys())
  wordKeys.reverse()
  resultArr = []
  # Start searching
  for key in wordKeys:
    if num >= int(key):
      
      resultArr.append(NUM_WORD[key])
      num -= int(key)
    if(num == 0):
      
      text = ""
      # Generate the result text
      for word in resultArr:
        text += f"{word} "
      return text.rstrip()
      

