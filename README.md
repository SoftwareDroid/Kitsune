# Kitsune
*Kitsune* is a program designed to help with learning Japanese.
It converts a subtitle file (srt) for an anime into a format suitable for reading and learning.
In doing so, furigana are added in parentheses (and no kanji to learn).
Spaces are added between words to make it easier to recognize words.
Added an automatic translation into e.g. English.
As well as in a separate file a list by looked up words in the subtitles in a dictionary.
This list also contains references to the first file.

The settings can be in the config.toml.
 - input
   - filename = the input file
   - lines = the processed sentence numbers
 - output
   - language = the output language (translations)
   - folder = the output folder
   - mode = only txt is supported
   - practice_sheet = output file 1
   - word_sheet = output file 2


Source for downloading Japanese anime subtitles:
- http://kitsunekko.net/

Used website to create furigana, spaces and look up the individual words:
- https://nihongodera.com/tools/text-analyzer

## Example Output

### File Sentences
---
Sentences

0. 『となりのトトロ』＞
"My Neighbor Totoro">

1. ＜小学生[しょうがくせい] のサツキと　妹[いもうと] のメイ＞
<Satsuki in elementary school and Mei in my sister>

2. （サツキ）　大きい[おおきい] ね。
(Satsuki) It's big.

---
### File looked up words
Words:
となり <br>
neighbor (neighbour), next to (esp. living next door to)
<br>[0]<br>

の<br>
   indicates possessive, nominalizes verbs and adjectives, substitutes for "ga" in subordinate phrases, (at sentence-end, falling tone) indicates a confident conclusion, (at sentence-end) indicates emotional emphasis, (at sentence-end, rising tone) indicates question
   <br>[0, 1, 1]<br>

ととろ<br>
   roaring<br>
   [0]<br>

小学生 (しょうがくせい)<br>
   elementary school student, primary school student, grade school student
   [1]<br>

さつき<br>
   fifth month of the lunar calendar, satsuki azalea (Rhododendron indicum)<br>
   [1, 2]<br>

と<br>
   if, when, and, with, particle used for quoting (with speech, thoughts, etc.), quoting particle, promoted pawn, indicates question (sentence end)<br>
   [1]<br>

妹 (いもうと)<br>
   younger sister<br>
   [1]<br>
めい nein<br>

   command, decree, life, destiny<br>
   [1]<br><br>
大きい (おおきい)<br>

   big, large, great, loud<br>
   [2]<br>

ね<br>
   indicates emphasis, agreement, request for confirmation, etc., is it so, hey, come on, listen, not<br>
   [2]<br>

---
## Contact <a name="contact"></a>
Created by Patrick Mispelhorn (patrick.mispelhorn@web.de) - feel free to contact me!
## License
GNU AFFERO GENERAL PUBLIC LICENSE
