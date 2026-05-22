#Task_01
task = "Data Cleanup"
priority = "High"
year = 2026

metadata = (task, priority, year)

print("Extracted Priority:", metadata[1])

#Task_02
text = "Agentic systems are completely rewriting software."

short_text = text[:10] + "..." + text[-10:]

print(short_text)

#Task_03
secret = "AGENT_SECRET"

result = secret[::-2]

print(result)

#Task_04
topics = ["Weather", "Math", "Coding"]

topics.append("Deep Learning")

topics.pop(0)

print(topics)
print("Total:", len(topics))

#Task_05
scores = [88, 92, "ERROR", 74, 92, 85]

scores.remove("ERROR")

count_92 = scores.count(92)

scores.insert(1, 95)

scores.sort()

print("Final List:", scores)
print("Min:", min(scores))
print("Max:", max(scores))
print("Count of 92:", count_92)