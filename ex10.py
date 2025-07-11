# ✅ Problem 10 — User Feedback Analyzer

# Problem statement:
# You need to build a small tool that:
# Takes multiple feedback comments from users.
# For each comment, analyze:
# Number of words
# Number of characters (excluding spaces)
# Whether it contains any bad words (e.g., “bad”, “poor”, “worst”) — this should be case-insensitive.
# Save all the feedback + analysis to a file feedback_report.txt.
# At the end, display:
# Total number of comments
# Average number of words per comment
# How many comments contain bad words

# 📚 Things this tests:
# Loops
# String methods: .split(), .lower(), len()
# Basic logic with in
# File writing with with open()
# Summaries & averages

#Asking user for the number of feedbacks , he want to enter
f_sen = int(input("PLEASE ENTER THE NUMBER OF SENTENCES YOU WANT TO ENTER: "))
f_list = []
nf_list = []


with open("feedback_report.txt",'w') as r: 
    r.write("THE FEEDBACK REPORTS ARE SHOWN BELOW :- \n\n ALL FEEDBACKS: \n")

#Take each feedback and store in a list
for idx in range(f_sen):
    feedback = input(f"PLEASE ENTER FEEDBACK {idx + 1}: ")
    f_list.append(feedback)
    
    with open("feedback_report.txt",'w') as r: 
        r.write(f"{idx + 1}) {feedback}\n No. of words = {len(feedback.split())} \n No of char. = {len(feedback.replace(" ","").strip(",.?!"))} \n")

with open("feedback_report.txt",'w') as r: 
    r.write("\n\n\nNEGATIVE FEEDBACKS: \n")

w_list = []

for f in f_list :  
    words = f_list.split()
    w_list.append(words)
    for word in words:
        cleaned_word = word.strip(',!.?').lower()
        if cleaned_word in ('bad','worst','poor'):
            nf_list.append(f)
            p = len(nf_list)
            with open("feedback_report.txt",'a') as r:
                r.write(f'{p}) {f}')

#output result
print("===== FEEDBACK ANALYSIS =====\n")
print(f"TOTAL NUMBER OF FEEDBACKS = {f_sen}")
print(f"AVERAGE NUMBER OF WORDS IN EACH FEEDBACK = {(len(w_list))/f_sen}")
print(f"NUMBER OF FEEDBACKS WITH BAD COMMENTS = {len(nf_list)}")