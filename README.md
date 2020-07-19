# Vigenere-Cipher
Implementation of the Vigenere Cipher.

## Usage

```
python vigenere_cipher  <message>   <key>   --encode #to encode a message
python vigenere_cipher  <cipher>   <key>   --decode #to decode a message
python vigenere_cipher  --test #to run through test cases
```

## Examples
```
python vigenere_cipher "Attack at Dawn!" "pie" --encode #prints cipher: "Pbxpko pb Hper!"
python vigenere_cipher "Pbxpko pb Hper!" "pie" --decode #prints the original message: "Attack at Dawn!"
```
