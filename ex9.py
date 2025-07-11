# ✅ Problem 09 — Keyword Tracker in Sentences
# 🎯 Goal
# Write a program that:
# Takes multiple sentences from the user.
# Stores them in a list.
# Asks for a keyword to search for.
# Finds which sentences contain that keyword (case-insensitive).
# Writes the original sentences and the matched sentences to a file called keyword_log.txt.
# Shows the count of matches and which ones matched.
# 1️⃣ Ask how many sentences you want
num_sentences = int(input("PLEASE ENTER THE NUMBER OF SENTENCES YOU WANT TO ENTER: "))
s_list = []

# 2️⃣ Take each sentence and store in a list
for idx in range(num_sentences):
    sentence = input(f"PLEASE ENTER SENTENCE {idx + 1}: ")
    s_list.append(sentence)

# 3️⃣ Ask for keyword
keyword = input("ENTER KEYWORD TO SEARCH: ").lower()

# 4️⃣ Find matches
matched_sentences = []  # This will store tuples (index, sentence)

for idx, sentence in enumerate(s_list, start=1):
    if keyword in sentence.lower():
        matched_sentences.append((idx, sentence))

# 5️⃣ Write results to file
with open("keywordlog.txt", "w") as k:
    k.write("Original Sentences:\n")
    for idx, sentence in enumerate(s_list, start=1):
        k.write(f"{idx}) {sentence}\n")

    k.write("\nSentences containing the keyword:\n")
    if matched_sentences:
        for idx, sentence in matched_sentences:
            k.write(f"{idx}) {sentence}\n")
    else:
        k.write("No sentences contain the keyword.\n")

# 6️⃣ Display results to user
print("\n===== SEARCH RESULTS =====")
print(f"Total sentences entered: {num_sentences}")
print(f"Keyword: '{keyword}'")
if matched_sentences:
    print(f"Sentences containing the keyword: {len(matched_sentences)}")
    for idx, sentence in matched_sentences:
        print(f"{idx}) {sentence}")
else:
    print("No sentences contain the keyword.")
print("\n✅ Results saved to keywordlog.txt")
